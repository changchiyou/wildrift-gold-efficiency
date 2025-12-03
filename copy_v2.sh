#!/bin/bash
# This script is intended for updating versions from 6.0d onwards.
# It copies the old folder content to a new folder and performs text replacements
# within markdown files, as well as updates certain metadata such as dates and file references.
if [ $# -lt 2 ] || [ $# -gt 3 ]; then
  echo "usage: $0 <old-version> <new-version> [date]"
  exit 1
fi
old=$1
new=$2
custom_date=$3

# Validate date format (YYYY/MM/DD)
validate_date() {
  local date=$1
  if [[ $date =~ ^[0-9]{4}/[0-9]{2}/[0-9]{2}$ ]]; then
    return 0
  else
    return 1
  fi
}

# Determine the date to use
if [ -n "$custom_date" ]; then
  if validate_date "$custom_date"; then
    date_to_use=$custom_date
  else
    echo "Error: Invalid date format. Please use YYYY/MM/DD."
    exit 1
  fi
else
  date_to_use=$(date +'%Y/%m/%d')
fi

# Copy the entire old folder to a new folder
cp -r "_pages/${old}" "_pages/${new}"
cp "_data/items_${old}.yml" "_data/items_${new}.yml"
cp "_data/stats_${old}.yml" "_data/stats_${new}.yml"

replace_underscore() {
  local text=$1
  local replacement=$2
  echo "${text//_/$replacement}"
}

# Find all *.md files in the new folder and apply text replacements
find "_pages/${new}" -type f -name '*.md' | while read -r file; do
  # Text replacements in the new version file
  sed -i "s/${old}/${new}/g" "$file"
  sed -i "s/$(replace_underscore $old '\.')/$(replace_underscore $new '\.')/g" "$file"
  sed -i "s/$(replace_underscore $old '-')/$(replace_underscore $new '-')/g" "$file"
  # Update the date in the new version file
  sed -i "s|date: .*|date: ${date_to_use}|g" "$file"
  # Update patch_note.compare.items/stats/item_prefix
  sed -i "/patch_note:/,/^$/ { /compare:/,/^$/ s/items_.*/items_${old}/ }" "$file"
  sed -i "/patch_note:/,/^$/ { /compare:/,/^$/ s/stats_.*/stats_${old}/ }" "$file"
  sed -i "/patch_note:/,/^$/ { /compare:/,/^$/ s/item_prefix: [0-9]\.[0-9][a-z]/item_prefix: $(replace_underscore $old '.')/ }" "$file"
  # Clear patch_note.statuses.buffed/adjusted/nerfed/new
  sed -i "/patch_note:/,/}/ {
    /statuses:/,/}/ {
      s/buffed: .*/buffed: \"\"/
      s/adjusted: .*/adjusted: \"\"/
      s/nerfed: .*/nerfed: \"\"/
      s/new: .*/new: \"\"/
    }
  }" "$file"
  # Clear patch_note.excludes
  sed -i "/patch_note:/,/}/ {
    s/excludes: .*/excludes: \"\"/
  }" "$file"
  # Clear patch_note.compare.force/force_sep/excludes
  sed -i "/patch_note:/,/}/ {
    /compare:/,/}/ {
      s/force: .*/force: \"\"/
      s/force_sep: .*/force_sep: \"\"/
      s/excludes: .*/excludes: \"\"/
    }
  }" "$file"
done

# Clear redirect_from block and latest_version in the old version files
find "_pages/${old}" -type f -name '*.md' | while read -r file; do
  sed -i '/redirect_from:/,/^[^ ]/d' "$file"
  sed -i '/latest_version:/d' "$file"
done

echo "${new} folder, items_${new}.yml, and stats_${new}.yml have been generated."

