var path = require('path');
var fs = require('fs-extra');
var exec = require('child_process').exec;
var runSeries = require('run-series');
var glob = require('glob');

var common = require('./util/common');
var constants = require('./util/constants');
var pkg = require('../package.json');

var year = (new Date()).getFullYear();

var copyrightAndLicense = [
    '## Copyright and license',
    '',
    'Code and documentation copyright ' + year + ' Plotly, Inc.',
    '',
    'Code released under the [MIT license](https://github.com/plotly/plotly.js/blob/master/LICENSE).',
    '',
    'Docs released under the [Creative Commons license](https://github.com/plotly/documentation/blob/source/LICENSE).',
    ''
].join('\n');

// sync "partial bundle" packages
constants.partialBundlePaths
    .map(function(d) {
        return {
            name: 'plotly.js-' + d.name + '-dist',
            index: d.index,
            main: 'plotly-' + d.name + '.js',
            dist: d.dist,
            desc: 'Ready-to-use plotly.js ' + d.name + ' distributed bundle.',
        };
    })
    .concat([{
        name: 'plotly.js-dist',
        index: path.join(constants.pathToLib, 'index.js'),
        main: 'plotly.js',
        dist: constants.pathToPlotlyDist,
        desc: 'Ready-to-use plotly.js distributed bundle.',
    }])
    .forEach(syncPartialBundlePkg);

// sync "locales" package
syncLocalesPkg({
    name: 'plotly.js-locales',
    dir: path.join(constants.pathToLib, 'locales'),
    main: 'index.js',
    desc: 'Ready-to-use plotly.js locales',
});

function syncPartialBundlePkg(d) {
    var pkgPath = path.join(constants.pathToBuild, d.name);

    var initDirectory = _initDirectory(d, pkgPath);

    function writePackageJSON(cb) {
        var cnt = {
            name: d.name,
            version: pkg.version,
            description: d.desc,
            license: pkg.license,
            main: d.main,
            repository: pkg.repository,
            bugs: pkg.bugs,
            author: pkg.author,
            keywords: pkg.keywords,
            files: [
                'LICENSE',
                'README.md',
                d.main
            ]
        };

        fs.writeFile(
            path.join(pkgPath, 'package.json'),
            JSON.stringify(cnt, null, 2) + '\n',
            cb
        );
    }


    function writeREADME(cb) {
        var moduleList = common.findModuleList(d.index);

        var cnt = [
            '# ' + d.name,
            '',
            d.desc,
            '',
            'Contains trace modules ' + common.formatEnumeration(moduleList) + '.',
            '',
            'For more info on plotly.js, go to https://github.com/plotly/plotly.js',
            '',
            '## Installation',
            '',
            '```',
            'npm install ' + d.name,
            '```',
            '## Usage',
            '',
            '```js',
            '// ES6 module',
            'import Plotly from \'' + d.name + '\';',
            '',
            '// CommonJS',
            'var Plotly = require(\'' + d.name + '\');',
            '```',
            '',
            copyrightAndLicense
        ];

        fs.writeFile(
            path.join(pkgPath, 'README.md'),
            cnt.join('\n'),
            cb
        );
    }

    function copyMain(cb) {
        fs.copy(d.dist, path.join(pkgPath, d.main), cb);
    }

    var copyLicense = _copyLicense(d, pkgPath);

    var publishToNPM = _publishToNPM(d, pkgPath);

    runSeries([
        initDirectory,
        writePackageJSON,
        writeREADME,
        copyMain,
        copyLicense,
        publishToNPM
    ], function(err) {
        if(err) throw err;
    });
}

function syncLocalesPkg(d) {
    var pkgPath = path.join(constants.pathToBuild, d.name);

    var initDirectory = _initDirectory(d, pkgPath);

    var localeFiles;
    function listLocalFiles(cb) {
        var localeGlob = path.join(constants.pathToLib, 'locales', '*.js');
        glob(localeGlob, function(err, _localeFiles) {
            if(err) cb(null);
            localeFiles = _localeFiles;
            cb();
        });
    }

    function writePackageJSON(cb) {
        var cnt = {
            name: d.name,
            version: pkg.version,
            description: d.desc,
            license: pkg.license,
            main: d.main,
            repository: pkg.repository,
            bugs: pkg.bugs,
            author: pkg.author,
            keywords: pkg.keywords,
            files: [
                'LICENSE',
                'README.md',
                d.main
            ].concat(localeFiles.map(function(f) { return path.basename(f); }))
        };

        fs.writeFile(
            path.join(pkgPath, 'package.json'),
            JSON.stringify(cnt, null, 2) + '\n',
            cb
        );
    }

    function writeREADME(cb) {
        var cnt = [
            '# ' + d.name,
            '',
            d.desc,
            '',
            'For more info on plotly.js, go to https://github.com/plotly/plotly.js',
            '',
            '## Installation',
            '',
            '```',
            'npm install ' + d.name,
            '```',
            '## Usage',
            '',
            'For example to setup the `fr` locale:',
            '',
            '```js',
            '// ES6 module',
            'import Plotly from \'plotly.js\';',
            'import locale from \'' + d.name + '/fr' + '\';',
            '',
            '// CommonJS',
            'var Plotly = require(\'plotly.js\');',
            'var locale = require(\'' + d.name + '/fr\');',
            '',
            '// then',
            'Plotly.register(locale);',
            'Plotly.setPlotConfig({locale: \'fr\'})',
            '```',
            '',
            copyrightAndLicense
        ];

        fs.writeFile(
            path.join(pkgPath, 'README.md'),
            cnt.join('\n'),
            cb
        );
    }

    function writeMain(cb) {
        var cnt = [constants.licenseSrc, ''];
        localeFiles.forEach(function(f) {
            var n = path.basename(f, '.js');
            cnt.push('exports[\'' + n + '\'] = require(\'./' + n + '.js\');');
        });
        cnt.push('');

        fs.writeFile(
            path.join(pkgPath, d.main),
            cnt.join('\n'),
            cb
        );
    }

    function copyLocaleFiles(cb) {
        runSeries(localeFiles.map(function(f) {
            return function(cb) {
                fs.copy(f, path.join(pkgPath, path.basename(f)), cb);
            };
        }), cb);
    }

    var copyLicense = _copyLicense(d, pkgPath);

    var publishToNPM = _publishToNPM(d, pkgPath);

    runSeries([
        initDirectory,
        listLocalFiles,
        writePackageJSON,
        writeREADME,
        writeMain,
        copyLocaleFiles,
        copyLicense,
        publishToNPM
    ], function(err) {
        if(err) throw err;
    });
}

function _initDirectory(d, pkgPath) {
    return function(cb) {
        if(common.doesDirExist(pkgPath)) {
            cb();
        } else {
            fs.mkdir(pkgPath, cb);
        }
    };
}

function _copyLicense(d, pkgPath) {
    return function(cb) {
        fs.copy(
            path.join(constants.pathToRoot, 'LICENSE'),
            path.join(pkgPath, 'LICENSE'),
            cb
        );
    };
}

function _publishToNPM(d, pkgPath) {
    return function(cb) {
        if(process.env.DRYRUN) {
            console.log('dry run, did not publish ' + d.name);
            cb();
            return;
        }
        exec('npm publish', {cwd: pkgPath}, cb).stdout.pipe(process.stdout);
    };
}
