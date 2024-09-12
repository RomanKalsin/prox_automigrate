#!/bin/bash

release=$(lsb_release -a | grep Release | awk '{print $2}')

apt update -y
apt install curl python3-venv python3-pip lz4 pv -y
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true
make install
make build

if [ "$release" = 12 ]
then
    apt install pipx python3-full -y    
    make package-installx
elif [ "$release" = 11 ]
then
    make package-install
fi

echo "for help 'prox-am -h'"
