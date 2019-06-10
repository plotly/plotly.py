/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var requiredVersion = '0.45.0';

module.exports = {
    requiredVersion: requiredVersion,

    styleUrlPrefix: 'mapbox://styles/mapbox/',
    styleUrlSuffix: 'v9',

    controlContainerClassName: 'mapboxgl-control-container',

    wrongVersionErrorMsg: [
        'Your custom plotly.js bundle is not using the correct mapbox-gl version',
        'Please install mapbox-gl@' + requiredVersion + '.'
    ].join('\n'),

    noAccessTokenErrorMsg: [
        'Missing Mapbox access token.',
        'Mapbox trace type require a Mapbox access token to be registered.',
        'For example:',
        '  Plotly.plot(gd, data, layout, { mapboxAccessToken: \'my-access-token\' });',
        'More info here: https://www.mapbox.com/help/define-access-token/'
    ].join('\n'),

    mapOnErrorMsg: 'Mapbox error.',

    // a subset of node_modules/mapbox-gl/dist/mapbox-gl.css
    styleRules: {
        map: 'overflow:hidden;position:relative;',
        'missing-css': 'display:none',
    }
};
