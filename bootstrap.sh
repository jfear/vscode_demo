#!/bin/bash

# Create Conda Environment
if [ ! -f ./venv ]; then
    conda env create -f environment.yaml -p ./venv;
fi
