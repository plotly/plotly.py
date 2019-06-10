/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var convertTextOpts = require('./convert_text_opts');

function MapboxLayer(mapbox, index) {
    this.mapbox = mapbox;
    this.map = mapbox.map;

    this.uid = mapbox.uid + '-' + 'layer' + index;

    this.idSource = this.uid + '-source';
    this.idLayer = this.uid + '-layer';

    // some state variable to check if a remove/add step is needed
    this.sourceType = null;
    this.source = null;
    this.layerType = null;
    this.below = null;

    // is layer currently visible
    this.visible = false;
}

var proto = MapboxLayer.prototype;

proto.update = function update(opts) {
    if(!this.visible) {
        // IMPORTANT: must create source before layer to not cause errors
        this.updateSource(opts);
        this.updateLayer(opts);
    } else if(this.needsNewSource(opts)) {
        // IMPORTANT: must delete layer before source to not cause errors
        this.removeLayer();
        this.updateSource(opts);
        this.updateLayer(opts);
    } else if(this.needsNewLayer(opts)) {
        this.updateLayer(opts);
    } else {
        this.updateStyle(opts);
    }

    this.visible = isVisible(opts);
};

proto.needsNewSource = function(opts) {
    // for some reason changing layer to 'fill' or 'symbol'
    // w/o changing the source throws an exception in mapbox-gl 0.18 ;
    // stay safe and make new source on type changes
    return (
        this.sourceType !== opts.sourcetype ||
        this.source !== opts.source ||
        this.layerType !== opts.type
    );
};

proto.needsNewLayer = function(opts) {
    return (
        this.layerType !== opts.type ||
        this.below !== opts.below
    );
};

proto.updateSource = function(opts) {
    var map = this.map;

    if(map.getSource(this.idSource)) map.removeSource(this.idSource);

    this.sourceType = opts.sourcetype;
    this.source = opts.source;

    if(!isVisible(opts)) return;

    var sourceOpts = convertSourceOpts(opts);

    map.addSource(this.idSource, sourceOpts);
};

proto.updateLayer = function(opts) {
    var map = this.map;
    var convertedOpts = convertOpts(opts);

    this.removeLayer();
    this.layerType = opts.type;

    if(isVisible(opts)) {
        map.addLayer({
            id: this.idLayer,
            source: this.idSource,
            'source-layer': opts.sourcelayer || '',
            type: opts.type,
            minzoom: opts.minzoom,
            maxzoom: opts.maxzoom,
            layout: convertedOpts.layout,
            paint: convertedOpts.paint
        }, opts.below);
    }
};

proto.updateStyle = function(opts) {
    if(isVisible(opts)) {
        var convertedOpts = convertOpts(opts);
        this.mapbox.setOptions(this.idLayer, 'setLayoutProperty', convertedOpts.layout);
        this.mapbox.setOptions(this.idLayer, 'setPaintProperty', convertedOpts.paint);
    }
};

proto.removeLayer = function() {
    var map = this.map;
    if(map.getLayer(this.idLayer)) {
        map.removeLayer(this.idLayer);
    }
};

proto.dispose = function dispose() {
    var map = this.map;
    map.removeLayer(this.idLayer);
    map.removeSource(this.idSource);
};

function isVisible(opts) {
    var source = opts.source;

    return opts.visible && (
        Lib.isPlainObject(source) ||
        (typeof source === 'string' && source.length > 0)
    );
}

function convertOpts(opts) {
    var layout = {};
    var paint = {};

    switch(opts.type) {
        case 'circle':
            Lib.extendFlat(paint, {
                'circle-radius': opts.circle.radius,
                'circle-color': opts.color,
                'circle-opacity': opts.opacity
            });
            break;

        case 'line':
            Lib.extendFlat(paint, {
                'line-width': opts.line.width,
                'line-color': opts.color,
                'line-opacity': opts.opacity,
                'line-dasharray': opts.line.dash
            });
            break;

        case 'fill':
            Lib.extendFlat(paint, {
                'fill-color': opts.color,
                'fill-outline-color': opts.fill.outlinecolor,
                'fill-opacity': opts.opacity

                // no way to pass specify outline width at the moment
            });
            break;

        case 'symbol':
            var symbol = opts.symbol;
            var textOpts = convertTextOpts(symbol.textposition, symbol.iconsize);

            Lib.extendFlat(layout, {
                'icon-image': symbol.icon + '-15',
                'icon-size': symbol.iconsize / 10,

                'text-field': symbol.text,
                'text-size': symbol.textfont.size,
                'text-anchor': textOpts.anchor,
                'text-offset': textOpts.offset,
                'symbol-placement': symbol.placement,

                // TODO font family
                // 'text-font': symbol.textfont.family.split(', '),
            });

            Lib.extendFlat(paint, {
                'icon-color': opts.color,
                'text-color': symbol.textfont.color,
                'text-opacity': opts.opacity
            });
            break;
    }

    return { layout: layout, paint: paint };
}

function convertSourceOpts(opts) {
    var sourceType = opts.sourcetype;
    var source = opts.source;
    var sourceOpts = {type: sourceType};
    var field;

    if(sourceType === 'geojson') {
        field = 'data';
    } else if(sourceType === 'vector') {
        field = typeof source === 'string' ? 'url' : 'tiles';
    }

    sourceOpts[field] = source;
    return sourceOpts;
}

module.exports = function createMapboxLayer(mapbox, index, opts) {
    var mapboxLayer = new MapboxLayer(mapbox, index);

    mapboxLayer.update(opts);

    return mapboxLayer;
};
