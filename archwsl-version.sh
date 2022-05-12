#!/bin/sh
V="22.3.18.0"
echo "current: $V"
echo -n " latest: "
curl -s -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/yuk7/ArchWSL/releases | \
  grep "tag_name" | \
  head -1 | cut -c 18-26

