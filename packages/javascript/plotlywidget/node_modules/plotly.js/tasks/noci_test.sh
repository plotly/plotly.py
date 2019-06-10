#! /bin/bash
#
# Run tests that aren't ran on CI (yet)
#
# to run all no-ci tests
# $ (plotly.js) ./tasks/noci_test.sh
#
# to run jasmine no-ci tests
# $ (plotly.js) ./tasks/noci_test.sh jasmine

# to run image no-ci tests
# $ (plotly.js) ./tasks/noci_test.sh image
#
# -----------------------------------------------

EXIT_STATE=0
root=$(dirname $0)/..

# jasmine specs with @noCI tag
test_jasmine () {
    npm run test-jasmine -- --tags=noCI,noCIdep --nowatch || EXIT_STATE=$?
}

# mapbox image tests take too much resources on CI
#
# since the update to mapbox-gl@0.44.0, we must use orca
# as mapbox-gl versions >0.22.1 aren't supported on nw.js@0.12 used in the
# 'old' image server
#
# cone traces don't render correctly in the imagetest container
test_image () {
    $root/../orca/bin/orca.js graph \
        $root/test/image/mocks/mapbox_* \
        --plotly $root/build/plotly.js \
        --mapbox-access-token "pk.eyJ1IjoiZXRwaW5hcmQiLCJhIjoiY2luMHIzdHE0MGFxNXVubTRxczZ2YmUxaCJ9.hwWZful0U2CQxit4ItNsiQ" \
        --output-dir $root/test/image/baselines/ \
        --verbose || EXIT_STATE=$?
}

case $1 in
    jasmine)
        test_jasmine
        ;;
    image)
        test_image
        ;;
    *)
        test_jasmine
        test_image
        ;;
esac

exit $EXIT_STATE
