var path = require('path');
var fs = require('fs');

var gzipSize = require('gzip-size');
var prettySize = require('prettysize');

var common = require('./util/common');
var constants = require('./util/constants');
var pkg = require('../package.json');

var pathDistREADME = path.join(constants.pathToDist, 'README.md');
var cdnRoot = 'https://cdn.plot.ly/plotly-';

var ENC = 'utf-8';
var JS = '.js';
var MINJS = '.min.js';

// main
common.writeFile(pathDistREADME, getReadMeContent());

function getReadMeContent() {
    return []
        .concat(getInfoContent())
        .concat(getMainBundleInfo())
        .concat(getPartialBundleInfo())
        .concat(getFooter())
        .join('\n');
}

// general info about distributed files
function getInfoContent() {
    return [
        '# Using distributed files',
        '',
        'All plotly.js dist bundles inject an object `Plotly` into the global scope.',
        '',
        'Import plotly.js as:',
        '',
        '```html',
        '<script src="plotly.min.js"></script>',
        '```',
        '',
        'or the un-minified version as:',
        '',
        '```html',
        '<script src="plotly.js" charset="utf-8"></script>',
        '```',
        '',
        '### To support IE9',
        '',
        '*Before* the plotly.js script tag, add:',
        '',
        '```html',
        '<script>if(typeof window.Int16Array !== \'function\')document.write("<scri"+"pt src=\'extras/typedarray.min.js\'></scr"+"ipt>");</script>',
        '<script>document.write("<scri"+"pt src=\'extras/request_animation_frame.js\'></scr"+"ipt>");</script>',
        '```',
        '',
        '### To support MathJax',
        '',
        '*Before* the plotly.js script tag, add:',
        '',
        '```html',
        '<script src="mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>',
        '```',
        '',
        'You can grab the relevant MathJax files in `./dist/extras/mathjax/`.',
        '',
        'By default, plotly.js will modify the global MathJax configuration on load.',
        'This can lead to undesirable behavior if plotly.js is loaded alongside',
        'other libraries that also rely on MathJax. To disable this global configuration',
        'process, set the `MathJaxConfig` property to `\'local\'` in the `window.PlotlyConfig`',
        'object.  This property must be set before the plotly.js script tag, for example:',
        '',
        '```html',
        '<script>',
        '   window.PlotlyConfig = {MathJaxConfig: \'local\'}',
        '</script>',
        '<script src="plotly.min.js"></script>',
        '```',
        '',
        '### To include localization',
        '',
        'Plotly.js defaults to US English (en-US) and includes British English (en) in the standard bundle.',
        'Many other localizations are available - here is an example using Swiss-German (de-CH),',
        'see the contents of this directory for the full list.',
        'They are also available on our CDN as ' + cdnRoot + 'locale-de-ch-latest.js OR ' + cdnRoot + 'locale-de-ch-' + pkg.version + '.js',
        'Note that the file names are all lowercase, even though the region is uppercase when you apply a locale.',
        '',
        '*After* the plotly.js script tag, add:',
        '',
        '```html',
        '<script src="plotly-locale-de-ch.js"></script>',
        '<script>Plotly.setPlotConfig({locale: \'de-CH\'})</script>',
        '```',
        '',
        'The first line loads and registers the locale definition with plotly.js, the second sets it as the default for all Plotly plots.',
        'You can also include multiple locale definitions and apply them to each plot separately as a `config` parameter:',
        '',
        '```js',
        'Plotly.newPlot(graphDiv, data, layout, {locale: \'de-CH\'})',
        '```',
        ''
    ];
}

// info about main bundle
function getMainBundleInfo() {
    var mainSizes = findSizes({
        dist: constants.pathToPlotlyDist,
        distMin: constants.pathToPlotlyDistMin,
        withMeta: constants.pathToPlotlyDistWithMeta
    });

    return [
        '# Bundle information',
        '',
        'The main plotly.js bundle includes all the official (non-beta) trace modules.',
        '',
        'It be can imported as minified javascript',
        '- using dist file `dist/plotly.min.js`',
        '- using CDN URL ' + cdnRoot + 'latest' + MINJS + ' OR ' + cdnRoot + pkg.version + MINJS,
        '',
        'or as raw javascript:',
        '- using the `plotly.js-dist` npm package (starting in `v1.39.0`)',
        '- using dist file `dist/plotly.js`',
        '- using CDN URL ' + cdnRoot + 'latest' + JS + ' OR ' + cdnRoot + pkg.version + JS,
        '- using CommonJS with `require(\'plotly.js\')`',
        '',
        'If you would like to have access to the attribute meta information ' +
        '(including attribute descriptions as on the [schema reference page](https://plot.ly/javascript/reference/)), ' +
        'use dist file `dist/plotly-with-meta.js`',
        '',
        'The main plotly.js bundle weights in at:',
        '',
        '| plotly.js | plotly.min.js | plotly.min.js + gzip | plotly-with-meta.js |',
        '|-----------|---------------|----------------------|---------------------|',
        '| ' + mainSizes.raw + ' | ' + mainSizes.minified + ' | ' + mainSizes.gzipped + ' | ' + mainSizes.withMeta + ' |',
        '',
        '## Partial bundles',
        '',
        'Starting in `v1.15.0`, plotly.js also ships with several _partial_ bundles:',
        '',
        constants.partialBundlePaths.map(makeBundleHeaderInfo).join('\n'),
        '',
        'Starting in `v1.39.0`, each plotly.js partial bundle has a corresponding npm package with no dependencies.'
    ];
}

// info about partial bundles
function getPartialBundleInfo() {
    return constants.partialBundlePaths.map(makeBundleInfo);
}

// footer info
function getFooter() {
    return [
        '----------------',
        '',
        '_This file is auto-generated by `npm run stats`. ' +
        'Please do not edit this file directly._'
    ];
}

function makeBundleHeaderInfo(pathObj) {
    var name = pathObj.name;
    return '- [' + name + '](#plotlyjs-' + name + ')';
}

function makeBundleInfo(pathObj) {
    var name = pathObj.name;
    var sizes = findSizes(pathObj);
    var moduleList = common.findModuleList(pathObj.index);
    var pkgName = 'plotly.js-' + name + '-dist';

    return [
        '### plotly.js ' + name,
        '',
        'The `' + name + '` partial bundle contains trace modules ' + common.formatEnumeration(moduleList) + '.',
        '',
        '#### Stats',
        '',
        '| Raw size | Minified size | Minified + gzip size |',
        '|------|-----------------|------------------------|',
        '| ' + sizes.raw + ' | ' + sizes.minified + ' | ' + sizes.gzipped + ' |',
        '',
        '#### CDN links',
        '',
        '| Flavor | URL |',
        '| ------ | --- |',
        '| Latest | ' + cdnRoot + name + '-latest' + JS + ' |',
        '| Latest minified | ' + cdnRoot + name + '-latest' + MINJS + ' |',
        '| Tagged | ' + cdnRoot + name + '-' + pkg.version + JS + ' |',
        '| Tagged minified | ' + cdnRoot + name + '-' + pkg.version + MINJS + ' |',
        '',
        '#### npm package (starting in `v1.39.0`)',
        '',
        'Install [`' + pkgName + '`](https://www.npmjs.com/package/' + pkgName + ') with',
        '```',
        'npm install ' + pkgName,
        '```',
        '',
        'ES6 module usage:',
        '```js',
        'import Plotly from \'' + pkgName + '\'',
        '```',
        '',
        'CommonJS usage:',
        '```js',
        'var Plotly = require(\'' + pkgName + '\');',
        '```',
        '',
        '#### Other plotly.js entry points',
        '',
        '| Flavor | Location |',
        '|---------------|----------|',
        '| dist bundle | ' + '`dist/plotly-' + name + JS + '` |',
        '| dist bundle (minified) | ' + '`dist/plotly-' + name + MINJS + '` |',
        '| ES6 module | ' + '`import Plotly from \'plotly.js/lib/' + 'index-' + name + '\'`' + ' |',
        '| CommonJS | ' + '`require(\'plotly.js/lib/' + 'index-' + name + '\')`' + ' |',
        '',
        ''
    ].join('\n');
}

function findSizes(pathObj) {
    var codeDist = fs.readFileSync(pathObj.dist, ENC);
    var codeDistMin = fs.readFileSync(pathObj.distMin, ENC);

    var sizes = {
        raw: prettySize(codeDist.length),
        minified: prettySize(codeDistMin.length),
        gzipped: prettySize(gzipSize.sync(codeDistMin))
    };

    if(pathObj.withMeta) {
        var codeWithMeta = fs.readFileSync(pathObj.withMeta, ENC);
        sizes.withMeta = prettySize(codeWithMeta.length);
    }

    return sizes;
}
