var fs = require('fs');

var browserify = require('browserify');
var watchify = require('watchify');
var prettySize = require('prettysize');

var constants = require('./constants');
var common = require('./common');
var strictD3 = require('./strict_d3');

/**
 * Make a plotly.js browserify bundle function watched by watchify.
 *
 * N.B. This module is meant for dev builds; the output bundle is placed
 *      in plotly.js/build/
 *      Use `npm run build` for dist builds.
 *
 * @param {function} onFirstBundleCallback executed when first bundle is completed
 *
 */
module.exports = function makeWatchifiedBundle(onFirstBundleCallback) {
    var b = browserify(constants.pathToPlotlyIndex, {
        debug: true,
        standalone: 'Plotly',
        transform: [strictD3],
        cache: {},
        packageCache: {},
        plugin: [watchify]
    });

    var firstBundle = true;

    if(firstBundle) {
        console.log([
            '***',
            'Building the first bundle, this should take ~10 seconds',
            '***\n'
        ].join(' '));
    }

    b.on('update', bundle);
    formatBundleMsg(b, 'plotly.js');

    function bundle() {
        b.bundle(function(err) {
            if(err) console.error(JSON.stringify(String(err)));

            if(firstBundle) {
                onFirstBundleCallback();
                firstBundle = false;
            }
        })
        .pipe(
            fs.createWriteStream(constants.pathToPlotlyBuild)
        );
    }

    return bundle;
};

function formatBundleMsg(b, bundleName) {
    var msgParts = [
        bundleName, ':', '',
        'written', 'in', '', 'sec',
        '[', '', ']'
    ];

    b.on('bytes', function(bytes) {
        msgParts[2] = prettySize(bytes, true);
    });

    b.on('time', function(time) {
        msgParts[5] = (time / 1000).toFixed(2);
    });

    b.on('log', function() {
        var formattedTime = common.formatTime(new Date());

        msgParts[msgParts.length - 2] = formattedTime;

        console.log(msgParts.join(' '));
    });
}
