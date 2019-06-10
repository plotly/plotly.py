/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Registry = require('../../registry');
var Plots = require('../../plots/plots');
var axisIds = require('../../plots/cartesian/axis_ids');
var Lib = require('../../lib');
var Icons = require('../../../build/ploticon');

var _ = Lib._;

var modeBarButtons = module.exports = {};

/**
 * ModeBar buttons configuration
 *
 * @param {string} name
 *      name / id of the buttons (for tracking)
 * @param {string} title
 *      text that appears while hovering over the button,
 *      enter null, false or '' for no hover text
 * @param {string} icon
 *      svg icon object associated with the button
 *      can be linked to Plotly.Icons to use the default plotly icons
 * @param {string} [gravity]
 *      icon positioning
 * @param {function} click
 *      click handler associated with the button, a function of
 *      'gd' (the main graph object) and
 *      'ev' (the event object)
 * @param {string} [attr]
 *      attribute associated with button,
 *      use this with 'val' to keep track of the state
 * @param {*} [val]
 *      initial 'attr' value, can be a function of gd
 * @param {boolean} [toggle]
 *      is the button a toggle button?
 */
modeBarButtons.toImage = {
    name: 'toImage',
    title: function(gd) {
        var opts = gd._context.toImageButtonOptions || {};
        var format = opts.format || 'png';
        return format === 'png' ?
            _(gd, 'Download plot as a png') : // legacy text
            _(gd, 'Download plot'); // generic non-PNG text
    },
    icon: Icons.camera,
    click: function(gd) {
        var toImageButtonOptions = gd._context.toImageButtonOptions;
        var opts = {format: toImageButtonOptions.format || 'png'};

        Lib.notifier(_(gd, 'Taking snapshot - this may take a few seconds'), 'long');

        if(opts.format !== 'svg' && Lib.isIE()) {
            Lib.notifier(_(gd, 'IE only supports svg.  Changing format to svg.'), 'long');
            opts.format = 'svg';
        }

        ['filename', 'width', 'height', 'scale'].forEach(function(key) {
            if(key in toImageButtonOptions) {
                opts[key] = toImageButtonOptions[key];
            }
        });

        Registry.call('downloadImage', gd, opts)
          .then(function(filename) {
              Lib.notifier(_(gd, 'Snapshot succeeded') + ' - ' + filename, 'long');
          })
          .catch(function() {
              Lib.notifier(_(gd, 'Sorry, there was a problem downloading your snapshot!'), 'long');
          });
    }
};

modeBarButtons.sendDataToCloud = {
    name: 'sendDataToCloud',
    title: function(gd) { return _(gd, 'Edit in Chart Studio'); },
    icon: Icons.disk,
    click: function(gd) {
        Plots.sendDataToCloud(gd);
    }
};

modeBarButtons.zoom2d = {
    name: 'zoom2d',
    title: function(gd) { return _(gd, 'Zoom'); },
    attr: 'dragmode',
    val: 'zoom',
    icon: Icons.zoombox,
    click: handleCartesian
};

modeBarButtons.pan2d = {
    name: 'pan2d',
    title: function(gd) { return _(gd, 'Pan'); },
    attr: 'dragmode',
    val: 'pan',
    icon: Icons.pan,
    click: handleCartesian
};

modeBarButtons.select2d = {
    name: 'select2d',
    title: function(gd) { return _(gd, 'Box Select'); },
    attr: 'dragmode',
    val: 'select',
    icon: Icons.selectbox,
    click: handleCartesian
};

modeBarButtons.lasso2d = {
    name: 'lasso2d',
    title: function(gd) { return _(gd, 'Lasso Select'); },
    attr: 'dragmode',
    val: 'lasso',
    icon: Icons.lasso,
    click: handleCartesian
};

modeBarButtons.zoomIn2d = {
    name: 'zoomIn2d',
    title: function(gd) { return _(gd, 'Zoom in'); },
    attr: 'zoom',
    val: 'in',
    icon: Icons.zoom_plus,
    click: handleCartesian
};

modeBarButtons.zoomOut2d = {
    name: 'zoomOut2d',
    title: function(gd) { return _(gd, 'Zoom out'); },
    attr: 'zoom',
    val: 'out',
    icon: Icons.zoom_minus,
    click: handleCartesian
};

modeBarButtons.autoScale2d = {
    name: 'autoScale2d',
    title: function(gd) { return _(gd, 'Autoscale'); },
    attr: 'zoom',
    val: 'auto',
    icon: Icons.autoscale,
    click: handleCartesian
};

modeBarButtons.resetScale2d = {
    name: 'resetScale2d',
    title: function(gd) { return _(gd, 'Reset axes'); },
    attr: 'zoom',
    val: 'reset',
    icon: Icons.home,
    click: handleCartesian
};

modeBarButtons.hoverClosestCartesian = {
    name: 'hoverClosestCartesian',
    title: function(gd) { return _(gd, 'Show closest data on hover'); },
    attr: 'hovermode',
    val: 'closest',
    icon: Icons.tooltip_basic,
    gravity: 'ne',
    click: handleCartesian
};

modeBarButtons.hoverCompareCartesian = {
    name: 'hoverCompareCartesian',
    title: function(gd) { return _(gd, 'Compare data on hover'); },
    attr: 'hovermode',
    val: function(gd) {
        return gd._fullLayout._isHoriz ? 'y' : 'x';
    },
    icon: Icons.tooltip_compare,
    gravity: 'ne',
    click: handleCartesian
};

function handleCartesian(gd, ev) {
    var button = ev.currentTarget;
    var astr = button.getAttribute('data-attr');
    var val = button.getAttribute('data-val') || true;
    var fullLayout = gd._fullLayout;
    var aobj = {};
    var axList = axisIds.list(gd, null, true);
    var allSpikesEnabled = 'on';

    var ax, i;

    if(astr === 'zoom') {
        var mag = (val === 'in') ? 0.5 : 2;
        var r0 = (1 + mag) / 2;
        var r1 = (1 - mag) / 2;
        var axName;

        for(i = 0; i < axList.length; i++) {
            ax = axList[i];

            if(!ax.fixedrange) {
                axName = ax._name;
                if(val === 'auto') aobj[axName + '.autorange'] = true;
                else if(val === 'reset') {
                    if(ax._rangeInitial === undefined) {
                        aobj[axName + '.autorange'] = true;
                    } else {
                        var rangeInitial = ax._rangeInitial.slice();
                        aobj[axName + '.range[0]'] = rangeInitial[0];
                        aobj[axName + '.range[1]'] = rangeInitial[1];
                    }
                    if(ax._showSpikeInitial !== undefined) {
                        aobj[axName + '.showspikes'] = ax._showSpikeInitial;
                        if(allSpikesEnabled === 'on' && !ax._showSpikeInitial) {
                            allSpikesEnabled = 'off';
                        }
                    }
                } else {
                    var rangeNow = [
                        ax.r2l(ax.range[0]),
                        ax.r2l(ax.range[1]),
                    ];

                    var rangeNew = [
                        r0 * rangeNow[0] + r1 * rangeNow[1],
                        r0 * rangeNow[1] + r1 * rangeNow[0]
                    ];

                    aobj[axName + '.range[0]'] = ax.l2r(rangeNew[0]);
                    aobj[axName + '.range[1]'] = ax.l2r(rangeNew[1]);
                }
            }
        }
        fullLayout._cartesianSpikesEnabled = allSpikesEnabled;
    } else {
        // if ALL traces have orientation 'h', 'hovermode': 'x' otherwise: 'y'
        if(astr === 'hovermode' && (val === 'x' || val === 'y')) {
            val = fullLayout._isHoriz ? 'y' : 'x';
            button.setAttribute('data-val', val);
        } else if(astr === 'hovermode' && val === 'closest') {
            for(i = 0; i < axList.length; i++) {
                ax = axList[i];
                if(allSpikesEnabled === 'on' && !ax.showspikes) {
                    allSpikesEnabled = 'off';
                }
            }
            fullLayout._cartesianSpikesEnabled = allSpikesEnabled;
        }

        aobj[astr] = val;
    }

    Registry.call('_guiRelayout', gd, aobj);
}

modeBarButtons.zoom3d = {
    name: 'zoom3d',
    title: function(gd) { return _(gd, 'Zoom'); },
    attr: 'scene.dragmode',
    val: 'zoom',
    icon: Icons.zoombox,
    click: handleDrag3d
};

modeBarButtons.pan3d = {
    name: 'pan3d',
    title: function(gd) { return _(gd, 'Pan'); },
    attr: 'scene.dragmode',
    val: 'pan',
    icon: Icons.pan,
    click: handleDrag3d
};

modeBarButtons.orbitRotation = {
    name: 'orbitRotation',
    title: function(gd) { return _(gd, 'Orbital rotation'); },
    attr: 'scene.dragmode',
    val: 'orbit',
    icon: Icons['3d_rotate'],
    click: handleDrag3d
};

modeBarButtons.tableRotation = {
    name: 'tableRotation',
    title: function(gd) { return _(gd, 'Turntable rotation'); },
    attr: 'scene.dragmode',
    val: 'turntable',
    icon: Icons['z-axis'],
    click: handleDrag3d
};

function handleDrag3d(gd, ev) {
    var button = ev.currentTarget;
    var attr = button.getAttribute('data-attr');
    var val = button.getAttribute('data-val') || true;
    var sceneIds = gd._fullLayout._subplots.gl3d;
    var layoutUpdate = {};

    var parts = attr.split('.');

    for(var i = 0; i < sceneIds.length; i++) {
        layoutUpdate[sceneIds[i] + '.' + parts[1]] = val;
    }

    // for multi-type subplots
    var val2d = (val === 'pan') ? val : 'zoom';
    layoutUpdate.dragmode = val2d;

    Registry.call('_guiRelayout', gd, layoutUpdate);
}

modeBarButtons.resetCameraDefault3d = {
    name: 'resetCameraDefault3d',
    title: function(gd) { return _(gd, 'Reset camera to default'); },
    attr: 'resetDefault',
    icon: Icons.home,
    click: handleCamera3d
};

modeBarButtons.resetCameraLastSave3d = {
    name: 'resetCameraLastSave3d',
    title: function(gd) { return _(gd, 'Reset camera to last save'); },
    attr: 'resetLastSave',
    icon: Icons.movie,
    click: handleCamera3d
};

function handleCamera3d(gd, ev) {
    var button = ev.currentTarget;
    var attr = button.getAttribute('data-attr');
    var fullLayout = gd._fullLayout;
    var sceneIds = fullLayout._subplots.gl3d;
    var aobj = {};

    for(var i = 0; i < sceneIds.length; i++) {
        var sceneId = sceneIds[i];
        var key = sceneId + '.camera';
        var scene = fullLayout[sceneId]._scene;

        if(attr === 'resetLastSave') {
            aobj[key + '.up'] = scene.viewInitial.up;
            aobj[key + '.eye'] = scene.viewInitial.eye;
            aobj[key + '.center'] = scene.viewInitial.center;
        } else if(attr === 'resetDefault') {
            aobj[key + '.up'] = null;
            aobj[key + '.eye'] = null;
            aobj[key + '.center'] = null;
        }
    }

    Registry.call('_guiRelayout', gd, aobj);
}

modeBarButtons.hoverClosest3d = {
    name: 'hoverClosest3d',
    title: function(gd) { return _(gd, 'Toggle show closest data on hover'); },
    attr: 'hovermode',
    val: null,
    toggle: true,
    icon: Icons.tooltip_basic,
    gravity: 'ne',
    click: handleHover3d
};

function getNextHover3d(gd, ev) {
    var button = ev.currentTarget;
    var val = button._previousVal;
    var fullLayout = gd._fullLayout;
    var sceneIds = fullLayout._subplots.gl3d;

    var axes = ['xaxis', 'yaxis', 'zaxis'];

    // initialize 'current spike' object to be stored in the DOM
    var currentSpikes = {};
    var layoutUpdate = {};

    if(val) {
        layoutUpdate = val;
        button._previousVal = null;
    } else {
        for(var i = 0; i < sceneIds.length; i++) {
            var sceneId = sceneIds[i];
            var sceneLayout = fullLayout[sceneId];

            var hovermodeAStr = sceneId + '.hovermode';
            currentSpikes[hovermodeAStr] = sceneLayout.hovermode;
            layoutUpdate[hovermodeAStr] = false;

            // copy all the current spike attrs
            for(var j = 0; j < 3; j++) {
                var axis = axes[j];
                var spikeAStr = sceneId + '.' + axis + '.showspikes';
                layoutUpdate[spikeAStr] = false;
                currentSpikes[spikeAStr] = sceneLayout[axis].showspikes;
            }
        }

        button._previousVal = currentSpikes;
    }
    return layoutUpdate;
}

function handleHover3d(gd, ev) {
    var layoutUpdate = getNextHover3d(gd, ev);
    Registry.call('_guiRelayout', gd, layoutUpdate);
}

modeBarButtons.zoomInGeo = {
    name: 'zoomInGeo',
    title: function(gd) { return _(gd, 'Zoom in'); },
    attr: 'zoom',
    val: 'in',
    icon: Icons.zoom_plus,
    click: handleGeo
};

modeBarButtons.zoomOutGeo = {
    name: 'zoomOutGeo',
    title: function(gd) { return _(gd, 'Zoom out'); },
    attr: 'zoom',
    val: 'out',
    icon: Icons.zoom_minus,
    click: handleGeo
};

modeBarButtons.resetGeo = {
    name: 'resetGeo',
    title: function(gd) { return _(gd, 'Reset'); },
    attr: 'reset',
    val: null,
    icon: Icons.autoscale,
    click: handleGeo
};

modeBarButtons.hoverClosestGeo = {
    name: 'hoverClosestGeo',
    title: function(gd) { return _(gd, 'Toggle show closest data on hover'); },
    attr: 'hovermode',
    val: null,
    toggle: true,
    icon: Icons.tooltip_basic,
    gravity: 'ne',
    click: toggleHover
};

function handleGeo(gd, ev) {
    var button = ev.currentTarget;
    var attr = button.getAttribute('data-attr');
    var val = button.getAttribute('data-val') || true;
    var fullLayout = gd._fullLayout;
    var geoIds = fullLayout._subplots.geo;

    for(var i = 0; i < geoIds.length; i++) {
        var id = geoIds[i];
        var geoLayout = fullLayout[id];

        if(attr === 'zoom') {
            var scale = geoLayout.projection.scale;
            var newScale = (val === 'in') ? 2 * scale : 0.5 * scale;

            Registry.call('_guiRelayout', gd, id + '.projection.scale', newScale);
        } else if(attr === 'reset') {
            resetView(gd, 'geo');
        }
    }
}

modeBarButtons.hoverClosestGl2d = {
    name: 'hoverClosestGl2d',
    title: function(gd) { return _(gd, 'Toggle show closest data on hover'); },
    attr: 'hovermode',
    val: null,
    toggle: true,
    icon: Icons.tooltip_basic,
    gravity: 'ne',
    click: toggleHover
};

modeBarButtons.hoverClosestPie = {
    name: 'hoverClosestPie',
    title: function(gd) { return _(gd, 'Toggle show closest data on hover'); },
    attr: 'hovermode',
    val: 'closest',
    icon: Icons.tooltip_basic,
    gravity: 'ne',
    click: toggleHover
};

function getNextHover(gd) {
    var fullLayout = gd._fullLayout;

    if(fullLayout.hovermode) return false;

    if(fullLayout._has('cartesian')) {
        return fullLayout._isHoriz ? 'y' : 'x';
    }
    return 'closest';
}

function toggleHover(gd) {
    var newHover = getNextHover(gd);
    Registry.call('_guiRelayout', gd, 'hovermode', newHover);
}

modeBarButtons.resetViewSankey = {
    name: 'resetSankeyGroup',
    title: function(gd) { return _(gd, 'Reset view'); },
    icon: Icons.home,
    click: function(gd) {
        var aObj = {
            'node.groups': [],
            'node.x': [],
            'node.y': []
        };
        for(var i = 0; i < gd._fullData.length; i++) {
            var viewInitial = gd._fullData[i]._viewInitial;
            aObj['node.groups'].push(viewInitial.node.groups.slice());
            aObj['node.x'].push(viewInitial.node.x.slice());
            aObj['node.y'].push(viewInitial.node.y.slice());
        }
        Registry.call('restyle', gd, aObj);
    }
};

// buttons when more then one plot types are present

modeBarButtons.toggleHover = {
    name: 'toggleHover',
    title: function(gd) { return _(gd, 'Toggle show closest data on hover'); },
    attr: 'hovermode',
    val: null,
    toggle: true,
    icon: Icons.tooltip_basic,
    gravity: 'ne',
    click: function(gd, ev) {
        var layoutUpdate = getNextHover3d(gd, ev);
        layoutUpdate.hovermode = getNextHover(gd);

        Registry.call('_guiRelayout', gd, layoutUpdate);
    }
};

modeBarButtons.resetViews = {
    name: 'resetViews',
    title: function(gd) { return _(gd, 'Reset views'); },
    icon: Icons.home,
    click: function(gd, ev) {
        var button = ev.currentTarget;

        button.setAttribute('data-attr', 'zoom');
        button.setAttribute('data-val', 'reset');
        handleCartesian(gd, ev);

        button.setAttribute('data-attr', 'resetLastSave');
        handleCamera3d(gd, ev);

        resetView(gd, 'geo');
        resetView(gd, 'mapbox');
    }
};

modeBarButtons.toggleSpikelines = {
    name: 'toggleSpikelines',
    title: function(gd) { return _(gd, 'Toggle Spike Lines'); },
    icon: Icons.spikeline,
    attr: '_cartesianSpikesEnabled',
    val: 'on',
    click: function(gd) {
        var fullLayout = gd._fullLayout;

        fullLayout._cartesianSpikesEnabled = fullLayout._cartesianSpikesEnabled === 'on' ? 'off' : 'on';

        var aobj = setSpikelineVisibility(gd);

        Registry.call('_guiRelayout', gd, aobj);
    }
};

function setSpikelineVisibility(gd) {
    var fullLayout = gd._fullLayout;
    var axList = axisIds.list(gd, null, true);
    var aobj = {};

    var ax, axName;

    for(var i = 0; i < axList.length; i++) {
        ax = axList[i];
        axName = ax._name;
        aobj[axName + '.showspikes'] = fullLayout._cartesianSpikesEnabled === 'on' ? true : ax._showSpikeInitial;
    }

    return aobj;
}

modeBarButtons.resetViewMapbox = {
    name: 'resetViewMapbox',
    title: function(gd) { return _(gd, 'Reset view'); },
    attr: 'reset',
    icon: Icons.home,
    click: function(gd) {
        resetView(gd, 'mapbox');
    }
};

function resetView(gd, subplotType) {
    var fullLayout = gd._fullLayout;
    var subplotIds = fullLayout._subplots[subplotType];
    var aObj = {};

    for(var i = 0; i < subplotIds.length; i++) {
        var id = subplotIds[i];
        var subplotObj = fullLayout[id]._subplot;
        var viewInitial = subplotObj.viewInitial;
        var viewKeys = Object.keys(viewInitial);

        for(var j = 0; j < viewKeys.length; j++) {
            var key = viewKeys[j];
            aObj[id + '.' + key] = viewInitial[key];
        }
    }

    Registry.call('_guiRelayout', gd, aObj);
}
