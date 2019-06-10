/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

var d3 = require('d3');

var Lib = require('../lib');
var Drawing = require('../components/drawing');
var Color = require('../components/color');

var xmlnsNamespaces = require('../constants/xmlns_namespaces');
var DOUBLEQUOTE_REGEX = /"/g;
var DUMMY_SUB = 'TOBESTRIPPED';
var DUMMY_REGEX = new RegExp('("' + DUMMY_SUB + ')|(' + DUMMY_SUB + '")', 'g');

function htmlEntityDecode(s) {
    var hiddenDiv = d3.select('body').append('div').style({display: 'none'}).html('');
    var replaced = s.replace(/(&[^;]*;)/gi, function(d) {
        if(d === '&lt;') { return '&#60;'; } // special handling for brackets
        if(d === '&rt;') { return '&#62;'; }
        if(d.indexOf('<') !== -1 || d.indexOf('>') !== -1) { return ''; }
        return hiddenDiv.html(d).text(); // everything else, let the browser decode it to unicode
    });
    hiddenDiv.remove();
    return replaced;
}

function xmlEntityEncode(str) {
    return str.replace(/&(?!\w+;|\#[0-9]+;| \#x[0-9A-F]+;)/g, '&amp;');
}

module.exports = function toSVG(gd, format, scale) {
    var fullLayout = gd._fullLayout;
    var svg = fullLayout._paper;
    var toppaper = fullLayout._toppaper;
    var width = fullLayout.width;
    var height = fullLayout.height;
    var i;

    // make background color a rect in the svg, then revert after scraping
    // all other alterations have been dealt with by properly preparing the svg
    // in the first place... like setting cursors with css classes so we don't
    // have to remove them, and providing the right namespaces in the svg to
    // begin with
    svg.insert('rect', ':first-child')
        .call(Drawing.setRect, 0, 0, width, height)
        .call(Color.fill, fullLayout.paper_bgcolor);

    // subplot-specific to-SVG methods
    // which notably add the contents of the gl-container
    // into the main svg node
    var basePlotModules = fullLayout._basePlotModules || [];
    for(i = 0; i < basePlotModules.length; i++) {
        var _module = basePlotModules[i];

        if(_module.toSVG) _module.toSVG(gd);
    }

    // add top items above them assumes everything in toppaper is either
    // a group or a defs, and if it's empty (like hoverlayer) we can ignore it.
    if(toppaper) {
        var nodes = toppaper.node().childNodes;

        // make copy of nodes as childNodes prop gets mutated in loop below
        var topGroups = Array.prototype.slice.call(nodes);

        for(i = 0; i < topGroups.length; i++) {
            var topGroup = topGroups[i];

            if(topGroup.childNodes.length) svg.node().appendChild(topGroup);
        }
    }

    // remove draglayer for Adobe Illustrator compatibility
    if(fullLayout._draggers) {
        fullLayout._draggers.remove();
    }

    // in case the svg element had an explicit background color, remove this
    // we want the rect to get the color so it's the right size; svg bg will
    // fill whatever container it's displayed in regardless of plot size.
    svg.node().style.background = '';

    svg.selectAll('text')
        .attr({'data-unformatted': null, 'data-math': null})
        .each(function() {
            var txt = d3.select(this);

            // hidden text is pre-formatting mathjax, the browser ignores it
            // but in a static plot it's useless and it can confuse batik
            // we've tried to standardize on display:none but make sure we still
            // catch visibility:hidden if it ever arises
            if(this.style.visibility === 'hidden' || this.style.display === 'none') {
                txt.remove();
                return;
            } else {
                // clear other visibility/display values to default
                // to not potentially confuse non-browser SVG implementations
                txt.style({visibility: null, display: null});
            }

            // Font family styles break things because of quotation marks,
            // so we must remove them *after* the SVG DOM has been serialized
            // to a string (browsers convert singles back)
            var ff = this.style.fontFamily;
            if(ff && ff.indexOf('"') !== -1) {
                txt.style('font-family', ff.replace(DOUBLEQUOTE_REGEX, DUMMY_SUB));
            }
        });

    svg.selectAll('.point, .scatterpts, .legendfill>path, .legendlines>path, .cbfill').each(function() {
        var pt = d3.select(this);

        // similar to font family styles above,
        // we must remove " after the SVG DOM has been serialized
        var fill = this.style.fill;
        if(fill && fill.indexOf('url(') !== -1) {
            pt.style('fill', fill.replace(DOUBLEQUOTE_REGEX, DUMMY_SUB));
        }

        var stroke = this.style.stroke;
        if(stroke && stroke.indexOf('url(') !== -1) {
            pt.style('stroke', stroke.replace(DOUBLEQUOTE_REGEX, DUMMY_SUB));
        }
    });

    if(format === 'pdf' || format === 'eps') {
        // these formats make the extra line MathJax adds around symbols look super thick in some cases
        // it looks better if this is removed entirely.
        svg.selectAll('#MathJax_SVG_glyphs path')
            .attr('stroke-width', 0);
    }

    // fix for IE namespacing quirk?
    // http://stackoverflow.com/questions/19610089/unwanted-namespaces-on-svg-markup-when-using-xmlserializer-in-javascript-with-ie
    svg.node().setAttributeNS(xmlnsNamespaces.xmlns, 'xmlns', xmlnsNamespaces.svg);
    svg.node().setAttributeNS(xmlnsNamespaces.xmlns, 'xmlns:xlink', xmlnsNamespaces.xlink);

    if(format === 'svg' && scale) {
        svg.attr('width', scale * width);
        svg.attr('height', scale * height);
        svg.attr('viewBox', '0 0 ' + width + ' ' + height);
    }

    var s = new window.XMLSerializer().serializeToString(svg.node());
    s = htmlEntityDecode(s);
    s = xmlEntityEncode(s);

    // Fix quotations around font strings and gradient URLs
    s = s.replace(DUMMY_REGEX, '\'');

    // IE is very strict, so we will need to clean
    //  svg with the following regex
    //  yes this is messy, but do not know a better way
    // Even with this IE will not work due to tainted canvas
    //  see https://github.com/kangax/fabric.js/issues/1957
    //      http://stackoverflow.com/questions/18112047/canvas-todataurl-working-in-all-browsers-except-ie10
    // Leave here just in case the CORS/tainted IE issue gets resolved
    if(Lib.isIE()) {
        // replace double quote with single quote
        s = s.replace(/"/gi, '\'');
        // url in svg are single quoted
        //   since we changed double to single
        //   we'll need to change these to double-quoted
        s = s.replace(/(\('#)([^']*)('\))/gi, '(\"#$2\")');
        // font names with spaces will be escaped single-quoted
        //   we'll need to change these to double-quoted
        s = s.replace(/(\\')/gi, '\"');
    }

    return s;
};
