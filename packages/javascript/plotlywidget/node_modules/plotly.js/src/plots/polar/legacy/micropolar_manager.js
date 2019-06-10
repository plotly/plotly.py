/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

/* eslint-disable new-cap */

'use strict';

var d3 = require('d3');
var Lib = require('../../../lib');
var Color = require('../../../components/color');

var micropolar = require('./micropolar');
var UndoManager = require('./undo_manager');
var extendDeepAll = Lib.extendDeepAll;

var manager = module.exports = {};

manager.framework = function(_gd) {
    var config, previousConfigClone, plot, convertedInput, container;
    var undoManager = new UndoManager();

    function exports(_inputConfig, _container) {
        if(_container) container = _container;
        d3.select(d3.select(container).node().parentNode).selectAll('.svg-container>*:not(.chart-root)').remove();

        config = (!config) ?
            _inputConfig :
            extendDeepAll(config, _inputConfig);

        if(!plot) plot = micropolar.Axis();
        convertedInput = micropolar.adapter.plotly().convert(config);
        plot.config(convertedInput).render(container);
        _gd.data = config.data;
        _gd.layout = config.layout;
        manager.fillLayout(_gd);
        return config;
    }
    exports.isPolar = true;
    exports.svg = function() { return plot.svg(); };
    exports.getConfig = function() { return config; };
    exports.getLiveConfig = function() {
        return micropolar.adapter.plotly().convert(plot.getLiveConfig(), true);
    };
    exports.getLiveScales = function() { return {t: plot.angularScale(), r: plot.radialScale()}; };
    exports.setUndoPoint = function() {
        var that = this;
        var configClone = micropolar.util.cloneJson(config);
        (function(_configClone, _previousConfigClone) {
            undoManager.add({
                undo: function() {
                    if(_previousConfigClone) that(_previousConfigClone);
                },
                redo: function() {
                    that(_configClone);
                }
            });
        })(configClone, previousConfigClone);
        previousConfigClone = micropolar.util.cloneJson(configClone);
    };
    exports.undo = function() { undoManager.undo(); };
    exports.redo = function() { undoManager.redo(); };
    return exports;
};

manager.fillLayout = function(_gd) {
    var container = d3.select(_gd).selectAll('.plot-container');
    var paperDiv = container.selectAll('.svg-container');
    var paper = _gd.framework && _gd.framework.svg && _gd.framework.svg();
    var dflts = {
        width: 800,
        height: 600,
        paper_bgcolor: Color.background,
        _container: container,
        _paperdiv: paperDiv,
        _paper: paper
    };

    _gd._fullLayout = extendDeepAll(dflts, _gd.layout);
};
