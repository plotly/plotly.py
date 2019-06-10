var fs = require('fs');
var path = require('path');

var minify = require('minify-stream');
var intoStream = require('into-stream');

var constants = require('./constants');

var prefix = 'Plotly.register(';
var suffix = ');';

var moduleMarker = 'module.exports = ';

/** Wrap a locale json file into a standalone js file
 *
 * @param {string} pathToInput path to the locale json file
 * @param {string} pathToOutput path to destination file
 *
 * Logs basename of bundle when completed.
 */
module.exports = function wrapLocale(pathToInput, pathToOutput) {
    fs.readFile(pathToInput, 'utf8', function(err, data) {
        var moduleStart = data.indexOf(moduleMarker) + moduleMarker.length;
        var moduleEnd = data.indexOf(';', moduleStart);

        var rawOut = prefix + data.substr(moduleStart, moduleEnd - moduleStart) + suffix;

        intoStream(rawOut)
            .pipe(minify(constants.uglifyOptions))
            .pipe(fs.createWriteStream(pathToOutput))
            .on('finish', function() {
                logger(pathToOutput);
            });
    });
};

function logger(pathToOutput) {
    var log = 'ok ' + path.basename(pathToOutput);

    console.log(log);
}
