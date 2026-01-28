# Claude Code Configuration

This file contains configuration and commands for Claude Code to better assist with this Wild Rift Gold Efficiency project.

## Project Information
- **Name**: Wild Rift Gold Efficiency
- **Type**: Jekyll static site for tracking item gold efficiency across Wild Rift patches
- **Languages**: Bash, Python (data processing), Jekyll/Markdown (site generation)

## Common Commands

### Data Processing
```bash
# Process specific version
python data.py --items items_6_0e.yml --stats stats_6_0e.yml

# Process all item files
python data.py

# Clean only (remove gold efficiency data)
python data.py --clean_only

# Debug mode
python data.py -d
```

### Version Updates
```bash
# Copy previous version to new version
bash copy_v2.sh 6_0d 6_0e
```

## Project Structure
- Data files: `_data/items_{version}.yml`, `_data/stats_{version}.yml`
- Page templates: `_pages/{version}/*.md`
- Main data processor: `data.py`
- Version copy script: `copy_v2.sh`
- Documentation: `docs/`

## Workflow for New Version Updates
1. Run `bash copy_v2.sh {old_version} {new_version}` to copy previous version
2. Update item data in `_data/items_{new_version}.yml` based on patch notes
3. Update `_data/stats_{new_version}.yml` if needed
4. Run `python data.py --items items_{new_version}.yml --stats stats_{new_version}.yml`
5. Update `_pages/{new_version}/*.md` files if needed:
   - Add items in patch_note.statuses based on items' adjustment (buffed/adjusted/nerfed/new)
   - **IMPORTANT**: Only add items to patch_note.statuses when their **stats** have changed (including price, base stats, or stats from passives), NOT when only passive mechanics or descriptions change
   - **IMPORTANT**: Use the exact item names as they appear in the `name` field of `_data/items_{version}.yml`, NOT lowercase or processed versions (e.g., use `Runaan's Hurricane` not `runanns_hurricane`)
   - **Item matching rules**: When only the base item name is specified (e.g., `Psychic Projector`), it will automatically include all passive variants of that item (e.g., `Psychic Projector (Conversion)`, `Psychic Projector (Conversion, Projection)`). Specify the exact variant name only when needed based on actual changes.
   - If input contains JSON with og_image field, extract the og_image URL and update the `image:` parameter in all markdown files to use this new preview image instead of the default favicon

## i18n (Internationalization) Updates

### Translation Files Location
- Translation files are located in `_data/i18n/{language}.yml`
- Available languages: `en-US.yml`, `zh-TW.yml`, `ja-JP.yml`, `pt-BR.yml`, `de-DE.yml`

### Updating Item Names and Passives
When new items are added or item names/passives change:

1. **Update English translations** (primary language) in `_data/i18n/en-US.yml`:
   - Add new item names under `item.name` section (use kebab-case keys)
   - Add new passive names under `item.passive` section (use kebab-case keys)

2. **Key naming convention**:
   - Item names: Use lowercase with hyphens (e.g., `bloodthirster`, `guardian-angel`)
   - Passive variants: Include passive name in parentheses (e.g., `bloodthirster-bloody[crit]`)
   - Passive keys: Use kebab-case (e.g., `bloody`, `last-whisper`, `bloody[crit]`)

3. **Example structure**:
   ```yaml
   item:
     name:
       bloodthirster: Bloodthirster
       bloodthirster-bloody[crit]: Bloodthirster (Bloody[Crit])
     passive:
       bloody: Bloody
       bloody[crit]: Bloddy[Crit]
       lifeline: Lifeline
   ```

4. **Focus on English updates**: Unless specifically required, only update the English (`en-US.yml`) translation file. Other language translations can be handled separately by contributors via Crowdin or other localization tools.

## Version Format Handling

The project supports two version number formats due to a change in Wild Rift's patch note URL structure starting from version 7.0:

### Old Format (up to 6.x)
- **URL format**: `wild-rift-patch-notes-6-3e` (with dash separator)
- **File/folder format**: `6_3e` (with underscore separator)
- **Display format**: `6.3e` (with dot separator)

### New Format (from 7.0 onwards)
- **URL format**: `wild-rift-patch-notes-70` (no separator, concatenated digits)
- **File/folder format**: `7_0` (with underscore separator, same as old format)
- **Display format**: `7.0` (with dot separator)

### Conversion Examples
- URL `patch-notes-6-3e` → version `6_3e`
- URL `patch-notes-70` → version `7_0` (inserting underscore between major.minor)
- URL `patch-notes-70a` → version `7_0a`

### Implementation Notes
- The CI/CD workflow (`.github/workflows/auto-update-patch.yml`) automatically detects and converts both formats
- All internal file naming uses underscore format (`6_3e`, `7_0`)
- Scripts like `copy_v2.sh` work with both formats without modification
- Version detection tries old format first, then falls back to new format

## Important Notes
- Project tracks gold efficiency changes across Wild Rift patches
- Uses Jekyll for static site generation
- Python script calculates gold efficiency from item and stat data
- When executing python script, don't try to install requirements by yourself and creat a virtual environment, just execute with `python` directly
- I you recieve the patch-note with massive amount of texts, please refer to `_data/stats_{new_version}.yml` and focus on the changing of listed stats. Ignore the passive effect unless it effect the stats.
- When a item become more expensive, it's a nerf. When a item has greater stats, it's a buff. When a item got nerfed and buffed at the same time, it's a adjustment. Follow this rule to decide which patch_note.statuses does the item belong to.
