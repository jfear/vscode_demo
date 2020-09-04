#!/bin/bash

# Create Conda Environment
[ ! -d "./venv" ] && conda env create -f environment/environment.yaml -p ./venv
[ ! -d "./rvenv" ] && conda env create -f environment/r_environment.yaml -p ./rvenv
