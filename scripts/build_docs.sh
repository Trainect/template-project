#!/bin/bash

# run this script from the project root using `./scripts/build_docs.sh`

echo "-----------------------------------"
echo "Generating API reference via Sphinx"
echo "-----------------------------------"
cd docs || exit
rm -rf _autosummary
make clean
make html
cd .. || exit
