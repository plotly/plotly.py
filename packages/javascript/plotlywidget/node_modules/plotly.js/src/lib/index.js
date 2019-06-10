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

var numConstants = require('../constants/numerical');
var FP_SAFE = numConstants.FP_SAFE;
var BADNUM = numConstants.BADNUM;

var lib = module.exports = {};

lib.nestedProperty = require('./nested_property');
lib.keyedContainer = require('./keyed_container');
lib.relativeAttr = require('./relative_attr');
lib.isPlainObject = require('./is_plain_object');
lib.toLogRange = require('./to_log_range');
lib.relinkPrivateKeys = require('./relink_private');

var arrayModule = require('./array');
lib.isTypedArray = arrayModule.isTypedArray;
lib.isArrayOrTypedArray = arrayModule.isArrayOrTypedArray;
lib.isArray1D = arrayModule.isArray1D;
lib.ensureArray = arrayModule.ensureArray;
lib.concat = arrayModule.concat;
lib.maxRowLength = arrayModule.maxRowLength;
lib.minRowLength = arrayModule.minRowLength;

var modModule = require('./mod');
lib.mod = modModule.mod;
lib.modHalf = modModule.modHalf;

var coerceModule = require('./coerce');
lib.valObjectMeta = coerceModule.valObjectMeta;
lib.coerce = coerceModule.coerce;
lib.coerce2 = coerceModule.coerce2;
lib.coerceFont = coerceModule.coerceFont;
lib.coerceHoverinfo = coerceModule.coerceHoverinfo;
lib.coerceSelectionMarkerOpacity = coerceModule.coerceSelectionMarkerOpacity;
lib.validate = coerceModule.validate;

var datesModule = require('./dates');
lib.dateTime2ms = datesModule.dateTime2ms;
lib.isDateTime = datesModule.isDateTime;
lib.ms2DateTime = datesModule.ms2DateTime;
lib.ms2DateTimeLocal = datesModule.ms2DateTimeLocal;
lib.cleanDate = datesModule.cleanDate;
lib.isJSDate = datesModule.isJSDate;
lib.formatDate = datesModule.formatDate;
lib.incrementMonth = datesModule.incrementMonth;
lib.dateTick0 = datesModule.dateTick0;
lib.dfltRange = datesModule.dfltRange;
lib.findExactDates = datesModule.findExactDates;
lib.MIN_MS = datesModule.MIN_MS;
lib.MAX_MS = datesModule.MAX_MS;

var searchModule = require('./search');
lib.findBin = searchModule.findBin;
lib.sorterAsc = searchModule.sorterAsc;
lib.sorterDes = searchModule.sorterDes;
lib.distinctVals = searchModule.distinctVals;
lib.roundUp = searchModule.roundUp;
lib.sort = searchModule.sort;
lib.findIndexOfMin = searchModule.findIndexOfMin;

var statsModule = require('./stats');
lib.aggNums = statsModule.aggNums;
lib.len = statsModule.len;
lib.mean = statsModule.mean;
lib.median = statsModule.median;
lib.midRange = statsModule.midRange;
lib.variance = statsModule.variance;
lib.stdev = statsModule.stdev;
lib.interp = statsModule.interp;

var matrixModule = require('./matrix');
lib.init2dArray = matrixModule.init2dArray;
lib.transposeRagged = matrixModule.transposeRagged;
lib.dot = matrixModule.dot;
lib.translationMatrix = matrixModule.translationMatrix;
lib.rotationMatrix = matrixModule.rotationMatrix;
lib.rotationXYMatrix = matrixModule.rotationXYMatrix;
lib.apply2DTransform = matrixModule.apply2DTransform;
lib.apply2DTransform2 = matrixModule.apply2DTransform2;

var anglesModule = require('./angles');
lib.deg2rad = anglesModule.deg2rad;
lib.rad2deg = anglesModule.rad2deg;
lib.angleDelta = anglesModule.angleDelta;
lib.angleDist = anglesModule.angleDist;
lib.isFullCircle = anglesModule.isFullCircle;
lib.isAngleInsideSector = anglesModule.isAngleInsideSector;
lib.isPtInsideSector = anglesModule.isPtInsideSector;
lib.pathArc = anglesModule.pathArc;
lib.pathSector = anglesModule.pathSector;
lib.pathAnnulus = anglesModule.pathAnnulus;

var anchorUtils = require('./anchor_utils');
lib.isLeftAnchor = anchorUtils.isLeftAnchor;
lib.isCenterAnchor = anchorUtils.isCenterAnchor;
lib.isRightAnchor = anchorUtils.isRightAnchor;
lib.isTopAnchor = anchorUtils.isTopAnchor;
lib.isMiddleAnchor = anchorUtils.isMiddleAnchor;
lib.isBottomAnchor = anchorUtils.isBottomAnchor;

var geom2dModule = require('./geometry2d');
lib.segmentsIntersect = geom2dModule.segmentsIntersect;
lib.segmentDistance = geom2dModule.segmentDistance;
lib.getTextLocation = geom2dModule.getTextLocation;
lib.clearLocationCache = geom2dModule.clearLocationCache;
lib.getVisibleSegment = geom2dModule.getVisibleSegment;
lib.findPointOnPath = geom2dModule.findPointOnPath;

var extendModule = require('./extend');
lib.extendFlat = extendModule.extendFlat;
lib.extendDeep = extendModule.extendDeep;
lib.extendDeepAll = extendModule.extendDeepAll;
lib.extendDeepNoArrays = extendModule.extendDeepNoArrays;

var loggersModule = require('./loggers');
lib.log = loggersModule.log;
lib.warn = loggersModule.warn;
lib.error = loggersModule.error;

var regexModule = require('./regex');
lib.counterRegex = regexModule.counter;

var throttleModule = require('./throttle');
lib.throttle = throttleModule.throttle;
lib.throttleDone = throttleModule.done;
lib.clearThrottle = throttleModule.clear;

lib.getGraphDiv = require('./get_graph_div');

lib.clearResponsive = require('./clear_responsive');

lib.makeTraceGroups = require('./make_trace_groups');

lib._ = require('./localize');

lib.notifier = require('./notifier');

lib.filterUnique = require('./filter_unique');
lib.filterVisible = require('./filter_visible');
lib.pushUnique = require('./push_unique');

lib.cleanNumber = require('./clean_number');

lib.ensureNumber = function ensureNumber(v) {
    if(!isNumeric(v)) return BADNUM;
    v = Number(v);
    if(v < -FP_SAFE || v > FP_SAFE) return BADNUM;
    return isNumeric(v) ? Number(v) : BADNUM;
};

/**
 * Is v a valid array index? Accepts numeric strings as well as numbers.
 *
 * @param {any} v: the value to test
 * @param {Optional[integer]} len: the array length we are indexing
 *
 * @return {bool}: v is a valid array index
 */
lib.isIndex = function(v, len) {
    if(len !== undefined && v >= len) return false;
    return isNumeric(v) && (v >= 0) && (v % 1 === 0);
};

lib.noop = require('./noop');
lib.identity = require('./identity');

/**
 * create an array of length 'cnt' filled with 'v' at all indices
 *
 * @param {any} v
 * @param {number} cnt
 * @return {array}
 */
lib.repeat = function(v, cnt) {
    var out = new Array(cnt);
    for(var i = 0; i < cnt; i++) {
        out[i] = v;
    }
    return out;
};

/**
 * swap x and y of the same attribute in container cont
 * specify attr with a ? in place of x/y
 * you can also swap other things than x/y by providing part1 and part2
 */
lib.swapAttrs = function(cont, attrList, part1, part2) {
    if(!part1) part1 = 'x';
    if(!part2) part2 = 'y';
    for(var i = 0; i < attrList.length; i++) {
        var attr = attrList[i];
        var xp = lib.nestedProperty(cont, attr.replace('?', part1));
        var yp = lib.nestedProperty(cont, attr.replace('?', part2));
        var temp = xp.get();
        xp.set(yp.get());
        yp.set(temp);
    }
};

/**
 * SVG painter's algo worked around with reinsertion
 */
lib.raiseToTop = function raiseToTop(elem) {
    elem.parentNode.appendChild(elem);
};

/**
 * cancel a possibly pending transition; returned selection may be used by caller
 */
lib.cancelTransition = function(selection) {
    return selection.transition().duration(0);
};

// constrain - restrict a number v to be between v0 and v1
lib.constrain = function(v, v0, v1) {
    if(v0 > v1) return Math.max(v1, Math.min(v0, v));
    return Math.max(v0, Math.min(v1, v));
};

/**
 * do two bounding boxes from getBoundingClientRect,
 * ie {left,right,top,bottom,width,height}, overlap?
 * takes optional padding pixels
 */
lib.bBoxIntersect = function(a, b, pad) {
    pad = pad || 0;
    return (a.left <= b.right + pad &&
            b.left <= a.right + pad &&
            a.top <= b.bottom + pad &&
            b.top <= a.bottom + pad);
};

/*
 * simpleMap: alternative to Array.map that only
 * passes on the element and up to 2 extra args you
 * provide (but not the array index or the whole array)
 *
 * array: the array to map it to
 * func: the function to apply
 * x1, x2: optional extra args
 */
lib.simpleMap = function(array, func, x1, x2) {
    var len = array.length;
    var out = new Array(len);
    for(var i = 0; i < len; i++) out[i] = func(array[i], x1, x2);
    return out;
};

/**
 * Random string generator
 *
 * @param {object} existing
 *     pass in strings to avoid as keys with truthy values
 * @param {int} bits
 *     bits of information in the output string, default 24
 * @param {int} base
 *     base of string representation, default 16. Should be a power of 2.
 */
lib.randstr = function randstr(existing, bits, base, _recursion) {
    if(!base) base = 16;
    if(bits === undefined) bits = 24;
    if(bits <= 0) return '0';

    var digits = Math.log(Math.pow(2, bits)) / Math.log(base);
    var res = '';
    var i, b, x;

    for(i = 2; digits === Infinity; i *= 2) {
        digits = Math.log(Math.pow(2, bits / i)) / Math.log(base) * i;
    }

    var rem = digits - Math.floor(digits);

    for(i = 0; i < Math.floor(digits); i++) {
        x = Math.floor(Math.random() * base).toString(base);
        res = x + res;
    }

    if(rem) {
        b = Math.pow(base, rem);
        x = Math.floor(Math.random() * b).toString(base);
        res = x + res;
    }

    var parsed = parseInt(res, base);
    if((existing && existing[res]) ||
         (parsed !== Infinity && parsed >= Math.pow(2, bits))) {
        if(_recursion > 10) {
            lib.warn('randstr failed uniqueness');
            return res;
        }
        return randstr(existing, bits, base, (_recursion || 0) + 1);
    } else return res;
};

lib.OptionControl = function(opt, optname) {
    /*
     * An environment to contain all option setters and
     * getters that collectively modify opts.
     *
     * You can call up opts from any function in new object
     * as this.optname || this.opt
     *
     * See FitOpts for example of usage
     */
    if(!opt) opt = {};
    if(!optname) optname = 'opt';

    var self = {};
    self.optionList = [];

    self._newoption = function(optObj) {
        optObj[optname] = opt;
        self[optObj.name] = optObj;
        self.optionList.push(optObj);
    };

    self['_' + optname] = opt;
    return self;
};

/**
 * lib.smooth: smooth arrayIn by convolving with
 * a hann window with given full width at half max
 * bounce the ends in, so the output has the same length as the input
 */
lib.smooth = function(arrayIn, FWHM) {
    FWHM = Math.round(FWHM) || 0; // only makes sense for integers
    if(FWHM < 2) return arrayIn;

    var alen = arrayIn.length;
    var alen2 = 2 * alen;
    var wlen = 2 * FWHM - 1;
    var w = new Array(wlen);
    var arrayOut = new Array(alen);
    var i;
    var j;
    var k;
    var v;

    // first make the window array
    for(i = 0; i < wlen; i++) {
        w[i] = (1 - Math.cos(Math.PI * (i + 1) / FWHM)) / (2 * FWHM);
    }

    // now do the convolution
    for(i = 0; i < alen; i++) {
        v = 0;
        for(j = 0; j < wlen; j++) {
            k = i + j + 1 - FWHM;

            // multibounce
            if(k < -alen) k -= alen2 * Math.round(k / alen2);
            else if(k >= alen2) k -= alen2 * Math.floor(k / alen2);

            // single bounce
            if(k < 0) k = - 1 - k;
            else if(k >= alen) k = alen2 - 1 - k;

            v += arrayIn[k] * w[j];
        }
        arrayOut[i] = v;
    }

    return arrayOut;
};

/**
 * syncOrAsync: run a sequence of functions synchronously
 * as long as its returns are not promises (ie have no .then)
 * includes one argument arg to send to all functions...
 * this is mainly just to prevent us having to make wrapper functions
 * when the only purpose of the wrapper is to reference gd
 * and a final step to be executed at the end
 * TODO: if there's an error and everything is sync,
 * this doesn't happen yet because we want to make sure
 * that it gets reported
 */
lib.syncOrAsync = function(sequence, arg, finalStep) {
    var ret, fni;

    function continueAsync() {
        return lib.syncOrAsync(sequence, arg, finalStep);
    }

    while(sequence.length) {
        fni = sequence.splice(0, 1)[0];
        ret = fni(arg);

        if(ret && ret.then) {
            return ret.then(continueAsync)
                .then(undefined, lib.promiseError);
        }
    }

    return finalStep && finalStep(arg);
};


/**
 * Helper to strip trailing slash, from
 * http://stackoverflow.com/questions/6680825/return-string-without-trailing-slash
 */
lib.stripTrailingSlash = function(str) {
    if(str.substr(-1) === '/') return str.substr(0, str.length - 1);
    return str;
};

lib.noneOrAll = function(containerIn, containerOut, attrList) {
    /**
     * some attributes come together, so if you have one of them
     * in the input, you should copy the default values of the others
     * to the input as well.
     */
    if(!containerIn) return;

    var hasAny = false;
    var hasAll = true;
    var i;
    var val;

    for(i = 0; i < attrList.length; i++) {
        val = containerIn[attrList[i]];
        if(val !== undefined && val !== null) hasAny = true;
        else hasAll = false;
    }

    if(hasAny && !hasAll) {
        for(i = 0; i < attrList.length; i++) {
            containerIn[attrList[i]] = containerOut[attrList[i]];
        }
    }
};

/** merges calcdata field (given by cdAttr) with traceAttr values
 *
 * N.B. Loop over minimum of cd.length and traceAttr.length
 * i.e. it does not try to fill in beyond traceAttr.length-1
 *
 * @param {array} traceAttr : trace attribute
 * @param {object} cd : calcdata trace
 * @param {string} cdAttr : calcdata key
 */
lib.mergeArray = function(traceAttr, cd, cdAttr) {
    if(lib.isArrayOrTypedArray(traceAttr)) {
        var imax = Math.min(traceAttr.length, cd.length);
        for(var i = 0; i < imax; i++) cd[i][cdAttr] = traceAttr[i];
    }
};

/** fills calcdata field (given by cdAttr) with traceAttr values
 *  or function of traceAttr values (e.g. some fallback)
 *
 * N.B. Loops over all cd items.
 *
 * @param {array} traceAttr : trace attribute
 * @param {object} cd : calcdata trace
 * @param {string} cdAttr : calcdata key
 * @param {function} [fn] : optional function to apply to each array item
 */
lib.fillArray = function(traceAttr, cd, cdAttr, fn) {
    fn = fn || lib.identity;

    if(lib.isArrayOrTypedArray(traceAttr)) {
        for(var i = 0; i < cd.length; i++) {
            cd[i][cdAttr] = fn(traceAttr[i]);
        }
    }
};

/** Handler for trace-wide vs per-point options
 *
 * @param {object} trace : (full) trace object
 * @param {number} ptNumber : index of the point in question
 * @param {string} astr : attribute string
 * @param {function} [fn] : optional function to apply to each array item
 *
 * @return {any}
 */
lib.castOption = function(trace, ptNumber, astr, fn) {
    fn = fn || lib.identity;

    var val = lib.nestedProperty(trace, astr).get();

    if(lib.isArrayOrTypedArray(val)) {
        if(Array.isArray(ptNumber) && lib.isArrayOrTypedArray(val[ptNumber[0]])) {
            return fn(val[ptNumber[0]][ptNumber[1]]);
        } else {
            return fn(val[ptNumber]);
        }
    } else {
        return val;
    }
};

/** Extract option from calcdata item, correctly falling back to
 *  trace value if not found.
 *
 *  @param {object} calcPt : calcdata[i][j] item
 *  @param {object} trace : (full) trace object
 *  @param {string} calcKey : calcdata key
 *  @param {string} traceKey : aka trace attribute string
 *  @return {any}
 */
lib.extractOption = function(calcPt, trace, calcKey, traceKey) {
    if(calcKey in calcPt) return calcPt[calcKey];

    // fallback to trace value,
    //   must check if value isn't itself an array
    //   which means the trace attribute has a corresponding
    //   calcdata key, but its value is falsy
    var traceVal = lib.nestedProperty(trace, traceKey).get();
    if(!Array.isArray(traceVal)) return traceVal;
};

function makePtIndex2PtNumber(indexToPoints) {
    var ptIndex2ptNumber = {};
    for(var k in indexToPoints) {
        var pts = indexToPoints[k];
        for(var j = 0; j < pts.length; j++) {
            ptIndex2ptNumber[pts[j]] = +k;
        }
    }
    return ptIndex2ptNumber;
}

/** Tag selected calcdata items
 *
 * N.B. note that point 'index' corresponds to input data array index
 *  whereas 'number' is its post-transform version.
 *
 * @param {array} calcTrace
 * @param {object} trace
 *  - selectedpoints {array}
 *  - _indexToPoints {object}
 * @param {ptNumber2cdIndex} ptNumber2cdIndex (optional)
 *  optional map object for trace types that do not have 1-to-1 point number to
 *  calcdata item index correspondence (e.g. histogram)
 */
lib.tagSelected = function(calcTrace, trace, ptNumber2cdIndex) {
    var selectedpoints = trace.selectedpoints;
    var indexToPoints = trace._indexToPoints;
    var ptIndex2ptNumber;

    // make pt index-to-number map object, which takes care of transformed traces
    if(indexToPoints) {
        ptIndex2ptNumber = makePtIndex2PtNumber(indexToPoints);
    }

    function isCdIndexValid(v) {
        return v !== undefined && v < calcTrace.length;
    }

    for(var i = 0; i < selectedpoints.length; i++) {
        var ptIndex = selectedpoints[i];

        if(lib.isIndex(ptIndex)) {
            var ptNumber = ptIndex2ptNumber ? ptIndex2ptNumber[ptIndex] : ptIndex;
            var cdIndex = ptNumber2cdIndex ? ptNumber2cdIndex[ptNumber] : ptNumber;

            if(isCdIndexValid(cdIndex)) {
                calcTrace[cdIndex].selected = 1;
            }
        }
    }
};

lib.selIndices2selPoints = function(trace) {
    var selectedpoints = trace.selectedpoints;
    var indexToPoints = trace._indexToPoints;

    if(indexToPoints) {
        var ptIndex2ptNumber = makePtIndex2PtNumber(indexToPoints);
        var out = [];

        for(var i = 0; i < selectedpoints.length; i++) {
            var ptIndex = selectedpoints[i];
            if(lib.isIndex(ptIndex)) {
                var ptNumber = ptIndex2ptNumber[ptIndex];
                if(lib.isIndex(ptNumber)) {
                    out.push(ptNumber);
                }
            }
        }

        return out;
    } else {
        return selectedpoints;
    }
};

/** Returns target as set by 'target' transform attribute
 *
 * @param {object} trace : full trace object
 * @param {object} transformOpts : transform option object
 *  - target (string} :
 *      either an attribute string referencing an array in the trace object, or
 *      a set array.
 *
 * @return {array or false} : the target array (NOT a copy!!) or false if invalid
 */
lib.getTargetArray = function(trace, transformOpts) {
    var target = transformOpts.target;

    if(typeof target === 'string' && target) {
        var array = lib.nestedProperty(trace, target).get();
        return Array.isArray(array) ? array : false;
    } else if(Array.isArray(target)) {
        return target;
    }

    return false;
};

/**
 * modified version of jQuery's extend to strip out private objs and functions,
 * and cut arrays down to first <arraylen> or 1 elements
 * because extend-like algorithms are hella slow
 * obj2 is assumed to already be clean of these things (including no arrays)
 */
lib.minExtend = function(obj1, obj2) {
    var objOut = {};
    if(typeof obj2 !== 'object') obj2 = {};
    var arrayLen = 3;
    var keys = Object.keys(obj1);
    var i, k, v;

    for(i = 0; i < keys.length; i++) {
        k = keys[i];
        v = obj1[k];
        if(k.charAt(0) === '_' || typeof v === 'function') continue;
        else if(k === 'module') objOut[k] = v;
        else if(Array.isArray(v)) {
            if(k === 'colorscale') {
                objOut[k] = v.slice();
            } else {
                objOut[k] = v.slice(0, arrayLen);
            }
        } else if(v && (typeof v === 'object')) objOut[k] = lib.minExtend(obj1[k], obj2[k]);
        else objOut[k] = v;
    }

    keys = Object.keys(obj2);
    for(i = 0; i < keys.length; i++) {
        k = keys[i];
        v = obj2[k];
        if(typeof v !== 'object' || !(k in objOut) || typeof objOut[k] !== 'object') {
            objOut[k] = v;
        }
    }

    return objOut;
};

lib.titleCase = function(s) {
    return s.charAt(0).toUpperCase() + s.substr(1);
};

lib.containsAny = function(s, fragments) {
    for(var i = 0; i < fragments.length; i++) {
        if(s.indexOf(fragments[i]) !== -1) return true;
    }
    return false;
};

lib.isPlotDiv = function(el) {
    var el3 = d3.select(el);
    return el3.node() instanceof HTMLElement &&
        el3.size() &&
        el3.classed('js-plotly-plot');
};

lib.removeElement = function(el) {
    var elParent = el && el.parentNode;
    if(elParent) elParent.removeChild(el);
};

/**
 * for dynamically adding style rules
 * makes one stylesheet that contains all rules added
 * by all calls to this function
 */
lib.addStyleRule = function(selector, styleString) {
    lib.addRelatedStyleRule('global', selector, styleString);
};

/**
 * for dynamically adding style rules
 * to a stylesheet uniquely identified by a uid
 */
lib.addRelatedStyleRule = function(uid, selector, styleString) {
    var id = 'plotly.js-style-' + uid;
    var style = document.getElementById(id);
    if(!style) {
        style = document.createElement('style');
        style.setAttribute('id', id);
        // WebKit hack :(
        style.appendChild(document.createTextNode(''));
        document.head.appendChild(style);
    }
    var styleSheet = style.sheet;

    if(styleSheet.insertRule) {
        styleSheet.insertRule(selector + '{' + styleString + '}', 0);
    } else if(styleSheet.addRule) {
        styleSheet.addRule(selector, styleString, 0);
    } else lib.warn('addStyleRule failed');
};

/**
 * to remove from the page a stylesheet identified by a given uid
 */
lib.deleteRelatedStyleRule = function(uid) {
    var id = 'plotly.js-style-' + uid;
    var style = document.getElementById(id);
    if(style) lib.removeElement(style);
};

lib.isIE = function() {
    return typeof window.navigator.msSaveBlob !== 'undefined';
};

/**
 * Duck typing to recognize a d3 selection, mostly for IE9's benefit
 * because it doesn't handle instanceof like modern browsers
 */
lib.isD3Selection = function(obj) {
    return obj && (typeof obj.classed === 'function');
};

/**
 * Append element to DOM only if not present.
 *
 * @param {d3 selection} parent : parent selection of the element in question
 * @param {string} nodeType : node type of element to append
 * @param {string} className (optional) : class name of element in question
 * @param {fn} enterFn (optional) : optional fn applied to entering elements only
 * @return {d3 selection} selection of new layer
 *
 * Previously, we were using the following pattern:
 *
 * ```
 * var sel = parent.selectAll('.' + className)
 *     .data([0]);
 *
 * sel.enter().append(nodeType)
 *     .classed(className, true);
 *
 * return sel;
 * ```
 *
 * in numerous places in our codebase to achieve the same behavior.
 *
 * The logic below performs much better, mostly as we are using
 * `.select` instead `.selectAll` that is `querySelector` instead of
 * `querySelectorAll`.
 *
 */
lib.ensureSingle = function(parent, nodeType, className, enterFn) {
    var sel = parent.select(nodeType + (className ? '.' + className : ''));
    if(sel.size()) return sel;

    var layer = parent.append(nodeType);
    if(className) layer.classed(className, true);
    if(enterFn) layer.call(enterFn);

    return layer;
};

/**
 * Same as Lib.ensureSingle, but using id as selector.
 * This version is mostly used for clipPath nodes.
 *
 * @param {d3 selection} parent : parent selection of the element in question
 * @param {string} nodeType : node type of element to append
 * @param {string} id : id of element in question
 * @param {fn} enterFn (optional) : optional fn applied to entering elements only
 * @return {d3 selection} selection of new layer
 */
lib.ensureSingleById = function(parent, nodeType, id, enterFn) {
    var sel = parent.select(nodeType + '#' + id);
    if(sel.size()) return sel;

    var layer = parent.append(nodeType).attr('id', id);
    if(enterFn) layer.call(enterFn);

    return layer;
};

/**
 * Converts a string path to an object.
 *
 * When given a string containing an array element, it will create a `null`
 * filled array of the given size.
 *
 * @example
 * lib.objectFromPath('nested.test[2].path', 'value');
 * // returns { nested: { test: [null, null, { path: 'value' }]}
 *
 * @param   {string}    path to nested value
 * @param   {*}         any value to be set
 *
 * @return {Object} the constructed object with a full nested path
 */
lib.objectFromPath = function(path, value) {
    var keys = path.split('.');
    var tmpObj;
    var obj = tmpObj = {};

    for(var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var el = null;

        var parts = keys[i].match(/(.*)\[([0-9]+)\]/);

        if(parts) {
            key = parts[1];
            el = parts[2];

            tmpObj = tmpObj[key] = [];

            if(i === keys.length - 1) {
                tmpObj[el] = value;
            } else {
                tmpObj[el] = {};
            }

            tmpObj = tmpObj[el];
        } else {
            if(i === keys.length - 1) {
                tmpObj[key] = value;
            } else {
                tmpObj[key] = {};
            }

            tmpObj = tmpObj[key];
        }
    }

    return obj;
};

/**
 * Iterate through an object in-place, converting dotted properties to objects.
 *
 * Examples:
 *
 *   lib.expandObjectPaths({'nested.test.path': 'value'});
 *     => { nested: { test: {path: 'value'}}}
 *
 * It also handles array notation, e.g.:
 *
 *   lib.expandObjectPaths({'foo[1].bar': 'value'});
 *     => { foo: [null, {bar: value}] }
 *
 * It handles merges the results when two properties are specified in parallel:
 *
 *   lib.expandObjectPaths({'foo[1].bar': 10, 'foo[0].bar': 20});
 *     => { foo: [{bar: 10}, {bar: 20}] }
 *
 * It does NOT, however, merge mulitple mutliply-nested arrays::
 *
 *   lib.expandObjectPaths({'marker[1].range[1]': 5, 'marker[1].range[0]': 4})
 *     => { marker: [null, {range: 4}] }
 */

// Store this to avoid recompiling regex on *every* prop since this may happen many
// many times for animations. Could maybe be inside the function. Not sure about
// scoping vs. recompilation tradeoff, but at least it's not just inlining it into
// the inner loop.
var dottedPropertyRegex = /^([^\[\.]+)\.(.+)?/;
var indexedPropertyRegex = /^([^\.]+)\[([0-9]+)\](\.)?(.+)?/;

lib.expandObjectPaths = function(data) {
    var match, key, prop, datum, idx, dest, trailingPath;
    if(typeof data === 'object' && !Array.isArray(data)) {
        for(key in data) {
            if(data.hasOwnProperty(key)) {
                if((match = key.match(dottedPropertyRegex))) {
                    datum = data[key];
                    prop = match[1];

                    delete data[key];

                    data[prop] = lib.extendDeepNoArrays(data[prop] || {}, lib.objectFromPath(key, lib.expandObjectPaths(datum))[prop]);
                } else if((match = key.match(indexedPropertyRegex))) {
                    datum = data[key];

                    prop = match[1];
                    idx = parseInt(match[2]);

                    delete data[key];

                    data[prop] = data[prop] || [];

                    if(match[3] === '.') {
                        // This is the case where theere are subsequent properties into which
                        // we must recurse, e.g. transforms[0].value
                        trailingPath = match[4];
                        dest = data[prop][idx] = data[prop][idx] || {};

                        // NB: Extend deep no arrays prevents this from working on multiple
                        // nested properties in the same object, e.g.
                        //
                        // {
                        //   foo[0].bar[1].range
                        //   foo[0].bar[0].range
                        // }
                        //
                        // In this case, the extendDeepNoArrays will overwrite one array with
                        // the other, so that both properties *will not* be present in the
                        // result. Fixing this would require a more intelligent tracking
                        // of changes and merging than extendDeepNoArrays currently accomplishes.
                        lib.extendDeepNoArrays(dest, lib.objectFromPath(trailingPath, lib.expandObjectPaths(datum)));
                    } else {
                        // This is the case where this property is the end of the line,
                        // e.g. xaxis.range[0]
                        data[prop][idx] = lib.expandObjectPaths(datum);
                    }
                } else {
                    data[key] = lib.expandObjectPaths(data[key]);
                }
            }
        }
    }

    return data;
};

/**
 * Converts value to string separated by the provided separators.
 *
 * @example
 * lib.numSeparate(2016, '.,');
 * // returns '2016'
 *
 * @example
 * lib.numSeparate(3000, '.,', true);
 * // returns '3,000'
 *
 * @example
 * lib.numSeparate(1234.56, '|,')
 * // returns '1,234|56'
 *
 * @param   {string|number} value       the value to be converted
 * @param   {string}    separators  string of decimal, then thousands separators
 * @param   {boolean}    separatethousands  boolean, 4-digit integers are separated if true
 *
 * @return  {string}    the value that has been separated
 */
lib.numSeparate = function(value, separators, separatethousands) {
    if(!separatethousands) separatethousands = false;

    if(typeof separators !== 'string' || separators.length === 0) {
        throw new Error('Separator string required for formatting!');
    }

    if(typeof value === 'number') {
        value = String(value);
    }

    var thousandsRe = /(\d+)(\d{3})/;
    var decimalSep = separators.charAt(0);
    var thouSep = separators.charAt(1);

    var x = value.split('.');
    var x1 = x[0];
    var x2 = x.length > 1 ? decimalSep + x[1] : '';

    // Years are ignored for thousands separators
    if(thouSep && (x.length > 1 || x1.length > 4 || separatethousands)) {
        while(thousandsRe.test(x1)) {
            x1 = x1.replace(thousandsRe, '$1' + thouSep + '$2');
        }
    }

    return x1 + x2;
};

lib.TEMPLATE_STRING_REGEX = /%{([^\s%{}:]*)(:[^}]*)?}/g;
var SIMPLE_PROPERTY_REGEX = /^\w*$/;

/**
 * Substitute values from an object into a string
 *
 * Examples:
 *  Lib.templateString('name: %{trace}', {trace: 'asdf'}) --> 'name: asdf'
 *  Lib.templateString('name: %{trace[0].name}', {trace: [{name: 'asdf'}]}) --> 'name: asdf'
 *
 * @param {string}  input string containing %{...} template strings
 * @param {obj}     data object containing substitution values
 *
 * @return {string} templated string
 */
lib.templateString = function(string, obj) {
    // Not all that useful, but cache nestedProperty instantiation
    // just in case it speeds things up *slightly*:
    var getterCache = {};

    return string.replace(lib.TEMPLATE_STRING_REGEX, function(dummy, key) {
        if(SIMPLE_PROPERTY_REGEX.test(key)) {
            return obj[key] || '';
        }
        getterCache[key] = getterCache[key] || lib.nestedProperty(obj, key).get;
        return getterCache[key]() || '';
    });
};

var TEMPLATE_STRING_FORMAT_SEPARATOR = /^:/;
var numberOfHoverTemplateWarnings = 0;
var maximumNumberOfHoverTemplateWarnings = 10;
/**
 * Substitute values from an object into a string and optionally formats them using d3-format,
 * or fallback to associated labels.
 *
 * Examples:
 *  Lib.hovertemplateString('name: %{trace}', {trace: 'asdf'}) --> 'name: asdf'
 *  Lib.hovertemplateString('name: %{trace[0].name}', {trace: [{name: 'asdf'}]}) --> 'name: asdf'
 *  Lib.hovertemplateString('price: %{y:$.2f}', {y: 1}) --> 'price: $1.00'
 *
 * @param {obj}     d3 locale
 * @param {string}  input string containing %{...:...} template strings
 * @param {obj}     data object containing fallback text when no formatting is specified, ex.: {yLabel: 'formattedYValue'}
 * @param {obj}     data objects containing substitution values
 *
 * @return {string} templated string
 */
lib.hovertemplateString = function(string, labels, d3locale) {
    var args = arguments;
    // Not all that useful, but cache nestedProperty instantiation
    // just in case it speeds things up *slightly*:
    var getterCache = {};

    return string.replace(lib.TEMPLATE_STRING_REGEX, function(match, key, format) {
        var obj, value, i;
        for(i = 3; i < args.length; i++) {
            obj = args[i];
            if(obj.hasOwnProperty(key)) {
                value = obj[key];
                break;
            }

            if(!SIMPLE_PROPERTY_REGEX.test(key)) {
                value = getterCache[key] || lib.nestedProperty(obj, key).get();
                if(value) getterCache[key] = value;
            }
            if(value !== undefined) break;
        }

        if(value === undefined) {
            if(numberOfHoverTemplateWarnings < maximumNumberOfHoverTemplateWarnings) {
                lib.warn('Variable \'' + key + '\' in hovertemplate could not be found!');
                value = match;
            }

            if(numberOfHoverTemplateWarnings === maximumNumberOfHoverTemplateWarnings) {
                lib.warn('Too many hovertemplate warnings - additional warnings will be suppressed');
            }
            numberOfHoverTemplateWarnings++;
        }

        if(format) {
            var fmt;
            if(d3locale) {
                fmt = d3locale.numberFormat;
            } else {
                fmt = d3.format;
            }
            value = fmt(format.replace(TEMPLATE_STRING_FORMAT_SEPARATOR, ''))(value);
        } else {
            if(labels.hasOwnProperty(key + 'Label')) value = labels[key + 'Label'];
        }
        return value;
    });
};

/*
 * alphanumeric string sort, tailored for subplot IDs like scene2, scene10, x10y13 etc
 */
var char0 = 48;
var char9 = 57;
lib.subplotSort = function(a, b) {
    var l = Math.min(a.length, b.length) + 1;
    var numA = 0;
    var numB = 0;
    for(var i = 0; i < l; i++) {
        var charA = a.charCodeAt(i) || 0;
        var charB = b.charCodeAt(i) || 0;
        var isNumA = charA >= char0 && charA <= char9;
        var isNumB = charB >= char0 && charB <= char9;

        if(isNumA) numA = 10 * numA + charA - char0;
        if(isNumB) numB = 10 * numB + charB - char0;

        if(!isNumA || !isNumB) {
            if(numA !== numB) return numA - numB;
            if(charA !== charB) return charA - charB;
        }
    }
    return numB - numA;
};

// repeatable pseudorandom generator
var randSeed = 2000000000;

lib.seedPseudoRandom = function() {
    randSeed = 2000000000;
};

lib.pseudoRandom = function() {
    var lastVal = randSeed;
    randSeed = (69069 * randSeed + 1) % 4294967296;
    // don't let consecutive vals be too close together
    // gets away from really trying to be random, in favor of better local uniformity
    if(Math.abs(randSeed - lastVal) < 429496729) return lib.pseudoRandom();
    return randSeed / 4294967296;
};


/** Fill hover 'pointData' container with 'correct' hover text value
 *
 * - If trace hoverinfo contains a 'text' flag and hovertext is not set,
 *   the text elements will be seen in the hover labels.
 *
 * - If trace hoverinfo contains a 'text' flag and hovertext is set,
 *   hovertext takes precedence over text
 *   i.e. the hoverinfo elements will be seen in the hover labels
 *
 *  @param {object} calcPt
 *  @param {object} trace
 *  @param {object || array} contOut (mutated here)
 */
lib.fillText = function(calcPt, trace, contOut) {
    var fill = Array.isArray(contOut) ?
        function(v) { contOut.push(v); } :
        function(v) { contOut.text = v; };

    var htx = lib.extractOption(calcPt, trace, 'htx', 'hovertext');
    if(lib.isValidTextValue(htx)) return fill(htx);

    var tx = lib.extractOption(calcPt, trace, 'tx', 'text');
    if(lib.isValidTextValue(tx)) return fill(tx);
};

// accept all truthy values and 0 (which gets cast to '0' in the hover labels)
lib.isValidTextValue = function(v) {
    return v || v === 0;
};

lib.formatPercent = function(ratio, n) {
    n = n || 0;
    var str = (Math.round(100 * ratio * Math.pow(10, n)) * Math.pow(0.1, n)).toFixed(n) + '%';
    for(var i = 0; i < n; i++) {
        if(str.indexOf('.') !== -1) {
            str = str.replace('0%', '%');
            str = str.replace('.%', '%');
        }
    }
    return str;
};
