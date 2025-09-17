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
5. Update `_pages/{new_version}/*.md` files if needed (don't forget to add items in patch_note.statuses based on items' adjustment)

## Important Notes
- Project tracks gold efficiency changes across Wild Rift patches
- Uses Jekyll for static site generation
- Python script calculates gold efficiency from item and stat data
- When executing python script, don't try to install requirements by yourself and creat a virtual environment, just execute with `python` directly
- I you recieve the patch-note with massive amount of texts, please refer to `_data/stats_{new_version}.yml` and focus on the changing of listed stats. Ignore the passive effect unless it effect the stats.
- When a item become more expensive, it's a nerf. When a item has greater stats, it's a buff. When a item got nerfed and buffed at the same time, it's a adjustment. Follow this rule to decide which patch_note.statuses does the item belong to.
