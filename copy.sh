#!/bin/bash

if [ $# -ne 2 ]; then
  echo "usage: $0 <old-version> <new-version>"
  exit 1
fi

old=$1
new=$2

cp "_pages/${old}.md" "_pages/${new}.md"
cp "_data/items_${old}.yml" "_data/items_${new}.yml"
cp "_data/stats_${old}.yml" "_data/stats_${new}.yml"

replace_underscore() {
  local text=$1
  local replacement=$2

  echo "${text//_/$replacement}"
}

# Text replacements in the new version file
sed -i "s/${old}/${new}/g" "_pages/${new}.md"
sed -i "s/$(replace_underscore $old '.')/$(replace_underscore $new '.')/g" "_pages/${new}.md"
sed -i "s/$(replace_underscore $old '-')/$(replace_underscore $new '-')/g" "_pages/${new}.md"

# Clear redirect_from and latest_version in the old version file
sed -i '/redirect_from:/d' "_pages/${old}.md"
sed -i '/latest_version:/d' "_pages/${old}.md"

# Update the date in the new version file
current_date=$(date +'%Y/%m/%d')
sed -i "s|date: .*|date: ${current_date}|g" "_pages/${new}.md"

# Update patch_note.compare.items/stats/item_prefix
sed -i "/patch_note:/,/^$/ { /compare:/,/^$/ s/items_.*/items_${old}/ }" "_pages/${new}.md"
sed -i "/patch_note:/,/^$/ { /compare:/,/^$/ s/stats_.*/stats_${old}/ }" "_pages/${new}.md"
sed -i "/patch_note:/,/^$/ { /compare:/,/^$/ s/item_prefix: [0-9]\.[0-9][a-z]/item_prefix: $(replace_underscore $old '.')/ }" "_pages/${new}.md"

echo "${new}.md, items_${new}.yml, and stats_${new}.yml have been generated."
