#!/usr/bin/env bash

if [ ! -d $HOME/miniconda/envs/circle_optional ]; then
    # Download miniconda
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

    chmod +x miniconda.sh

    # Install miniconda
    ./miniconda.sh -b -p $HOME/miniconda

    # Create environment
    $HOME/miniconda/bin/conda create -n circle_optional --yes python=$PYTHON_VERSION poppler

    # Install orca into environment
    $HOME/miniconda/bin/conda install --yes -n circle_optional -c plotly plotly-orca==1.3.1

    # Install additional dependencies
    . /home/circleci/miniconda/etc/profile.d/conda.sh
    conda activate circle_optional
    cd packages/python/
    python -m pip install -r ./plotly/test_requirements/requirements_37_optional.txt
fi
