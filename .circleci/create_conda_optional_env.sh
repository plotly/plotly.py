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
    $HOME/miniconda/bin/conda create -n circle_optional --yes python==$PYTHON_VERSION \
requests six pytz retrying numpy ipython jupyter \
pandas scipy shapely geopandas \
pillow psutil pytest mock nose

    # Install orca into environment
    $HOME/miniconda/bin/conda install --yes -n circle_optional -c plotly plotly-orca

    # conda-forge only
    $HOME/miniconda/bin/conda install --yes -n circle_optional -c conda-forge pyshp
fi
