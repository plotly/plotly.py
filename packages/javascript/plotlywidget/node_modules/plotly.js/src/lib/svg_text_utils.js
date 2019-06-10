/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/


'use strict';

/* global MathJax:false */

var d3 = require('d3');

var Lib = require('../lib');
var xmlnsNamespaces = require('../constants/xmlns_namespaces');
var LINE_SPACING = require('../constants/alignment').LINE_SPACING;

// text converter

function getSize(_selection, _dimension) {
    return _selection.node().getBoundingClientRect()[_dimension];
}

var FIND_TEX = /([^$]*)([$]+[^$]*[$]+)([^$]*)/;

exports.convertToTspans = function(_context, gd, _callback) {
    var str = _context.text();

    // Until we get tex integrated more fully (so it can be used along with non-tex)
    // allow some elements to prohibit it by attaching 'data-notex' to the original
    var tex = (!_context.attr('data-notex')) &&
        (typeof MathJax !== 'undefined') &&
        str.match(FIND_TEX);

    var parent = d3.select(_context.node().parentNode);
    if(parent.empty()) return;
    var svgClass = (_context.attr('class')) ? _context.attr('class').split(' ')[0] : 'text';
    svgClass += '-math';
    parent.selectAll('svg.' + svgClass).remove();
    parent.selectAll('g.' + svgClass + '-group').remove();
    _context.style('display', null)
        .attr({
            // some callers use data-unformatted *from the <text> element* in 'cancel'
            // so we need it here even if we're going to turn it into math
            // these two (plus style and text-anchor attributes) form the key we're
            // going to use for Drawing.bBox
            'data-unformatted': str,
            'data-math': 'N'
        });

    function showText() {
        if(!parent.empty()) {
            svgClass = _context.attr('class') + '-math';
            parent.select('svg.' + svgClass).remove();
        }
        _context.text('')
            .style('white-space', 'pre');

        var hasLink = buildSVGText(_context.node(), str);

        if(hasLink) {
            // at least in Chrome, pointer-events does not seem
            // to be honored in children of <text> elements
            // so if we have an anchor, we have to make the
            // whole element respond
            _context.style('pointer-events', 'all');
        }

        exports.positionText(_context);

        if(_callback) _callback.call(_context);
    }

    if(tex) {
        ((gd && gd._promises) || []).push(new Promise(function(resolve) {
            _context.style('display', 'none');
            var fontSize = parseInt(_context.node().style.fontSize, 10);
            var config = {fontSize: fontSize};

            texToSVG(tex[2], config, function(_svgEl, _glyphDefs, _svgBBox) {
                parent.selectAll('svg.' + svgClass).remove();
                parent.selectAll('g.' + svgClass + '-group').remove();

                var newSvg = _svgEl && _svgEl.select('svg');
                if(!newSvg || !newSvg.node()) {
                    showText();
                    resolve();
                    return;
                }

                var mathjaxGroup = parent.append('g')
                    .classed(svgClass + '-group', true)
                    .attr({
                        'pointer-events': 'none',
                        'data-unformatted': str,
                        'data-math': 'Y'
                    });

                mathjaxGroup.node().appendChild(newSvg.node());

                // stitch the glyph defs
                if(_glyphDefs && _glyphDefs.node()) {
                    newSvg.node().insertBefore(_glyphDefs.node().cloneNode(true),
                                               newSvg.node().firstChild);
                }

                newSvg.attr({
                    'class': svgClass,
                    height: _svgBBox.height,
                    preserveAspectRatio: 'xMinYMin meet'
                })
                .style({overflow: 'visible', 'pointer-events': 'none'});

                var fill = _context.node().style.fill || 'black';
                var g = newSvg.select('g');
                g.attr({fill: fill, stroke: fill});

                var newSvgW = getSize(g, 'width');
                var newSvgH = getSize(g, 'height');
                var newX = +_context.attr('x') - newSvgW *
                    {start: 0, middle: 0.5, end: 1}[_context.attr('text-anchor') || 'start'];
                // font baseline is about 1/4 fontSize below centerline
                var textHeight = fontSize || getSize(_context, 'height');
                var dy = -textHeight / 4;

                if(svgClass[0] === 'y') {
                    mathjaxGroup.attr({
                        transform: 'rotate(' + [-90, +_context.attr('x'), +_context.attr('y')] +
                        ') translate(' + [-newSvgW / 2, dy - newSvgH / 2] + ')'
                    });
                    newSvg.attr({x: +_context.attr('x'), y: +_context.attr('y')});
                } else if(svgClass[0] === 'l') {
                    newSvg.attr({x: _context.attr('x'), y: dy - (newSvgH / 2)});
                } else if(svgClass[0] === 'a' && svgClass.indexOf('atitle') !== 0) {
                    newSvg.attr({x: 0, y: dy});
                } else {
                    newSvg.attr({x: newX, y: (+_context.attr('y') + dy - newSvgH / 2)});
                }

                if(_callback) _callback.call(_context, mathjaxGroup);
                resolve(mathjaxGroup);
            });
        }));
    } else showText();

    return _context;
};


// MathJax

var LT_MATCH = /(<|&lt;|&#60;)/g;
var GT_MATCH = /(>|&gt;|&#62;)/g;

function cleanEscapesForTex(s) {
    return s.replace(LT_MATCH, '\\lt ')
        .replace(GT_MATCH, '\\gt ');
}

function texToSVG(_texString, _config, _callback) {
    var originalRenderer,
        originalConfig,
        originalProcessSectionDelay,
        tmpDiv;

    MathJax.Hub.Queue(
    function() {
        originalConfig = Lib.extendDeepAll({}, MathJax.Hub.config);

        originalProcessSectionDelay = MathJax.Hub.processSectionDelay;
        if(MathJax.Hub.processSectionDelay !== undefined) {
            // MathJax 2.5+
            MathJax.Hub.processSectionDelay = 0;
        }

        return MathJax.Hub.Config({
            messageStyle: 'none',
            tex2jax: {
                inlineMath: [['$', '$'], ['\\(', '\\)']]
            },
            displayAlign: 'left',
        });
    },
    function() {
        // Get original renderer
        originalRenderer = MathJax.Hub.config.menuSettings.renderer;
        if(originalRenderer !== 'SVG') {
            return MathJax.Hub.setRenderer('SVG');
        }
    },
    function() {
        var randomID = 'math-output-' + Lib.randstr({}, 64);
        tmpDiv = d3.select('body').append('div')
            .attr({id: randomID})
            .style({visibility: 'hidden', position: 'absolute'})
            .style({'font-size': _config.fontSize + 'px'})
            .text(cleanEscapesForTex(_texString));

        return MathJax.Hub.Typeset(tmpDiv.node());
    },
    function() {
        var glyphDefs = d3.select('body').select('#MathJax_SVG_glyphs');

        if(tmpDiv.select('.MathJax_SVG').empty() || !tmpDiv.select('svg').node()) {
            Lib.log('There was an error in the tex syntax.', _texString);
            _callback();
        } else {
            var svgBBox = tmpDiv.select('svg').node().getBoundingClientRect();
            _callback(tmpDiv.select('.MathJax_SVG'), glyphDefs, svgBBox);
        }

        tmpDiv.remove();

        if(originalRenderer !== 'SVG') {
            return MathJax.Hub.setRenderer(originalRenderer);
        }
    },
    function() {
        if(originalProcessSectionDelay !== undefined) {
            MathJax.Hub.processSectionDelay = originalProcessSectionDelay;
        }
        return MathJax.Hub.Config(originalConfig);
    });
}

var TAG_STYLES = {
    // would like to use baseline-shift for sub/sup but FF doesn't support it
    // so we need to use dy along with the uber hacky shift-back-to
    // baseline below
    sup: 'font-size:70%',
    sub: 'font-size:70%',
    b: 'font-weight:bold',
    i: 'font-style:italic',
    a: 'cursor:pointer',
    span: '',
    em: 'font-style:italic;font-weight:bold'
};

// baseline shifts for sub and sup
var SHIFT_DY = {
    sub: '0.3em',
    sup: '-0.6em'
};
// reset baseline by adding a tspan (empty except for a zero-width space)
// with dy of -70% * SHIFT_DY (because font-size=70%)
var RESET_DY = {
    sub: '-0.21em',
    sup: '0.42em'
};
var ZERO_WIDTH_SPACE = '\u200b';

/*
 * Whitelist of protocols in user-supplied urls. Mostly we want to avoid javascript
 * and related attack vectors. The empty items are there for IE, that in various
 * versions treats relative paths as having different flavors of no protocol, while
 * other browsers have these explicitly inherit the protocol of the page they're in.
 */
var PROTOCOLS = ['http:', 'https:', 'mailto:', '', undefined, ':'];

var NEWLINES = /(\r\n?|\n)/g;

var SPLIT_TAGS = /(<[^<>]*>)/;

var ONE_TAG = /<(\/?)([^ >]*)(\s+(.*))?>/i;

var BR_TAG = /<br(\s+.*)?>/i;

/*
 * style and href: pull them out of either single or double quotes. Also
 * - target: (_blank|_self|_parent|_top|framename)
 *     note that you can't use target to get a popup but if you use popup,
 *     a `framename` will be passed along as the name of the popup window.
 *     per the spec, cannot contain whitespace.
 *     for backward compatibility we default to '_blank'
 * - popup: a custom one for us to enable popup (new window) links. String
 *     for window.open -> strWindowFeatures, like 'menubar=yes,width=500,height=550'
 *     note that at least in Chrome, you need to give at least one property
 *     in this string or the page will open in a new tab anyway. We follow this
 *     convention and will not make a popup if this string is empty.
 *     per the spec, cannot contain whitespace.
 *
 * Because we hack in other attributes with style (sub & sup), drop any trailing
 * semicolon in user-supplied styles so we can consistently append the tag-dependent style
 *
 * These are for tag attributes; Chrome anyway will convert entities in
 * attribute values, but not in attribute names
 * you can test this by for example:
 * > p = document.createElement('p')
 * > p.innerHTML = '<span styl&#x65;="font-color:r&#x65;d;">Hi</span>'
 * > p.innerHTML
 * <- '<span styl&#x65;="font-color:red;">Hi</span>'
 */
var STYLEMATCH = /(^|[\s"'])style\s*=\s*("([^"]*);?"|'([^']*);?')/i;
var HREFMATCH = /(^|[\s"'])href\s*=\s*("([^"]*)"|'([^']*)')/i;
var TARGETMATCH = /(^|[\s"'])target\s*=\s*("([^"\s]*)"|'([^'\s]*)')/i;
var POPUPMATCH = /(^|[\s"'])popup\s*=\s*("([\w=,]*)"|'([\w=,]*)')/i;

// dedicated matcher for these quoted regexes, that can return their results
// in two different places
function getQuotedMatch(_str, re) {
    if(!_str) return null;
    var match = _str.match(re);
    var result = match && (match[3] || match[4]);
    return result && convertEntities(result);
}

var COLORMATCH = /(^|;)\s*color:/;

/**
 * Strip string of tags
 *
 * @param {string} _str : input string
 * @param {object} opts :
 * - len {number} max length of output string
 * - allowedTags {array} list of pseudo-html tags to NOT strip
 * @return {string}
 */
exports.plainText = function(_str, opts) {
    opts = opts || {};

    var len = (opts.len !== undefined && opts.len !== -1) ? opts.len : Infinity;
    var allowedTags = opts.allowedTags !== undefined ? opts.allowedTags : ['br'];

    var ellipsis = '...';
    var eLen = ellipsis.length;

    var oldParts = _str.split(SPLIT_TAGS);
    var newParts = [];
    var prevTag = '';
    var l = 0;

    for(var i = 0; i < oldParts.length; i++) {
        var p = oldParts[i];
        var match = p.match(ONE_TAG);
        var tagType = match && match[2].toLowerCase();

        if(tagType) {
            // N.B. tags do not count towards string length
            if(allowedTags.indexOf(tagType) !== -1) {
                newParts.push(p);
                prevTag = tagType;
            }
        } else {
            var pLen = p.length;

            if((l + pLen) < len) {
                newParts.push(p);
                l += pLen;
            } else if(l < len) {
                var pLen2 = len - l;

                if(prevTag && (prevTag !== 'br' || pLen2 <= eLen || pLen <= eLen)) {
                    newParts.pop();
                }

                if(len > eLen) {
                    newParts.push(p.substr(0, pLen2 - eLen) + ellipsis);
                } else {
                    newParts.push(p.substr(0, pLen2));
                }
                break;
            }

            prevTag = '';
        }
    }

    return newParts.join('');
};

/*
 * N.B. HTML entities are listed without the leading '&' and trailing ';'
 * https://www.freeformatter.com/html-entities.html
 *
 * FWIW if we wanted to support the full set, it has 2261 entries:
 * https://www.w3.org/TR/html5/entities.json
 * though I notice that some of these are duplicates and/or are missing ";"
 * eg: "&amp;", "&amp", "&AMP;", and "&AMP" all map to "&"
 * We no longer need to include numeric entities here, these are now handled
 * by String.fromCodePoint/fromCharCode
 *
 * Anyway the only ones that are really important to allow are the HTML special
 * chars <, >, and &, because these ones can trigger special processing if not
 * replaced by the corresponding entity.
 */
var entityToUnicode = {
    mu: 'μ',
    amp: '&',
    lt: '<',
    gt: '>',
    nbsp: ' ',
    times: '×',
    plusmn: '±',
    deg: '°'
};

// NOTE: in general entities can contain uppercase too (so [a-zA-Z]) but all the
// ones we support use only lowercase. If we ever change that, update the regex.
var ENTITY_MATCH = /&(#\d+|#x[\da-fA-F]+|[a-z]+);/g;
function convertEntities(_str) {
    return _str.replace(ENTITY_MATCH, function(fullMatch, innerMatch) {
        var outChar;
        if(innerMatch.charAt(0) === '#') {
            // cannot use String.fromCodePoint in IE
            outChar = fromCodePoint(
                innerMatch.charAt(1) === 'x' ?
                    parseInt(innerMatch.substr(2), 16) :
                    parseInt(innerMatch.substr(1), 10)
            );
        } else outChar = entityToUnicode[innerMatch];

        // as in regular HTML, if we didn't decode the entity just
        // leave the raw text in place.
        return outChar || fullMatch;
    });
}
exports.convertEntities = convertEntities;

function fromCodePoint(code) {
    // Don't allow overflow. In Chrome this turns into � but I feel like it's
    // more useful to just not convert it at all.
    if(code > 0x10FFFF) return;
    var stringFromCodePoint = String.fromCodePoint;
    if(stringFromCodePoint) return stringFromCodePoint(code);

    // IE doesn't have String.fromCodePoint
    // see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCodePoint
    var stringFromCharCode = String.fromCharCode;
    if(code <= 0xFFFF) return stringFromCharCode(code);
    return stringFromCharCode(
        (code >> 10) + 0xD7C0,
        (code % 0x400) + 0xDC00
    );
}

/*
 * buildSVGText: convert our pseudo-html into SVG tspan elements, and attach these
 * to containerNode
 *
 * @param {svg text element} containerNode: the <text> node to insert this text into
 * @param {string} str: the pseudo-html string to convert to svg
 *
 * @returns {bool}: does the result contain any links? We need to handle the text element
 *   somewhat differently if it does, so just keep track of this when it happens.
 */
function buildSVGText(containerNode, str) {
    /*
     * Normalize behavior between IE and others wrt newlines and whitespace:pre
     * this combination makes IE barf https://github.com/plotly/plotly.js/issues/746
     * Chrome and FF display \n, \r, or \r\n as a space in this mode.
     * I feel like at some point we turned these into <br> but currently we don't so
     * I'm just going to cement what we do now in Chrome and FF
     */
    str = str.replace(NEWLINES, ' ');

    var hasLink = false;

    // as we're building the text, keep track of what elements we're nested inside
    // nodeStack will be an array of {node, type, style, href, target, popup}
    // where only type: 'a' gets the last 3 and node is only added when it's created
    var nodeStack = [];
    var currentNode;
    var currentLine = -1;

    function newLine() {
        currentLine++;

        var lineNode = document.createElementNS(xmlnsNamespaces.svg, 'tspan');
        d3.select(lineNode).attr({
            class: 'line',
            dy: (currentLine * LINE_SPACING) + 'em'
        });
        containerNode.appendChild(lineNode);

        currentNode = lineNode;

        var oldNodeStack = nodeStack;
        nodeStack = [{node: lineNode}];

        if(oldNodeStack.length > 1) {
            for(var i = 1; i < oldNodeStack.length; i++) {
                enterNode(oldNodeStack[i]);
            }
        }
    }

    function enterNode(nodeSpec) {
        var type = nodeSpec.type;
        var nodeAttrs = {};
        var nodeType;

        if(type === 'a') {
            nodeType = 'a';
            var target = nodeSpec.target;
            var href = nodeSpec.href;
            var popup = nodeSpec.popup;
            if(href) {
                nodeAttrs = {
                    'xlink:xlink:show': (target === '_blank' || target.charAt(0) !== '_') ? 'new' : 'replace',
                    target: target,
                    'xlink:xlink:href': href
                };
                if(popup) {
                    // security: href and target are not inserted as code but
                    // as attributes. popup is, but limited to /[A-Za-z0-9_=,]/
                    nodeAttrs.onclick = 'window.open(this.href.baseVal,this.target.baseVal,"' +
                        popup + '");return false;';
                }
            }
        } else nodeType = 'tspan';

        if(nodeSpec.style) nodeAttrs.style = nodeSpec.style;

        var newNode = document.createElementNS(xmlnsNamespaces.svg, nodeType);

        if(type === 'sup' || type === 'sub') {
            addTextNode(currentNode, ZERO_WIDTH_SPACE);
            currentNode.appendChild(newNode);

            var resetter = document.createElementNS(xmlnsNamespaces.svg, 'tspan');
            addTextNode(resetter, ZERO_WIDTH_SPACE);
            d3.select(resetter).attr('dy', RESET_DY[type]);
            nodeAttrs.dy = SHIFT_DY[type];

            currentNode.appendChild(newNode);
            currentNode.appendChild(resetter);
        } else {
            currentNode.appendChild(newNode);
        }

        d3.select(newNode).attr(nodeAttrs);

        currentNode = nodeSpec.node = newNode;
        nodeStack.push(nodeSpec);
    }

    function addTextNode(node, text) {
        node.appendChild(document.createTextNode(text));
    }

    function exitNode(type) {
        // A bare closing tag can't close the root node. If we encounter this it
        // means there's an extra closing tag that can just be ignored:
        if(nodeStack.length === 1) {
            Lib.log('Ignoring unexpected end tag </' + type + '>.', str);
            return;
        }

        var innerNode = nodeStack.pop();

        if(type !== innerNode.type) {
            Lib.log('Start tag <' + innerNode.type + '> doesnt match end tag <' +
                type + '>. Pretending it did match.', str);
        }
        currentNode = nodeStack[nodeStack.length - 1].node;
    }

    var hasLines = BR_TAG.test(str);

    if(hasLines) newLine();
    else {
        currentNode = containerNode;
        nodeStack = [{node: containerNode}];
    }

    var parts = str.split(SPLIT_TAGS);
    for(var i = 0; i < parts.length; i++) {
        var parti = parts[i];
        var match = parti.match(ONE_TAG);
        var tagType = match && match[2].toLowerCase();
        var tagStyle = TAG_STYLES[tagType];

        if(tagType === 'br') {
            newLine();
        } else if(tagStyle === undefined) {
            addTextNode(currentNode, convertEntities(parti));
        } else {
            // tag - open or close
            if(match[1]) {
                exitNode(tagType);
            } else {
                var extra = match[4];

                var nodeSpec = {type: tagType};

                // now add style, from both the tag name and any extra css
                // Most of the svg css that users will care about is just like html,
                // but font color is different (uses fill). Let our users ignore this.
                var css = getQuotedMatch(extra, STYLEMATCH);
                if(css) {
                    css = css.replace(COLORMATCH, '$1 fill:');
                    if(tagStyle) css += ';' + tagStyle;
                } else if(tagStyle) css = tagStyle;

                if(css) nodeSpec.style = css;

                if(tagType === 'a') {
                    hasLink = true;

                    var href = getQuotedMatch(extra, HREFMATCH);

                    if(href) {
                        // check safe protocols
                        var dummyAnchor = document.createElement('a');
                        dummyAnchor.href = href;
                        if(PROTOCOLS.indexOf(dummyAnchor.protocol) !== -1) {
                            // Decode href to allow both already encoded and not encoded
                            // URIs. Without decoding prior encoding, an already encoded
                            // URI would be encoded twice producing a semantically different URI.
                            nodeSpec.href = encodeURI(decodeURI(href));
                            nodeSpec.target = getQuotedMatch(extra, TARGETMATCH) || '_blank';
                            nodeSpec.popup = getQuotedMatch(extra, POPUPMATCH);
                        }
                    }
                }

                enterNode(nodeSpec);
            }
        }
    }

    return hasLink;
}

exports.lineCount = function lineCount(s) {
    return s.selectAll('tspan.line').size() || 1;
};

exports.positionText = function positionText(s, x, y) {
    return s.each(function() {
        var text = d3.select(this);

        function setOrGet(attr, val) {
            if(val === undefined) {
                val = text.attr(attr);
                if(val === null) {
                    text.attr(attr, 0);
                    val = 0;
                }
            } else text.attr(attr, val);
            return val;
        }

        var thisX = setOrGet('x', x);
        var thisY = setOrGet('y', y);

        if(this.nodeName === 'text') {
            text.selectAll('tspan.line').attr({x: thisX, y: thisY});
        }
    });
};

function alignHTMLWith(_base, container, options) {
    var alignH = options.horizontalAlign;
    var alignV = options.verticalAlign || 'top';
    var bRect = _base.node().getBoundingClientRect();
    var cRect = container.node().getBoundingClientRect();
    var thisRect;
    var getTop;
    var getLeft;

    if(alignV === 'bottom') {
        getTop = function() { return bRect.bottom - thisRect.height; };
    } else if(alignV === 'middle') {
        getTop = function() { return bRect.top + (bRect.height - thisRect.height) / 2; };
    } else { // default: top
        getTop = function() { return bRect.top; };
    }

    if(alignH === 'right') {
        getLeft = function() { return bRect.right - thisRect.width; };
    } else if(alignH === 'center') {
        getLeft = function() { return bRect.left + (bRect.width - thisRect.width) / 2; };
    } else { // default: left
        getLeft = function() { return bRect.left; };
    }

    return function() {
        thisRect = this.node().getBoundingClientRect();
        this.style({
            top: (getTop() - cRect.top) + 'px',
            left: (getLeft() - cRect.left) + 'px',
            'z-index': 1000
        });
        return this;
    };
}

/*
 * Editable title
 * @param {d3.selection} context: the element being edited. Normally text,
 *   but if it isn't, you should provide the styling options
 * @param {object} options:
 *   @param {div} options.gd: graphDiv
 *   @param {d3.selection} options.delegate: item to bind events to if not this
 *   @param {boolean} options.immediate: start editing now (true) or on click (false, default)
 *   @param {string} options.fill: font color if not as shown
 *   @param {string} options.background: background color if not as shown
 *   @param {string} options.text: initial text, if not as shown
 *   @param {string} options.horizontalAlign: alignment of the edit box wrt. the bound element
 *   @param {string} options.verticalAlign: alignment of the edit box wrt. the bound element
 */

exports.makeEditable = function(context, options) {
    var gd = options.gd;
    var _delegate = options.delegate;
    var dispatch = d3.dispatch('edit', 'input', 'cancel');
    var handlerElement = _delegate || context;

    context.style({'pointer-events': _delegate ? 'none' : 'all'});

    if(context.size() !== 1) throw new Error('boo');

    function handleClick() {
        appendEditable();
        context.style({opacity: 0});
        // also hide any mathjax svg
        var svgClass = handlerElement.attr('class');
        var mathjaxClass;
        if(svgClass) mathjaxClass = '.' + svgClass.split(' ')[0] + '-math-group';
        else mathjaxClass = '[class*=-math-group]';
        if(mathjaxClass) {
            d3.select(context.node().parentNode).select(mathjaxClass).style({opacity: 0});
        }
    }

    function selectElementContents(_el) {
        var el = _el.node();
        var range = document.createRange();
        range.selectNodeContents(el);
        var sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        el.focus();
    }

    function appendEditable() {
        var plotDiv = d3.select(gd);
        var container = plotDiv.select('.svg-container');
        var div = container.append('div');
        var cStyle = context.node().style;
        var fontSize = parseFloat(cStyle.fontSize || 12);

        var initialText = options.text;
        if(initialText === undefined) initialText = context.attr('data-unformatted');

        div.classed('plugin-editable editable', true)
            .style({
                position: 'absolute',
                'font-family': cStyle.fontFamily || 'Arial',
                'font-size': fontSize,
                color: options.fill || cStyle.fill || 'black',
                opacity: 1,
                'background-color': options.background || 'transparent',
                outline: '#ffffff33 1px solid',
                margin: [-fontSize / 8 + 1, 0, 0, -1].join('px ') + 'px',
                padding: '0',
                'box-sizing': 'border-box'
            })
            .attr({contenteditable: true})
            .text(initialText)
            .call(alignHTMLWith(context, container, options))
            .on('blur', function() {
                gd._editing = false;
                context.text(this.textContent)
                    .style({opacity: 1});
                var svgClass = d3.select(this).attr('class');
                var mathjaxClass;
                if(svgClass) mathjaxClass = '.' + svgClass.split(' ')[0] + '-math-group';
                else mathjaxClass = '[class*=-math-group]';
                if(mathjaxClass) {
                    d3.select(context.node().parentNode).select(mathjaxClass).style({opacity: 0});
                }
                var text = this.textContent;
                d3.select(this).transition().duration(0).remove();
                d3.select(document).on('mouseup', null);
                dispatch.edit.call(context, text);
            })
            .on('focus', function() {
                var editDiv = this;
                gd._editing = true;
                d3.select(document).on('mouseup', function() {
                    if(d3.event.target === editDiv) return false;
                    if(document.activeElement === div.node()) div.node().blur();
                });
            })
            .on('keyup', function() {
                if(d3.event.which === 27) {
                    gd._editing = false;
                    context.style({opacity: 1});
                    d3.select(this)
                        .style({opacity: 0})
                        .on('blur', function() { return false; })
                        .transition().remove();
                    dispatch.cancel.call(context, this.textContent);
                } else {
                    dispatch.input.call(context, this.textContent);
                    d3.select(this).call(alignHTMLWith(context, container, options));
                }
            })
            .on('keydown', function() {
                if(d3.event.which === 13) this.blur();
            })
            .call(selectElementContents);
    }

    if(options.immediate) handleClick();
    else handlerElement.on('click', handleClick);

    return d3.rebind(context, dispatch, 'on');
};
