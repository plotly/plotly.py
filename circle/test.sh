#!/bin/bash

echo "running test routine with python versions:"
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo "    ${version}"
done

PROGNAME=$(basename $0)
function error_exit
{
    echo "${PROGNAME}: ${1:-"Unknown Error"}\n" 1>&2
    exit 1
}

# for each version we want, setup a functional virtual environment
for version in ${PLOTLY_PYTHON_VERSIONS[@]}; do
    echo Testing Python ${version}

    # get rid of the current virtualenv if we're in one
    if [ ${VIRTUAL_ENV} ]; then
        deactivate
    fi

    # drop us into a virtualenv
    source ${PLOTLY_VENV_DIR}/${version}/bin/activate

    # install plotly (ignoring possibly cached versions)
    pip install -I ${PLOTLY_PACKAGE_ROOT}

    # import it once to make sure that works and to create .plotly dir if DNE
    python -c 'import plotly'

#    # test that it imports when you don't have file permissions
#    chmod 000 ${PLOTLY_CONFIG_DIR} && python -c "import plotly"
#
#    # test that setting permissions will work for import (and tests)
#    chmod 660 ${PLOTLY_CONFIG_DIR} && python -c "import plotly"

    if [ $version == '2.7' ]
    then
        nosetests -xv plotly/tests/test_core --with-coverage --cover-package=plotly
        coverage html -d ${CIRCLE_ARTIFACTS}
    else
        nosetests -xv plotly/tests/test_core
    fi
done
