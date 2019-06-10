/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

var calendars = require('./calendars');

var Lib = require('../../lib');
var constants = require('../../constants/numerical');

var EPOCHJD = constants.EPOCHJD;
var ONEDAY = constants.ONEDAY;

var attributes = {
    valType: 'enumerated',
    values: Object.keys(calendars.calendars),
    role: 'info',
    editType: 'calc',
    dflt: 'gregorian'
};

var handleDefaults = function(contIn, contOut, attr, dflt) {
    var attrs = {};
    attrs[attr] = attributes;

    return Lib.coerce(contIn, contOut, attrs, attr, dflt);
};

var handleTraceDefaults = function(traceIn, traceOut, coords, layout) {
    for(var i = 0; i < coords.length; i++) {
        handleDefaults(traceIn, traceOut, coords[i] + 'calendar', layout.calendar);
    }
};

// each calendar needs its own default canonical tick. I would love to use
// 2000-01-01 (or even 0000-01-01) for them all but they don't necessarily
// all support either of those dates. Instead I'll use the most significant
// number they *do* support, biased toward the present day.
var CANONICAL_TICK = {
    chinese: '2000-01-01',
    coptic: '2000-01-01',
    discworld: '2000-01-01',
    ethiopian: '2000-01-01',
    hebrew: '5000-01-01',
    islamic: '1000-01-01',
    julian: '2000-01-01',
    mayan: '5000-01-01',
    nanakshahi: '1000-01-01',
    nepali: '2000-01-01',
    persian: '1000-01-01',
    jalali: '1000-01-01',
    taiwan: '1000-01-01',
    thai: '2000-01-01',
    ummalqura: '1400-01-01'
};

// Start on a Sunday - for week ticks
// Discworld and Mayan calendars don't have 7-day weeks but we're going to give them
// 7-day week ticks so start on our Sundays.
// If anyone really cares we can customize the auto tick spacings for these calendars.
var CANONICAL_SUNDAY = {
    chinese: '2000-01-02',
    coptic: '2000-01-03',
    discworld: '2000-01-03',
    ethiopian: '2000-01-05',
    hebrew: '5000-01-01',
    islamic: '1000-01-02',
    julian: '2000-01-03',
    mayan: '5000-01-01',
    nanakshahi: '1000-01-05',
    nepali: '2000-01-05',
    persian: '1000-01-01',
    jalali: '1000-01-01',
    taiwan: '1000-01-04',
    thai: '2000-01-04',
    ummalqura: '1400-01-06'
};

var DFLTRANGE = {
    chinese: ['2000-01-01', '2001-01-01'],
    coptic: ['1700-01-01', '1701-01-01'],
    discworld: ['1800-01-01', '1801-01-01'],
    ethiopian: ['2000-01-01', '2001-01-01'],
    hebrew: ['5700-01-01', '5701-01-01'],
    islamic: ['1400-01-01', '1401-01-01'],
    julian: ['2000-01-01', '2001-01-01'],
    mayan: ['5200-01-01', '5201-01-01'],
    nanakshahi: ['0500-01-01', '0501-01-01'],
    nepali: ['2000-01-01', '2001-01-01'],
    persian: ['1400-01-01', '1401-01-01'],
    jalali: ['1400-01-01', '1401-01-01'],
    taiwan: ['0100-01-01', '0101-01-01'],
    thai: ['2500-01-01', '2501-01-01'],
    ummalqura: ['1400-01-01', '1401-01-01']
};

/*
 * convert d3 templates to world-calendars templates, so our users only need
 * to know d3's specifiers. Map space padding to no padding, and unknown fields
 * to an ugly placeholder
 */
var UNKNOWN = '##';
var d3ToWorldCalendars = {
    'd': {'0': 'dd', '-': 'd'}, // 2-digit or unpadded day of month
    'e': {'0': 'd', '-': 'd'}, // alternate, always unpadded day of month
    'a': {'0': 'D', '-': 'D'}, // short weekday name
    'A': {'0': 'DD', '-': 'DD'}, // full weekday name
    'j': {'0': 'oo', '-': 'o'}, // 3-digit or unpadded day of the year
    'W': {'0': 'ww', '-': 'w'}, // 2-digit or unpadded week of the year (Monday first)
    'm': {'0': 'mm', '-': 'm'}, // 2-digit or unpadded month number
    'b': {'0': 'M', '-': 'M'}, // short month name
    'B': {'0': 'MM', '-': 'MM'}, // full month name
    'y': {'0': 'yy', '-': 'yy'}, // 2-digit year (map unpadded to zero-padded)
    'Y': {'0': 'yyyy', '-': 'yyyy'}, // 4-digit year (map unpadded to zero-padded)
    'U': UNKNOWN, // Sunday-first week of the year
    'w': UNKNOWN, // day of the week [0(sunday),6]
    // combined format, we replace the date part with the world-calendar version
    // and the %X stays there for d3 to handle with time parts
    'c': {'0': 'D M d %X yyyy', '-': 'D M d %X yyyy'},
    'x': {'0': 'mm/dd/yyyy', '-': 'mm/dd/yyyy'}
};

function worldCalFmt(fmt, x, calendar) {
    var dateJD = Math.floor((x + 0.05) / ONEDAY) + EPOCHJD;
    var cDate = getCal(calendar).fromJD(dateJD);
    var i = 0;
    var modifier, directive, directiveLen, directiveObj, replacementPart;

    while((i = fmt.indexOf('%', i)) !== -1) {
        modifier = fmt.charAt(i + 1);
        if(modifier === '0' || modifier === '-' || modifier === '_') {
            directiveLen = 3;
            directive = fmt.charAt(i + 2);
            if(modifier === '_') modifier = '-';
        } else {
            directive = modifier;
            modifier = '0';
            directiveLen = 2;
        }
        directiveObj = d3ToWorldCalendars[directive];
        if(!directiveObj) {
            i += directiveLen;
        } else {
            // code is recognized as a date part but world-calendars doesn't support it
            if(directiveObj === UNKNOWN) replacementPart = UNKNOWN;

            // format the cDate according to the translated directive
            else replacementPart = cDate.formatDate(directiveObj[modifier]);

            fmt = fmt.substr(0, i) + replacementPart + fmt.substr(i + directiveLen);
            i += replacementPart.length;
        }
    }
    return fmt;
}

// cache world calendars, so we don't have to reinstantiate
// during each date-time conversion
var allCals = {};
function getCal(calendar) {
    var calendarObj = allCals[calendar];
    if(calendarObj) return calendarObj;

    calendarObj = allCals[calendar] = calendars.instance(calendar);
    return calendarObj;
}

function makeAttrs(description) {
    return Lib.extendFlat({}, attributes, { description: description });
}

function makeTraceAttrsDescription(coord) {
    return 'Sets the calendar system to use with `' + coord + '` date data.';
}

var xAttrs = {
    xcalendar: makeAttrs(makeTraceAttrsDescription('x'))
};

var xyAttrs = Lib.extendFlat({}, xAttrs, {
    ycalendar: makeAttrs(makeTraceAttrsDescription('y'))
});

var xyzAttrs = Lib.extendFlat({}, xyAttrs, {
    zcalendar: makeAttrs(makeTraceAttrsDescription('z'))
});

var axisAttrs = makeAttrs([
    'Sets the calendar system to use for `range` and `tick0`',
    'if this is a date axis. This does not set the calendar for',
    'interpreting data on this axis, that\'s specified in the trace',
    'or via the global `layout.calendar`'
].join(' '));

module.exports = {
    moduleType: 'component',
    name: 'calendars',

    schema: {
        traces: {
            scatter: xyAttrs,
            bar: xyAttrs,
            box: xyAttrs,
            heatmap: xyAttrs,
            contour: xyAttrs,
            histogram: xyAttrs,
            histogram2d: xyAttrs,
            histogram2dcontour: xyAttrs,
            scatter3d: xyzAttrs,
            surface: xyzAttrs,
            mesh3d: xyzAttrs,
            scattergl: xyAttrs,
            ohlc: xAttrs,
            candlestick: xAttrs
        },
        layout: {
            calendar: makeAttrs([
                'Sets the default calendar system to use for interpreting and',
                'displaying dates throughout the plot.'
            ].join(' '))
        },
        subplots: {
            xaxis: {calendar: axisAttrs},
            yaxis: {calendar: axisAttrs},
            scene: {
                xaxis: {calendar: axisAttrs},
                // TODO: it's actually redundant to include yaxis and zaxis here
                // because in the scene attributes these are the same object so merging
                // into one merges into them all. However, I left them in for parity with
                // cartesian, where yaxis is unused until we Plotschema.get() when we
                // use its presence or absence to determine whether to delete attributes
                // from yaxis if they only apply to x (rangeselector/rangeslider)
                yaxis: {calendar: axisAttrs},
                zaxis: {calendar: axisAttrs}
            },
            polar: {
                radialaxis: {calendar: axisAttrs}
            }
        },
        transforms: {
            filter: {
                valuecalendar: makeAttrs([
                    'Sets the calendar system to use for `value`, if it is a date.'
                ].join(' ')),
                targetcalendar: makeAttrs([
                    'Sets the calendar system to use for `target`, if it is an',
                    'array of dates. If `target` is a string (eg *x*) we use the',
                    'corresponding trace attribute (eg `xcalendar`) if it exists,',
                    'even if `targetcalendar` is provided.'
                ].join(' '))
            }
        }
    },

    layoutAttributes: attributes,

    handleDefaults: handleDefaults,
    handleTraceDefaults: handleTraceDefaults,

    CANONICAL_SUNDAY: CANONICAL_SUNDAY,
    CANONICAL_TICK: CANONICAL_TICK,
    DFLTRANGE: DFLTRANGE,

    getCal: getCal,
    worldCalFmt: worldCalFmt
};
