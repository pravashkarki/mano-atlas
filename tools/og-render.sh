#!/bin/sh
# Render the Open Graph images: assets/og/src/<slug>.html -> assets/og/<slug>.png (1200x630).
# Run after `python3 build.py`. Needs Google Chrome; fonts load from Google Fonts, so be online.
set -e
cd "$(dirname "$0")/.."
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for f in assets/og/src/*.html; do
  slug=$(basename "$f" .html)
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --window-size=1200,630 --virtual-time-budget=6000 \
    --screenshot="assets/og/$slug.png" "file://$PWD/$f" >/dev/null 2>&1
  printf '%s ' "$slug"
done
echo
echo "rendered $(ls assets/og/*.png | wc -l | tr -d ' ') images"
