#!/bin/bash
# This script is intended for updating versions from 6.0d onwards.
# It copies the old folder content to a new folder and performs text replacements
# within markdown files, as well as updates certain metadata such as dates and file references.
#
# Portable across macOS (BSD) and Linux (GNU): no sed -i (flag semantics differ)
# and no nested sed ranges (unsupported by BSD sed). Frontmatter rewriting is
# done with POSIX awk via a temp file.
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
old_dash=${old//_/-}
new_dash=${new//_/-}
old_dot=${old//_/.}
new_dot=${new//_/.}

# Rewrite one markdown file for the new version (in place, via temp file).
# Handles: version string replacements, date, patch_note.statuses / excludes
# clearing, and pointing patch_note.compare back at the old version.
rewrite_md() {
  local file=$1
  local tmp
  tmp=$(mktemp) || return 1
  awk -v old="$old" -v new="$new" \
      -v old_dot="$old_dot" -v new_dot="$new_dot" \
      -v old_dash="$old_dash" -v new_dash="$new_dash" \
      -v new_date="$date_to_use" '
    function esc(s) { gsub(/[].[^$*[]/, "\\\\&", s); return s }
    function kv(line, val,   i) {
      i = index(line, ":")
      if (!i) return line
      return substr(line, 1, i) " " val
    }
    {
      # Global version replacements (underscore, dot, dash forms)
      gsub(esc(old), new)
      gsub(esc(old_dot), new_dot)
      gsub(esc(old_dash), new_dash)

      if ($0 ~ /^date:/) { print "date: " new_date; next }

      if ($0 ~ /^---$/ && NR > 1) { inpatch = 0; incompare = 0 }
      if ($0 ~ /^patch_note:/) inpatch = 1

      if (inpatch) {
        if ($0 ~ /^[[:space:]]+compare:/) { incompare = 1; print; next }
        if ($0 ~ /^[[:space:]]+(buffed|adjusted|nerfed|new):/) { print kv($0, "\"\""); next }
        if ($0 ~ /^[[:space:]]+excludes:/)       { print kv($0, "\"\""); next }
        if ($0 ~ /^[[:space:]]+excludes_sep:/)   { print kv($0, "\",\""); next }
        if (incompare) {
          if ($0 ~ /^[[:space:]]+items:/)        { print kv($0, "items_" old); next }
          if ($0 ~ /^[[:space:]]+stats:/)        { print kv($0, "stats_" old); next }
          if ($0 ~ /^[[:space:]]+item_prefix:/)  { print kv($0, old_dot); next }
          if ($0 ~ /^[[:space:]]+force:/)        { print kv($0, "\"\""); next }
          if ($0 ~ /^[[:space:]]+force_sep:/)    { print kv($0, "\"\""); next }
        }
      }
      print
    }
  ' "$file" > "$tmp" || { rm -f "$tmp"; return 1; }
  mv "$tmp" "$file"
}

# Strip the redirect_from block and latest_version flag (file is no longer latest).
strip_latest() {
  local file=$1
  local tmp
  tmp=$(mktemp) || return 1
  awk '
    {
      if (!skip && $0 ~ /^redirect_from:/) { skip = 1; next }
      if (skip) {
        # the block ends at the first non-indented line (also removed)
        if ($0 !~ /^[[:space:]]/) skip = 0
        next
      }
      if ($0 ~ /^latest_version:/) next
      print
    }
  ' "$file" > "$tmp" || { rm -f "$tmp"; return 1; }
  mv "$tmp" "$file"
}

# Copy the entire old folder to a new folder
cp -r "_pages/${old}/." "_pages/${new}"
cp "_data/items_${old}.yml" "_data/items_${new}.yml"
cp "_data/stats_${old}.yml" "_data/stats_${new}.yml"

# Rewrite all *.md files in the new folder for the new version
find "_pages/${new}" -type f -name '*.md' | while read -r file; do
  rewrite_md "$file" || exit 1
done

# Clear redirect_from block and latest_version in the old version files
find "_pages/${old}" -type f -name '*.md' | while read -r file; do
  strip_latest "$file" || exit 1
done

echo "${new} folder, items_${new}.yml, and stats_${new}.yml have been generated."
