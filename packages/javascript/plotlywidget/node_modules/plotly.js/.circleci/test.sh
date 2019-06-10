#!/bin/bash

# override CircleCi's default run settings
set +e
set +o pipefail

ROOT=$(dirname $0)/..
EXIT_STATE=0
MAX_AUTO_RETRY=5

log () {
    echo -e "\n$1"
}

# inspired by https://unix.stackexchange.com/a/82602
retry () {
    local n=1

    until [ $n -ge $MAX_AUTO_RETRY ]; do
        "$@" --failFast && break
        log "run $n of $MAX_AUTO_RETRY failed, trying again ..."
        n=$[$n+1]
    done

    if [ $n -eq $MAX_AUTO_RETRY ]; then
        log "one last time, w/o failing fast"
        "$@" && n=0
    fi

    if [ $n -eq $MAX_AUTO_RETRY ]; then
        log "all $n runs failed, moving on."
        EXIT_STATE=1
    fi
}

# set timezone to Alaska time (arbitrary timezone to test date logic)
set_tz () {
    sudo cp /usr/share/zoneinfo/America/Anchorage /etc/localtime
    export TZ='America/Anchorage'
}

case $1 in

    jasmine)
        set_tz

        SUITE=$(circleci tests glob "$ROOT/test/jasmine/tests/*" | circleci tests split)
        npm run test-jasmine -- $SUITE --skip-tags=gl,noCI,flaky --showSkipped || EXIT_STATE=$?

        exit $EXIT_STATE
        ;;

    jasmine2)
        set_tz

        SHARDS=($(node $ROOT/tasks/shard_jasmine_tests.js --limit=5 --tag=gl | circleci tests split))
        for s in ${SHARDS[@]}; do
            retry npm run test-jasmine -- "$s" --tags=gl --skip-tags=noCI --showSkipped
        done

        exit $EXIT_STATE
        ;;

    jasmine3)
        set_tz

        SHARDS=($(node $ROOT/tasks/shard_jasmine_tests.js --limit=1 --tag=flaky | circleci tests split))

        for s in ${SHARDS[@]}; do
            retry npm run test-jasmine -- "$s" --tags=flaky --skip-tags=noCI --showSkipped
        done

        exit $EXIT_STATE
        ;;

    image)
        SUITE=$(find $ROOT/test/image/mocks/ -type f -printf "%f\n" | circleci tests split)
        npm run test-image -- $SUITE --filter || EXIT_STATE=$?
        exit $EXIT_STATE
        ;;

    image2)
        npm run test-export     || EXIT_STATE=$?
        exit $EXIT_STATE
        ;;

    bundle)
        set_tz
        npm run test-bundle || EXIT_STATE=$?
        exit $EXIT_STATE
        ;;

    syntax)
        npm run lint        || EXIT_STATE=$?
        npm run test-syntax || EXIT_STATE=$?
        exit $EXIT_STATE
        ;;

esac
