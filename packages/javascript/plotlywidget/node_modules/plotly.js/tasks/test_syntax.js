var path = require('path');
var fs = require('fs');

var falafel = require('falafel');
var glob = require('glob');
var madge = require('madge');
var readLastLines = require('read-last-lines');
var eslint = require('eslint');
var trueCasePath = require('true-case-path');

var common = require('./util/common');
var isJasmineTestIt = common.isJasmineTestIt;
var isJasmineTestDescribe = common.isJasmineTestDescribe;
var hasJasmineTestTag = common.hasJasmineTestTag;

var constants = require('./util/constants');
var srcGlob = path.join(constants.pathToSrc, '**/*.js');
var libGlob = path.join(constants.pathToLib, '**/*.js');
var testGlob = path.join(constants.pathToJasmineTests, '**/*.js');
var bundleTestGlob = path.join(constants.pathToJasmineBundleTests, '**/*.js');

var EXIT_CODE = 0;

// main
assertJasmineSuites();
assertSrcContents();
assertFileNames();
assertTrailingNewLine();
assertCircularDeps();
assertES5();


// check for for focus and exclude jasmine blocks
function assertJasmineSuites() {
    var BLACK_LIST = ['fdescribe', 'fit', 'xdescribe', 'xit'];
    var TAGS = ['noCI', 'noCIdep', 'gl', 'flaky'];
    var IT_ONLY_TAGS = ['gl', 'flaky'];
    var logs = [];

    var addTagPrefix = function(t) { return '@' + t; };

    glob(combineGlobs([testGlob, bundleTestGlob]), function(err, files) {
        files.forEach(function(file) {
            var code = fs.readFileSync(file, 'utf-8');
            var bn = path.basename(file);

            falafel(code, {locations: true}, function(node) {
                var lineInfo = '[line ' + node.loc.start.line + '] :';

                if(node.type === 'Identifier' && BLACK_LIST.indexOf(node.name) !== -1) {
                    logs.push([
                        bn, lineInfo,
                        'contains either a *fdescribe*, *fit*,',
                        '*xdescribe* or *xit* block.'
                    ].join(' '));
                }

                if(isJasmineTestIt(node)) {
                    if(hasJasmineTestTag(node)) {
                        if(TAGS.every(function(t) { return !hasJasmineTestTag(node, t); })) {
                            logs.push([
                                bn, lineInfo,
                                'contains an unrecognized tag,',
                                'not one of: ' + TAGS.map(addTagPrefix).join(', ')
                            ].join(' '));
                        }
                    }

                    if(hasJasmineTestTag(node, 'gl') && hasJasmineTestTag(node, 'flaky')) {
                        logs.push([
                            bn, lineInfo,
                            'contains a @gl tag AND a @flaky tag, which is not allowed'
                        ].join(' '));
                    }
                }

                IT_ONLY_TAGS.forEach(function(t) {
                    if(isJasmineTestDescribe(node, t)) {
                        logs.push([
                            bn, lineInfo,
                            'contains a', addTagPrefix(t), 'tag is a *describe* block,',
                            addTagPrefix(t), 'tags are only allowed in jasmine *it* blocks.'
                        ].join(' '));
                    }
                });
            });
        });

        log('no jasmine suites focus/exclude blocks or wrong tag patterns', logs);
    });
}

/*
 * tests about the contents of source (and lib) files:
 * - check for header comment
 * - check that we don't have any features that break in IE
 * - check that we don't use getComputedStyle unexpectedly
 * - check that require statements use lowercase (to match assertFileNames)
 *   or match the case of the source file
 */
function assertSrcContents() {
    var licenseSrc = constants.licenseSrc;
    var licenseStr = licenseSrc.substring(2, licenseSrc.length - 2);
    var logs = [];

    // These are forbidden in IE *only in SVG* but since
    // that's 99% of what we do here, we'll forbid them entirely
    // until there's some HTML use case where we need them.
    // (not sure what we'd do then, but we'd think of something!)
    var IE_SVG_BLACK_LIST = ['innerHTML', 'parentElement', 'children'];

    // Forbidden in IE in any context
    var IE_BLACK_LIST = ['classList'];

    // not implemented in FF, or inconsistent with others
    var FF_BLACK_LIST = ['offsetX', 'offsetY'];

    // require'd built-in modules
    var BUILTINS = ['events'];

    var getComputedStyleCnt = 0;

    glob(combineGlobs([srcGlob, libGlob]), function(err, files) {
        files.forEach(function(file) {
            var code = fs.readFileSync(file, 'utf-8');

            // parse through code string while keeping track of comments
            var comments = [];
            falafel(code, {onComment: comments, locations: true}, function(node) {
                // look for .classList
                if(node.type === 'MemberExpression') {
                    var source = node.source();
                    var parts = source.split('.');
                    var lastPart = parts[parts.length - 1];

                    if(source === 'Math.sign') {
                        logs.push(file + ' : contains Math.sign (IE failure)');
                    } else if(source === 'window.getComputedStyle') {
                        getComputedStyleCnt++;
                    } else if(IE_BLACK_LIST.indexOf(lastPart) !== -1) {
                        logs.push(file + ' : contains .' + lastPart + ' (IE failure)');
                    } else if(IE_SVG_BLACK_LIST.indexOf(lastPart) !== -1) {
                        // add special case for sunburst where we use 'children'
                        // off the d3-hierarchy output
                        var dirParts = path.dirname(file).split(path.sep);
                        var isSunburstFile = dirParts[dirParts.length - 1] === 'sunburst';
                        var isLinkedToObject = ['pt', 'd', 'parent'].indexOf(parts[parts.length - 2]) !== -1;
                        if(!(isSunburstFile && isLinkedToObject)) {
                            logs.push(file + ' : contains .' + lastPart + ' (IE failure in SVG)');
                        }
                    } else if(FF_BLACK_LIST.indexOf(lastPart) !== -1) {
                        logs.push(file + ' : contains .' + lastPart + ' (FF failure)');
                    }
                } else if(node.type === 'Identifier' && node.source() === 'getComputedStyle') {
                    if(node.parent.source() !== 'window.getComputedStyle') {
                        logs.push(file + ' : getComputedStyle must be called as a `window` property.');
                    }
                } else if(node.type === 'CallExpression' && node.callee.name === 'require') {
                    var pathNode = node.arguments[0];
                    var pathStr = pathNode.value;
                    if(pathNode.type !== 'Literal') {
                        logs.push(file + ' : You may only `require` literals.');
                    } else if(BUILTINS.indexOf(pathStr) === -1) {
                        // node version 8.9.0+ can use require.resolve(request, {paths: [...]})
                        // and avoid this explicit conversion to the current location
                        if(pathStr.charAt(0) === '.') {
                            pathStr = path.relative(__dirname, path.join(path.dirname(file), pathStr));
                        }
                        var fullPath = require.resolve(pathStr);
                        var casedPath = trueCasePath(fullPath);

                        if(fullPath !== trueCasePath(fullPath)) {
                            logs.push(file + ' : `require` path is not case-correct:\n' +
                                fullPath + ' -> ' + casedPath);
                        }
                    }
                }
            });

            var header = comments[0];

            if(!header || header.loc.start.line > 1) {
                logs.push(file + ' : has no header information.');
                return;
            }

            if(header.value !== licenseStr) {
                logs.push(file + ' : has incorrect header information.');
            }
        });

        /*
         * window.getComputedStyle calls are restricted, so we want to be
         * explicit about it whenever we add or remove these calls. This is
         * the reason d3.selection.style is forbidden as a getter.
         *
         * The rule is:
         * - You MAY NOT call getComputedStyle during rendering a plot, EXCEPT
         *   in calculating autosize for the plot (which only makes sense if
         *   the plot is displayed). Other uses of getComputedStyle while
         *   rendering will fail, at least in Chrome, if the plot div is not
         *   attached to the DOM.
         *
         * - You MAY call getComputedStyle during interactions (hover etc)
         *   because at that point it's known that the plot is displayed.
         *
         * - You must use the explicit `window.getComputedStyle` rather than
         *   the implicit global scope `getComputedStyle` for jsdom compat.
         *
         * - If you use conforms to these rules, you may update
         *   KNOWN_GET_COMPUTED_STYLE_CALLS to count the new use.
         */
        var KNOWN_GET_COMPUTED_STYLE_CALLS = 5;
        if(getComputedStyleCnt !== KNOWN_GET_COMPUTED_STYLE_CALLS) {
            logs.push('Expected ' + KNOWN_GET_COMPUTED_STYLE_CALLS +
                ' window.getComputedStyle calls, found ' + getComputedStyleCnt +
                '. See ' + __filename + ' for details how to proceed.');
        }

        log('correct headers and contents in lib/ and src/', logs);
    });
}

// check that all file names are in lower case
function assertFileNames() {
    var pattern = combineGlobs([
        path.join(constants.pathToRoot, '*.*'),
        path.join(constants.pathToSrc, '**/*.*'),
        path.join(constants.pathToLib, '**/*.*'),
        path.join(constants.pathToDist, '**/*.*'),
        path.join(constants.pathToRoot, 'test', '**/*.*'),
        path.join(constants.pathToRoot, 'tasks', '**/*.*'),
        path.join(constants.pathToRoot, 'devtools', '**/*.*')
    ]);

    var logs = [];

    glob(pattern, function(err, files) {
        files.forEach(function(file) {
            var base = path.basename(file);

            if(
                base === 'README.md' ||
                base === 'CONTRIBUTING.md' ||
                base === 'CHANGELOG.md' ||
                base === 'SECURITY.md' ||
                base === 'BUILDING.md' ||
                file.indexOf('mathjax') !== -1
            ) return;

            if(base !== base.toLowerCase()) {
                logs.push([
                    file, ':',
                    'has a file name containing some',
                    'non-lower-case characters'
                ].join(' '));
            }
        });

        log('lower case only file names', logs);
    });
}

// check that all files have a trailing new line character
function assertTrailingNewLine() {
    var pattern = combineGlobs([
        path.join(constants.pathToSrc, '**/*.glsl'),
        path.join(constants.pathToRoot, 'test', 'image', 'mocks', '*')
    ]);

    var regexNewLine = /\r?\n$/;
    var regexEmptyNewLine = /^\r?\n$/;
    var promises = [];
    var logs = [];

    glob(pattern, function(err, files) {
        files.forEach(function(file) {
            var promise = readLastLines.read(file, 1);

            promises.push(promise);

            promise.then(function(lines) {
                if(!regexNewLine.test(lines)) {
                    logs.push([
                        file, ':',
                        'does not have a trailing new line character'
                    ].join(' '));
                } else if(regexEmptyNewLine.test(lines)) {
                    logs.push([
                        file, ':',
                        'has more than one trailing new line'
                    ].join(' '));
                }
            });
        });

        Promise.all(promises).then(function() {
            log('trailing new line character', logs);
        });
    });
}

// check circular dependencies
function assertCircularDeps() {
    madge(constants.pathToSrc).then(function(res) {
        var circularDeps = res.circular();
        var logs = [];

        if(circularDeps.length) {
            console.log(circularDeps.join('\n'));
            logs.push('some circular dependencies were found in src/');
        }

        log('circular dependencies: ' + circularDeps.length, logs);
    });
}

// Ensure no ES6 has snuck through into the build:
function assertES5() {
    var CLIEngine = eslint.CLIEngine;

    var cli = new CLIEngine({
        useEslintrc: false,
        ignore: false,
        parserOptions: {
            ecmaVersion: 5
        }
    });

    var files = constants.partialBundlePaths.map(function(f) { return f.dist; });
    files.unshift(constants.pathToPlotlyBuild, constants.pathToPlotlyDist);

    var report = cli.executeOnFiles(files);
    var formatter = cli.getFormatter();

    var errors = [];
    if(report.errorCount > 0) {
        console.log(formatter(report.results));

        // It doesn't work well to pass formatted logs into this,
        // so instead pass the empty string in a way that causes
        // the test to fail
        errors.push('');
    }

    log('es5-only syntax', errors);
}


function combineGlobs(arr) {
    return '{' + arr.join(',') + '}';
}

function log(name, logs) {
    if(logs.length) {
        console.error('test-syntax error [' + name + ']');
        console.error(logs.join('\n'));
        EXIT_CODE = 1;
    } else {
        console.log('ok ' + name);
    }
}

process.on('exit', function() {
    if(EXIT_CODE) {
        throw new Error('test syntax failed.');
    }
});
