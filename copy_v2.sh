#!/bin/bash

# This script is intended for updating versions from 6.0d onwards.
# It copies the old folder content to a new folder and performs text replacements 
# within markdown files, as well as updates certain metadata such as dates and file references.

if [ $# -ne 2 ]; then
  echo "usage: $0 <old-version> <new-version>"
  exit 1
fi

old=$1
new=$2

# Copy the entire old folder to new folder
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
  current_date=$(date +'%Y/%m/%d')
  sed -i "s|date: .*|date: ${current_date}|g" "$file"

  # Update patch_note.compare.items/stats/item_prefix
  sed -i "/patch_note:/,/^$/ { /compare:/,/^$/ s/items_.*/items_${old}/ }" "$file"
  sed -i "/patch_note:/,/^$/ { /compare:/,/^$/ s/stats_.*/stats_${old}/ }" "$file"
  sed -i "/patch_note:/,/^$/ { /compare:/,/^$/ s/item_prefix: [0-9]\.[0-9][a-z]/item_prefix: $(replace_underscore $old '.')/ }" "$file"
done

# Clear redirect_from block and latest_version in the old version files
find "_pages/${old}" -type f -name '*.md' | while read -r file; do
  sed -i '/redirect_from:/,/^[^ ]/d' "$file"
  sed -i '/latest_version:/d' "$file"
done

echo "${new} folder, items_${new}.yml, and stats_${new}.yml have been generated."
