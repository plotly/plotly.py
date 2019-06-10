/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Plotly = require('./core');

// traces
Plotly.register([
    require('./bar'),
    require('./box'),
    require('./heatmap'),
    require('./histogram'),
    require('./histogram2d'),
    require('./histogram2dcontour'),
    require('./contour'),
    require('./scatterternary'),
    require('./violin'),
    require('./funnel'),
    require('./waterfall'),

    require('./pie'),
    require('./sunburst'),
    require('./funnelarea'),

    require('./scatter3d'),
    require('./surface'),
    require('./isosurface'),
    require('./volume'),
    require('./mesh3d'),
    require('./cone'),
    require('./streamtube'),

    require('./scattergeo'),
    require('./choropleth'),

    require('./scattergl'),
    require('./splom'),

    require('./pointcloud'),
    require('./heatmapgl'),
    require('./parcoords'),
    require('./parcats'),
    require('./scattermapbox'),

    require('./sankey'),

    require('./table'),

    require('./carpet'),
    require('./scattercarpet'),
    require('./contourcarpet'),

    require('./ohlc'),
    require('./candlestick'),

    require('./scatterpolar'),
    require('./scatterpolargl'),
    require('./barpolar')
]);

// transforms
//
// Please note that all *transform* methods are executed before
// all *calcTransform* methods - which could possibly lead to
// unexpected results when applying multiple transforms of different types
// to a given trace.
//
// For more info, see:
// https://github.com/plotly/plotly.js/pull/978#pullrequestreview-2403353
//
Plotly.register([
    require('./aggregate'),
    require('./filter'),
    require('./groupby'),
    require('./sort')
]);

// components
Plotly.register([
    require('./calendars')
]);

module.exports = Plotly;
