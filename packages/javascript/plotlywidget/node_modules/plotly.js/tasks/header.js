var path = require('path');
var fs = require('fs');

var prependFile = require('prepend-file');
var falafel = require('falafel');
var glob = require('glob');

var constants = require('./util/constants');
var common = require('./util/common');

// main
addHeadersInDistFiles();
updateHeadersInSrcFiles();

// add headers to dist files
function addHeadersInDistFiles() {
    function _prepend(path, header) {
        prependFile(path, header + '\n', common.throwOnError);
    }

    // add header to main dist bundles
    var pathsDist = [
        constants.pathToPlotlyDistMin,
        constants.pathToPlotlyDist,
        constants.pathToPlotlyDistWithMeta,
        constants.pathToPlotlyGeoAssetsDist
    ];
    pathsDist.forEach(function(path) {
        _prepend(path, constants.licenseDist);
    });

    // add header and bundle name to partial bundle
    constants.partialBundlePaths.forEach(function(pathObj) {
        var headerDist = constants.licenseDist
            .replace('plotly.js', 'plotly.js (' + pathObj.name + ')');
        _prepend(pathObj.dist, headerDist);

        var headerDistMin = constants.licenseDist
            .replace('plotly.js', 'plotly.js (' + pathObj.name + ' - minified)');
        _prepend(pathObj.distMin, headerDistMin);
    });
}

// add or update header to src/ lib/ files
function updateHeadersInSrcFiles() {
    var srcGlob = path.join(constants.pathToSrc, '**/*.js');
    var libGlob = path.join(constants.pathToLib, '**/*.js');

    // remove leading '/*' and trailing '*/' for comparison with falafel output
    var licenseSrc = constants.licenseSrc;
    var licenseStr = licenseSrc.substring(2, licenseSrc.length - 2);

    glob('{' + srcGlob + ',' + libGlob + '}', function(err, files) {
        files.forEach(function(file) {
            fs.readFile(file, 'utf-8', function(err, code) {
                // parse through code string while keeping track of comments
                var comments = [];
                falafel(code, {onComment: comments, locations: true}, function() {});

                var header = comments[0];

                // error out if no header is found
                if(!header || header.loc.start.line > 1) {
                    throw new Error(file + ' : has no header information.');
                }

                // if header and license are the same, do nothing
                if(isCorrect(header)) return;

                // if header and license only differ by date, update header
                else if(hasWrongDate(header)) {
                    var codeLines = code.split('\n');

                    codeLines.splice(header.loc.start.line - 1, header.loc.end.line);

                    var newCode = licenseSrc + '\n' + codeLines.join('\n');

                    common.writeFile(file, newCode);
                } else {
                    // otherwise, throw an error
                    throw new Error(file + ' : has wrong header information.');
                }
            });
        });
    });

    function isCorrect(header) {
        return (
            header.value.replace(/\s+$/gm, '') ===
            licenseStr.replace(/\s+$/gm, '')
        );
    }

    function hasWrongDate(header) {
        var regex = /Copyright 20[0-9][0-9]-20[0-9][0-9]/g;

        return (header.value.replace(regex, '') === licenseStr.replace(regex, ''));
    }
}
