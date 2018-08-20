#!/usr/bin/env bash

if [ ! -d $HOME/miniconda/envs/circle_optional ]; then
    # Download miniconda
    # wget http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda.sh
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    chmod +x miniconda.sh

    # Install miniconda
    ./miniconda.sh -b -p $HOME/miniconda

    # Create environment
    # PYTHON_VERSION=3.6
    $HOME/miniconda/bin/conda create -n circle_optional --yes python==$PYTHON_VERSION

    # Install orca into environment
    $HOME/miniconda/bin/conda install --yes -n circle_optional -c plotly plotly-orca

    # Install requirements into environment
    $HOME/miniconda/bin/conda install --yes -n circle_optional requests \
six pytz retrying

    $HOME/miniconda/bin/conda install --yes -n circle_optional numpy ipython jupyter \
    pandas scipy shapely geopandas \
    pillow psutil pytest mock nose

    # conda-forge only
    $HOME/miniconda/bin/conda install --yes -n circle_optional -c conda-forge pyshp
fi
