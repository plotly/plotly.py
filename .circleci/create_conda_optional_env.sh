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
    $HOME/miniconda/bin/conda create -n circle_optional --yes python=$PYTHON_VERSION

    # Install orca into environment
    $HOME/miniconda/bin/conda install --yes -n circle_optional -c plotly plotly-orca

    # Install requirements into environment
    $HOME/miniconda/bin/conda install --yes -n circle_optional --file requirements.txt
    $HOME/miniconda/bin/conda install --yes -n circle_optional numpy==1.11.3 ipython==5.1.0 jupyter==1.0.0 \
    pandas==0.19.2 scipy==0.18.1 shapely==1.6.4 geopandas==0.3.0 \
    pillow==5.2.0 psutil==5.4.6 pytest==3.5.1 mock==2.0.0 nose==1.3.3

    # conda-forge only
    $HOME/miniconda/bin/conda install --yes -n circle_optional -c conda-forge pyshp==1.2.10
fi
