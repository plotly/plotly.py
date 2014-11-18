#!/bin/bash

PROGNAME=$(basename $0)
function error_exit
{
    echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
    exit 1
}

# for each version we want, setup a functional virtual environment
for version in ${PYTHON_VERSIONS[@]}; do
    echo Testing Python ${version}

    # get rid of the current virtualenv if we're in one
    if [ ${VIRTUAL_ENV} ]; then
        deactivate
    fi

    # drop us into a virtualenv
    source ~/venvs/${version}/bin/activate

    chmod 000 ${PLOTLY_CONFIG_DIR} && python -c "import plotly"

    chmod 600 ${PLOTLY_CONFIG_DIR} && python -c "import plotly"



    if [ $version == '2.7' ]
    then
        nosetests -xv plotly/tests/test_core --with-coverage --cover-package=plotly
        coverage html -d ${CIRCLE_ARTIFACTS}
    else
        nosetests -xv plotly/tests/test_core
    fi
done
