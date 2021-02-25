#!/bin/sh

mkdir sources
cp prog.py sources
cp Classes.py sources
zip -r sources.zip sources

for c in {a..f}; do
    python prog.py 'All Data Set'/$c.txt > $c.out.txt
done
