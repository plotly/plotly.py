#!/bin/bash

SIG="☁☀☂"

echo "${SIG} Running setup routine with Python versions:"
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
    echo "${SIG} Setting up Python ${version}"

    # exporting this variable (in this scope) chooses the python version
    export PYENV_VERSION=${version}
    echo "${SIG} Using pyenv version $(pyenv version)"

    # this was a major issue previously, sanity check that we're using the
    # version we *think* we're using (that pyenv is pointing to)
    echo "${SIG} python -c 'import sys; print(sys.version)'"
    python -c 'import sys; print(sys.version)'

    # install core requirements all versions need
    pip install -r ${PLOTLY_CORE_REQUIREMENTS_FILE} ||
        error_exit "${SIG} ${LINENO}: can't install core reqs for Python ${version}."

    pip install -r ${PLOTLY_OPTIONAL_REQUIREMENTS_FILE} ||
        error_exit "${SIG} ${LINENO}: can't install optional for Python ${version}."

    # install some test tools
    pip install nose coverage ||
        error_exit "${SIG} ${LINENO}: can't install test tools for Python ${version}."
done
