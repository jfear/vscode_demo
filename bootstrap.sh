#!/bin/bash

# Create Conda Environment
[ ! -d "./venv" ] && conda env create -f environment.yaml -p ./venv
[ ! -d "./rvenv" ] && conda env create -f r_environment.yaml -p ./rvenv
