var fs = require('fs-extra');
var sass = require('node-sass');

var constants = require('./util/constants');
var common = require('./util/common');
var pullCSS = require('./util/pull_css');
var pullFontSVG = require('./util/pull_font_svg');
var updateVersion = require('./util/update_version');

// main
makeBuildCSS();
makeBuildFontSVG();
copyTopojsonFiles();
updateVersion(constants.pathToPlotlyCore);
updateVersion(constants.pathToPlotlyGeoAssetsSrc);

// convert scss to css to js
function makeBuildCSS() {
    sass.render({
        file: constants.pathToSCSS,
        outputStyle: 'compressed'
    }, function(err, result) {
        if(err) throw err;

        // css to js
        pullCSS(String(result.css), constants.pathToCSSBuild);
    });
}

// convert font svg into js
function makeBuildFontSVG() {
    fs.readFile(constants.pathToFontSVG, function(err, data) {
        if(err) throw err;

        pullFontSVG(data.toString(), constants.pathToFontSVGBuild);
    });
}

// copy topojson files from sane-topojson to dist/
function copyTopojsonFiles() {
    fs.copy(
        constants.pathToTopojsonSrc,
        constants.pathToTopojsonDist,
        { clobber: true },
        common.throwOnError
    );
}
