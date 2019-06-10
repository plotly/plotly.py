/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var getSubplotCalcData = require('../../plots/get_data').getSubplotCalcData;
var counterRegex = require('../../lib').counterRegex;

var createGeo = require('./geo');

var GEO = 'geo';
var counter = counterRegex(GEO);

var attributes = {};
attributes[GEO] = {
    valType: 'subplotid',
    role: 'info',
    dflt: GEO,
    editType: 'calc',
    description: [
        'Sets a reference between this trace\'s geospatial coordinates and',
        'a geographic map.',
        'If *geo* (the default value), the geospatial coordinates refer to',
        '`layout.geo`.',
        'If *geo2*, the geospatial coordinates refer to `layout.geo2`,',
        'and so on.'
    ].join(' ')
};

function plotGeo(gd) {
    var fullLayout = gd._fullLayout;
    var calcData = gd.calcdata;
    var geoIds = fullLayout._subplots[GEO];

    /**
     * If 'plotly-geo-assets.js' is not included,
     * initialize object to keep reference to every loaded topojson
     */
    if(window.PlotlyGeoAssets === undefined) {
        window.PlotlyGeoAssets = {topojson: {}};
    }

    for(var i = 0; i < geoIds.length; i++) {
        var geoId = geoIds[i];
        var geoCalcData = getSubplotCalcData(calcData, GEO, geoId);
        var geoLayout = fullLayout[geoId];
        var geo = geoLayout._subplot;

        if(!geo) {
            geo = createGeo({
                id: geoId,
                graphDiv: gd,
                container: fullLayout._geolayer.node(),
                topojsonURL: gd._context.topojsonURL,
                staticPlot: gd._context.staticPlot
            });

            fullLayout[geoId]._subplot = geo;
        }

        geo.plot(geoCalcData, fullLayout, gd._promises);
    }
}

function clean(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var oldGeoKeys = oldFullLayout._subplots[GEO] || [];

    for(var i = 0; i < oldGeoKeys.length; i++) {
        var oldGeoKey = oldGeoKeys[i];
        var oldGeo = oldFullLayout[oldGeoKey]._subplot;

        if(!newFullLayout[oldGeoKey] && !!oldGeo) {
            oldGeo.framework.remove();
            oldGeo.clipDef.remove();
        }
    }
}

function updateFx(gd) {
    var fullLayout = gd._fullLayout;
    var subplotIds = fullLayout._subplots[GEO];

    for(var i = 0; i < subplotIds.length; i++) {
        var subplotLayout = fullLayout[subplotIds[i]];
        var subplotObj = subplotLayout._subplot;
        subplotObj.updateFx(fullLayout, subplotLayout);
    }
}

module.exports = {
    attr: GEO,
    name: GEO,
    idRoot: GEO,
    idRegex: counter,
    attrRegex: counter,
    attributes: attributes,
    layoutAttributes: require('./layout_attributes'),
    supplyLayoutDefaults: require('./layout_defaults'),
    plot: plotGeo,
    updateFx: updateFx,
    clean: clean
};
