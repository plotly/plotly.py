#!/usr/bin/env bash

if [ ! -d $HOME/miniconda/ ]; then
    # Download miniconda
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

    chmod +x miniconda.sh

    # Install miniconda
    ./miniconda.sh -b -p $HOME/miniconda

    # Create environment
    # PYTHON_VERSION=3.6
    $HOME/miniconda/bin/conda install conda-build conda-verify
fi
