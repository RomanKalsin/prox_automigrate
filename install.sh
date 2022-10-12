#!/bin/bash

apt update -y
apt install curl python3-venv python3-pip lz4 -y
curl -sSL https://install.python-poetry.org | python3 - 
poetry config virtualenvs.in-project true
make install
make build
make package-install
echo "for help 'prox-am -h'"