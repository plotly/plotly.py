var path = require('path');
var pkg = require('../../package.json');

var pathToRoot = path.join(__dirname, '../../');
var pathToSrc = path.join(pathToRoot, 'src/');
var pathToLib = path.join(pathToRoot, 'lib/');
var pathToImageTest = path.join(pathToRoot, 'test/image');
var pathToDist = path.join(pathToRoot, 'dist/');
var pathToBuild = path.join(pathToRoot, 'build/');

var pathToTopojsonSrc;
try {
    pathToTopojsonSrc = path.join(path.dirname(require.resolve('sane-topojson')), 'dist/');
} catch(e) {
    console.log([
        '',
        'WARN: Cannot resolve path to *sane-topojson* package.',
        '  This can happen when one `npm link sane-topojson`',
        '  and runs a command in a Docker container.',
        '  There is nothing to worry, if you see this warning while running',
        '  `npm run test-image`, `npm run test-export` or `npm run baseline` ;)',
        ''
    ].join('\n'));
}

var partialBundleNames = [
    'basic', 'cartesian', 'geo', 'gl3d', 'gl2d', 'mapbox', 'finance'
];

var partialBundlePaths = partialBundleNames.map(function(name) {
    return {
        name: name,
        index: path.join(pathToLib, 'index-' + name + '.js'),
        dist: path.join(pathToDist, 'plotly-' + name + '.js'),
        distMin: path.join(pathToDist, 'plotly-' + name + '.min.js')
    };
});

var year = (new Date()).getFullYear();

module.exports = {
    pathToRoot: pathToRoot,
    pathToSrc: pathToSrc,
    pathToLib: pathToLib,
    pathToBuild: pathToBuild,
    pathToDist: pathToDist,

    pathToPlotlyIndex: path.join(pathToLib, 'index.js'),
    pathToPlotlyCore: path.join(pathToSrc, 'core.js'),
    pathToPlotlyBuild: path.join(pathToBuild, 'plotly.js'),
    pathToPlotlyDist: path.join(pathToDist, 'plotly.js'),
    pathToPlotlyDistMin: path.join(pathToDist, 'plotly.min.js'),
    pathToPlotlyDistWithMeta: path.join(pathToDist, 'plotly-with-meta.js'),

    pathToSchema: path.join(pathToDist, 'plot-schema.json'),
    pathToTranslationKeys: path.join(pathToDist, 'translation-keys.txt'),

    partialBundleNames: partialBundleNames,
    partialBundlePaths: partialBundlePaths,

    pathToTopojsonSrc: pathToTopojsonSrc,
    pathToTopojsonDist: path.join(pathToDist, 'topojson/'),
    pathToPlotlyGeoAssetsSrc: path.join(pathToSrc, 'assets/geo_assets.js'),
    pathToPlotlyGeoAssetsDist: path.join(pathToDist, 'plotly-geo-assets.js'),

    pathToFontSVG: path.join(pathToSrc, 'fonts/ploticon/ploticon.svg'),
    pathToFontSVGBuild: path.join(pathToBuild, 'ploticon.js'),

    pathToSCSS: path.join(pathToSrc, 'css/style.scss'),
    pathToCSSBuild: path.join(pathToBuild, 'plotcss.js'),

    pathToTestDashboardBundle: path.join(pathToBuild, 'test_dashboard-bundle.js'),
    pathToImageViewerBundle: path.join(pathToBuild, 'image_viewer-bundle.js'),

    pathToImageTest: pathToImageTest,
    pathToTestImageMocks: path.join(pathToImageTest, 'mocks/'),
    pathToTestImageBaselines: path.join(pathToImageTest, 'baselines/'),
    pathToTestImages: path.join(pathToBuild, 'test_images/'),
    pathToTestImagesDiff: path.join(pathToBuild, 'test_images_diff/'),
    pathToTestImagesDiffList: path.join(pathToBuild, 'list_of_incorrect_images.txt'),

    pathToJasmineTests: path.join(pathToRoot, 'test/jasmine/tests'),
    pathToJasmineBundleTests: path.join(pathToRoot, 'test/jasmine/bundle_tests'),
    pathToRequireJS: path.join(pathToRoot, 'node_modules', 'requirejs', 'require.js'),
    pathToRequireJSFixture: path.join(pathToBuild, 'requirejs_fixture.js'),

    // this mapbox access token is 'public', no need to hide it
    // more info: https://www.mapbox.com/help/define-access-token/
    mapboxAccessToken: 'pk.eyJ1IjoiZXRwaW5hcmQiLCJhIjoiY2luMHIzdHE0MGFxNXVubTRxczZ2YmUxaCJ9.hwWZful0U2CQxit4ItNsiQ',
    pathToCredentials: path.join(pathToBuild, 'credentials.json'),

    testContainerImage: 'plotly/testbed:latest',
    testContainerName: process.env.PLOTLYJS_TEST_CONTAINER_NAME || 'imagetest',
    testContainerPort: '9010',
    testContainerUrl: 'http://localhost:9010/',
    testContainerHome: '/var/www/streambed/image_server/plotly.js',

    uglifyOptions: {
        ecma: 5,
        mangle: true,
        compress: {
            // see full list of compress option
            // https://github.com/fabiosantoscode/terser#compress-options
            //
            // need to turn off 'typeofs' to make mapbox-gl work in
            // minified bundles, for more info see:
            // https://github.com/plotly/plotly.js/issues/2787
            typeofs: false
        },
        output: {
            beautify: false,
            ascii_only: true
        },

        sourceMap: false
    },

    licenseDist: [
        '/**',
        '* plotly.js v' + pkg.version,
        '* Copyright 2012-' + year + ', Plotly, Inc.',
        '* All rights reserved.',
        '* Licensed under the MIT license',
        '*/'
    ].join('\n'),

    licenseSrc: [
        '/**',
        '* Copyright 2012-' + year + ', Plotly, Inc.',
        '* All rights reserved.',
        '*',
        '* This source code is licensed under the MIT license found in the',
        '* LICENSE file in the root directory of this source tree.',
        '*/'
    ].join('\n')
};
