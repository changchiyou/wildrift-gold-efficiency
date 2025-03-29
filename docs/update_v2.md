# Establish Gold Efficiency Page for the New Version v2 (for maintainer)

> [!INFO]
> This document is intended for updating versions from 6.0d onwards.

Taking the update from [6.0d](https://changchiyou.github.io/wildrift-gold-efficiency/en-us/6.0d/) to 6.0e (May not existed, just for example) as an example:

1. Simply execute [copy_v2.sh](/copy_v2.sh) with `bash copy.sh 6_0d 6_0e`. This script will generate `_data/items_6_0e.yml`, `_data/stats_6_0e.yml` and `_pages/6_0e/*.md` based on previous version for you.

2. Manually update item data in generated item file `_data/items_6_0e.yml` based on the the official 6.0e patch note. (Please refer to [`item_{version}.yml`](/docs/config.md#items_versionyml))

3. Manually update [stats_5_1b.yml](/_data/stats_5_1b.yml) if needed. (Please refer to [`stats_{version}.yml`](/docs/config.md#stats_versionyml))

4. (Execute `pip install -r requirements.txt` to install python dependencies in your enviroment then) Execute [data.py](/data.py) to re-generate `amount` and `formula` in `_data/items_6_0e.yml`:
    - Specific `6.0e`:
        ```
        python data.py --items items_6_0e.yml --stats stats_6_0e.yml
        ```

    - All items.yml files in `_data` directory:
        ```
        python data.py
        ```

    > For more info of params, execute:
    > ```
    > python data.py -h
    > ```
    >
    > ```shell
    > usage: data.py [-h] [--items ITEMS] [--stats STATS] [--clean_only] [-d]
    > 
    > Extract data from WR Meta via web scraping, or calculate the gold efficiency of item data.
    >
    > options:
    >  -h, --help     show this help message and exit
    >  --items ITEMS  The file storage item data
    >  --stats STATS  The file storage stat data
    >  --clean_only   Only clean gold efficiency and base statistic price from item data
    >  -d, --debug    Enable debug mode

6. Update `_pages/6_0e/*.md` if needed. (Please refer to [`_page/{version}/*.md`](/docs/config.md#_pageversionmd)) In most case you only have to modify `patch_note.statuses` and `patch_note.excludes` to hightlight the updated items.
