#!/usr/bin/env bash

set -e

rm -f combined-examples.json
find . -type f -name "*.json" | while read file; do echo "Processing $file"; cat "$file" >> combined-examples.json; done
