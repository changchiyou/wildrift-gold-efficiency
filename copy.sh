#!/bin/bash

# 檢查是否有提供足夠的參數
if [ $# -ne 2 ]; then
  echo "usage: $0 <old-version> <new-version>"
  exit 1
fi

# 取得輸入的參數
a=$1
b=$2

# 執行複製命令
cp "_pages/${a}.md" "_pages/${b}.md"
cp "_data/items_${a}.yml" "_data/items_${b}.yml"
cp "_data/stats_${a}.yml" "_data/stats_${b}.yml"

echo "${b}.md, items_${b}.yml, and stats_${b}.yml have been generated."