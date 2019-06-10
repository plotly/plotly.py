var path = require('path');
var transformTools = require('browserify-transform-tools');
var constants = require('./constants');

var pathToStrictD3Module = path.join(
    constants.pathToImageTest,
    'strict-d3.js'
);
/**
 * Transform `require('d3')` expressions to `require(/path/to/strict-d3.js)`
 */

module.exports = transformTools.makeRequireTransform('requireTransform',
    { evaluateArguments: true, jsFilesOnly: true },
    function(args, opts, cb) {
        var pathIn = args[0];
        var pathOut;

        if(pathIn === 'd3' && opts.file !== pathToStrictD3Module) {
            // JSON.stringify: fix npm-scripts for windows users, for whom
            // path has \ in it, without stringify that turns into control chars.
            pathOut = 'require(' + JSON.stringify(pathToStrictD3Module) + ')';
        }

        if(pathOut) return cb(null, pathOut);
        else return cb();
    });
