# Config Structure

This page introduce the structure of the config files mainly located in `_data`/`_pages` directories.

## items_{version}.yml

The field info of `items_{version}.yml`:

| Field | Requirement | Description |
|-|-|-|
|`amount`|no need|Generated by [data.py](/data.py)|
|`category`|required|Determines where the item belongs to. For instance, set `category` as `PHYSICAL DAMAGE ITEMS` to make the item belong to [📌 Physical Damage Items](https://changchiyou.github.io/wildrift-gold-efficiency/5.1b/#PHYSICAL-DAMAGE-ITEMS).|
|`cost`|required|The cost of the item.|
|`formula`|no need|Generated by [data.py](/data.py)|
|`image`|required|The image reference of the item.|
|`name`|required|The name of the item. The notes in `()` would be extracted and rendered with different style (only allowed 1 `()` set exists).|
|`stats`|required|The stats info of the item. Check more detail info in following sheet.|

The fields info of `stats` field:

| Field | Requirement | Description |
|-|-|-|
|`formula`|no need|Generated by [data.py](/data.py) (only if `ratio`&(`ref`or`ref_type`) are set)|
|`passive`|optional|The unique passive which give the item the stat.|
|`ratio`|optional|The ratio calculates with `ref` ( and the stats of `ref_type`) to generate `value`|
|`ref`|optional|The base target stat for `value`'s calculation|
|`ref_type`|optional|The target stat from current item for `value`'s calculation|
|`type`|required|The type of the stat|
|`value`|required|The value of the stat|
|`value`*|required|Must be set before the value generated by [data.py](/data.py) (only if `ratio`&(`ref`or`ref_type`) are set)*|

Some example:

1. Basic:
    https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/items_5_1b.yml#L15-L34

2. `ratio` & `ref`:
    https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/items_5_1b.yml#L819-L836

3. `ref_type` & `ref`:
    https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/items_5_1b.yml#L367-L386

4. `ref_type` & empty `ratio` in another stat & single type `Unstable Passives' Stats`:
    https://github.com/changchiyou/wildrift-gold-efficiency/blob/72a0ff695d138eb5494f9d9752c486170955cf79/_data/items_5_1b.yml#L1986-L2012

## stats_{version}.yml

The fields info of `stats_{version}.yml`:

| Field | Requirement | Description |
|-|-|-|
| `image`     | required    | The reference of the image / pure text.|
| `base_type` | optional    | Determines where the statistic price belongs in [💰 Base Statistic Prices](https://changchiyou.github.io/wildrift-gold-efficiency/5.1b/#Base-Statistic-Prices). (`first`: base stat with *First-tier Base Item*, `second`: base stat with *Second-tier Base Item*, `exclude`: base stat *without any Base Item*.) |
| `base_item` | optional    | The item used as the basis for calculating the statistic price.|
| `type`      | required    | Determines the classification of the stat in the [🔎 Stat Filters](https://changchiyou.github.io/wildrift-gold-efficiency/5.1b/#stat-filters). Set `""` to exclude from filters.|

Some examples:

1. Basic:
    https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/stats_5_1b.yml#L41-L45

2. Excluded from statistic price calculation:
    https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/stats_5_1b.yml#L61-L63

3. Exclude from statistic price calculation and filters:
    https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/stats_5_1b.yml#L88-L90

4. Pure text + (ii.):
    https://github.com/changchiyou/wildrift-gold-efficiency/blob/72a0ff695d138eb5494f9d9752c486170955cf79/_data/stats_5_1b.yml#L91-L93

## _page/{version}/*.md

The params info of page.md:

| Field | Requirement | Description |
|-|-|-|
|`layout`|fixed value|Set `gold_efficiency_v2` means the page is using the layout of [gold_efficiency_v2.html](/_layouts/gold_efficiency_v2.html).|
|`title`|required|The title of the page, normally named with version name.|
|`date`|required|The publish date of the page. Required for generating rss with [feed.xml](/feed.xml). (`2024/04/19 12:02 a.m.` or simply `2024/04/19` are both valid value)|
|`description`|required|Briefly describe the page.|
|`image`|fixed value|`/assets/favicon512x512.png`|
|`permalink`|required|Specific the sub-path for this page.|
|`redirect_from`|optional|Set to `/` to redirect the root path to this page.|
|`latest_version`|optional|Set to `true` if this page indicate to the latest version.|
|`lang`|optional|Default value is `en-us` if not set. Set to `zh-tw` means current page's language is Traditional Chinese and the i18n include would find [_data/i18n/zh-tw.yml](/_data/i18n/zh-tw.yml) to translate this page|
|`data`|required|Fields for item data.|
|`data.refer_url`|required|The URL of wildrift badge.|
|`data.refer_text`|required|The TEXT of wildrift badge.|
|`data.items`|required|The item datas.|
|`data.stats`|required|The base stats info.|
|`patch_note`|optional|Fields for comparing last version. (icon, row)|
|`patch_note.statuses`|required|A string combining item names separated by commas(`,`) with uppercase. The item names in string would be listed with following patch-note statuses.|
|`patch_note.statuses.buffed`|optional|Items that have been buffed.|
|`patch_note.statuses.adjusted`|optional|Items that have been adjusted.|
|`patch_note.statuses.nerfed`|optional|Items that have been nerfed.|
|`patch_note.statuses.new`|optional|Items that have been added.|
|`patch_note.excludes`|optional|The specific item name to be excluded from listing patch-note statuses.|
|`patch_note.compare`|optional|Fields for comparing last version. (generate a row of item data from last version)|
|`patch_note.compare.statuses`|fixed value|The patch-note statuses would find the item data from last version to compare with.|
|`patch_note.compare.items`|optional|The item datas to compare with.|
|`patch_note.compare.stats`|optional|The stats to compare with.|
|`patch_note.compare.item_prefix`|optional|The prefix which would be render in front of the row of comparing item data.|
|`patch_note.compare.force`|optional|Forces the comparison of items in pairs, particularly in situations where items have been added, removed, or updated with prefixes, such as `hextech/light/ruin`|

For example:

1. `6.0d`:
    https://github.com/changchiyou/wildrift-gold-efficiency/blob/35ee1d75f7078262bf590232416051afc72cd597/_pages/6_0d/en-us.md?plain=1#L1-L35
