#!/bin/sh

python3 ./tools/preformatter.py ./scripts/body.md ./output

npx vivliostyle build -o output/output.pdf