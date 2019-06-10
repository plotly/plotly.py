/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var Lib = require('../../lib');
var attributes = require('./attributes');
var Color = require('../../components/color');
var tinycolor = require('tinycolor2');
var handleDomainDefaults = require('../../plots/domain').defaults;
var handleHoverLabelDefaults = require('../../components/fx/hoverlabel_defaults');
var Template = require('../../plot_api/plot_template');
var handleArrayContainerDefaults = require('../../plots/array_container_defaults');

module.exports = function supplyDefaults(traceIn, traceOut, defaultColor, layout) {
    function coerce(attr, dflt) {
        return Lib.coerce(traceIn, traceOut, attributes, attr, dflt);
    }

    var hoverlabelDefault = Lib.extendDeep(layout.hoverlabel, traceIn.hoverlabel);

    // node attributes
    var nodeIn = traceIn.node;
    var nodeOut = Template.newContainer(traceOut, 'node');

    function coerceNode(attr, dflt) {
        return Lib.coerce(nodeIn, nodeOut, attributes.node, attr, dflt);
    }
    coerceNode('label');
    coerceNode('groups');
    coerceNode('x');
    coerceNode('y');
    coerceNode('pad');
    coerceNode('thickness');
    coerceNode('line.color');
    coerceNode('line.width');
    coerceNode('hoverinfo', traceIn.hoverinfo);
    handleHoverLabelDefaults(nodeIn, nodeOut, coerceNode, hoverlabelDefault);
    coerceNode('hovertemplate');

    var colors = layout.colorway;

    var defaultNodePalette = function(i) {return colors[i % colors.length];};

    coerceNode('color', nodeOut.label.map(function(d, i) {
        return Color.addOpacity(defaultNodePalette(i), 0.8);
    }));

    // link attributes
    var linkIn = traceIn.link || {};
    var linkOut = Template.newContainer(traceOut, 'link');

    function coerceLink(attr, dflt) {
        return Lib.coerce(linkIn, linkOut, attributes.link, attr, dflt);
    }
    coerceLink('label');
    coerceLink('source');
    coerceLink('target');
    coerceLink('value');
    coerceLink('line.color');
    coerceLink('line.width');
    coerceLink('hoverinfo', traceIn.hoverinfo);
    handleHoverLabelDefaults(linkIn, linkOut, coerceLink, hoverlabelDefault);
    coerceLink('hovertemplate');

    var defaultLinkColor = tinycolor(layout.paper_bgcolor).getLuminance() < 0.333 ?
                'rgba(255, 255, 255, 0.6)' :
                'rgba(0, 0, 0, 0.2)';

    coerceLink('color', Lib.repeat(defaultLinkColor, linkOut.value.length));

    handleArrayContainerDefaults(linkIn, linkOut, {
        name: 'colorscales',
        handleItemDefaults: concentrationscalesDefaults
    });

    handleDomainDefaults(traceOut, layout, coerce);

    coerce('orientation');
    coerce('valueformat');
    coerce('valuesuffix');

    var dfltArrangement;
    if(nodeOut.x.length && nodeOut.y.length) {
        dfltArrangement = 'freeform';
    }
    coerce('arrangement', dfltArrangement);

    Lib.coerceFont(coerce, 'textfont', Lib.extendFlat({}, layout.font));

    // disable 1D transforms - arrays here are 1D but their lengths/meanings
    // don't match, between nodes and links
    traceOut._length = null;
};

function concentrationscalesDefaults(In, Out) {
    function coerce(attr, dflt) {
        return Lib.coerce(In, Out, attributes.link.colorscales, attr, dflt);
    }

    coerce('label');
    coerce('cmin');
    coerce('cmax');
    coerce('colorscale');
}
