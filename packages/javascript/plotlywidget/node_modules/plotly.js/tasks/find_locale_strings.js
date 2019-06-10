var path = require('path');
var fs = require('fs');

var falafel = require('falafel');
var glob = require('glob');

var constants = require('./util/constants');
var srcGlob = path.join(constants.pathToSrc, '**/*.js');

var common = require('./util/common');

var EXIT_CODE = 0;

var localizeRE = /(^|[\.])(_|localize)$/;

var noOutput = process.argv.indexOf('--no-output') !== -1;

// main
findLocaleStrings();

function findLocaleStrings() {
    glob(srcGlob, function(err, files) {
        if(err) {
            EXIT_CODE = 1;
            console.log(err);
            return;
        }

        var dict = {};
        var hasTranslation = false;
        var maxLen = 0;

        files.forEach(function(file) {
            var code = fs.readFileSync(file, 'utf-8');
            var filePartialPath = file.substr(constants.pathToSrc.length);

            falafel(code, {locations: true}, function(node) {
                if(node.type === 'CallExpression' &&
                    (node.callee.name === '_' || node.callee.source() === 'Lib._')
                ) {
                    // parse through code string looking for translated strings
                    // You may either assign `Lib.localize` to `_` and use that, or
                    // call `Lib.localize` directly.

                    var strNode = node.arguments[1];
                    if(node.arguments.length !== 2) {
                        logError(file, node, 'Localize takes 2 args');
                    }
                    if(strNode.type !== 'Literal') {
                        logError(file, node, 'Translated string must be a literal');
                    }
                    if(!dict[strNode.value]) {
                        dict[strNode.value] = filePartialPath + ':' + node.loc.start.line;
                        maxLen = Math.max(maxLen, strNode.value.length);
                        hasTranslation = true;
                    }
                } else if(node.type === 'VariableDeclarator' && node.id.name === '_') {
                    // make sure localize is the only thing we assign to a variable `_`
                    // NB: this does not preclude using `_` for an unused function arg

                    var src = node.init.source();
                    if(!localizeRE.test(src)) {
                        logError(file, node, 'Use `_` only to mean localization');
                    }
                }
            });
        });

        if(!hasTranslation) {
            console.error('Found no translations.');
            EXIT_CODE = 1;
        }

        if(!EXIT_CODE) {
            if(noOutput) {
                console.log('ok find_locale_strings - no output requested.');
            } else {
                var strings = Object.keys(dict).sort().map(function(k) {
                    return k + spaces(maxLen - k.length) + '  // ' + dict[k];
                }).join('\n');
                common.writeFile(constants.pathToTranslationKeys, strings);
                console.log('ok find_locale_strings - wrote new key file.');
            }
        }
    });
}

function logError(file, node, msg) {
    console.error(file + ' [line ' + node.loc.start.line + '] ' + msg +
        '\n   ' + node.source());
    EXIT_CODE = 1;
}

function spaces(len) {
    var out = '';
    for(var i = 0; i < len; i++) out += ' ';
    return out;
}

process.on('exit', function() {
    if(EXIT_CODE) {
        throw new Error('find_locale_strings failed.');
    }
});
