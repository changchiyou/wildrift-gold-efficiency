// @ts-check
import { test, expect } from "@playwright/test";
import { readdirSync } from "node:fs";

// Discover patch pages from _pages/ (dir names like "7_3a" -> permalink "/7.3a/"),
// sorted so the tests keep working on future patches.
const patchDirs = readdirSync("_pages", { withFileTypes: true })
  .filter((d) => d.isDirectory() && /^\d+_\d+[a-z]*$/.test(d.name))
  .map((d) => d.name.replace("_", "."))
  .sort((a, b) => {
    const pa = /^(\d+)\.(\d+)([a-z]*)$/.exec(a);
    const pb = /^(\d+)\.(\d+)([a-z]*)$/.exec(b);
    const va = Number(pa[1]) * 1000 + Number(pa[2]) * 10 + (pa[3].charCodeAt(0) || 96);
    const vb = Number(pb[1]) * 1000 + Number(pb[2]) * 10 + (pb[3].charCodeAt(0) || 96);
    return va - vb;
  });

const latest = patchDirs.at(-1);
const LOCALES = ["en-US", "zh-TW", "de-DE", "ja-JP", "pt-BR"];

/** Parse the sortable values of column `col` from the top-level (non-compare) rows. */
function columnValues(table, col, numeric) {
  return table.locator("tbody tr:not(.compare)").evaluateAll(
    (rows, { col, numeric }) => {
      const header = rows[0].closest("table").querySelector(`th[column="${col}"]`);
      const index = Array.from(header.parentNode.children).indexOf(header);
      return rows.map((r) => {
        const text = r.cells[index].innerText.trim();
        return numeric ? Number(text.replace("%", "")) : text;
      });
    },
    { col, numeric },
  );
}

function isNonAscending(values) {
  return values.every((v, i) => i === 0 || values[i - 1] >= v);
}
function isNonDescending(values) {
  return values.every((v, i) => i === 0 || values[i - 1] <= v);
}

async function clickHeader(table, col) {
  const th = table.locator(`th[column="${col}"]`);
  await th.scrollIntoViewIfNeeded();
  // Real pointer click at the header's center (what a user does).
  const box = await th.boundingBox();
  await table.page().mouse.click(box.x + box.width / 2, box.y + box.height / 2);
}

test("latest patch page renders with working JavaScript", async ({ page }) => {
  /** @type {Error[]} */
  const errors = [];
  page.on("pageerror", (e) => errors.push(e));

  await page.goto(`/en-US/${latest}/`);

  // renderTable.js must have produced data rows: an empty table here means the
  // page's JS crashed (the failure mode a plain HTML check would miss).
  const table = page.locator("table.sortable-table").first();
  await expect(table.locator("tbody tr:not(.compare)")).not.toHaveCount(0);
  await expect(table.locator("tbody tr").first()).toBeVisible();

  expect(errors, `page errors: ${errors.map(String).join("; ")}`).toHaveLength(0);
});

for (const col of ["cost", "amount"]) {
  test(`sort header "${col}" cycles non-order -> descending -> ascending -> non-order`, async ({ page }) => {
    await page.goto(`/en-US/${latest}/`);
    const table = page.locator("table.sortable-table").first();
    await expect(table.locator("tbody tr:not(.compare)")).not.toHaveCount(0);
    const numeric = col === "cost" || col === "amount";

    const original = await columnValues(table, col, numeric);
    const th = table.locator(`th[column="${col}"]`);

    // Click 1: must go to descending (with duplicated click listeners it used
    // to advance 8 state-machine steps and land on "ascending" instead).
    await clickHeader(table, col);
    await expect(th).toHaveAttribute("data-order", "descending");
    expect(isNonAscending(await columnValues(table, col, numeric))).toBe(true);

    // Click 2: ascending.
    await clickHeader(table, col);
    await expect(th).toHaveAttribute("data-order", "ascending");
    expect(isNonDescending(await columnValues(table, col, numeric))).toBe(true);

    // Click 3: back to the original (unsorted) order.
    await clickHeader(table, col);
    await expect(th).toHaveAttribute("data-order", "non-order");
    expect(await columnValues(table, col, numeric)).toEqual(original);
  });
}

test("Removed Items section shows on patches that removed items", async ({ page }) => {
  // 7.3 retired items; its page must always render the section with rows.
  await page.goto("/en-US/7.3/");
  const heading = page.locator("h3#REMOVED-ITEMS");
  await expect(heading).toBeVisible();
  await expect(heading.locator("xpath=following::table[1]/tbody/tr")).not.toHaveCount(0);
});

for (const lang of LOCALES) {
  test(`${lang} index redirects to the latest patch page`, async ({ page }) => {
    await page.goto(`/${lang}/`); // redirect_from meta-refresh -> latest patch
    await expect(page).toHaveURL(new RegExp(`/${lang}/${latest}/`));
    await expect(page.locator("html")).toHaveAttribute("lang", lang);
    await expect(page.locator("table.sortable-table").first()).toBeAttached();
  });
}
