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

var Loggers = require('./loggers');
var mod = require('./mod').mod;

var constants = require('../constants/numerical');
var BADNUM = constants.BADNUM;
var ONEDAY = constants.ONEDAY;
var ONEHOUR = constants.ONEHOUR;
var ONEMIN = constants.ONEMIN;
var ONESEC = constants.ONESEC;
var EPOCHJD = constants.EPOCHJD;

var Registry = require('../registry');

var utcFormat = d3.time.format.utc;

var DATETIME_REGEXP = /^\s*(-?\d\d\d\d|\d\d)(-(\d?\d)(-(\d?\d)([ Tt]([01]?\d|2[0-3])(:([0-5]\d)(:([0-5]\d(\.\d+)?))?(Z|z|[+\-]\d\d:?\d\d)?)?)?)?)?\s*$/m;
// special regex for chinese calendars to support yyyy-mmi-dd etc for intercalary months
var DATETIME_REGEXP_CN = /^\s*(-?\d\d\d\d|\d\d)(-(\d?\di?)(-(\d?\d)([ Tt]([01]?\d|2[0-3])(:([0-5]\d)(:([0-5]\d(\.\d+)?))?(Z|z|[+\-]\d\d:?\d\d)?)?)?)?)?\s*$/m;

// for 2-digit years, the first year we map them onto
var YFIRST = new Date().getFullYear() - 70;

function isWorldCalendar(calendar) {
    return (
        calendar &&
        Registry.componentsRegistry.calendars &&
        typeof calendar === 'string' && calendar !== 'gregorian'
    );
}

/*
 * dateTick0: get the canonical tick for this calendar
 *
 * bool sunday is for week ticks, shift it to a Sunday.
 */
exports.dateTick0 = function(calendar, sunday) {
    if(isWorldCalendar(calendar)) {
        return sunday ?
            Registry.getComponentMethod('calendars', 'CANONICAL_SUNDAY')[calendar] :
            Registry.getComponentMethod('calendars', 'CANONICAL_TICK')[calendar];
    } else {
        return sunday ? '2000-01-02' : '2000-01-01';
    }
};

/*
 * dfltRange: for each calendar, give a valid default range
 */
exports.dfltRange = function(calendar) {
    if(isWorldCalendar(calendar)) {
        return Registry.getComponentMethod('calendars', 'DFLTRANGE')[calendar];
    } else {
        return ['2000-01-01', '2001-01-01'];
    }
};

// is an object a javascript date?
exports.isJSDate = function(v) {
    return typeof v === 'object' && v !== null && typeof v.getTime === 'function';
};

// The absolute limits of our date-time system
// This is a little weird: we use MIN_MS and MAX_MS in dateTime2ms
// but we use dateTime2ms to calculate them (after defining it!)
var MIN_MS, MAX_MS;

/**
 * dateTime2ms - turn a date object or string s into milliseconds
 * (relative to 1970-01-01, per javascript standard)
 * optional calendar (string) to use a non-gregorian calendar
 *
 * Returns BADNUM if it doesn't find a date
 *
 * strings should have the form:
 *
 *    -?YYYY-mm-dd<sep>HH:MM:SS.sss<tzInfo>?
 *
 * <sep>: space (our normal standard) or T or t (ISO-8601)
 * <tzInfo>: Z, z, or [+\-]HH:?MM and we THROW IT AWAY
 * this format comes from https://tools.ietf.org/html/rfc3339#section-5.6
 * but we allow it even with a space as the separator
 *
 * May truncate after any full field, and sss can be any length
 * even >3 digits, though javascript dates truncate to milliseconds,
 * we keep as much as javascript numeric precision can hold, but we only
 * report back up to 100 microsecond precision, because most dates support
 * this precision (close to 1970 support more, very far away support less)
 *
 * Expanded to support negative years to -9999 but you must always
 * give 4 digits, except for 2-digit positive years which we assume are
 * near the present time.
 * Note that we follow ISO 8601:2004: there *is* a year 0, which
 * is 1BC/BCE, and -1===2BC etc.
 *
 * World calendars: not all of these *have* agreed extensions to this full range,
 * if you have another calendar system but want a date range outside its validity,
 * you can use a gregorian date string prefixed with 'G' or 'g'.
 *
 * Where to cut off 2-digit years between 1900s and 2000s?
 * from http://support.microsoft.com/kb/244664:
 *   1930-2029 (the most retro of all...)
 * but in my mac chrome from eg. d=new Date(Date.parse('8/19/50')):
 *   1950-2049
 * by Java, from http://stackoverflow.com/questions/2024273/:
 *   now-80 - now+19
 * or FileMaker Pro, from
 *      http://www.filemaker.com/12help/html/add_view_data.4.21.html:
 *   now-70 - now+29
 * but python strptime etc, via
 *      http://docs.python.org/py3k/library/time.html:
 *   1969-2068 (super forward-looking, but static, not sliding!)
 *
 * lets go with now-70 to now+29, and if anyone runs into this problem
 * they can learn the hard way not to use 2-digit years, as no choice we
 * make now will cover all possibilities. mostly this will all be taken
 * care of in initial parsing, should only be an issue for hand-entered data
 * currently (2016) this range is:
 *   1946-2045
 */
exports.dateTime2ms = function(s, calendar) {
    // first check if s is a date object
    if(exports.isJSDate(s)) {
        // Convert to the UTC milliseconds that give the same
        // hours as this date has in the local timezone
        var tzOffset = s.getTimezoneOffset() * ONEMIN;
        var offsetTweak = (s.getUTCMinutes() - s.getMinutes()) * ONEMIN +
            (s.getUTCSeconds() - s.getSeconds()) * ONESEC +
            (s.getUTCMilliseconds() - s.getMilliseconds());

        if(offsetTweak) {
            var comb = 3 * ONEMIN;
            tzOffset = tzOffset - comb / 2 + mod(offsetTweak - tzOffset + comb / 2, comb);
        }
        s = Number(s) - tzOffset;
        if(s >= MIN_MS && s <= MAX_MS) return s;
        return BADNUM;
    }
    // otherwise only accept strings and numbers
    if(typeof s !== 'string' && typeof s !== 'number') return BADNUM;

    s = String(s);

    var isWorld = isWorldCalendar(calendar);

    // to handle out-of-range dates in international calendars, accept
    // 'G' as a prefix to force the built-in gregorian calendar.
    var s0 = s.charAt(0);
    if(isWorld && (s0 === 'G' || s0 === 'g')) {
        s = s.substr(1);
        calendar = '';
    }

    var isChinese = isWorld && calendar.substr(0, 7) === 'chinese';

    var match = s.match(isChinese ? DATETIME_REGEXP_CN : DATETIME_REGEXP);
    if(!match) return BADNUM;
    var y = match[1];
    var m = match[3] || '1';
    var d = Number(match[5] || 1);
    var H = Number(match[7] || 0);
    var M = Number(match[9] || 0);
    var S = Number(match[11] || 0);

    if(isWorld) {
        // disallow 2-digit years for world calendars
        if(y.length === 2) return BADNUM;
        y = Number(y);

        var cDate;
        try {
            var calInstance = Registry.getComponentMethod('calendars', 'getCal')(calendar);
            if(isChinese) {
                var isIntercalary = m.charAt(m.length - 1) === 'i';
                m = parseInt(m, 10);
                cDate = calInstance.newDate(y, calInstance.toMonthIndex(y, m, isIntercalary), d);
            } else {
                cDate = calInstance.newDate(y, Number(m), d);
            }
        } catch(e) { return BADNUM; } // Invalid ... date

        if(!cDate) return BADNUM;

        return ((cDate.toJD() - EPOCHJD) * ONEDAY) +
            (H * ONEHOUR) + (M * ONEMIN) + (S * ONESEC);
    }

    if(y.length === 2) {
        y = (Number(y) + 2000 - YFIRST) % 100 + YFIRST;
    } else y = Number(y);

    // new Date uses months from 0; subtract 1 here just so we
    // don't have to do it again during the validity test below
    m -= 1;

    // javascript takes new Date(0..99,m,d) to mean 1900-1999, so
    // to support years 0-99 we need to use setFullYear explicitly
    // Note that 2000 is a leap year.
    var date = new Date(Date.UTC(2000, m, d, H, M));
    date.setUTCFullYear(y);

    if(date.getUTCMonth() !== m) return BADNUM;
    if(date.getUTCDate() !== d) return BADNUM;

    return date.getTime() + S * ONESEC;
};

MIN_MS = exports.MIN_MS = exports.dateTime2ms('-9999');
MAX_MS = exports.MAX_MS = exports.dateTime2ms('9999-12-31 23:59:59.9999');

// is string s a date? (see above)
exports.isDateTime = function(s, calendar) {
    return (exports.dateTime2ms(s, calendar) !== BADNUM);
};

// pad a number with zeroes, to given # of digits before the decimal point
function lpad(val, digits) {
    return String(val + Math.pow(10, digits)).substr(1);
}

/**
 * Turn ms into string of the form YYYY-mm-dd HH:MM:SS.ssss
 * Crop any trailing zeros in time, except never stop right after hours
 * (we could choose to crop '-01' from date too but for now we always
 * show the whole date)
 * Optional range r is the data range that applies, also in ms.
 * If rng is big, the later parts of time will be omitted
 */
var NINETYDAYS = 90 * ONEDAY;
var THREEHOURS = 3 * ONEHOUR;
var FIVEMIN = 5 * ONEMIN;
exports.ms2DateTime = function(ms, r, calendar) {
    if(typeof ms !== 'number' || !(ms >= MIN_MS && ms <= MAX_MS)) return BADNUM;

    if(!r) r = 0;

    var msecTenths = Math.floor(mod(ms + 0.05, 1) * 10);
    var msRounded = Math.round(ms - msecTenths / 10);
    var dateStr, h, m, s, msec10, d;

    if(isWorldCalendar(calendar)) {
        var dateJD = Math.floor(msRounded / ONEDAY) + EPOCHJD;
        var timeMs = Math.floor(mod(ms, ONEDAY));
        try {
            dateStr = Registry.getComponentMethod('calendars', 'getCal')(calendar)
                .fromJD(dateJD).formatDate('yyyy-mm-dd');
        } catch(e) {
            // invalid date in this calendar - fall back to Gyyyy-mm-dd
            dateStr = utcFormat('G%Y-%m-%d')(new Date(msRounded));
        }

        // yyyy does NOT guarantee 4-digit years. YYYY mostly does, but does
        // other things for a few calendars, so we can't trust it. Just pad
        // it manually (after the '-' if there is one)
        if(dateStr.charAt(0) === '-') {
            while(dateStr.length < 11) dateStr = '-0' + dateStr.substr(1);
        } else {
            while(dateStr.length < 10) dateStr = '0' + dateStr;
        }

        // TODO: if this is faster, we could use this block for extracting
        // the time components of regular gregorian too
        h = (r < NINETYDAYS) ? Math.floor(timeMs / ONEHOUR) : 0;
        m = (r < NINETYDAYS) ? Math.floor((timeMs % ONEHOUR) / ONEMIN) : 0;
        s = (r < THREEHOURS) ? Math.floor((timeMs % ONEMIN) / ONESEC) : 0;
        msec10 = (r < FIVEMIN) ? (timeMs % ONESEC) * 10 + msecTenths : 0;
    } else {
        d = new Date(msRounded);

        dateStr = utcFormat('%Y-%m-%d')(d);

        // <90 days: add hours and minutes - never *only* add hours
        h = (r < NINETYDAYS) ? d.getUTCHours() : 0;
        m = (r < NINETYDAYS) ? d.getUTCMinutes() : 0;
        // <3 hours: add seconds
        s = (r < THREEHOURS) ? d.getUTCSeconds() : 0;
        // <5 minutes: add ms (plus one extra digit, this is msec*10)
        msec10 = (r < FIVEMIN) ? d.getUTCMilliseconds() * 10 + msecTenths : 0;
    }

    return includeTime(dateStr, h, m, s, msec10);
};

// For converting old-style milliseconds to date strings,
// we use the local timezone rather than UTC like we use
// everywhere else, both for backward compatibility and
// because that's how people mostly use javasript date objects.
// Clip one extra day off our date range though so we can't get
// thrown beyond the range by the timezone shift.
exports.ms2DateTimeLocal = function(ms) {
    if(!(ms >= MIN_MS + ONEDAY && ms <= MAX_MS - ONEDAY)) return BADNUM;

    var msecTenths = Math.floor(mod(ms + 0.05, 1) * 10);
    var d = new Date(Math.round(ms - msecTenths / 10));
    var dateStr = d3.time.format('%Y-%m-%d')(d);
    var h = d.getHours();
    var m = d.getMinutes();
    var s = d.getSeconds();
    var msec10 = d.getUTCMilliseconds() * 10 + msecTenths;

    return includeTime(dateStr, h, m, s, msec10);
};

function includeTime(dateStr, h, m, s, msec10) {
    // include each part that has nonzero data in or after it
    if(h || m || s || msec10) {
        dateStr += ' ' + lpad(h, 2) + ':' + lpad(m, 2);
        if(s || msec10) {
            dateStr += ':' + lpad(s, 2);
            if(msec10) {
                var digits = 4;
                while(msec10 % 10 === 0) {
                    digits -= 1;
                    msec10 /= 10;
                }
                dateStr += '.' + lpad(msec10, digits);
            }
        }
    }
    return dateStr;
}

// normalize date format to date string, in case it starts as
// a Date object or milliseconds
// optional dflt is the return value if cleaning fails
exports.cleanDate = function(v, dflt, calendar) {
    // let us use cleanDate to provide a missing default without an error
    if(v === BADNUM) return dflt;
    if(exports.isJSDate(v) || (typeof v === 'number' && isFinite(v))) {
        // do not allow milliseconds (old) or jsdate objects (inherently
        // described as gregorian dates) with world calendars
        if(isWorldCalendar(calendar)) {
            Loggers.error('JS Dates and milliseconds are incompatible with world calendars', v);
            return dflt;
        }

        // NOTE: if someone puts in a year as a number rather than a string,
        // this will mistakenly convert it thinking it's milliseconds from 1970
        // that is: '2012' -> Jan. 1, 2012, but 2012 -> 2012 epoch milliseconds
        v = exports.ms2DateTimeLocal(+v);
        if(!v && dflt !== undefined) return dflt;
    } else if(!exports.isDateTime(v, calendar)) {
        Loggers.error('unrecognized date', v);
        return dflt;
    }
    return v;
};

/*
 *  Date formatting for ticks and hovertext
 */

/*
 * modDateFormat: Support world calendars, and add one item to
 * d3's vocabulary:
 * %{n}f where n is the max number of digits of fractional seconds
 */
var fracMatch = /%\d?f/g;
function modDateFormat(fmt, x, formatter, calendar) {
    fmt = fmt.replace(fracMatch, function(match) {
        var digits = Math.min(+(match.charAt(1)) || 6, 6);
        var fracSecs = ((x / 1000 % 1) + 2)
            .toFixed(digits)
            .substr(2).replace(/0+$/, '') || '0';
        return fracSecs;
    });

    var d = new Date(Math.floor(x + 0.05));

    if(isWorldCalendar(calendar)) {
        try {
            fmt = Registry.getComponentMethod('calendars', 'worldCalFmt')(fmt, x, calendar);
        } catch(e) {
            return 'Invalid';
        }
    }
    return formatter(fmt)(d);
}

/*
 * formatTime: create a time string from:
 *   x: milliseconds
 *   tr: tickround ('M', 'S', or # digits)
 * only supports UTC times (where every day is 24 hours and 0 is at midnight)
 */
var MAXSECONDS = [59, 59.9, 59.99, 59.999, 59.9999];
function formatTime(x, tr) {
    var timePart = mod(x + 0.05, ONEDAY);

    var timeStr = lpad(Math.floor(timePart / ONEHOUR), 2) + ':' +
        lpad(mod(Math.floor(timePart / ONEMIN), 60), 2);

    if(tr !== 'M') {
        if(!isNumeric(tr)) tr = 0; // should only be 'S'

        /*
         * this is a weird one - and shouldn't come up unless people
         * monkey with tick0 in weird ways, but we need to do something!
         * IN PARTICULAR we had better not display garbage (see below)
         * for numbers we always round to the nearest increment of the
         * precision we're showing, and this seems like the right way to
         * handle seconds and milliseconds, as they have a decimal point
         * and people will interpret that to mean rounding like numbers.
         * but for larger increments we floor the value: it's always
         * 2013 until the ball drops on the new year. We could argue about
         * which field it is where we start rounding (should 12:08:59
         * round to 12:09 if we're stopping at minutes?) but for now I'll
         * say we round seconds but floor everything else. BUT that means
         * we need to never round up to 60 seconds, ie 23:59:60
         */
        var sec = Math.min(mod(x / ONESEC, 60), MAXSECONDS[tr]);

        var secStr = (100 + sec).toFixed(tr).substr(1);
        if(tr > 0) {
            secStr = secStr.replace(/0+$/, '').replace(/[\.]$/, '');
        }

        timeStr += ':' + secStr;
    }
    return timeStr;
}

/*
 * formatDate: turn a date into tick or hover label text.
 *
 *   x: milliseconds, the value to convert
 *   fmt: optional, an explicit format string (d3 format, even for world calendars)
 *   tr: tickround ('y', 'm', 'd', 'M', 'S', or # digits)
 *      used if no explicit fmt is provided
 *   formatter: locale-aware d3 date formatter for standard gregorian calendars
 *      should be the result of exports.getD3DateFormat(gd)
 *   calendar: optional string, the world calendar system to use
 *
 * returns the date/time as a string, potentially with the leading portion
 * on a separate line (after '\n')
 * Note that this means if you provide an explicit format which includes '\n'
 * the axis may choose to strip things after it when they don't change from
 * one tick to the next (as it does with automatic formatting)
 */
exports.formatDate = function(x, fmt, tr, formatter, calendar, extraFormat) {
    calendar = isWorldCalendar(calendar) && calendar;

    if(!fmt) {
        if(tr === 'y') fmt = extraFormat.year;
        else if(tr === 'm') fmt = extraFormat.month;
        else if(tr === 'd') {
            fmt = extraFormat.dayMonth + '\n' + extraFormat.year;
        } else {
            return formatTime(x, tr) + '\n' + modDateFormat(extraFormat.dayMonthYear, x, formatter, calendar);
        }
    }

    return modDateFormat(fmt, x, formatter, calendar);
};

/*
 * incrementMonth: make a new milliseconds value from the given one,
 * having changed the month
 *
 * special case for world calendars: multiples of 12 are treated as years,
 * even for calendar systems that don't have (always or ever) 12 months/year
 * TODO: perhaps we need a different code for year increments to support this?
 *
 * ms (number): the initial millisecond value
 * dMonth (int): the (signed) number of months to shift
 * calendar (string): the calendar system to use
 *
 * changing month does not (and CANNOT) always preserve day, since
 * months have different lengths. The worst example of this is:
 *   d = new Date(1970,0,31); d.setMonth(1) -> Feb 31 turns into Mar 3
 *
 * But we want to be able to iterate over the last day of each month,
 * regardless of what its number is.
 * So shift 3 days forward, THEN set the new month, then unshift:
 *   1/31 -> 2/28 (or 29) -> 3/31 -> 4/30 -> ...
 *
 * Note that odd behavior still exists if you start from the 26th-28th:
 *   1/28 -> 2/28 -> 3/31
 * but at least you can't shift any dates into the wrong month,
 * and ticks on these days incrementing by month would be very unusual
 */
var THREEDAYS = 3 * ONEDAY;
exports.incrementMonth = function(ms, dMonth, calendar) {
    calendar = isWorldCalendar(calendar) && calendar;

    // pull time out and operate on pure dates, then add time back at the end
    // this gives maximum precision - not that we *normally* care if we're
    // incrementing by month, but better to be safe!
    var timeMs = mod(ms, ONEDAY);
    ms = Math.round(ms - timeMs);

    if(calendar) {
        try {
            var dateJD = Math.round(ms / ONEDAY) + EPOCHJD;
            var calInstance = Registry.getComponentMethod('calendars', 'getCal')(calendar);
            var cDate = calInstance.fromJD(dateJD);

            if(dMonth % 12) calInstance.add(cDate, dMonth, 'm');
            else calInstance.add(cDate, dMonth / 12, 'y');

            return (cDate.toJD() - EPOCHJD) * ONEDAY + timeMs;
        } catch(e) {
            Loggers.error('invalid ms ' + ms + ' in calendar ' + calendar);
            // then keep going in gregorian even though the result will be 'Invalid'
        }
    }

    var y = new Date(ms + THREEDAYS);
    return y.setUTCMonth(y.getUTCMonth() + dMonth) + timeMs - THREEDAYS;
};

/*
 * findExactDates: what fraction of data is exact days, months, or years?
 *
 * data: array of millisecond values
 * calendar (string) the calendar to test against
 */
exports.findExactDates = function(data, calendar) {
    var exactYears = 0;
    var exactMonths = 0;
    var exactDays = 0;
    var blankCount = 0;
    var d;
    var di;

    var calInstance = (
        isWorldCalendar(calendar) &&
        Registry.getComponentMethod('calendars', 'getCal')(calendar)
    );

    for(var i = 0; i < data.length; i++) {
        di = data[i];

        // not date data at all
        if(!isNumeric(di)) {
            blankCount ++;
            continue;
        }

        // not an exact date
        if(di % ONEDAY) continue;

        if(calInstance) {
            try {
                d = calInstance.fromJD(di / ONEDAY + EPOCHJD);
                if(d.day() === 1) {
                    if(d.month() === 1) exactYears++;
                    else exactMonths++;
                } else exactDays++;
            } catch(e) {
                // invalid date in this calendar - ignore it here.
            }
        } else {
            d = new Date(di);
            if(d.getUTCDate() === 1) {
                if(d.getUTCMonth() === 0) exactYears++;
                else exactMonths++;
            } else exactDays++;
        }
    }
    exactMonths += exactYears;
    exactDays += exactMonths;

    var dataCount = data.length - blankCount;

    return {
        exactYears: exactYears / dataCount,
        exactMonths: exactMonths / dataCount,
        exactDays: exactDays / dataCount
    };
};
