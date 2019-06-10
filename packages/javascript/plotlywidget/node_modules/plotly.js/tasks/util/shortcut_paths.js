var path = require('path');

var transformTools = require('browserify-transform-tools');

var constants = require('./constants');

/**
 * Transform require paths starting with '@' to appropriate folder paths
 */

var shortcutsConfig = {
    '@src': constants.pathToSrc,
    '@lib': constants.pathToLib,
    '@mocks': constants.pathToTestImageMocks,
    '@build': constants.pathToBuild
};

module.exports = transformTools.makeRequireTransform('requireTransform',
    { evaluateArguments: true, jsFilesOnly: true },
    function(args, opts, cb) {
        var pathIn = args[0];
        var pathOut;

        Object.keys(shortcutsConfig).forEach(function(k) {
            if(pathIn.indexOf(k) !== -1) {
                var tail = pathIn.split(k)[1];
                var newPath = path.join(shortcutsConfig[k], tail).replace(/\\/g, '/');
                pathOut = 'require(\'' + newPath + '\')';
            }
        });

        if(pathOut) return cb(null, pathOut);
        else return cb();
    });
