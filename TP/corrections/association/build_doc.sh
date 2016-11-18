#!/bin/bash

mkdir docs
cd docs

sphinx-quickstart

echo "mettre à jour l'accès (relatif) aux sources ..."
vim source/conf.py

launch_sphinx-apidoc.sh
