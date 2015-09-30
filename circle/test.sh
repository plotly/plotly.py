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

# PYENV shims need to be infront of the rest of the path to work!
echo "adding pyenv shims to the beginning of the path in this shell"
export PATH="/home/ubuntu/.pyenv/shims:$PATH"

# for each version we want, setup a functional virtual environment
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo Testing Python ${version}

    # exporting this variable (in this scope) chooses the python version
    export PYENV_VERSION=${version}
    echo "Using pyenv version $(pyenv version)"

    # this was a major issue previously, sanity check that we're using the
    # version we *think* we're using (that pyenv is pointing to)
    echo "Running: python -c 'import sys; print(sys.version)'. We've got:"
    python -c 'import sys; print(sys.version)'


    echo "install plotly (ignoring possibly cached versions)"
    pip install -I ${PLOTLY_PACKAGE_ROOT} >/dev/null ||
        error_exit "${LINENO}: can't install plotly package from project root"

    echo "import plotly to create .plotly dir if DNE"
    python -c 'import plotly' >/dev/null ||
        error_exit "${LINENO}: can't import plotly package"

    echo "running tests for Python ${version} as user '$(whoami)'"
    nosetests -x plotly/tests ||
        error_exit "${LINENO}: test suite failed for Python ${version}"

done
