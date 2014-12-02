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
    echo "Using pyenv version $(pyenv version)"

    echo "install plotly (ignoring possibly cached versions)"
    pip install -I ${PLOTLY_PACKAGE_ROOT} ||
        error_exit "${LINENO}: can't install plotly package from project root"

    echo "import plotly to create .plotly dir if DNE"
    python -c 'import plotly' ||
        error_exit "${LINENO}: can't import plotly package"

#    echo "${HOME}"
#    echo "${PLOTLY_CONFIG_DIR}"
#
#    # test that it imports when you don't have write permissions
#    sudo chmod -R 444 ${PLOTLY_CONFIG_DIR} && python -c "import plotly" ||
#        error_exit "${LINENO}: permissions test 444 on .plotly dir failed"
#
#    # test that setting write permissions will work for import (and tests)
#    sudo chmod -R 666 ${PLOTLY_CONFIG_DIR} && python -c "import plotly" ||
#        error_exit "${LINENO}: permissions test 666 on .plotly dir failed"

    echo "running tests for Python ${version} as user '$(whoami)'"
    nosetests -xv plotly/tests --with-coverage --cover-package=plotly ||
        error_exit "${LINENO}: test suite failed for Python ${version}"
    mkdir "${CIRCLE_ARTIFACTS}/${PYENV_VERSION}" || true
    coverage html -d "${CIRCLE_ARTIFACTS}/${PYENV_VERSION}" \
        --title=${PYENV_VERSION}

done
