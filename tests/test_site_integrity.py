"""Site integrity checks: i18n completeness and image availability.

Two layers:
  1. Data-level (no build): replicate the Liquid token generation from
     `_includes/trans.html` / `_includes/filter.html` / `_includes/item_row.html`
     and verify, for every patch page's items/stats (and its compare data),
     that every locale has the required `item.name.*`, `item.passive.*`,
     `stat.attr.*`, `stat.type.*` keys and that every stat type used has an
     image in the stats yml (`_includes/stat_image.html` renders a bare value
     / empty icon when the image is missing).
  2. Built-output (requires `_site`, skips otherwise): assert no rendered page
     contains the i18n error marker, and every image URL referenced by an
     <img> tag answers with HTTP 200 (network; set SKIP_NETWORK_TESTS=1 to skip).

Run:
    python3 -m unittest tests.test_site_integrity -v
    (or) python3 tests/test_site_integrity.py -v
"""

import os
import unittest
import urllib.error
import urllib.request
import re
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path

import yaml

ROOT = Path(os.environ.get("SITE_ROOT", Path(__file__).resolve().parent.parent))
DATA = ROOT / "_data"
I18N = DATA / "i18n"
PAGES = ROOT / "_pages"
SITE = ROOT / "_site"

LOCALES = sorted(p.stem for p in I18N.glob("*.yml"))

_yaml_cache = {}


def load_yaml(path):
    key = str(path)
    if key not in _yaml_cache:
        with open(path, encoding="utf-8") as f:
            _yaml_cache[key] = yaml.safe_load(f)
    return _yaml_cache[key]


def i18n(locale):
    return load_yaml(I18N / f"{locale}.yml")


def trans(text):
    """Replicates `_includes/trans.html` (Liquid filters, in order)."""
    out = text.lower()
    for old, new in (
        (" / ", "-"),
        (" - ", "-"),
        (" & ", "-"),
        (": ", "-"),
        ("(", ""),
        (")", ""),
        (",", ""),
        (".", ""),
        ("''", "-"),
        ("'", "-"),
        (" ", "-"),
    ):
        out = out.replace(old, new)
    return out


def stat_id(stat_type):
    """Replicates `stat.type | downcase | replace:" ","-" | replace:"%","percentage"`."""
    return stat_type.lower().replace(" ", "-").replace("%", "percentage")


def lookup(tree, dotted):
    node = tree
    for part in dotted.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


def front_matter(page_path):
    text = page_path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    return yaml.safe_load(parts[1])


def patch_pages():
    """Every `_pages/<version>/<locale>.md` with its parsed front matter."""
    for page in sorted(PAGES.glob("*/*.md")):
        fm = front_matter(page)
        if not fm or "data" not in fm or "items" not in fm["data"]:
            continue
        yield page, fm


class DataIntegrityMixin:
    def iter_data_refs(self):
        """(page, locale, dataset, items_file, stats_file) per page data set."""
        for page, fm in patch_pages():
            locale = fm.get("lang") or page.parent.name
            if locale not in LOCALES:
                continue
            yield page, locale, "data", fm["data"]["items"], fm["data"]["stats"]
            compare = (fm.get("patch_note") or {}).get("compare") or {}
            if compare.get("items") and compare.get("stats"):
                yield page, locale, "compare", compare["items"], compare["stats"]


class TestI18nKeys(unittest.TestCase, DataIntegrityMixin):
    def test_item_names(self):
        """item.name.<trans(name)> exists for every locale that renders the item."""
        missing = {}
        for page, locale, dataset, items_file, _ in self.iter_data_refs():
            names = {r["name"] for r in load_yaml(DATA / f"{items_file}.yml")}
            tree = i18n(locale)
            for name in sorted(names):
                token = f"item.name.{trans(name)}"
                if lookup(tree, token) is None:
                    missing.setdefault(locale, []).append(f"{page.parent.name}: {token}")
        self.assertEqual(missing, {}, f"Missing item.name keys: {missing}")

    def test_passive_names(self):
        """item.passive.<trans(passive)> exists for every passive label."""
        missing = {}
        for page, locale, dataset, items_file, _ in self.iter_data_refs():
            passives = {
                stat["passive"]
                for r in load_yaml(DATA / f"{items_file}.yml")
                for stat in r["stats"]
                if "passive" in stat
            }
            tree = i18n(locale)
            for passive in sorted(passives):
                token = f"item.passive.{trans(passive)}"
                if lookup(tree, token) is None:
                    missing.setdefault(locale, []).append(f"{page.parent.name}: {token}")
        self.assertEqual(missing, {}, f"Missing item.passive keys: {missing}")

    def test_stat_attr_keys(self):
        """stat.attr.<stat_id> for every stats-yml entry the filter renders
        (non-empty type) plus every stat type actually used by items."""
        missing = {}
        for page, locale, dataset, items_file, stats_file in self.iter_data_refs():
            stats = load_yaml(DATA / f"{stats_file}.yml") or {}
            shown = {name for name, v in stats.items() if v and v.get("type")}
            used = {
                stat["type"]
                for r in load_yaml(DATA / f"{items_file}.yml")
                for stat in r["stats"]
            }
            tree = i18n(locale)
            for stype in sorted(shown | used):
                token = f"stat.attr.{stat_id(stype)}"
                if lookup(tree, token) is None:
                    missing.setdefault(locale, []).append(f"{page.parent.name}: {token}")
        self.assertEqual(missing, {}, f"Missing stat.attr keys: {missing}")

    def test_stat_type_keys(self):
        """stat.type.<type> for every non-empty type in every stats yml."""
        missing = {}
        for page, locale, dataset, _, stats_file in self.iter_data_refs():
            stats = load_yaml(DATA / f"{stats_file}.yml") or {}
            tree = i18n(locale)
            types = {v["type"] for v in stats.values() if v and v.get("type")}
            for stype in sorted(types):
                token = f"stat.type.{stype}"
                if lookup(tree, token) is None:
                    missing.setdefault(locale, []).append(f"{page.parent.name}: {token}")
        self.assertEqual(missing, {}, f"Missing stat.type keys: {missing}")


class TestStatImages(unittest.TestCase, DataIntegrityMixin):
    def test_stat_types_have_images(self):
        """Every stat type used in items has an image in its stats yml
        (missing image renders an empty icon)."""
        missing = {}
        for page, locale, dataset, items_file, stats_file in self.iter_data_refs():
            stats = load_yaml(DATA / f"{stats_file}.yml") or {}
            used = {
                stat["type"]
                for r in load_yaml(DATA / f"{items_file}.yml")
                for stat in r["stats"]
            }
            for stype in sorted(used):
                entry = stats.get(stype) or {}
                if not entry.get("image"):
                    missing.setdefault(f"{page.parent.name}/{locale}", []).append(stype)
        self.assertEqual(missing, {}, f"Stat types without image: {missing}")

    def test_items_have_images(self):
        missing = {}
        for page, locale, dataset, items_file, _ in self.iter_data_refs():
            for r in load_yaml(DATA / f"{items_file}.yml"):
                if not r.get("image"):
                    missing.setdefault(f"{page.parent.name}/{locale}", []).append(r["name"])
        self.assertEqual(missing, {}, f"Items without image URL: {missing}")


class _ImgSrcParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.srcs = set()

    def handle_starttag(self, tag, attrs):
        if tag in ("img", "source"):
            for k, v in attrs:
                if k == "src" and v:
                    self.srcs.add(v)


def _ssl_context():
    try:
        import ssl

        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:  # noqa: BLE001 — fall back to OS trust store
        return None


def _reachable(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20, context=_ssl_context()) as resp:
            return None if resp.status == 200 else f"{url}: HTTP {resp.status}"
    except urllib.error.HTTPError as e:
        # Bot protection (wiki.leagueoflegends.com et al.) answers 403 to
        # non-browser TLS fingerprints while real browsers load fine.
        if e.code in (401, 403, 405, 429):
            return None
        return f"{url}: HTTP {e.code}"
    except Exception as e:  # noqa: BLE001 — network layer
        return f"{url}: {e}"


def _version_key(name):
    """Sort key for rendered patch dir names like `7.3`, `6.2e` (newest last)."""
    m = re.match(r"^(\d+)\.(\d+)([a-z]?)$", name)
    return (int(m.group(1)), int(m.group(2)), m.group(3)) if m else (-1, -1, name)


class TestBuiltSite(unittest.TestCase):
    ERROR_MARKER = "Error: Add in"

    def built_pages(self):
        return sorted(SITE.rglob("*.html")) if SITE.is_dir() else []

    def test_no_missing_i18n_in_built_pages(self):
        pages = self.built_pages()
        if not pages:
            self.skipTest("_site/ not built; run `bundle exec jekyll build` first")
        broken = []
        for page in pages:
            if self.ERROR_MARKER in page.read_text(encoding="utf-8", errors="replace"):
                broken.append(str(page.relative_to(SITE)))
        self.assertEqual(broken, [], f"Pages with missing i18n tokens: {broken}")

    def test_latest_patch_images_reachable(self):
        """Every <img> on the newest patch page (all locales) returns 200.
        Older patches are pinned history and may reference retired CDNs;
        override the target with TEST_PATCH=7_3."""
        if os.environ.get("SKIP_NETWORK_TESTS"):
            self.skipTest("SKIP_NETWORK_TESTS set")
        if not SITE.is_dir():
            self.skipTest("_site/ not built; run `bundle exec jekyll build` first")
        patch = os.environ.get("TEST_PATCH")
        if not patch:
            pattern = re.compile(r"^\d+\.\d+[a-z]?$")
            candidates = {
                d.name
                for loc in SITE.iterdir()
                if loc.is_dir()
                for d in loc.iterdir()
                if d.is_dir() and pattern.match(d.name) and (d / "index.html").is_file()
            }
            self.assertTrue(candidates, "no patch pages in _site")
            patch = max(candidates, key=_version_key)
        pages = sorted(SITE.glob(f"*/{patch}/index.html"))
        self.assertTrue(pages, f"no _site/*/{patch}/index.html")
        urls = set()
        for page in pages:
            parser = _ImgSrcParser()
            parser.feed(page.read_text(encoding="utf-8", errors="replace"))
            urls |= parser.srcs
        remote = sorted(u for u in urls if u.startswith(("http://", "https://")))
        self.assertTrue(remote, f"no remote <img> sources in {patch}")
        with ThreadPoolExecutor(max_workers=4) as pool:
            failures = [f for f in pool.map(_reachable, remote) if f]
        self.assertEqual(
            failures,
            [],
            f"Unreachable images on {patch} ({len(failures)}/{len(remote)}):\n"
            + "\n".join(failures),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
