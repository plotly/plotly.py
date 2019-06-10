/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var convert = require('./convert');

function ScatterMapbox(subplot, uid) {
    this.subplot = subplot;
    this.uid = uid;

    this.sourceIds = {
        fill: uid + '-source-fill',
        line: uid + '-source-line',
        circle: uid + '-source-circle',
        symbol: uid + '-source-symbol'
    };

    this.layerIds = {
        fill: uid + '-layer-fill',
        line: uid + '-layer-line',
        circle: uid + '-layer-circle',
        symbol: uid + '-layer-symbol'
    };

    this.order = ['fill', 'line', 'circle', 'symbol'];

    // We could merge the 'fill' source with the 'line' source and
    // the 'circle' source with the 'symbol' source if ever having
    // for up-to 4 sources per 'scattermapbox' traces becomes a problem.
}

var proto = ScatterMapbox.prototype;

proto.addSource = function(k, opts) {
    this.subplot.map.addSource(this.sourceIds[k], {
        type: 'geojson',
        data: opts.geojson
    });
};

proto.setSourceData = function(k, opts) {
    this.subplot.map
        .getSource(this.sourceIds[k])
        .setData(opts.geojson);
};

proto.addLayer = function(k, opts) {
    this.subplot.map.addLayer({
        type: k,
        id: this.layerIds[k],
        source: this.sourceIds[k],
        layout: opts.layout,
        paint: opts.paint
    });
};

proto.update = function update(calcTrace) {
    var subplot = this.subplot;
    var optsAll = convert(calcTrace);

    for(var i = 0; i < this.order.length; i++) {
        var k = this.order[i];
        var opts = optsAll[k];

        subplot.setOptions(this.layerIds[k], 'setLayoutProperty', opts.layout);

        if(opts.layout.visibility === 'visible') {
            this.setSourceData(k, opts);
            subplot.setOptions(this.layerIds[k], 'setPaintProperty', opts.paint);
        }
    }

    // link ref for quick update during selections
    calcTrace[0].trace._glTrace = this;
};

proto.dispose = function dispose() {
    var map = this.subplot.map;

    for(var i = 0; i < this.order.length; i++) {
        var k = this.order[i];
        map.removeLayer(this.layerIds[k]);
        map.removeSource(this.sourceIds[k]);
    }
};

module.exports = function createScatterMapbox(subplot, calcTrace) {
    var trace = calcTrace[0].trace;
    var scatterMapbox = new ScatterMapbox(subplot, trace.uid);
    var optsAll = convert(calcTrace);

    for(var i = 0; i < scatterMapbox.order.length; i++) {
        var k = scatterMapbox.order[i];
        var opts = optsAll[k];

        scatterMapbox.addSource(k, opts);
        scatterMapbox.addLayer(k, opts);
    }

    // link ref for quick update during selections
    calcTrace[0].trace._glTrace = scatterMapbox;

    return scatterMapbox;
};
