#!/bin/bash
for f in *.drawio; do
  drawio --export --format pdf --output . "$f"
  drawio --export --format svg --output . "$f"
done
