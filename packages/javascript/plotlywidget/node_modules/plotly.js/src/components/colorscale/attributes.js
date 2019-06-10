/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var colorbarAttrs = require('../colorbar/attributes');
var counterRegex = require('../../lib/regex').counter;

var palettes = require('./scales.js').scales;
var paletteStr = Object.keys(palettes);

function code(s) {
    return '`' + s + '`';
}

/**
 * Make colorscale attribute declarations for
 *
 * - colorscale,
 * - (c|z)auto, (c|z)min, (c|z)max,
 * - autocolorscale, reversescale,
 * - showscale (optionally)
 * - color (optionally)
 *
 * @param {string} context (dflt: '', i.e. from trace root):
 *     the container this is in ('', *marker*, *marker.line* etc)
 *
 * @param {object} opts:
 *   - cLetter {string} (dflt: 'c'):
 *     leading letter for 'min', 'max and 'auto' attribute (either 'z' or 'c')
 *
 *   - colorAttr {string} (dflt: 'z' if `cLetter: 'z'`, 'color' if `cLetter: 'c'`):
 *     (for descriptions) sets the name of the color attribute that maps to the colorscale.
 *
 *     N.B. if `colorAttr: 'color'`, we include the `color` declaration here.
 *
 *   - onlyIfNumerical {string} (dflt: false' if `cLetter: 'z'`, true if `cLetter: 'c'`):
 *     (for descriptions) set to true if colorscale attribute only
 *
 *   - colorscaleDflt {string}:
 *     overrides the colorscale dflt
 *
 *   - autoColorDflt {boolean} (dflt true):
 *     normally autocolorscale.dflt is `true`, but pass `false` to override
 *
 *   - noScale {boolean} (dflt: true if `context: 'marker.line'`, false otherwise):
 *     set to `false` to not include showscale attribute (e.g. for 'marker.line')
 *
 *   - showScaleDflt {boolean} (dflt: true if `cLetter: 'z'`, false otherwise)
 *
 *   - editTypeOverride {boolean} (dflt: ''):
 *     most of these attributes already require a recalc, but the ones that do not
 *     have editType *style* or *plot* unless you override (presumably with *calc*)
 *
 *   - anim {boolean) (dflt: undefined): is 'color' animatable?
 *
 * @return {object}
 */
module.exports = function colorScaleAttrs(context, opts) {
    context = context || '';
    opts = opts || {};

    var cLetter = opts.cLetter || 'c';
    var onlyIfNumerical = ('onlyIfNumerical' in opts) ? opts.onlyIfNumerical : Boolean(context);
    var noScale = ('noScale' in opts) ? opts.noScale : context === 'marker.line';
    var showScaleDflt = ('showScaleDflt' in opts) ? opts.showScaleDflt : cLetter === 'z';
    var colorscaleDflt = typeof opts.colorscaleDflt === 'string' ? palettes[opts.colorscaleDflt] : null;
    var editTypeOverride = opts.editTypeOverride || '';
    var contextHead = context ? (context + '.') : '';

    var colorAttr, colorAttrFull;

    if('colorAttr' in opts) {
        colorAttr = opts.colorAttr;
        colorAttrFull = opts.colorAttr;
    } else {
        colorAttr = {z: 'z', c: 'color'}[cLetter];
        colorAttrFull = 'in ' + code(contextHead + colorAttr);
    }

    var effectDesc = onlyIfNumerical ?
        ' Has an effect only if ' + colorAttrFull + 'is set to a numerical array.' :
        '';

    var auto = cLetter + 'auto';
    var min = cLetter + 'min';
    var max = cLetter + 'max';
    var mid = cLetter + 'mid';
    var autoFull = code(contextHead + auto);
    var minFull = code(contextHead + min);
    var maxFull = code(contextHead + max);
    var minmaxFull = minFull + ' and ' + maxFull;
    var autoImpliedEdits = {};
    autoImpliedEdits[min] = autoImpliedEdits[max] = undefined;
    var minmaxImpliedEdits = {};
    minmaxImpliedEdits[auto] = false;

    var attrs = {};

    if(colorAttr === 'color') {
        attrs.color = {
            valType: 'color',
            arrayOk: true,
            role: 'style',
            editType: editTypeOverride || 'style',
            description: [
                'Sets the', context, 'color.',
                ' It accepts either a specific color',
                ' or an array of numbers that are mapped to the colorscale',
                ' relative to the max and min values of the array or relative to',
                ' ' + minmaxFull + ' if set.'
            ].join('')
        };

        if(opts.anim) {
            attrs.color.anim = true;
        }
    }

    attrs[auto] = {
        valType: 'boolean',
        role: 'info',
        dflt: true,
        editType: 'calc',
        impliedEdits: autoImpliedEdits,
        description: [
            'Determines whether or not the color domain is computed',
            ' with respect to the input data (here ' + colorAttrFull + ') or the bounds set in',
            ' ', minmaxFull,
            ' ', effectDesc,
            ' Defaults to `false` when ', minmaxFull, ' are set by the user.'
        ].join('')
    };

    attrs[min] = {
        valType: 'number',
        role: 'info',
        dflt: null,
        editType: editTypeOverride || 'plot',
        impliedEdits: minmaxImpliedEdits,
        description: [
            'Sets the lower bound of the color domain.',
            effectDesc,
            ' Value should have the same units as ', colorAttrFull,
            ' and if set, ', maxFull, ' must be set as well.'
        ].join('')
    };

    attrs[max] = {
        valType: 'number',
        role: 'info',
        dflt: null,
        editType: editTypeOverride || 'plot',
        impliedEdits: minmaxImpliedEdits,
        description: [
            'Sets the upper bound of the color domain.',
            effectDesc,
            ' Value should have the same units as ', colorAttrFull,
            ' and if set, ', minFull, ' must be set as well.'
        ].join('')
    };

    attrs[mid] = {
        valType: 'number',
        role: 'info',
        dflt: null,
        editType: 'calc',
        impliedEdits: autoImpliedEdits,
        description: [
            'Sets the mid-point of the color domain by scaling ', minFull,
            ' and/or ', maxFull, ' to be equidistant to this point.',
            effectDesc,
            ' Value should have the same units as ', colorAttrFull, '. ',
            'Has no effect when ', autoFull, ' is `false`.'
        ].join('')
    };

    attrs.colorscale = {
        valType: 'colorscale',
        role: 'style',
        editType: 'calc',
        dflt: colorscaleDflt,
        impliedEdits: {autocolorscale: false},
        description: [
            'Sets the colorscale.',
            effectDesc,
            ' The colorscale must be an array containing',
            ' arrays mapping a normalized value to an',
            ' rgb, rgba, hex, hsl, hsv, or named color string.',
            ' At minimum, a mapping for the lowest (0) and highest (1)',
            ' values are required. For example,',
            ' `[[0, \'rgb(0,0,255)\', [1, \'rgb(255,0,0)\']]`.',
            ' To control the bounds of the colorscale in color space,',
            ' use', minmaxFull, '.',
            ' Alternatively, `colorscale` may be a palette name string',
            ' of the following list: ' + paletteStr + '.'
        ].join('')
    };

    attrs.autocolorscale = {
        valType: 'boolean',
        role: 'style',
        // gets overrode in 'heatmap' & 'surface' for backwards comp.
        dflt: opts.autoColorDflt === false ? false : true,
        editType: 'calc',
        impliedEdits: {colorscale: undefined},
        description: [
            'Determines whether the colorscale is a default palette (`autocolorscale: true`)',
            ' or the palette determined by ', code(contextHead + 'colorscale'), '.',
            effectDesc,
            ' In case `colorscale` is unspecified or `autocolorscale` is true, the default ',
            ' palette will be chosen according to whether numbers in the `color` array are',
            ' all positive, all negative or mixed.'
        ].join('')
    };

    attrs.reversescale = {
        valType: 'boolean',
        role: 'style',
        dflt: false,
        editType: 'plot',
        description: [
            'Reverses the color mapping if true.',
            effectDesc,
            ' If true, ', minFull, ' will correspond to the last color',
            ' in the array and ', maxFull, ' will correspond to the first color.'
        ].join('')
    };

    if(!noScale) {
        attrs.showscale = {
            valType: 'boolean',
            role: 'info',
            dflt: showScaleDflt,
            editType: 'calc',
            description: [
                'Determines whether or not a colorbar is displayed for this trace.',
                effectDesc
            ].join('')
        };

        attrs.colorbar = colorbarAttrs;
    }

    if(!opts.noColorAxis) {
        attrs.coloraxis = {
            valType: 'subplotid',
            role: 'info',
            regex: counterRegex('coloraxis'),
            dflt: null,
            editType: 'calc',
            description: [
                'Sets a reference to a shared color axis.',
                'References to these shared color axes are *coloraxis*, *coloraxis2*, *coloraxis3*, etc.',
                'Settings for these shared color axes are set in the layout, under',
                '`layout.coloraxis`, `layout.coloraxis2`, etc.',
                'Note that multiple color scales can be linked to the same color axis.'
            ].join(' ')
        };
    }

    return attrs;
};
