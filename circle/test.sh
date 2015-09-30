#!/bin/bash

SIG="☁☀☂"

echo "${SIG} Running test routine with python versions:"
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo "${SIG}     ${version}"
done

PROGNAME=$(basename $0)
function error_exit
{
    echo -e "${SIG} ${PROGNAME}: ${1:-"Unknown Error"}\n" 1>&2
    exit 1
}

# PYENV shims need to be infront of the rest of the path to work!
echo "${SIG} Adding pyenv shims to the beginning of the path in this shell."
export PATH="/home/ubuntu/.pyenv/shims:$PATH"

# for each version we want, setup a functional virtual environment
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo "${SIG} Testing Python ${version}"

    # exporting this variable (in this scope) chooses the python version
    export PYENV_VERSION=${version}
    echo "${SIG} Using pyenv version $(pyenv version)."

    # this was a major issue previously, sanity check that we're using the
    # version we *think* we're using (that pyenv is pointing to)
    echo "${SIG} Running: python -c 'import sys; print(sys.version)'. We've got:"
    python -c 'import sys; print(sys.version)'


    echo "${SIG} Install plotly (ignoring possibly cached versions)."
    pip install -I ${PLOTLY_PACKAGE_ROOT} >/dev/null ||
        error_exit "${SIG} ${LINENO}: can't install plotly package from project root"

    echo "${SIG} Import plotly to create .plotly dir if DNE."
    python -c 'import plotly' >/dev/null ||
        error_exit "${SIG} ${LINENO}: can't import plotly package"

    echo "${SIG} Running tests for Python ${version} as user '$(whoami)'."
    nosetests -x plotly/tests ||
        error_exit "${SIG} ${LINENO}: test suite failed for Python ${version}"

done
