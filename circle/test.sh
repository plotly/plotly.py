#!/bin/bash

echo "running test routine with python versions:"
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo "    ${version}"
done

PROGNAME=$(basename $0)
function error_exit
{
    echo -e "${PROGNAME}: ${1:-"Unknown Error"}\n" 1>&2
    exit 1
}

# for each version we want, setup a functional virtual environment
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo Testing Python ${version}

    # exporting this variable (in this scope) chooses the python version
    export PYENV_VERSION=${version}

    echo "get rid of the current virtualenv if we're in one"
    if [ ${VIRTUAL_ENV} ]; then
        deactivate
    fi

    echo "drop us into a virtualenv"
    source ${PLOTLY_VENV_DIR}/${version}/bin/activate ||
        error_exit "${LINENO}: can't activate virtualenv for Python ${version}"

    echo "install plotly (ignoring possibly cached versions)"
    pip install -I ${PLOTLY_PACKAGE_ROOT} ||
        error_exit "${LINENO}: can't install plotly package from project root"

    echo "import plotly to create .plotly dir if DNE"
    python -c 'import plotly' ||
        error_exit "${LINENO}: can't import plotly package"

#    # test that it imports when you don't have file permissions
#    chmod 000 ${PLOTLY_CONFIG_DIR} && python -c "import plotly"
#
#    # test that setting permissions will work for import (and tests)
#    chmod 660 ${PLOTLY_CONFIG_DIR} && python -c "import plotly"

    echo "running tests"
    if [ ${version:0:3} == '2.7' ]
    then
        nosetests -xv plotly/tests/test_core \
            --with-coverage \
            --cover-package=plotly ||
            error_exit "${LINENO}: test suite failed for Python ${version}"
        coverage html -d ${CIRCLE_ARTIFACTS}
    else
        nosetests -xv plotly/tests/test_core ||
            error_exit "${LINENO}: test suite failed for Python ${version}"
    fi
done
