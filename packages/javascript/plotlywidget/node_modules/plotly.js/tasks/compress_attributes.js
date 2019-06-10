var through = require('through2');

/**
 * Browserify transform that strips meta attributes out
 * of the plotly.js bundles
 */


// one line string with or without trailing comma
function makeStringRegex(attr) {
    return attr + ': \'.*\'' + ',?';
}

// joined array of strings with or without trailing comma
function makeJoinedArrayRegex(attr) {
    return attr + ': \\[[\\s\\S]*?\\]' + '\\.join\\(.*' + ',?';
}

// array with or without trailing comma
function makeArrayRegex(attr) {
    return attr + ': \\[[\\s\\S]*?\\]' + ',?';
}

// ref: http://www.regexr.com/3cmac
var regexStr = [
    makeStringRegex('description'),
    makeJoinedArrayRegex('description'),
    makeArrayRegex('requiredOpts'),
    makeArrayRegex('otherOpts'),
    makeStringRegex('hrName'),
    makeStringRegex('role')
].join('|');

var regex = new RegExp(regexStr, 'g');

module.exports = function() {
    return through(function(buf, enc, next) {
        this.push(
            buf.toString('utf-8')
               .replace(regex, '')
        );
        next();
    });
};
