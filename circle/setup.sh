#!/bin/bash

echo "running setup routine with python versions:"
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo "    ${version}"
done

PROGNAME=$(basename $0)
function error_exit
{
    echo -e "${PROGNAME}: ${1:-"Unknown Error"}\n" 1>&2
    exit 1
}

# make our directory to stash some python virtual environments
if [ ! -d ${PLOTLY_VENV_DIR} ]; then
    mkdir ${PLOTLY_VENV_DIR}
fi

# for each version we want, setup a functional virtual environment
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo Setting up Python ${version}

    # exporting this variable (in this scope) chooses the python version
    export PYENV_VERSION=${version}

    echo "Using pyenv version $(pyenv version)"

#    # only create a pyvenv if it doesn't already exist
#    if [ ! -d ${PLOTLY_VENV_DIR}/${version} ]; then
#        virtualenv ${PLOTLY_VENV_DIR}/${version} ||
#            error_exit "${LINENO}: can't install virtualenv for ${version}"
#    fi
#
#    # get rid of the current virtualenv if we're in one
#    if [ ${VIRTUAL_ENV} ]; then
#        deactivate
#    fi

#    # drop us into a virtualenv
#    source ${PLOTLY_VENV_DIR}/${version}/bin/activate ||
#        error_exit "${LINENO}: can't activate virtualenv for Python ${version}"

    # install core requirements all versions need
    pip install -r ${PLOTLY_CORE_REQUIREMENTS_FILE} ||
        error_exit "${LINENO}: can't install core reqs for Python ${version}"

    # handle funkiness around python 2.6
    if [ ${version:0:3} == '2.6' ]
    then
        pip install simplejson ordereddict ||
            error_exit "${LINENO}: can't install extras for Python ${version}"
#        pip install -r ${PLOTLY_OPTIONAL_REQUIREMENTS_FILE_2_6}
#    else
#        pip install -r ${PLOTLY_OPTIONAL_REQUIREMENTS_FILE}
    fi

    # install some test tools
    pip install nose coverage ||
        error_exit "${LINENO}: can't install test tools for Python ${version}"
done
