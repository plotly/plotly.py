/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var d3 = require('d3');
var isNumeric = require('fast-isnumeric');

var Registry = require('../registry');
var PlotSchema = require('../plot_api/plot_schema');
var Template = require('../plot_api/plot_template');
var Lib = require('../lib');
var Color = require('../components/color');
var BADNUM = require('../constants/numerical').BADNUM;

var axisIDs = require('./cartesian/axis_ids');

var animationAttrs = require('./animation_attributes');
var frameAttrs = require('./frame_attributes');

var relinkPrivateKeys = Lib.relinkPrivateKeys;
var _ = Lib._;

var plots = module.exports = {};

// Expose registry methods on Plots for backward-compatibility
Lib.extendFlat(plots, Registry);

plots.attributes = require('./attributes');
plots.attributes.type.values = plots.allTypes;
plots.fontAttrs = require('./font_attributes');
plots.layoutAttributes = require('./layout_attributes');

// TODO make this a plot attribute?
plots.fontWeight = 'normal';

var transformsRegistry = plots.transformsRegistry;

var commandModule = require('./command');
plots.executeAPICommand = commandModule.executeAPICommand;
plots.computeAPICommandBindings = commandModule.computeAPICommandBindings;
plots.manageCommandObserver = commandModule.manageCommandObserver;
plots.hasSimpleAPICommandBindings = commandModule.hasSimpleAPICommandBindings;

// in some cases the browser doesn't seem to know how big
// the text is at first, so it needs to draw it,
// then wait a little, then draw it again
plots.redrawText = function(gd) {
    gd = Lib.getGraphDiv(gd);

    var fullLayout = gd._fullLayout || {};
    var hasPolar = fullLayout._has && fullLayout._has('polar');
    var hasLegacyPolar = !hasPolar && gd.data && gd.data[0] && gd.data[0].r;

    // do not work if polar is present
    if(hasLegacyPolar) return;

    return new Promise(function(resolve) {
        setTimeout(function() {
            Registry.getComponentMethod('annotations', 'draw')(gd);
            Registry.getComponentMethod('legend', 'draw')(gd);
            Registry.getComponentMethod('colorbar', 'draw')(gd);
            resolve(plots.previousPromises(gd));
        }, 300);
    });
};

// resize plot about the container size
plots.resize = function(gd) {
    gd = Lib.getGraphDiv(gd);

    return new Promise(function(resolve, reject) {
        function isHidden(gd) {
            var display = window.getComputedStyle(gd).display;
            return !display || display === 'none';
        }

        if(!gd || isHidden(gd)) {
            reject(new Error('Resize must be passed a displayed plot div element.'));
        }

        if(gd._redrawTimer) clearTimeout(gd._redrawTimer);

        gd._redrawTimer = setTimeout(function() {
            // return if there is nothing to resize or is hidden
            if(!gd.layout || (gd.layout.width && gd.layout.height) || isHidden(gd)) {
                resolve(gd);
                return;
            }

            delete gd.layout.width;
            delete gd.layout.height;

            // autosizing doesn't count as a change that needs saving
            var oldchanged = gd.changed;

            // nor should it be included in the undo queue
            gd.autoplay = true;

            Registry.call('relayout', gd, {autosize: true}).then(function() {
                gd.changed = oldchanged;
                resolve(gd);
            });
        }, 100);
    });
};


// for use in Lib.syncOrAsync, check if there are any
// pending promises in this plot and wait for them
plots.previousPromises = function(gd) {
    if((gd._promises || []).length) {
        return Promise.all(gd._promises)
            .then(function() { gd._promises = []; });
    }
};

/**
 * Adds the 'Edit chart' link.
 * Note that now Plotly.plot() calls this so it can regenerate whenever it replots
 *
 * Add source links to your graph inside the 'showSources' config argument.
 */
plots.addLinks = function(gd) {
    // Do not do anything if showLink and showSources are not set to true in config
    if(!gd._context.showLink && !gd._context.showSources) return;

    var fullLayout = gd._fullLayout;

    var linkContainer = Lib.ensureSingle(fullLayout._paper, 'text', 'js-plot-link-container', function(s) {
        s.style({
            'font-family': '"Open Sans", Arial, sans-serif',
            'font-size': '12px',
            'fill': Color.defaultLine,
            'pointer-events': 'all'
        })
        .each(function() {
            var links = d3.select(this);
            links.append('tspan').classed('js-link-to-tool', true);
            links.append('tspan').classed('js-link-spacer', true);
            links.append('tspan').classed('js-sourcelinks', true);
        });
    });

    // The text node inside svg
    var text = linkContainer.node();
    var attrs = {y: fullLayout._paper.attr('height') - 9};

    // If text's width is bigger than the layout
    // Check that text is a child node or document.body
    // because otherwise IE/Edge might throw an exception
    // when calling getComputedTextLength().
    // Apparently offsetParent is null for invisibles.
    if(document.body.contains(text) && text.getComputedTextLength() >= (fullLayout.width - 20)) {
        // Align the text at the left
        attrs['text-anchor'] = 'start';
        attrs.x = 5;
    } else {
        // Align the text at the right
        attrs['text-anchor'] = 'end';
        attrs.x = fullLayout._paper.attr('width') - 7;
    }

    linkContainer.attr(attrs);

    var toolspan = linkContainer.select('.js-link-to-tool');
    var spacespan = linkContainer.select('.js-link-spacer');
    var sourcespan = linkContainer.select('.js-sourcelinks');

    if(gd._context.showSources) gd._context.showSources(gd);

    // 'view in plotly' link for embedded plots
    if(gd._context.showLink) positionPlayWithData(gd, toolspan);

    // separator if we have both sources and tool link
    spacespan.text((toolspan.text() && sourcespan.text()) ? ' - ' : '');
};

// note that now this function is only adding the brand in
// iframes and 3rd-party apps
function positionPlayWithData(gd, container) {
    container.text('');
    var link = container.append('a')
        .attr({
            'xlink:xlink:href': '#',
            'class': 'link--impt link--embedview',
            'font-weight': 'bold'
        })
        .text(gd._context.linkText + ' ' + String.fromCharCode(187));

    if(gd._context.sendData) {
        link.on('click', function() {
            plots.sendDataToCloud(gd);
        });
    } else {
        var path = window.location.pathname.split('/');
        var query = window.location.search;
        link.attr({
            'xlink:xlink:show': 'new',
            'xlink:xlink:href': '/' + path[2].split('.')[0] + '/' + path[1] + query
        });
    }
}

plots.sendDataToCloud = function(gd) {
    gd.emit('plotly_beforeexport');

    var baseUrl = (window.PLOTLYENV || {}).BASE_URL || gd._context.plotlyServerURL;

    var hiddenformDiv = d3.select(gd)
        .append('div')
        .attr('id', 'hiddenform')
        .style('display', 'none');

    var hiddenform = hiddenformDiv
        .append('form')
        .attr({
            action: baseUrl + '/external',
            method: 'post',
            target: '_blank'
        });

    var hiddenformInput = hiddenform
        .append('input')
        .attr({
            type: 'text',
            name: 'data'
        });

    hiddenformInput.node().value = plots.graphJson(gd, false, 'keepdata');
    hiddenform.node().submit();
    hiddenformDiv.remove();

    gd.emit('plotly_afterexport');
    return false;
};

var d3FormatKeys = [
    'days', 'shortDays', 'months', 'shortMonths', 'periods',
    'dateTime', 'date', 'time',
    'decimal', 'thousands', 'grouping', 'currency'
];

var extraFormatKeys = [
    'year', 'month', 'dayMonth', 'dayMonthYear'
];

/*
 * Fill in default values
 * @param {DOM element} gd
 * @param {object} opts
 * @param {boolean} opts.skipUpdateCalc: normally if the existing gd.calcdata looks
 *   compatible with the new gd._fullData we finish by linking the new _fullData traces
 *   to the old gd.calcdata, so it's correctly set if we're not going to recalc. But also,
 *   if there are calcTransforms on the trace, we first remap data arrays from the old full
 *   trace into the new one. Use skipUpdateCalc to defer this (needed by Plotly.react)
 *
 * gd.data, gd.layout:
 *   are precisely what the user specified (except as modified by cleanData/cleanLayout),
 *   these fields shouldn't be modified (except for filling in some auto values)
 *   nor used directly after the supply defaults step.
 *
 * gd._fullData, gd._fullLayout:
 *   are complete descriptions of how to draw the plot,
 *   use these fields in all required computations.
 *
 * gd._fullLayout._modules
 *   is a list of all the trace modules required to draw the plot.
 *
 * gd._fullLayout._visibleModules
 *   subset of _modules, a list of modules corresponding to visible:true traces.
 *
 * gd._fullLayout._basePlotModules
 *   is a list of all the plot modules required to draw the plot.
 *
 * gd._fullLayout._transformModules
 *   is a list of all the transform modules invoked.
 *
 */
plots.supplyDefaults = function(gd, opts) {
    var skipUpdateCalc = opts && opts.skipUpdateCalc;
    var oldFullLayout = gd._fullLayout || {};

    if(oldFullLayout._skipDefaults) {
        delete oldFullLayout._skipDefaults;
        return;
    }

    var newFullLayout = gd._fullLayout = {};
    var newLayout = gd.layout || {};

    var oldFullData = gd._fullData || [];
    var newFullData = gd._fullData = [];
    var newData = gd.data || [];

    var oldCalcdata = gd.calcdata || [];

    var context = gd._context || {};

    var i;

    // Create all the storage space for frames, but only if doesn't already exist
    if(!gd._transitionData) plots.createTransitionData(gd);

    // So we only need to do this once (and since we have gd here)
    // get the translated placeholder titles.
    // These ones get used as default values so need to be known at supplyDefaults
    // others keep their blank defaults but render the placeholder as desired later
    // TODO: make these work the same way, only inserting the placeholder text at draw time?
    // The challenge is that this has slightly different behavior right now in editable mode:
    // using the placeholder as default makes this text permanently (but lightly) visible,
    // but explicit '' for these titles gives you a placeholder that's hidden until you mouse
    // over it - so you're not distracted by it if you really don't want a title, but if you do
    // and you're new to plotly you may not be able to find it.
    // When editable=false the two behave the same, no title is drawn.
    newFullLayout._dfltTitle = {
        plot: _(gd, 'Click to enter Plot title'),
        x: _(gd, 'Click to enter X axis title'),
        y: _(gd, 'Click to enter Y axis title'),
        colorbar: _(gd, 'Click to enter Colorscale title'),
        annotation: _(gd, 'new text')
    };
    newFullLayout._traceWord = _(gd, 'trace');

    var formatObj = getFormatObj(gd, d3FormatKeys);

    // stash the token from context so mapbox subplots can use it as default
    newFullLayout._mapboxAccessToken = context.mapboxAccessToken;

    // first fill in what we can of layout without looking at data
    // because fullData needs a few things from layout
    if(oldFullLayout._initialAutoSizeIsDone) {
        // coerce the updated layout while preserving width and height
        var oldWidth = oldFullLayout.width;
        var oldHeight = oldFullLayout.height;

        plots.supplyLayoutGlobalDefaults(newLayout, newFullLayout, formatObj);

        if(!newLayout.width) newFullLayout.width = oldWidth;
        if(!newLayout.height) newFullLayout.height = oldHeight;
        plots.sanitizeMargins(newFullLayout);
    } else {
        // coerce the updated layout and autosize if needed
        plots.supplyLayoutGlobalDefaults(newLayout, newFullLayout, formatObj);

        var missingWidthOrHeight = (!newLayout.width || !newLayout.height);
        var autosize = newFullLayout.autosize;
        var autosizable = context.autosizable;
        var initialAutoSize = missingWidthOrHeight && (autosize || autosizable);

        if(initialAutoSize) plots.plotAutoSize(gd, newLayout, newFullLayout);
        else if(missingWidthOrHeight) plots.sanitizeMargins(newFullLayout);

        // for backwards-compatibility with Plotly v1.x.x
        if(!autosize && missingWidthOrHeight) {
            newLayout.width = newFullLayout.width;
            newLayout.height = newFullLayout.height;
        }
    }

    newFullLayout._d3locale = getFormatter(formatObj, newFullLayout.separators);
    newFullLayout._extraFormat = getFormatObj(gd, extraFormatKeys);

    newFullLayout._initialAutoSizeIsDone = true;

    // keep track of how many traces are inputted
    newFullLayout._dataLength = newData.length;

    // clear the lists of trace and baseplot modules, and subplots
    newFullLayout._modules = [];
    newFullLayout._visibleModules = [];
    newFullLayout._basePlotModules = [];
    var subplots = newFullLayout._subplots = emptySubplotLists();

    // initialize axis and subplot hash objects for splom-generated grids
    var splomAxes = newFullLayout._splomAxes = {x: {}, y: {}};
    var splomSubplots = newFullLayout._splomSubplots = {};
    // initialize splom grid defaults
    newFullLayout._splomGridDflt = {};

    // for stacked area traces to share config across traces
    newFullLayout._scatterStackOpts = {};
    // for the first scatter trace on each subplot (so it knows tonext->tozero)
    newFullLayout._firstScatter = {};
    // for grouped bar/box/violin trace to share config across traces
    newFullLayout._alignmentOpts = {};
    // track color axes referenced in the data
    newFullLayout._colorAxes = {};

    // for traces to request a default rangeslider on their x axes
    // eg set `_requestRangeslider.x2 = true` for xaxis2
    newFullLayout._requestRangeslider = {};

    // pull uids from old data to use as new defaults
    newFullLayout._traceUids = getTraceUids(oldFullData, newData);

    // then do the data
    newFullLayout._globalTransforms = (gd._context || {}).globalTransforms;
    plots.supplyDataDefaults(newData, newFullData, newLayout, newFullLayout);

    // redo grid size defaults with info about splom x/y axes,
    // and fill in generated cartesian axes and subplots
    var splomXa = Object.keys(splomAxes.x);
    var splomYa = Object.keys(splomAxes.y);
    if(splomXa.length > 1 && splomYa.length > 1) {
        Registry.getComponentMethod('grid', 'sizeDefaults')(newLayout, newFullLayout);

        for(i = 0; i < splomXa.length; i++) {
            Lib.pushUnique(subplots.xaxis, splomXa[i]);
        }
        for(i = 0; i < splomYa.length; i++) {
            Lib.pushUnique(subplots.yaxis, splomYa[i]);
        }
        for(var k in splomSubplots) {
            Lib.pushUnique(subplots.cartesian, k);
        }
    }

    // attach helper method to check whether a plot type is present on graph
    newFullLayout._has = plots._hasPlotType.bind(newFullLayout);

    if(oldFullData.length === newFullData.length) {
        for(i = 0; i < newFullData.length; i++) {
            relinkPrivateKeys(newFullData[i], oldFullData[i]);
        }
    }

    // finally, fill in the pieces of layout that may need to look at data
    plots.supplyLayoutModuleDefaults(newLayout, newFullLayout, newFullData, gd._transitionData);

    // Special cases that introduce interactions between traces.
    // This is after relinkPrivateKeys so we can use those in crossTraceDefaults
    // and after layout module defaults, so we can use eg barmode
    var _modules = newFullLayout._visibleModules;
    var crossTraceDefaultsFuncs = [];
    for(i = 0; i < _modules.length; i++) {
        var funci = _modules[i].crossTraceDefaults;
        // some trace types share crossTraceDefaults (ie histogram2d, histogram2dcontour)
        if(funci) Lib.pushUnique(crossTraceDefaultsFuncs, funci);
    }
    for(i = 0; i < crossTraceDefaultsFuncs.length; i++) {
        crossTraceDefaultsFuncs[i](newFullData, newFullLayout);
    }

    // turn on flag to optimize large splom-only graphs
    // mostly by omitting SVG layers during Cartesian.drawFramework
    newFullLayout._hasOnlyLargeSploms = (
        newFullLayout._basePlotModules.length === 1 &&
        newFullLayout._basePlotModules[0].name === 'splom' &&
        splomXa.length > 15 &&
        splomYa.length > 15 &&
        newFullLayout.shapes.length === 0 &&
        newFullLayout.images.length === 0
    );

    // TODO remove in v2.0.0
    // add has-plot-type refs to fullLayout for backward compatibility
    newFullLayout._hasCartesian = newFullLayout._has('cartesian');
    newFullLayout._hasGeo = newFullLayout._has('geo');
    newFullLayout._hasGL3D = newFullLayout._has('gl3d');
    newFullLayout._hasGL2D = newFullLayout._has('gl2d');
    newFullLayout._hasTernary = newFullLayout._has('ternary');
    newFullLayout._hasPie = newFullLayout._has('pie');

    // relink / initialize subplot axis objects
    plots.linkSubplots(newFullData, newFullLayout, oldFullData, oldFullLayout);

    // clean subplots and other artifacts from previous plot calls
    plots.cleanPlot(newFullData, newFullLayout, oldFullData, oldFullLayout);

    // clear selection outline until we implement persistent selection,
    // don't clear them though when drag handlers (e.g. listening to
    // `plotly_selecting`) update the graph.
    // we should try to come up with a better solution when implementing
    // https://github.com/plotly/plotly.js/issues/1851
    if(oldFullLayout._zoomlayer && !gd._dragging) {
        oldFullLayout._zoomlayer.selectAll('.select-outline').remove();
    }


    // fill in meta helpers
    fillMetaTextHelpers(newFullData, newFullLayout);

    // relink functions and _ attributes to promote consistency between plots
    relinkPrivateKeys(newFullLayout, oldFullLayout);

    // colorscale crossTraceDefaults needs newFullLayout with relinked keys
    Registry.getComponentMethod('colorscale', 'crossTraceDefaults')(newFullData, newFullLayout);

    // For persisting GUI-driven changes in layout
    // _preGUI and _tracePreGUI were already copied over in relinkPrivateKeys
    if(!newFullLayout._preGUI) newFullLayout._preGUI = {};
    // track trace GUI changes by uid rather than by trace index
    if(!newFullLayout._tracePreGUI) newFullLayout._tracePreGUI = {};
    var tracePreGUI = newFullLayout._tracePreGUI;
    var uids = {};
    var uid;
    for(uid in tracePreGUI) uids[uid] = 'old';
    for(i = 0; i < newFullData.length; i++) {
        uid = newFullData[i]._fullInput.uid;
        if(!uids[uid]) tracePreGUI[uid] = {};
        uids[uid] = 'new';
    }
    for(uid in uids) {
        if(uids[uid] === 'old') delete tracePreGUI[uid];
    }

    // set up containers for margin calculations
    initMargins(newFullLayout);

    // collect and do some initial calculations for rangesliders
    Registry.getComponentMethod('rangeslider', 'makeData')(newFullLayout);

    // update object references in calcdata
    if(!skipUpdateCalc && oldCalcdata.length === newFullData.length) {
        plots.supplyDefaultsUpdateCalc(oldCalcdata, newFullData);
    }
};

plots.supplyDefaultsUpdateCalc = function(oldCalcdata, newFullData) {
    for(var i = 0; i < newFullData.length; i++) {
        var newTrace = newFullData[i];
        var cd0 = (oldCalcdata[i] || [])[0];
        if(cd0 && cd0.trace) {
            var oldTrace = cd0.trace;
            if(oldTrace._hasCalcTransform) {
                var arrayAttrs = oldTrace._arrayAttrs;
                var j, astr, oldArrayVal;

                for(j = 0; j < arrayAttrs.length; j++) {
                    astr = arrayAttrs[j];
                    oldArrayVal = Lib.nestedProperty(oldTrace, astr).get().slice();
                    Lib.nestedProperty(newTrace, astr).set(oldArrayVal);
                }
            }
            cd0.trace = newTrace;
        }
    }
};

/**
 * Create a list of uid strings satisfying (in this order of importance):
 * 1. all unique, all strings
 * 2. matches input uids if provided
 * 3. matches previous data uids
 */
function getTraceUids(oldFullData, newData) {
    var len = newData.length;
    var oldFullInput = [];
    var i, prevFullInput;
    for(i = 0; i < oldFullData.length; i++) {
        var thisFullInput = oldFullData[i]._fullInput;
        if(thisFullInput !== prevFullInput) oldFullInput.push(thisFullInput);
        prevFullInput = thisFullInput;
    }
    var oldLen = oldFullInput.length;
    var out = new Array(len);
    var seenUids = {};

    function setUid(uid, i) {
        out[i] = uid;
        seenUids[uid] = 1;
    }

    function tryUid(uid, i) {
        if(uid && typeof uid === 'string' && !seenUids[uid]) {
            setUid(uid, i);
            return true;
        }
    }

    for(i = 0; i < len; i++) {
        var newUid = newData[i].uid;
        if(typeof newUid === 'number') newUid = String(newUid);

        if(tryUid(newUid, i)) continue;
        if(i < oldLen && tryUid(oldFullInput[i].uid, i)) continue;
        setUid(Lib.randstr(seenUids), i);
    }

    return out;
}

/**
 * Make a container for collecting subplots we need to display.
 *
 * Finds all subplot types we need to enumerate once and caches it,
 * but makes a new output object each time.
 * Single-trace subplots (which have no `id`) such as pie, table, etc
 * do not need to be collected because we just draw all visible traces.
 */
function emptySubplotLists() {
    var collectableSubplotTypes = Registry.collectableSubplotTypes;
    var out = {};
    var i, j;

    if(!collectableSubplotTypes) {
        collectableSubplotTypes = [];

        var subplotsRegistry = Registry.subplotsRegistry;

        for(var subplotType in subplotsRegistry) {
            var subplotModule = subplotsRegistry[subplotType];
            var subplotAttr = subplotModule.attr;

            if(subplotAttr) {
                collectableSubplotTypes.push(subplotType);

                // special case, currently just for cartesian:
                // we need to enumerate axes, not just subplots
                if(Array.isArray(subplotAttr)) {
                    for(j = 0; j < subplotAttr.length; j++) {
                        Lib.pushUnique(collectableSubplotTypes, subplotAttr[j]);
                    }
                }
            }
        }
    }

    for(i = 0; i < collectableSubplotTypes.length; i++) {
        out[collectableSubplotTypes[i]] = [];
    }
    return out;
}

/**
 * getFormatObj: use _context to get the format object from locale.
 * Used to get d3.locale argument object and extraFormat argument object
 *
 * Regarding d3.locale argument :
 * decimal and thousands can be overridden later by layout.separators
 * grouping and currency are not presently used by our automatic number
 * formatting system but can be used by custom formats.
 *
 * @returns {object} d3.locale format object
 */
function getFormatObj(gd, formatKeys) {
    var locale = gd._context.locale;
    if(!locale) locale === 'en-US';

    var formatDone = false;
    var formatObj = {};

    function includeFormat(newFormat) {
        var formatFinished = true;
        for(var i = 0; i < formatKeys.length; i++) {
            var formatKey = formatKeys[i];
            if(!formatObj[formatKey]) {
                if(newFormat[formatKey]) {
                    formatObj[formatKey] = newFormat[formatKey];
                } else formatFinished = false;
            }
        }
        if(formatFinished) formatDone = true;
    }

    // same as localize, look for format parts in each format spec in the chain
    for(var i = 0; i < 2; i++) {
        var locales = gd._context.locales;
        for(var j = 0; j < 2; j++) {
            var formatj = (locales[locale] || {}).format;
            if(formatj) {
                includeFormat(formatj);
                if(formatDone) break;
            }
            locales = Registry.localeRegistry;
        }

        var baseLocale = locale.split('-')[0];
        if(formatDone || baseLocale === locale) break;
        locale = baseLocale;
    }

    // lastly pick out defaults from english (non-US, as DMY is so much more common)
    if(!formatDone) includeFormat(Registry.localeRegistry.en.format);

    return formatObj;
}

/**
 * getFormatter: combine the final separators with the locale formatting object
 * we pulled earlier to generate number and time formatters
 * TODO: remove separators in v2, only use locale, so we don't need this step?
 *
 * @param {object} formatObj: d3.locale format object
 * @param {string} separators: length-2 string to override decimal and thousands
 *   separators in number formatting
 *
 * @returns {object} {numberFormat, timeFormat} d3 formatter factory functions
 *   for numbers and time
 */
function getFormatter(formatObj, separators) {
    formatObj.decimal = separators.charAt(0);
    formatObj.thousands = separators.charAt(1);

    return d3.locale(formatObj);
}

function fillMetaTextHelpers(newFullData, newFullLayout) {
    var _meta;
    var meta4data = [];

    if(newFullLayout.meta) {
        _meta = newFullLayout._meta = {
            meta: newFullLayout.meta,
            layout: {meta: newFullLayout.meta}
        };
    }

    for(var i = 0; i < newFullData.length; i++) {
        var trace = newFullData[i];

        if(trace.meta) {
            meta4data[trace.index] = trace._meta = {meta: trace.meta};
        } else if(newFullLayout.meta) {
            trace._meta = {meta: newFullLayout.meta};
        }
        if(newFullLayout.meta) {
            trace._meta.layout = {meta: newFullLayout.meta};
        }
    }

    if(meta4data.length) {
        if(!_meta) {
            _meta = newFullLayout._meta = {};
        }
        _meta.data = meta4data;
    }
}

// Create storage for all of the data related to frames and transitions:
plots.createTransitionData = function(gd) {
    // Set up the default keyframe if it doesn't exist:
    if(!gd._transitionData) {
        gd._transitionData = {};
    }

    if(!gd._transitionData._frames) {
        gd._transitionData._frames = [];
    }

    if(!gd._transitionData._frameHash) {
        gd._transitionData._frameHash = {};
    }

    if(!gd._transitionData._counter) {
        gd._transitionData._counter = 0;
    }

    if(!gd._transitionData._interruptCallbacks) {
        gd._transitionData._interruptCallbacks = [];
    }
};

// helper function to be bound to fullLayout to check
// whether a certain plot type is present on plot
// or trace has a category
plots._hasPlotType = function(category) {
    var i;

    // check base plot modules
    var basePlotModules = this._basePlotModules || [];
    for(i = 0; i < basePlotModules.length; i++) {
        if(basePlotModules[i].name === category) return true;
    }

    // check trace modules (including non-visible:true)
    var modules = this._modules || [];
    for(i = 0; i < modules.length; i++) {
        var name = modules[i].name;
        if(name === category) return true;
        // N.B. this is modules[i] along with 'categories' as a hash object
        var _module = Registry.modules[name];
        if(_module && _module.categories[category]) return true;
    }

    return false;
};

plots.cleanPlot = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var i, j;

    var basePlotModules = oldFullLayout._basePlotModules || [];
    for(i = 0; i < basePlotModules.length; i++) {
        var _module = basePlotModules[i];

        if(_module.clean) {
            _module.clean(newFullData, newFullLayout, oldFullData, oldFullLayout);
        }
    }

    var hadGl = oldFullLayout._has && oldFullLayout._has('gl');
    var hasGl = newFullLayout._has && newFullLayout._has('gl');

    if(hadGl && !hasGl) {
        if(oldFullLayout._glcontainer !== undefined) {
            oldFullLayout._glcontainer.selectAll('.gl-canvas').remove();
            oldFullLayout._glcontainer.selectAll('.no-webgl').remove();
            oldFullLayout._glcanvas = null;
        }
    }

    var hasInfoLayer = !!oldFullLayout._infolayer;

    oldLoop:
    for(i = 0; i < oldFullData.length; i++) {
        var oldTrace = oldFullData[i];
        var oldUid = oldTrace.uid;

        for(j = 0; j < newFullData.length; j++) {
            var newTrace = newFullData[j];

            if(oldUid === newTrace.uid) continue oldLoop;
        }

        // clean old colorbars
        if(hasInfoLayer) {
            oldFullLayout._infolayer.select('.cb' + oldUid).remove();
        }
    }
};

plots.linkSubplots = function(newFullData, newFullLayout, oldFullData, oldFullLayout) {
    var i, j;

    var oldSubplots = oldFullLayout._plots || {};
    var newSubplots = newFullLayout._plots = {};
    var newSubplotList = newFullLayout._subplots;

    var mockGd = {
        _fullData: newFullData,
        _fullLayout: newFullLayout
    };

    var ids = newSubplotList.cartesian.concat(newSubplotList.gl2d || []);

    for(i = 0; i < ids.length; i++) {
        var id = ids[i];
        var oldSubplot = oldSubplots[id];
        var xaxis = axisIDs.getFromId(mockGd, id, 'x');
        var yaxis = axisIDs.getFromId(mockGd, id, 'y');
        var plotinfo;

        // link or create subplot object
        if(oldSubplot) {
            plotinfo = newSubplots[id] = oldSubplot;
        } else {
            plotinfo = newSubplots[id] = {};
            plotinfo.id = id;
        }

        // add these axis ids to each others' subplot lists
        xaxis._counterAxes.push(yaxis._id);
        yaxis._counterAxes.push(xaxis._id);
        xaxis._subplotsWith.push(id);
        yaxis._subplotsWith.push(id);

        // update x and y axis layout object refs
        plotinfo.xaxis = xaxis;
        plotinfo.yaxis = yaxis;

        // By default, we clip at the subplot level,
        // but if one trace on a given subplot has *cliponaxis* set to false,
        // we need to clip at the trace module layer level;
        // find this out here, once of for all.
        plotinfo._hasClipOnAxisFalse = false;

        for(j = 0; j < newFullData.length; j++) {
            var trace = newFullData[j];

            if(
                trace.xaxis === plotinfo.xaxis._id &&
                trace.yaxis === plotinfo.yaxis._id &&
                trace.cliponaxis === false
            ) {
                plotinfo._hasClipOnAxisFalse = true;
                break;
            }
        }
    }

    // while we're at it, link overlaying axes to their main axes and
    // anchored axes to the axes they're anchored to
    var axList = axisIDs.list(mockGd, null, true);
    var ax;
    for(i = 0; i < axList.length; i++) {
        ax = axList[i];
        var mainAx = null;

        if(ax.overlaying) {
            mainAx = axisIDs.getFromId(mockGd, ax.overlaying);

            // you cannot overlay an axis that's already overlaying another
            if(mainAx && mainAx.overlaying) {
                ax.overlaying = false;
                mainAx = null;
            }
        }
        ax._mainAxis = mainAx || ax;

        /*
         * For now force overlays to overlay completely... so they
         * can drag together correctly and share backgrounds.
         * Later perhaps we make separate axis domain and
         * tick/line domain or something, so they can still share
         * the (possibly larger) dragger and background but don't
         * have to both be drawn over that whole domain
         */
        if(mainAx) ax.domain = mainAx.domain.slice();

        ax._anchorAxis = ax.anchor === 'free' ?
            null :
            axisIDs.getFromId(mockGd, ax.anchor);
    }

    // finally, we can find the main subplot for each axis
    // (on which the ticks & labels are drawn)
    for(i = 0; i < axList.length; i++) {
        ax = axList[i];
        ax._counterAxes.sort(axisIDs.idSort);
        ax._subplotsWith.sort(Lib.subplotSort);
        ax._mainSubplot = findMainSubplot(ax, newFullLayout);
    }
};

function findMainSubplot(ax, fullLayout) {
    var mockGd = {_fullLayout: fullLayout};

    var isX = ax._id.charAt(0) === 'x';
    var anchorAx = ax._mainAxis._anchorAxis;
    var mainSubplotID = '';
    var nextBestMainSubplotID = '';
    var anchorID = '';

    // First try the main ID with the anchor
    if(anchorAx) {
        anchorID = anchorAx._mainAxis._id;
        mainSubplotID = isX ? (ax._id + anchorID) : (anchorID + ax._id);
    }

    // Then look for a subplot with the counteraxis overlaying the anchor
    // If that fails just use the first subplot including this axis
    if(!mainSubplotID || !fullLayout._plots[mainSubplotID]) {
        mainSubplotID = '';

        var counterIDs = ax._counterAxes;
        for(var j = 0; j < counterIDs.length; j++) {
            var counterPart = counterIDs[j];
            var id = isX ? (ax._id + counterPart) : (counterPart + ax._id);
            if(!nextBestMainSubplotID) nextBestMainSubplotID = id;
            var counterAx = axisIDs.getFromId(mockGd, counterPart);
            if(anchorID && counterAx.overlaying === anchorID) {
                mainSubplotID = id;
                break;
            }
        }
    }

    return mainSubplotID || nextBestMainSubplotID;
}

// This function clears any trace attributes with valType: color and
// no set dflt filed in the plot schema. This is needed because groupby (which
// is the only transform for which this currently applies) supplies parent
// trace defaults, then expanded trace defaults. The result is that `null`
// colors are default-supplied and inherited as a color instead of a null.
// The result is that expanded trace default colors have no effect, with
// the final result that groups are indistinguishable. This function clears
// those colors so that individual groupby groups get unique colors.
plots.clearExpandedTraceDefaultColors = function(trace) {
    var colorAttrs, path, i;

    // This uses weird closure state in order to satisfy the linter rule
    // that we can't create functions in a loop.
    function locateColorAttrs(attr, attrName, attrs, level) {
        path[level] = attrName;
        path.length = level + 1;
        if(attr.valType === 'color' && attr.dflt === undefined) {
            colorAttrs.push(path.join('.'));
        }
    }

    path = [];

    // Get the cached colorAttrs:
    colorAttrs = trace._module._colorAttrs;

    // Or else compute and cache the colorAttrs on the module:
    if(!colorAttrs) {
        trace._module._colorAttrs = colorAttrs = [];
        PlotSchema.crawl(
            trace._module.attributes,
            locateColorAttrs
        );
    }

    for(i = 0; i < colorAttrs.length; i++) {
        var origprop = Lib.nestedProperty(trace, '_input.' + colorAttrs[i]);

        if(!origprop.get()) {
            Lib.nestedProperty(trace, colorAttrs[i]).set(null);
        }
    }
};


plots.supplyDataDefaults = function(dataIn, dataOut, layout, fullLayout) {
    var modules = fullLayout._modules;
    var visibleModules = fullLayout._visibleModules;
    var basePlotModules = fullLayout._basePlotModules;
    var cnt = 0;
    var colorCnt = 0;

    var i, fullTrace, trace;

    fullLayout._transformModules = [];

    function pushModule(fullTrace) {
        dataOut.push(fullTrace);

        var _module = fullTrace._module;
        if(!_module) return;

        Lib.pushUnique(modules, _module);
        if(fullTrace.visible === true) Lib.pushUnique(visibleModules, _module);
        Lib.pushUnique(basePlotModules, fullTrace._module.basePlotModule);
        cnt++;

        // TODO: do we really want color not to increment for explicitly invisible traces?
        // This logic is weird, but matches previous behavior: traces that you explicitly
        // set to visible:false do not increment the color, but traces WE determine to be
        // empty or invalid (and thus set to visible:false) DO increment color.
        // I kind of think we should just let all traces increment color, visible or not.
        // see mock: axes-autotype-empty vs. a test of restyling visible: false that
        // I can't find right now...
        if(fullTrace._input.visible !== false) colorCnt++;
    }

    var carpetIndex = {};
    var carpetDependents = [];
    var dataTemplate = (layout.template || {}).data || {};
    var templater = Template.traceTemplater(dataTemplate);

    for(i = 0; i < dataIn.length; i++) {
        trace = dataIn[i];

        // reuse uid we may have pulled out of oldFullData
        // Note: templater supplies trace type
        fullTrace = templater.newTrace(trace);
        fullTrace.uid = fullLayout._traceUids[i];
        plots.supplyTraceDefaults(trace, fullTrace, colorCnt, fullLayout, i);

        fullTrace.index = i;
        fullTrace._input = trace;
        fullTrace._expandedIndex = cnt;

        if(fullTrace.transforms && fullTrace.transforms.length) {
            var sdInvisible = trace.visible !== false && fullTrace.visible === false;

            var expandedTraces = applyTransforms(fullTrace, dataOut, layout, fullLayout);

            for(var j = 0; j < expandedTraces.length; j++) {
                var expandedTrace = expandedTraces[j];

                // No further templating during transforms.
                var fullExpandedTrace = {
                    _template: fullTrace._template,
                    type: fullTrace.type,
                    // set uid using parent uid and expanded index
                    // to promote consistency between update calls
                    uid: fullTrace.uid + j
                };

                // If the first supplyDefaults created `visible: false`,
                // clear it before running supplyDefaults a second time,
                // because sometimes there are items we still want to coerce
                // inside trace modules before determining that the trace is
                // again `visible: false`, for example partial visibilities
                // in `splom` traces.
                if(sdInvisible && expandedTrace.visible === false) {
                    delete expandedTrace.visible;
                }

                plots.supplyTraceDefaults(expandedTrace, fullExpandedTrace, cnt, fullLayout, i);

                // relink private (i.e. underscore) keys expanded trace to full expanded trace so
                // that transform supply-default methods can set _ keys for future use.
                relinkPrivateKeys(fullExpandedTrace, expandedTrace);

                // add info about parent data trace
                fullExpandedTrace.index = i;
                fullExpandedTrace._input = trace;
                fullExpandedTrace._fullInput = fullTrace;

                // add info about the expanded data
                fullExpandedTrace._expandedIndex = cnt;
                fullExpandedTrace._expandedInput = expandedTrace;

                pushModule(fullExpandedTrace);
            }
        } else {
            // add identify refs for consistency with transformed traces
            fullTrace._fullInput = fullTrace;
            fullTrace._expandedInput = fullTrace;

            pushModule(fullTrace);
        }

        if(Registry.traceIs(fullTrace, 'carpetAxis')) {
            carpetIndex[fullTrace.carpet] = fullTrace;
        }

        if(Registry.traceIs(fullTrace, 'carpetDependent')) {
            carpetDependents.push(i);
        }
    }

    for(i = 0; i < carpetDependents.length; i++) {
        fullTrace = dataOut[carpetDependents[i]];

        if(!fullTrace.visible) continue;

        var carpetAxis = carpetIndex[fullTrace.carpet];
        fullTrace._carpet = carpetAxis;

        if(!carpetAxis || !carpetAxis.visible) {
            fullTrace.visible = false;
            continue;
        }

        fullTrace.xaxis = carpetAxis.xaxis;
        fullTrace.yaxis = carpetAxis.yaxis;
    }
};

plots.supplyAnimationDefaults = function(opts) {
    opts = opts || {};
    var i;
    var optsOut = {};

    function coerce(attr, dflt) {
        return Lib.coerce(opts || {}, optsOut, animationAttrs, attr, dflt);
    }

    coerce('mode');
    coerce('direction');
    coerce('fromcurrent');

    if(Array.isArray(opts.frame)) {
        optsOut.frame = [];
        for(i = 0; i < opts.frame.length; i++) {
            optsOut.frame[i] = plots.supplyAnimationFrameDefaults(opts.frame[i] || {});
        }
    } else {
        optsOut.frame = plots.supplyAnimationFrameDefaults(opts.frame || {});
    }

    if(Array.isArray(opts.transition)) {
        optsOut.transition = [];
        for(i = 0; i < opts.transition.length; i++) {
            optsOut.transition[i] = plots.supplyAnimationTransitionDefaults(opts.transition[i] || {});
        }
    } else {
        optsOut.transition = plots.supplyAnimationTransitionDefaults(opts.transition || {});
    }

    return optsOut;
};

plots.supplyAnimationFrameDefaults = function(opts) {
    var optsOut = {};

    function coerce(attr, dflt) {
        return Lib.coerce(opts || {}, optsOut, animationAttrs.frame, attr, dflt);
    }

    coerce('duration');
    coerce('redraw');

    return optsOut;
};

plots.supplyAnimationTransitionDefaults = function(opts) {
    var optsOut = {};

    function coerce(attr, dflt) {
        return Lib.coerce(opts || {}, optsOut, animationAttrs.transition, attr, dflt);
    }

    coerce('duration');
    coerce('easing');

    return optsOut;
};

plots.supplyFrameDefaults = function(frameIn) {
    var frameOut = {};

    function coerce(attr, dflt) {
        return Lib.coerce(frameIn, frameOut, frameAttrs, attr, dflt);
    }

    coerce('group');
    coerce('name');
    coerce('traces');
    coerce('baseframe');
    coerce('data');
    coerce('layout');

    return frameOut;
};

plots.supplyTraceDefaults = function(traceIn, traceOut, colorIndex, layout, traceInIndex) {
    var colorway = layout.colorway || Color.defaults;
    var defaultColor = colorway[colorIndex % colorway.length];

    var i;

    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, plots.attributes, attr, dflt);
    }

    var visible = coerce('visible');

    coerce('type');
    coerce('name', layout._traceWord + ' ' + traceInIndex);

    coerce('uirevision', layout.uirevision);

    // we want even invisible traces to make their would-be subplots visible
    // so coerce the subplot id(s) now no matter what
    var _module = plots.getModule(traceOut);

    traceOut._module = _module;
    if(_module) {
        var basePlotModule = _module.basePlotModule;
        var subplotAttr = basePlotModule.attr;
        var subplotAttrs = basePlotModule.attributes;
        if(subplotAttr && subplotAttrs) {
            var subplots = layout._subplots;
            var subplotId = '';

            // TODO - currently if we draw an empty gl2d subplot, it draws
            // nothing then gets stuck and you can't get it back without newPlot
            // sort this out in the regl refactor? but for now just drop empty gl2d subplots
            if(basePlotModule.name !== 'gl2d' || visible) {
                if(Array.isArray(subplotAttr)) {
                    for(i = 0; i < subplotAttr.length; i++) {
                        var attri = subplotAttr[i];
                        var vali = Lib.coerce(traceIn, traceOut, subplotAttrs, attri);

                        if(subplots[attri]) Lib.pushUnique(subplots[attri], vali);
                        subplotId += vali;
                    }
                } else {
                    subplotId = Lib.coerce(traceIn, traceOut, subplotAttrs, subplotAttr);
                }

                if(subplots[basePlotModule.name]) {
                    Lib.pushUnique(subplots[basePlotModule.name], subplotId);
                }
            }
        }
    }

    if(visible) {
        coerce('customdata');
        coerce('ids');
        coerce('meta');

        if(Registry.traceIs(traceOut, 'showLegend')) {
            traceOut._dfltShowLegend = true;
            coerce('showlegend');
            coerce('legendgroup');
        } else {
            traceOut._dfltShowLegend = false;
        }

        if(_module) {
            _module.supplyDefaults(traceIn, traceOut, defaultColor, layout);
        }

        if(!Registry.traceIs(traceOut, 'noOpacity')) {
            coerce('opacity');
        }

        if(Registry.traceIs(traceOut, 'notLegendIsolatable')) {
            // This clears out the legendonly state for traces like carpet that
            // cannot be isolated in the legend
            traceOut.visible = !!traceOut.visible;
        }

        if(!Registry.traceIs(traceOut, 'noHover')) {
            if(!traceOut.hovertemplate) Lib.coerceHoverinfo(traceIn, traceOut, layout);

            // parcats support hover, but not hoverlabel stylings (yet)
            if(traceOut.type !== 'parcats') {
                Registry.getComponentMethod('fx', 'supplyDefaults')(traceIn, traceOut, defaultColor, layout);
            }
        }

        if(_module && _module.selectPoints) {
            coerce('selectedpoints');
        }

        plots.supplyTransformDefaults(traceIn, traceOut, layout);
    }

    return traceOut;
};

/**
 * hasMakesDataTransform: does this trace have a transform that makes its own
 * data, either by grabbing it from somewhere else or by creating it from input
 * parameters? If so, we should still keep going with supplyDefaults
 * even if the trace is invisible, which may just be because it has no data yet.
 */
function hasMakesDataTransform(trace) {
    var transforms = trace.transforms;
    if(Array.isArray(transforms) && transforms.length) {
        for(var i = 0; i < transforms.length; i++) {
            var ti = transforms[i];
            var _module = ti._module || transformsRegistry[ti.type];
            if(_module && _module.makesData) return true;
        }
    }
    return false;
}

plots.hasMakesDataTransform = hasMakesDataTransform;

plots.supplyTransformDefaults = function(traceIn, traceOut, layout) {
    // For now we only allow transforms on 1D traces, ie those that specify a _length.
    // If we were to implement 2D transforms, we'd need to have each transform
    // describe its own applicability and disable itself when it doesn't apply.
    // Also allow transforms that make their own data, but not in globalTransforms
    if(!(traceOut._length || hasMakesDataTransform(traceIn))) return;

    var globalTransforms = layout._globalTransforms || [];
    var transformModules = layout._transformModules || [];

    if(!Array.isArray(traceIn.transforms) && globalTransforms.length === 0) return;

    var containerIn = traceIn.transforms || [];
    var transformList = globalTransforms.concat(containerIn);
    var containerOut = traceOut.transforms = [];

    for(var i = 0; i < transformList.length; i++) {
        var transformIn = transformList[i];
        var type = transformIn.type;
        var _module = transformsRegistry[type];
        var transformOut;

        /*
         * Supply defaults may run twice. First pass runs all supply defaults steps
         * and adds the _module to any output transforms.
         * If transforms exist another pass is run so that any generated traces also
         * go through supply defaults. This has the effect of rerunning
         * supplyTransformDefaults. If the transform does not have a `transform`
         * function it could not have generated any new traces and the second stage
         * is unnecessary. We detect this case with the following variables.
         */
        var isFirstStage = !(transformIn._module && transformIn._module === _module);
        var doLaterStages = _module && typeof _module.transform === 'function';

        if(!_module) Lib.warn('Unrecognized transform type ' + type + '.');

        if(_module && _module.supplyDefaults && (isFirstStage || doLaterStages)) {
            transformOut = _module.supplyDefaults(transformIn, traceOut, layout, traceIn);
            transformOut.type = type;
            transformOut._module = _module;

            Lib.pushUnique(transformModules, _module);
        } else {
            transformOut = Lib.extendFlat({}, transformIn);
        }

        containerOut.push(transformOut);
    }
};

function applyTransforms(fullTrace, fullData, layout, fullLayout) {
    var container = fullTrace.transforms;
    var dataOut = [fullTrace];

    for(var i = 0; i < container.length; i++) {
        var transform = container[i];
        var _module = transformsRegistry[transform.type];

        if(_module && _module.transform) {
            dataOut = _module.transform(dataOut, {
                transform: transform,
                fullTrace: fullTrace,
                fullData: fullData,
                layout: layout,
                fullLayout: fullLayout,
                transformIndex: i
            });
        }
    }

    return dataOut;
}

plots.supplyLayoutGlobalDefaults = function(layoutIn, layoutOut, formatObj) {
    function coerce(attr, dflt) {
        return Lib.coerce(layoutIn, layoutOut, plots.layoutAttributes, attr, dflt);
    }

    var template = layoutIn.template;
    if(Lib.isPlainObject(template)) {
        layoutOut.template = template;
        layoutOut._template = template.layout;
        layoutOut._dataTemplate = template.data;
    }

    var globalFont = Lib.coerceFont(coerce, 'font');

    coerce('title.text', layoutOut._dfltTitle.plot);

    Lib.coerceFont(coerce, 'title.font', {
        family: globalFont.family,
        size: Math.round(globalFont.size * 1.4),
        color: globalFont.color
    });

    coerce('title.xref');
    coerce('title.yref');
    coerce('title.x');
    coerce('title.y');
    coerce('title.xanchor');
    coerce('title.yanchor');
    coerce('title.pad.t');
    coerce('title.pad.r');
    coerce('title.pad.b');
    coerce('title.pad.l');

    // Make sure that autosize is defaulted to *true*
    // on layouts with no set width and height for backward compatibly,
    // in particular https://plot.ly/javascript/responsive-fluid-layout/
    //
    // Before https://github.com/plotly/plotly.js/pull/635 ,
    // layouts with no set width and height were set temporary set to 'initial'
    // to pass through the autosize routine
    //
    // This behavior is subject to change in v2.
    coerce('autosize', !(layoutIn.width && layoutIn.height));

    coerce('width');
    coerce('height');
    coerce('margin.l');
    coerce('margin.r');
    coerce('margin.t');
    coerce('margin.b');
    coerce('margin.pad');
    coerce('margin.autoexpand');

    if(layoutIn.width && layoutIn.height) plots.sanitizeMargins(layoutOut);

    Registry.getComponentMethod('grid', 'sizeDefaults')(layoutIn, layoutOut);

    coerce('paper_bgcolor');

    coerce('separators', formatObj.decimal + formatObj.thousands);
    coerce('hidesources');

    coerce('colorway');

    coerce('datarevision');
    var uirevision = coerce('uirevision');
    coerce('editrevision', uirevision);
    coerce('selectionrevision', uirevision);

    coerce('modebar.orientation');
    coerce('modebar.bgcolor', Color.addOpacity(layoutOut.paper_bgcolor, 0.5));
    var modebarDefaultColor = Color.contrast(Color.rgb(layoutOut.modebar.bgcolor));
    coerce('modebar.color', Color.addOpacity(modebarDefaultColor, 0.3));
    coerce('modebar.activecolor', Color.addOpacity(modebarDefaultColor, 0.7));
    coerce('modebar.uirevision', uirevision);

    coerce('meta');

    // do not include defaults in fullLayout when users do not set transition
    if(Lib.isPlainObject(layoutIn.transition)) {
        coerce('transition.duration');
        coerce('transition.easing');
        coerce('transition.ordering');
    }

    Registry.getComponentMethod(
        'calendars',
        'handleDefaults'
    )(layoutIn, layoutOut, 'calendar');

    Registry.getComponentMethod(
        'fx',
        'supplyLayoutGlobalDefaults'
    )(layoutIn, layoutOut, coerce);
};

plots.plotAutoSize = function plotAutoSize(gd, layout, fullLayout) {
    var context = gd._context || {};
    var frameMargins = context.frameMargins;
    var newWidth;
    var newHeight;

    var isPlotDiv = Lib.isPlotDiv(gd);

    if(isPlotDiv) gd.emit('plotly_autosize');

    // embedded in an iframe - just take the full iframe size
    // if we get to this point, with no aspect ratio restrictions
    if(context.fillFrame) {
        newWidth = window.innerWidth;
        newHeight = window.innerHeight;

        // somehow we get a few extra px height sometimes...
        // just hide it
        document.body.style.overflow = 'hidden';
    } else {
        // plotly.js - let the developers do what they want, either
        // provide height and width for the container div,
        // specify size in layout, or take the defaults,
        // but don't enforce any ratio restrictions
        var computedStyle = isPlotDiv ? window.getComputedStyle(gd) : {};

        newWidth = parseFloat(computedStyle.width) || parseFloat(computedStyle.maxWidth) || fullLayout.width;
        newHeight = parseFloat(computedStyle.height) || parseFloat(computedStyle.maxHeight) || fullLayout.height;

        if(isNumeric(frameMargins) && frameMargins > 0) {
            var factor = 1 - 2 * frameMargins;
            newWidth = Math.round(factor * newWidth);
            newHeight = Math.round(factor * newHeight);
        }
    }

    var minWidth = plots.layoutAttributes.width.min;
    var minHeight = plots.layoutAttributes.height.min;
    if(newWidth < minWidth) newWidth = minWidth;
    if(newHeight < minHeight) newHeight = minHeight;

    var widthHasChanged = !layout.width &&
        (Math.abs(fullLayout.width - newWidth) > 1);
    var heightHasChanged = !layout.height &&
        (Math.abs(fullLayout.height - newHeight) > 1);

    if(heightHasChanged || widthHasChanged) {
        if(widthHasChanged) fullLayout.width = newWidth;
        if(heightHasChanged) fullLayout.height = newHeight;
    }

    // cache initial autosize value, used in relayout when
    // width or height values are set to null
    if(!gd._initialAutoSize) {
        gd._initialAutoSize = { width: newWidth, height: newHeight };
    }

    plots.sanitizeMargins(fullLayout);
};

plots.supplyLayoutModuleDefaults = function(layoutIn, layoutOut, fullData, transitionData) {
    var componentsRegistry = Registry.componentsRegistry;
    var basePlotModules = layoutOut._basePlotModules;
    var component, i, _module;

    var Cartesian = Registry.subplotsRegistry.cartesian;

    // check if any components need to add more base plot modules
    // that weren't captured by traces
    for(component in componentsRegistry) {
        _module = componentsRegistry[component];

        if(_module.includeBasePlot) {
            _module.includeBasePlot(layoutIn, layoutOut);
        }
    }

    // make sure we *at least* have some cartesian axes
    if(!basePlotModules.length) {
        basePlotModules.push(Cartesian);
    }

    // ensure all cartesian axes have at least one subplot
    if(layoutOut._has('cartesian')) {
        Registry.getComponentMethod('grid', 'contentDefaults')(layoutIn, layoutOut);
        Cartesian.finalizeSubplots(layoutIn, layoutOut);
    }

    // sort subplot lists
    for(var subplotType in layoutOut._subplots) {
        layoutOut._subplots[subplotType].sort(Lib.subplotSort);
    }

    // base plot module layout defaults
    for(i = 0; i < basePlotModules.length; i++) {
        _module = basePlotModules[i];

        // e.g. pie does not have a layout-defaults step
        if(_module.supplyLayoutDefaults) {
            _module.supplyLayoutDefaults(layoutIn, layoutOut, fullData);
        }
    }

    // trace module layout defaults
    // use _modules rather than _visibleModules so that even
    // legendonly traces can include settings - eg barmode, which affects
    // legend.traceorder default value.
    var modules = layoutOut._modules;
    for(i = 0; i < modules.length; i++) {
        _module = modules[i];

        if(_module.supplyLayoutDefaults) {
            _module.supplyLayoutDefaults(layoutIn, layoutOut, fullData);
        }
    }

    // transform module layout defaults
    var transformModules = layoutOut._transformModules;
    for(i = 0; i < transformModules.length; i++) {
        _module = transformModules[i];

        if(_module.supplyLayoutDefaults) {
            _module.supplyLayoutDefaults(layoutIn, layoutOut, fullData, transitionData);
        }
    }

    for(component in componentsRegistry) {
        _module = componentsRegistry[component];

        if(_module.supplyLayoutDefaults) {
            _module.supplyLayoutDefaults(layoutIn, layoutOut, fullData);
        }
    }
};

// Remove all plotly attributes from a div so it can be replotted fresh
// TODO: these really need to be encapsulated into a much smaller set...
plots.purge = function(gd) {
    // note: we DO NOT remove _context because it doesn't change when we insert
    // a new plot, and may have been set outside of our scope.

    var fullLayout = gd._fullLayout || {};
    if(fullLayout._glcontainer !== undefined) {
        fullLayout._glcontainer.selectAll('.gl-canvas').remove();
        fullLayout._glcontainer.remove();
        fullLayout._glcanvas = null;
    }
    if(fullLayout._geocontainer !== undefined) fullLayout._geocontainer.remove();

    // remove modebar
    if(fullLayout._modeBar) fullLayout._modeBar.destroy();

    if(gd._transitionData) {
        // Ensure any dangling callbacks are simply dropped if the plot is purged.
        // This is more or less only actually important for testing.
        if(gd._transitionData._interruptCallbacks) {
            gd._transitionData._interruptCallbacks.length = 0;
        }

        if(gd._transitionData._animationRaf) {
            window.cancelAnimationFrame(gd._transitionData._animationRaf);
        }
    }

    // remove any planned throttles
    Lib.clearThrottle();

    // remove responsive handler
    Lib.clearResponsive(gd);

    // data and layout
    delete gd.data;
    delete gd.layout;
    delete gd._fullData;
    delete gd._fullLayout;
    delete gd.calcdata;
    delete gd.framework;
    delete gd.empty;

    delete gd.fid;

    delete gd.undoqueue; // action queue
    delete gd.undonum;
    delete gd.autoplay; // are we doing an action that doesn't go in undo queue?
    delete gd.changed;

    // these get recreated on Plotly.plot anyway, but just to be safe
    // (and to have a record of them...)
    delete gd._promises;
    delete gd._redrawTimer;
    delete gd._hmlumcount;
    delete gd._hmpixcount;
    delete gd._transitionData;
    delete gd._transitioning;
    delete gd._initialAutoSize;
    delete gd._transitioningWithDuration;

    // created during certain events, that *should* clean them up
    // themselves, but may not if there was an error
    delete gd._dragging;
    delete gd._dragged;
    delete gd._dragdata;
    delete gd._hoverdata;
    delete gd._snapshotInProgress;
    delete gd._editing;
    delete gd._mouseDownTime;
    delete gd._legendMouseDownTime;

    // remove all event listeners
    if(gd.removeAllListeners) gd.removeAllListeners();
};

plots.style = function(gd) {
    var _modules = gd._fullLayout._visibleModules;
    var styleModules = [];
    var i;

    // some trace modules reuse the same style method,
    // make sure to not unnecessary call them multiple times.

    for(i = 0; i < _modules.length; i++) {
        var _module = _modules[i];
        if(_module.style) {
            Lib.pushUnique(styleModules, _module.style);
        }
    }

    for(i = 0; i < styleModules.length; i++) {
        styleModules[i](gd);
    }
};

plots.sanitizeMargins = function(fullLayout) {
    // polar doesn't do margins...
    if(!fullLayout || !fullLayout.margin) return;

    var width = fullLayout.width;
    var height = fullLayout.height;
    var margin = fullLayout.margin;
    var plotWidth = width - (margin.l + margin.r);
    var plotHeight = height - (margin.t + margin.b);
    var correction;

    // if margin.l + margin.r = 0 then plotWidth > 0
    // as width >= 10 by supplyDefaults
    // similarly for margin.t + margin.b

    if(plotWidth < 0) {
        correction = (width - 1) / (margin.l + margin.r);
        margin.l = Math.floor(correction * margin.l);
        margin.r = Math.floor(correction * margin.r);
    }

    if(plotHeight < 0) {
        correction = (height - 1) / (margin.t + margin.b);
        margin.t = Math.floor(correction * margin.t);
        margin.b = Math.floor(correction * margin.b);
    }
};

plots.clearAutoMarginIds = function(gd) {
    gd._fullLayout._pushmarginIds = {};
};

plots.allowAutoMargin = function(gd, id) {
    gd._fullLayout._pushmarginIds[id] = 1;
};

function initMargins(fullLayout) {
    var margin = fullLayout.margin;

    if(!fullLayout._size) {
        var gs = fullLayout._size = {
            l: Math.round(margin.l),
            r: Math.round(margin.r),
            t: Math.round(margin.t),
            b: Math.round(margin.b),
            p: Math.round(margin.pad)
        };
        gs.w = Math.round(fullLayout.width) - gs.l - gs.r;
        gs.h = Math.round(fullLayout.height) - gs.t - gs.b;
    }
    if(!fullLayout._pushmargin) fullLayout._pushmargin = {};
    if(!fullLayout._pushmarginIds) fullLayout._pushmarginIds = {};
}

/**
 * autoMargin: called by components that may need to expand the margins to
 * be rendered on-plot.
 *
 * @param {DOM element} gd
 * @param {string} id - an identifier unique (within this plot) to this object,
 *     so we can remove a previous margin expansion from the same object.
 * @param {object} o - the margin requirements of this object, or omit to delete
 *     this entry (like if it's hidden). Keys are:
 *     x, y: plot fraction of the anchor point.
 *     xl, xr, yt, yb: if the object has an extent defined in plot fraction,
 *         you can specify both edges as plot fractions in each dimension
 *     l, r, t, b: the pixels to pad past the plot fraction x[l|r] and y[t|b]
 *     pad: extra pixels to add in all directions, default 12 (why?)
 */
plots.autoMargin = function(gd, id, o) {
    var fullLayout = gd._fullLayout;

    var pushMargin = fullLayout._pushmargin;
    var pushMarginIds = fullLayout._pushmarginIds;

    if(fullLayout.margin.autoexpand !== false) {
        if(!o) {
            delete pushMargin[id];
            delete pushMarginIds[id];
        } else {
            var pad = o.pad;
            if(pad === undefined) {
                var margin = fullLayout.margin;
                // if no explicit pad is given, use 12px unless there's a
                // specified margin that's smaller than that
                pad = Math.min(12, margin.l, margin.r, margin.t, margin.b);
            }

            // if the item is too big, just give it enough automargin to
            // make sure you can still grab it and bring it back
            if(o.l + o.r > fullLayout.width * 0.5) o.l = o.r = 0;
            if(o.b + o.t > fullLayout.height * 0.5) o.b = o.t = 0;

            var xl = o.xl !== undefined ? o.xl : o.x;
            var xr = o.xr !== undefined ? o.xr : o.x;
            var yt = o.yt !== undefined ? o.yt : o.y;
            var yb = o.yb !== undefined ? o.yb : o.y;

            pushMargin[id] = {
                l: {val: xl, size: o.l + pad},
                r: {val: xr, size: o.r + pad},
                b: {val: yb, size: o.b + pad},
                t: {val: yt, size: o.t + pad}
            };
            pushMarginIds[id] = 1;
        }

        if(!fullLayout._replotting) {
            plots.doAutoMargin(gd);
        }
    }
};

plots.doAutoMargin = function(gd) {
    var fullLayout = gd._fullLayout;
    if(!fullLayout._size) fullLayout._size = {};
    initMargins(fullLayout);

    var gs = fullLayout._size;
    var margin = fullLayout.margin;
    var oldMargins = Lib.extendFlat({}, gs);

    // adjust margins for outside components
    // fullLayout.margin is the requested margin,
    // fullLayout._size has margins and plotsize after adjustment
    var ml = margin.l;
    var mr = margin.r;
    var mt = margin.t;
    var mb = margin.b;
    var width = fullLayout.width;
    var height = fullLayout.height;
    var pushMargin = fullLayout._pushmargin;
    var pushMarginIds = fullLayout._pushmarginIds;

    if(fullLayout.margin.autoexpand !== false) {
        for(var k in pushMargin) {
            if(!pushMarginIds[k]) delete pushMargin[k];
        }

        // fill in the requested margins
        pushMargin.base = {
            l: {val: 0, size: ml},
            r: {val: 1, size: mr},
            t: {val: 1, size: mt},
            b: {val: 0, size: mb}
        };

        // now cycle through all the combinations of l and r
        // (and t and b) to find the required margins

        for(var k1 in pushMargin) {
            var pushleft = pushMargin[k1].l || {};
            var pushbottom = pushMargin[k1].b || {};
            var fl = pushleft.val;
            var pl = pushleft.size;
            var fb = pushbottom.val;
            var pb = pushbottom.size;

            for(var k2 in pushMargin) {
                if(isNumeric(pl) && pushMargin[k2].r) {
                    var fr = pushMargin[k2].r.val;
                    var pr = pushMargin[k2].r.size;

                    if(fr > fl) {
                        var newL = (pl * fr + (pr - width) * fl) / (fr - fl);
                        var newR = (pr * (1 - fl) + (pl - width) * (1 - fr)) / (fr - fl);
                        if(newL >= 0 && newR >= 0 && width - (newL + newR) > 0 && newL + newR > ml + mr) {
                            ml = newL;
                            mr = newR;
                        }
                    }
                }

                if(isNumeric(pb) && pushMargin[k2].t) {
                    var ft = pushMargin[k2].t.val;
                    var pt = pushMargin[k2].t.size;

                    if(ft > fb) {
                        var newB = (pb * ft + (pt - height) * fb) / (ft - fb);
                        var newT = (pt * (1 - fb) + (pb - height) * (1 - ft)) / (ft - fb);
                        if(newB >= 0 && newT >= 0 && height - (newT + newB) > 0 && newB + newT > mb + mt) {
                            mb = newB;
                            mt = newT;
                        }
                    }
                }
            }
        }
    }

    gs.l = Math.round(ml);
    gs.r = Math.round(mr);
    gs.t = Math.round(mt);
    gs.b = Math.round(mb);
    gs.p = Math.round(margin.pad);
    gs.w = Math.round(width) - gs.l - gs.r;
    gs.h = Math.round(height) - gs.t - gs.b;

    // if things changed and we're not already redrawing, trigger a redraw
    if(!fullLayout._replotting && plots.didMarginChange(oldMargins, gs)) {
        if('_redrawFromAutoMarginCount' in fullLayout) {
            fullLayout._redrawFromAutoMarginCount++;
        } else {
            fullLayout._redrawFromAutoMarginCount = 1;
        }
        return Registry.call('plot', gd);
    }
};

var marginKeys = ['l', 'r', 't', 'b', 'p', 'w', 'h'];

plots.didMarginChange = function(margin0, margin1) {
    for(var i = 0; i < marginKeys.length; i++) {
        var k = marginKeys[i];
        var m0 = margin0[k];
        var m1 = margin1[k];
        // use 1px tolerance in case we old/new differ only
        // by rounding errors, which can lead to infinite loops
        if(!isNumeric(m0) || Math.abs(m1 - m0) > 1) {
            return true;
        }
    }
    return false;
};

/**
 * JSONify the graph data and layout
 *
 * This function needs to recurse because some src can be inside
 * sub-objects.
 *
 * It also strips out functions and private (starts with _) elements.
 * Therefore, we can add temporary things to data and layout that don't
 * get saved.
 *
 * @param gd The graphDiv
 * @param {Boolean} dataonly If true, don't return layout.
 * @param {'keepref'|'keepdata'|'keepall'} [mode='keepref'] Filter what's kept
 *      keepref: remove data for which there's a src present
 *          eg if there's xsrc present (and xsrc is well-formed,
 *          ie has : and some chars before it), strip out x
 *      keepdata: remove all src tags, don't remove the data itself
 *      keepall: keep data and src
 * @param {String} output If you specify 'object', the result will not be stringified
 * @param {Boolean} useDefaults If truthy, use _fullLayout and _fullData
 * @returns {Object|String}
 */
plots.graphJson = function(gd, dataonly, mode, output, useDefaults) {
    // if the defaults aren't supplied yet, we need to do that...
    if((useDefaults && dataonly && !gd._fullData) ||
            (useDefaults && !dataonly && !gd._fullLayout)) {
        plots.supplyDefaults(gd);
    }

    var data = (useDefaults) ? gd._fullData : gd.data;
    var layout = (useDefaults) ? gd._fullLayout : gd.layout;
    var frames = (gd._transitionData || {})._frames;

    function stripObj(d) {
        if(typeof d === 'function') {
            return null;
        }
        if(Lib.isPlainObject(d)) {
            var o = {};
            var v, src;
            for(v in d) {
                // remove private elements and functions
                // _ is for private, [ is a mistake ie [object Object]
                if(typeof d[v] === 'function' ||
                        ['_', '['].indexOf(v.charAt(0)) !== -1) {
                    continue;
                }

                // look for src/data matches and remove the appropriate one
                if(mode === 'keepdata') {
                    // keepdata: remove all ...src tags
                    if(v.substr(v.length - 3) === 'src') {
                        continue;
                    }
                } else if(mode === 'keepstream') {
                    // keep sourced data if it's being streamed.
                    // similar to keepref, but if the 'stream' object exists
                    // in a trace, we will keep the data array.
                    src = d[v + 'src'];
                    if(typeof src === 'string' && src.indexOf(':') > 0) {
                        if(!Lib.isPlainObject(d.stream)) {
                            continue;
                        }
                    }
                } else if(mode !== 'keepall') {
                    // keepref: remove sourced data but only
                    // if the source tag is well-formed
                    src = d[v + 'src'];
                    if(typeof src === 'string' && src.indexOf(':') > 0) {
                        continue;
                    }
                }

                // OK, we're including this... recurse into it
                o[v] = stripObj(d[v]);
            }
            return o;
        }

        if(Array.isArray(d)) {
            return d.map(stripObj);
        }

        if(Lib.isTypedArray(d)) {
            return Lib.simpleMap(d, Lib.identity);
        }

        // convert native dates to date strings...
        // mostly for external users exporting to plotly
        if(Lib.isJSDate(d)) return Lib.ms2DateTimeLocal(+d);

        return d;
    }

    var obj = {
        data: (data || []).map(function(v) {
            var d = stripObj(v);
            // fit has some little arrays in it that don't contain data,
            // just fit params and meta
            if(dataonly) { delete d.fit; }
            return d;
        })
    };
    if(!dataonly) { obj.layout = stripObj(layout); }

    if(gd.framework && gd.framework.isPolar) obj = gd.framework.getConfig();

    if(frames) obj.frames = stripObj(frames);

    return (output === 'object') ? obj : JSON.stringify(obj);
};

/**
 * Modify a keyframe using a list of operations:
 *
 * @param {array of objects} operations
 *      Sequence of operations to be performed on the keyframes
 */
plots.modifyFrames = function(gd, operations) {
    var i, op, frame;
    var _frames = gd._transitionData._frames;
    var _frameHash = gd._transitionData._frameHash;

    for(i = 0; i < operations.length; i++) {
        op = operations[i];

        switch(op.type) {
            // No reason this couldn't exist, but is currently unused/untested:
            /* case 'rename':
                frame = _frames[op.index];
                delete _frameHash[frame.name];
                _frameHash[op.name] = frame;
                frame.name = op.name;
                break;*/
            case 'replace':
                frame = op.value;
                var oldName = (_frames[op.index] || {}).name;
                var newName = frame.name;
                _frames[op.index] = _frameHash[newName] = frame;

                if(newName !== oldName) {
                    // If name has changed in addition to replacement, then update
                    // the lookup table:
                    delete _frameHash[oldName];
                    _frameHash[newName] = frame;
                }

                break;
            case 'insert':
                frame = op.value;
                _frameHash[frame.name] = frame;
                _frames.splice(op.index, 0, frame);
                break;
            case 'delete':
                frame = _frames[op.index];
                delete _frameHash[frame.name];
                _frames.splice(op.index, 1);
                break;
        }
    }

    return Promise.resolve();
};

/*
 * Compute a keyframe. Merge a keyframe into its base frame(s) and
 * expand properties.
 *
 * @param {object} frameLookup
 *      An object containing frames keyed by name (i.e. gd._transitionData._frameHash)
 * @param {string} frame
 *      The name of the keyframe to be computed
 *
 * Returns: a new object with the merged content
 */
plots.computeFrame = function(gd, frameName) {
    var frameLookup = gd._transitionData._frameHash;
    var i, traceIndices, traceIndex, destIndex;

    // Null or undefined will fail on .toString(). We'll allow numbers since we
    // make it clear frames must be given string names, but we'll allow numbers
    // here since they're otherwise fine for looking up frames as long as they're
    // properly cast to strings. We really just want to ensure here that this
    // 1) doesn't fail, and
    // 2) doens't give an incorrect answer (which String(frameName) would)
    if(!frameName) {
        throw new Error('computeFrame must be given a string frame name');
    }

    var framePtr = frameLookup[frameName.toString()];

    // Return false if the name is invalid:
    if(!framePtr) {
        return false;
    }

    var frameStack = [framePtr];
    var frameNameStack = [framePtr.name];

    // Follow frame pointers:
    while(framePtr.baseframe && (framePtr = frameLookup[framePtr.baseframe.toString()])) {
        // Avoid infinite loops:
        if(frameNameStack.indexOf(framePtr.name) !== -1) break;

        frameStack.push(framePtr);
        frameNameStack.push(framePtr.name);
    }

    // A new object for the merged result:
    var result = {};

    // Merge, starting with the last and ending with the desired frame:
    while((framePtr = frameStack.pop())) {
        if(framePtr.layout) {
            result.layout = plots.extendLayout(result.layout, framePtr.layout);
        }

        if(framePtr.data) {
            if(!result.data) {
                result.data = [];
            }
            traceIndices = framePtr.traces;

            if(!traceIndices) {
                // If not defined, assume serial order starting at zero
                traceIndices = [];
                for(i = 0; i < framePtr.data.length; i++) {
                    traceIndices[i] = i;
                }
            }

            if(!result.traces) {
                result.traces = [];
            }

            for(i = 0; i < framePtr.data.length; i++) {
                // Loop through this frames data, find out where it should go,
                // and merge it!
                traceIndex = traceIndices[i];
                if(traceIndex === undefined || traceIndex === null) {
                    continue;
                }

                destIndex = result.traces.indexOf(traceIndex);
                if(destIndex === -1) {
                    destIndex = result.data.length;
                    result.traces[destIndex] = traceIndex;
                }

                result.data[destIndex] = plots.extendTrace(result.data[destIndex], framePtr.data[i]);
            }
        }
    }

    return result;
};

/*
 * Recompute the lookup table that maps frame name -> frame object. addFrames/
 * deleteFrames already manages this data one at a time, so the only time this
 * is necessary is if you poke around manually in `gd._transitionData._frames`
 * and create and haven't updated the lookup table.
 */
plots.recomputeFrameHash = function(gd) {
    var hash = gd._transitionData._frameHash = {};
    var frames = gd._transitionData._frames;
    for(var i = 0; i < frames.length; i++) {
        var frame = frames[i];
        if(frame && frame.name) {
            hash[frame.name] = frame;
        }
    }
};

/**
 * Extend an object, treating container arrays very differently by extracting
 * their contents and merging them separately.
 *
 * This exists so that we can extendDeepNoArrays and avoid stepping into data
 * arrays without knowledge of the plot schema, but so that we may also manually
 * recurse into known container arrays, such as transforms.
 *
 * See extendTrace and extendLayout below for usage.
 */
plots.extendObjectWithContainers = function(dest, src, containerPaths) {
    var containerProp, containerVal, i, j, srcProp, destProp, srcContainer, destContainer;
    var copy = Lib.extendDeepNoArrays({}, src || {});
    var expandedObj = Lib.expandObjectPaths(copy);
    var containerObj = {};

    // Step through and extract any container properties. Otherwise extendDeepNoArrays
    // will clobber any existing properties with an empty array and then supplyDefaults
    // will reset everything to defaults.
    if(containerPaths && containerPaths.length) {
        for(i = 0; i < containerPaths.length; i++) {
            containerProp = Lib.nestedProperty(expandedObj, containerPaths[i]);
            containerVal = containerProp.get();

            if(containerVal === undefined) {
                Lib.nestedProperty(containerObj, containerPaths[i]).set(null);
            } else {
                containerProp.set(null);
                Lib.nestedProperty(containerObj, containerPaths[i]).set(containerVal);
            }
        }
    }

    dest = Lib.extendDeepNoArrays(dest || {}, expandedObj);

    if(containerPaths && containerPaths.length) {
        for(i = 0; i < containerPaths.length; i++) {
            srcProp = Lib.nestedProperty(containerObj, containerPaths[i]);
            srcContainer = srcProp.get();

            if(!srcContainer) continue;

            destProp = Lib.nestedProperty(dest, containerPaths[i]);
            destContainer = destProp.get();

            if(!Array.isArray(destContainer)) {
                destContainer = [];
                destProp.set(destContainer);
            }

            for(j = 0; j < srcContainer.length; j++) {
                var srcObj = srcContainer[j];

                if(srcObj === null) destContainer[j] = null;
                else {
                    destContainer[j] = plots.extendObjectWithContainers(destContainer[j], srcObj);
                }
            }

            destProp.set(destContainer);
        }
    }

    return dest;
};

plots.dataArrayContainers = ['transforms', 'dimensions'];
plots.layoutArrayContainers = Registry.layoutArrayContainers;

/*
 * Extend a trace definition. This method:
 *
 *  1. directly transfers any array references
 *  2. manually recurses into container arrays like transforms
 *
 * The result is the original object reference with the new contents merged in.
 */
plots.extendTrace = function(destTrace, srcTrace) {
    return plots.extendObjectWithContainers(destTrace, srcTrace, plots.dataArrayContainers);
};

/*
 * Extend a layout definition. This method:
 *
 *  1. directly transfers any array references (not critically important for
 *     layout since there aren't really data arrays)
 *  2. manually recurses into container arrays like annotations
 *
 * The result is the original object reference with the new contents merged in.
 */
plots.extendLayout = function(destLayout, srcLayout) {
    return plots.extendObjectWithContainers(destLayout, srcLayout, plots.layoutArrayContainers);
};

/**
 * Transition to a set of new data and layout properties from Plotly.animate
 *
 * @param {DOM element} gd
 * @param {Object[]} data
 *      an array of data objects following the normal Plotly data definition format
 * @param {Object} layout
 *      a layout object, following normal Plotly layout format
 * @param {Number[]} traces
 *      indices of the corresponding traces specified in `data`
 * @param {Object} frameOpts
 *      options for the frame (i.e. whether to redraw post-transition)
 * @param {Object} transitionOpts
 *      options for the transition
 */
plots.transition = function(gd, data, layout, traces, frameOpts, transitionOpts) {
    var opts = {redraw: frameOpts.redraw};
    var transitionedTraces = {};
    var axEdits = [];

    opts.prepareFn = function() {
        var dataLength = Array.isArray(data) ? data.length : 0;
        var traceIndices = traces.slice(0, dataLength);

        for(var i = 0; i < traceIndices.length; i++) {
            var traceIdx = traceIndices[i];
            var trace = gd._fullData[traceIdx];
            var _module = trace._module;

            // There's nothing to do if this module is not defined:
            if(!_module) continue;

            // Don't register the trace as transitioned if it doesn't know what to do.
            // If it *is* registered, it will receive a callback that it's responsible
            // for calling in order to register the transition as having completed.
            if(_module.animatable) {
                var n = _module.basePlotModule.name;
                if(!transitionedTraces[n]) transitionedTraces[n] = [];
                transitionedTraces[n].push(traceIdx);
            }

            gd.data[traceIndices[i]] = plots.extendTrace(gd.data[traceIndices[i]], data[i]);
        }

        // Follow the same procedure. Clone it so we don't mangle the input, then
        // expand any object paths so we can merge deep into gd.layout:
        var layoutUpdate = Lib.expandObjectPaths(Lib.extendDeepNoArrays({}, layout));

        // Before merging though, we need to modify the incoming layout. We only
        // know how to *transition* layout ranges, so it's imperative that a new
        // range not be sent to the layout before the transition has started. So
        // we must remove the things we can transition:
        var axisAttrRe = /^[xy]axis[0-9]*$/;
        for(var attr in layoutUpdate) {
            if(!axisAttrRe.test(attr)) continue;
            delete layoutUpdate[attr].range;
        }

        plots.extendLayout(gd.layout, layoutUpdate);

        // Supply defaults after applying the incoming properties. Note that any attempt
        // to simplify this step and reduce the amount of work resulted in the reconstruction
        // of essentially the whole supplyDefaults step, so that it seems sensible to just use
        // supplyDefaults even though it's heavier than would otherwise be desired for
        // transitions:

        // first delete calcdata so supplyDefaults knows a calc step is coming
        delete gd.calcdata;

        plots.supplyDefaults(gd);
        plots.doCalcdata(gd);

        var newLayout = Lib.expandObjectPaths(layout);

        if(newLayout) {
            var subplots = gd._fullLayout._plots;

            for(var k in subplots) {
                var plotinfo = subplots[k];
                var xa = plotinfo.xaxis;
                var ya = plotinfo.yaxis;
                var xr0 = xa.range.slice();
                var yr0 = ya.range.slice();

                var xr1;
                if(Array.isArray(newLayout[xa._name + '.range'])) {
                    xr1 = newLayout[xa._name + '.range'].slice();
                } else if(Array.isArray((newLayout[xa._name] || {}).range)) {
                    xr1 = newLayout[xa._name].range.slice();
                }

                var yr1;
                if(Array.isArray(newLayout[ya._name + '.range'])) {
                    yr1 = newLayout[ya._name + '.range'].slice();
                } else if(Array.isArray((newLayout[ya._name] || {}).range)) {
                    yr1 = newLayout[ya._name].range.slice();
                }

                var editX;
                if(xr0 && xr1 && (xr0[0] !== xr1[0] || xr0[1] !== xr1[1])) {
                    editX = {xr0: xr0, xr1: xr1};
                }

                var editY;
                if(yr0 && yr1 && (yr0[0] !== yr1[0] || yr0[1] !== yr1[1])) {
                    editY = {yr0: yr0, yr1: yr1};
                }

                if(editX || editY) {
                    axEdits.push(Lib.extendFlat({plotinfo: plotinfo}, editX, editY));
                }
            }
        }

        return Promise.resolve();
    };

    opts.runFn = function(makeCallback) {
        var traceTransitionOpts;
        var basePlotModules = gd._fullLayout._basePlotModules;
        var hasAxisTransition = axEdits.length;
        var i;

        if(layout) {
            for(i = 0; i < basePlotModules.length; i++) {
                if(basePlotModules[i].transitionAxes) {
                    basePlotModules[i].transitionAxes(gd, axEdits, transitionOpts, makeCallback);
                }
            }
        }

        // Here handle the exception that we refuse to animate scales and axes at the same
        // time. In other words, if there's an axis transition, then set the data transition
        // to instantaneous.
        if(hasAxisTransition) {
            traceTransitionOpts = Lib.extendFlat({}, transitionOpts);
            traceTransitionOpts.duration = 0;
            // This means do not transition cartesian traces,
            // this happens on layout-only (e.g. axis range) animations
            delete transitionedTraces.cartesian;
        } else {
            traceTransitionOpts = transitionOpts;
        }

        // Note that we pass a callback to *create* the callback that must be invoked on completion.
        // This is since not all traces know about transitions, so it greatly simplifies matters if
        // the trace is responsible for creating a callback, if needed, and then executing it when
        // the time is right.
        for(var n in transitionedTraces) {
            var traceIndices = transitionedTraces[n];
            var _module = gd._fullData[traceIndices[0]]._module;
            _module.basePlotModule.plot(gd, traceIndices, traceTransitionOpts, makeCallback);
        }
    };

    return _transition(gd, transitionOpts, opts);
};

/**
 * Transition to a set of new data and layout properties from Plotly.react
 *
 * @param {DOM element} gd
 * @param {object} restyleFlags
 * - anim {'all'|'some'}
 * @param {object} relayoutFlags
 * - anim {'all'|'some'}
 * @param {object} oldFullLayout : old (pre Plotly.react) fullLayout
 */
plots.transitionFromReact = function(gd, restyleFlags, relayoutFlags, oldFullLayout) {
    var fullLayout = gd._fullLayout;
    var transitionOpts = fullLayout.transition;
    var opts = {};
    var axEdits = [];

    opts.prepareFn = function() {
        var subplots = fullLayout._plots;

        // no need to redraw at end of transition,
        // if all changes are animatable
        opts.redraw = false;
        if(restyleFlags.anim === 'some') opts.redraw = true;
        if(relayoutFlags.anim === 'some') opts.redraw = true;

        for(var k in subplots) {
            var plotinfo = subplots[k];
            var xa = plotinfo.xaxis;
            var ya = plotinfo.yaxis;
            var xr0 = oldFullLayout[xa._name].range.slice();
            var yr0 = oldFullLayout[ya._name].range.slice();
            var xr1 = xa.range.slice();
            var yr1 = ya.range.slice();

            xa.setScale();
            ya.setScale();

            var editX;
            if(xr0[0] !== xr1[0] || xr0[1] !== xr1[1]) {
                editX = {xr0: xr0, xr1: xr1};
            }

            var editY;
            if(yr0[0] !== yr1[0] || yr0[1] !== yr1[1]) {
                editY = {yr0: yr0, yr1: yr1};
            }

            if(editX || editY) {
                axEdits.push(Lib.extendFlat({plotinfo: plotinfo}, editX, editY));
            }
        }

        return Promise.resolve();
    };

    opts.runFn = function(makeCallback) {
        var fullData = gd._fullData;
        var fullLayout = gd._fullLayout;
        var basePlotModules = fullLayout._basePlotModules;

        var axisTransitionOpts;
        var traceTransitionOpts;
        var transitionedTraces;

        var allTraceIndices = [];
        for(var i = 0; i < fullData.length; i++) {
            allTraceIndices.push(i);
        }

        function transitionAxes() {
            for(var j = 0; j < basePlotModules.length; j++) {
                if(basePlotModules[j].transitionAxes) {
                    basePlotModules[j].transitionAxes(gd, axEdits, axisTransitionOpts, makeCallback);
                }
            }
        }

        function transitionTraces() {
            for(var j = 0; j < basePlotModules.length; j++) {
                basePlotModules[j].plot(gd, transitionedTraces, traceTransitionOpts, makeCallback);
            }
        }

        if(axEdits.length && restyleFlags.anim) {
            if(transitionOpts.ordering === 'traces first') {
                axisTransitionOpts = Lib.extendFlat({}, transitionOpts, {duration: 0});
                transitionedTraces = allTraceIndices;
                traceTransitionOpts = transitionOpts;
                transitionTraces();
                setTimeout(transitionAxes, transitionOpts.duration);
            } else {
                axisTransitionOpts = transitionOpts;
                transitionedTraces = null;
                traceTransitionOpts = Lib.extendFlat({}, transitionOpts, {duration: 0});
                transitionAxes();
                transitionTraces();
            }
        } else if(axEdits.length) {
            axisTransitionOpts = transitionOpts;
            transitionAxes();
        } else if(restyleFlags.anim) {
            transitionedTraces = allTraceIndices;
            traceTransitionOpts = transitionOpts;
            transitionTraces();
        }
    };

    return _transition(gd, transitionOpts, opts);
};

/**
 * trace/layout transition wrapper that works
 * for transitions initiated by Plotly.animate and Plotly.react.
 *
 * @param {DOM element} gd
 * @param {object} transitionOpts
 * @param {object} opts
 * - redraw {boolean}
 * - prepareFn {function} *should return a Promise*
 * - runFn {function} ran inside executeTransitions
 */
function _transition(gd, transitionOpts, opts) {
    var aborted = false;

    function executeCallbacks(list) {
        var p = Promise.resolve();
        if(!list) return p;
        while(list.length) {
            p = p.then((list.shift()));
        }
        return p;
    }

    function flushCallbacks(list) {
        if(!list) return;
        while(list.length) {
            list.shift();
        }
    }

    function executeTransitions() {
        gd.emit('plotly_transitioning', []);

        return new Promise(function(resolve) {
            // This flag is used to disabled things like autorange:
            gd._transitioning = true;

            // When instantaneous updates are coming through quickly, it's too much to simply disable
            // all interaction, so store this flag so we can disambiguate whether mouse interactions
            // should be fully disabled or not:
            if(transitionOpts.duration > 0) {
                gd._transitioningWithDuration = true;
            }

            // If another transition is triggered, this callback will be executed simply because it's
            // in the interruptCallbacks queue. If this transition completes, it will instead flush
            // that queue and forget about this callback.
            gd._transitionData._interruptCallbacks.push(function() {
                aborted = true;
            });

            if(opts.redraw) {
                gd._transitionData._interruptCallbacks.push(function() {
                    return Registry.call('redraw', gd);
                });
            }

            // Emit this and make sure it happens last:
            gd._transitionData._interruptCallbacks.push(function() {
                gd.emit('plotly_transitioninterrupted', []);
            });

            // Construct callbacks that are executed on transition end. This ensures the d3 transitions
            // are *complete* before anything else is done.
            var numCallbacks = 0;
            var numCompleted = 0;
            function makeCallback() {
                numCallbacks++;
                return function() {
                    numCompleted++;
                    // When all are complete, perform a redraw:
                    if(!aborted && numCompleted === numCallbacks) {
                        completeTransition(resolve);
                    }
                };
            }

            opts.runFn(makeCallback);

            // If nothing else creates a callback, then this will trigger the completion in the next tick:
            setTimeout(makeCallback());
        });
    }

    function completeTransition(callback) {
        // This a simple workaround for tests which purge the graph before animations
        // have completed. That's not a very common case, so this is the simplest
        // fix.
        if(!gd._transitionData) return;

        flushCallbacks(gd._transitionData._interruptCallbacks);

        return Promise.resolve().then(function() {
            if(opts.redraw) {
                return Registry.call('redraw', gd);
            }
        }).then(function() {
            // Set transitioning false again once the redraw has occurred. This is used, for example,
            // to prevent the trailing redraw from autoranging:
            gd._transitioning = false;
            gd._transitioningWithDuration = false;

            gd.emit('plotly_transitioned', []);
        }).then(callback);
    }

    function interruptPreviousTransitions() {
        // Fail-safe against purged plot:
        if(!gd._transitionData) return;

        // If a transition is interrupted, set this to false. At the moment, the only thing that would
        // interrupt a transition is another transition, so that it will momentarily be set to true
        // again, but this determines whether autorange or dragbox work, so it's for the sake of
        // cleanliness:
        gd._transitioning = false;

        return executeCallbacks(gd._transitionData._interruptCallbacks);
    }

    var seq = [
        plots.previousPromises,
        interruptPreviousTransitions,
        opts.prepareFn,
        plots.rehover,
        executeTransitions
    ];

    var transitionStarting = Lib.syncOrAsync(seq, gd);

    if(!transitionStarting || !transitionStarting.then) {
        transitionStarting = Promise.resolve();
    }

    return transitionStarting.then(function() { return gd; });
}

plots.doCalcdata = function(gd, traces) {
    var axList = axisIDs.list(gd);
    var fullData = gd._fullData;
    var fullLayout = gd._fullLayout;

    var trace, _module, i, j;

    // XXX: Is this correct? Needs a closer look so that *some* traces can be recomputed without
    // *all* needing doCalcdata:
    var calcdata = new Array(fullData.length);
    var oldCalcdata = (gd.calcdata || []).slice(0);
    gd.calcdata = calcdata;

    // extra helper variables

    // how many box/violins plots do we have (in case they're grouped)
    fullLayout._numBoxes = 0;
    fullLayout._numViolins = 0;

    // initialize violin per-scale-group stats container
    fullLayout._violinScaleGroupStats = {};

    // for calculating avg luminosity of heatmaps
    gd._hmpixcount = 0;
    gd._hmlumcount = 0;

    // for sharing colors across pies / sunbursts / funnelarea (and for legend)
    fullLayout._piecolormap = {};
    fullLayout._sunburstcolormap = {};
    fullLayout._funnelareacolormap = {};

    // If traces were specified and this trace was not included,
    // then transfer it over from the old calcdata:
    for(i = 0; i < fullData.length; i++) {
        if(Array.isArray(traces) && traces.indexOf(i) === -1) {
            calcdata[i] = oldCalcdata[i];
            continue;
        }
    }

    for(i = 0; i < fullData.length; i++) {
        trace = fullData[i];

        trace._arrayAttrs = PlotSchema.findArrayAttributes(trace);

        // keep track of trace extremes (for autorange) in here
        trace._extremes = {};
    }

    // add polar axes to axis list
    var polarIds = fullLayout._subplots.polar || [];
    for(i = 0; i < polarIds.length; i++) {
        axList.push(
            fullLayout[polarIds[i]].radialaxis,
            fullLayout[polarIds[i]].angularaxis
        );
    }

    var hasCalcTransform = false;

    function transformCalci(i) {
        trace = fullData[i];
        _module = trace._module;

        if(trace.visible === true && trace.transforms) {
            // we need one round of trace module calc before
            // the calc transform to 'fill in' the categories list
            // used for example in the data-to-coordinate method
            if(_module && _module.calc) {
                var cdi = _module.calc(gd, trace);

                // must clear scene 'batches', so that 2nd
                // _module.calc call starts from scratch
                if(cdi[0] && cdi[0].t && cdi[0].t._scene) {
                    delete cdi[0].t._scene.dirty;
                }
            }

            for(j = 0; j < trace.transforms.length; j++) {
                var transform = trace.transforms[j];

                _module = transformsRegistry[transform.type];
                if(_module && _module.calcTransform) {
                    trace._hasCalcTransform = true;
                    hasCalcTransform = true;
                    _module.calcTransform(gd, trace, transform);
                }
            }
        }
    }

    function calci(i, isContainer) {
        trace = fullData[i];
        _module = trace._module;

        if(!!_module.isContainer !== isContainer) return;

        var cd = [];

        if(trace.visible === true && trace._length !== 0) {
            // clear existing ref in case it got relinked
            delete trace._indexToPoints;
            // keep ref of index-to-points map object of the *last* enabled transform,
            // this index-to-points map object is required to determine the calcdata indices
            // that correspond to input indices (e.g. from 'selectedpoints')
            var transforms = trace.transforms || [];
            for(j = transforms.length - 1; j >= 0; j--) {
                if(transforms[j].enabled) {
                    trace._indexToPoints = transforms[j]._indexToPoints;
                    break;
                }
            }

            if(_module && _module.calc) {
                cd = _module.calc(gd, trace);
            }
        }

        // Make sure there is a first point.
        //
        // This ensures there is a calcdata item for every trace,
        // even if cartesian logic doesn't handle it (for things like legends).
        if(!Array.isArray(cd) || !cd[0]) {
            cd = [{x: BADNUM, y: BADNUM}];
        }

        // add the trace-wide properties to the first point,
        // per point properties to every point
        // t is the holder for trace-wide properties
        if(!cd[0].t) cd[0].t = {};
        cd[0].trace = trace;

        calcdata[i] = cd;
    }

    setupAxisCategories(axList, fullData);

    // 'transform' loop - must calc container traces first
    // so that if their dependent traces can get transform properly
    for(i = 0; i < fullData.length; i++) calci(i, true);
    for(i = 0; i < fullData.length; i++) transformCalci(i);

    // clear stuff that should recomputed in 'regular' loop
    if(hasCalcTransform) setupAxisCategories(axList, fullData);

    // 'regular' loop - make sure container traces (eg carpet) calc before
    // contained traces (eg contourcarpet)
    for(i = 0; i < fullData.length; i++) calci(i, true);
    for(i = 0; i < fullData.length; i++) calci(i, false);

    doCrossTraceCalc(gd);

    // Sort axis categories per value if specified
    var sorted = sortAxisCategoriesByValue(axList, gd);
    if(sorted.length) {
        // If a sort operation was performed, run calc() again
        for(i = 0; i < sorted.length; i++) calci(sorted[i], true);
        for(i = 0; i < sorted.length; i++) calci(sorted[i], false);
        doCrossTraceCalc(gd);
    }

    Registry.getComponentMethod('fx', 'calc')(gd);
    Registry.getComponentMethod('errorbars', 'calc')(gd);
};

var sortAxisCategoriesByValueRegex = /(total|sum|min|max|mean|median) (ascending|descending)/;

function sortAxisCategoriesByValue(axList, gd) {
    var affectedTraces = [];
    var i, j, k, l, o;

    function zMapCategory(type, ax, value) {
        var axLetter = ax._id.charAt(0);
        if(type === 'histogram2dcontour') {
            var counterAxLetter = ax._counterAxes[0];
            var counterAx = axisIDs.getFromId(gd, counterAxLetter);

            var xCategorical = axLetter === 'x' || (counterAxLetter === 'x' && counterAx.type === 'category');
            var yCategorical = axLetter === 'y' || (counterAxLetter === 'y' && counterAx.type === 'category');

            return function(o, l) {
                if(o === 0 || l === 0) return -1; // Skip first row and column
                if(xCategorical && o === value[l].length - 1) return -1;
                if(yCategorical && l === value.length - 1) return -1;

                return (axLetter === 'y' ? l : o) - 1;
            };
        } else {
            return function(o, l) {
                return axLetter === 'y' ? l : o;
            };
        }
    }

    var aggFn = {
        'min': function(values) {return Lib.aggNums(Math.min, null, values);},
        'max': function(values) {return Lib.aggNums(Math.max, null, values);},
        'sum': function(values) {return Lib.aggNums(function(a, b) { return a + b;}, null, values);},
        'total': function(values) {return Lib.aggNums(function(a, b) { return a + b;}, null, values);},
        'mean': function(values) {return Lib.mean(values);},
        'median': function(values) {return Lib.median(values);}
    };

    for(i = 0; i < axList.length; i++) {
        var ax = axList[i];
        if(ax.type !== 'category') continue;

        // Order by value
        var match = ax.categoryorder.match(sortAxisCategoriesByValueRegex);
        if(match) {
            var aggregator = match[1];
            var order = match[2];

            // Store values associated with each category
            var categoriesValue = [];
            for(j = 0; j < ax._categories.length; j++) {
                categoriesValue.push([ax._categories[j], []]);
            }

            // Collect values across traces
            for(j = 0; j < ax._traceIndices.length; j++) {
                var traceIndex = ax._traceIndices[j];
                var fullTrace = gd._fullData[traceIndex];
                var axLetter = ax._id.charAt(0);

                // Skip over invisible traces
                if(fullTrace.visible !== true) continue;

                var type = fullTrace.type;
                if(Registry.traceIs(fullTrace, 'histogram')) {
                    delete fullTrace._xautoBinFinished;
                    delete fullTrace._yautoBinFinished;
                }

                var cd = gd.calcdata[traceIndex];
                for(k = 0; k < cd.length; k++) {
                    var cdi = cd[k];
                    var cat, catIndex, value;

                    if(type === 'splom') {
                        // If `splom`, collect values across dimensions
                        // Find which dimension the current axis is representing
                        var currentDimensionIndex = fullTrace._axesDim[ax._id];

                        // Apply logic to associated x axis if it's defined
                        if(axLetter === 'y') {
                            var associatedXAxisID = fullTrace._diag[currentDimensionIndex][0];
                            if(associatedXAxisID) ax = gd._fullLayout[axisIDs.id2name(associatedXAxisID)];
                        }

                        var categories = cdi.trace.dimensions[currentDimensionIndex].values;
                        for(l = 0; l < categories.length; l++) {
                            cat = categories[l];
                            catIndex = ax._categoriesMap[cat];

                            // Collect associated values at index `l` over all other dimensions
                            for(o = 0; o < cdi.trace.dimensions.length; o++) {
                                if(o === currentDimensionIndex) continue;
                                var dimension = cdi.trace.dimensions[o];
                                categoriesValue[catIndex][1].push(dimension.values[l]);
                            }
                        }
                    } else if(type === 'scattergl') {
                        // If `scattergl`, collect all values stashed under cdi.t
                        for(l = 0; l < cdi.t.x.length; l++) {
                            if(axLetter === 'x') {
                                cat = cdi.t.x[l];
                                catIndex = cat;
                                value = cdi.t.y[l];
                            }

                            if(axLetter === 'y') {
                                cat = cdi.t.y[l];
                                catIndex = cat;
                                value = cdi.t.x[l];
                            }
                            categoriesValue[catIndex][1].push(value);
                        }
                        // must clear scene 'batches', so that 2nd
                        // _module.calc call starts from scratch
                        if(cdi.t && cdi.t._scene) {
                            delete cdi.t._scene.dirty;
                        }
                    } else if(cdi.hasOwnProperty('z')) {
                        // If 2dMap, collect values in `z`
                        value = cdi.z;
                        var mapping = zMapCategory(fullTrace.type, ax, value);

                        for(l = 0; l < value.length; l++) {
                            for(o = 0; o < value[l].length; o++) {
                                catIndex = mapping(o, l);
                                if(catIndex + 1) categoriesValue[catIndex][1].push(value[l][o]);
                            }
                        }
                    } else {
                        // For all other 2d cartesian traces
                        if(axLetter === 'x') {
                            cat = cdi.p + 1 ? cdi.p : cdi.x;
                            value = cdi.s || cdi.v || cdi.y;
                        } else if(axLetter === 'y') {
                            cat = cdi.p + 1 ? cdi.p : cdi.y;
                            value = cdi.s || cdi.v || cdi.x;
                        }
                        if(!Array.isArray(value)) value = [value];
                        for(l = 0; l < value.length; l++) {
                            categoriesValue[cat][1].push(value[l]);
                        }
                    }
                }
            }

            ax._categoriesValue = categoriesValue;

            var categoriesAggregatedValue = [];
            for(j = 0; j < categoriesValue.length; j++) {
                categoriesAggregatedValue.push([
                    categoriesValue[j][0],
                    aggFn[aggregator](categoriesValue[j][1])
                ]);
            }

            // Sort by aggregated value
            categoriesAggregatedValue.sort(function(a, b) {
                return a[1] - b[1];
            });

            ax._categoriesAggregatedValue = categoriesAggregatedValue;

            // Set new category order
            ax._initialCategories = categoriesAggregatedValue.map(function(c) {
                return c[0];
            });

            // Reverse if descending
            if(order === 'descending') {
                ax._initialCategories.reverse();
            }

            // Sort all matching axes
            affectedTraces = affectedTraces.concat(ax.sortByInitialCategories());
        }
    }
    return affectedTraces;
}

function setupAxisCategories(axList, fullData) {
    for(var i = 0; i < axList.length; i++) {
        var ax = axList[i];
        ax.clearCalc();
        if(ax.type === 'multicategory') {
            ax.setupMultiCategory(fullData);
        }
    }
}

function doCrossTraceCalc(gd) {
    var fullLayout = gd._fullLayout;
    var modules = fullLayout._visibleModules;
    var hash = {};
    var i, j, k;

    // position and range calculations for traces that
    // depend on each other ie bars (stacked or grouped)
    // and boxes (grouped) push each other out of the way

    for(j = 0; j < modules.length; j++) {
        var _module = modules[j];
        var fn = _module.crossTraceCalc;
        if(fn) {
            var spType = _module.basePlotModule.name;
            if(hash[spType]) {
                Lib.pushUnique(hash[spType], fn);
            } else {
                hash[spType] = [fn];
            }
        }
    }

    for(k in hash) {
        var methods = hash[k];
        var subplots = fullLayout._subplots[k];

        if(Array.isArray(subplots)) {
            for(i = 0; i < subplots.length; i++) {
                var sp = subplots[i];
                var spInfo = k === 'cartesian' ?
                    fullLayout._plots[sp] :
                    fullLayout[sp];

                for(j = 0; j < methods.length; j++) {
                    methods[j](gd, spInfo, sp);
                }
            }
        } else {
            for(j = 0; j < methods.length; j++) {
                methods[j](gd);
            }
        }
    }
}

plots.rehover = function(gd) {
    if(gd._fullLayout._rehover) {
        gd._fullLayout._rehover();
    }
};

plots.redrag = function(gd) {
    if(gd._fullLayout._redrag) {
        gd._fullLayout._redrag();
    }
};

plots.generalUpdatePerTraceModule = function(gd, subplot, subplotCalcData, subplotLayout) {
    var traceHashOld = subplot.traceHash;
    var traceHash = {};
    var i;

    // build up moduleName -> calcData hash
    for(i = 0; i < subplotCalcData.length; i++) {
        var calcTraces = subplotCalcData[i];
        var trace = calcTraces[0].trace;

        // skip over visible === false traces
        // as they don't have `_module` ref
        if(trace.visible) {
            traceHash[trace.type] = traceHash[trace.type] || [];
            traceHash[trace.type].push(calcTraces);
        }
    }

    // when a trace gets deleted, make sure that its module's
    // plot method is called so that it is properly
    // removed from the DOM.
    for(var moduleNameOld in traceHashOld) {
        if(!traceHash[moduleNameOld]) {
            var fakeCalcTrace = traceHashOld[moduleNameOld][0];
            var fakeTrace = fakeCalcTrace[0].trace;

            fakeTrace.visible = false;
            traceHash[moduleNameOld] = [fakeCalcTrace];
        }
    }

    // call module plot method
    for(var moduleName in traceHash) {
        var moduleCalcData = traceHash[moduleName];
        var _module = moduleCalcData[0][0].trace._module;

        _module.plot(gd, subplot, Lib.filterVisible(moduleCalcData), subplotLayout);
    }

    // update moduleName -> calcData hash
    subplot.traceHash = traceHash;
};
