var path = require('path');
var fs = require('fs');
var constants = require('./util/constants');
var common = require('./util/common');

var args = process.argv.slice(2);
var argLocale = args[0];

var pathToEn = path.join(constants.pathToSrc, 'locale-en.js');
var pathToWCRegions = path.dirname(require.resolve('world-calendars/dist/regional/en-GB'));

if(!argLocale) {
    fs.readdir(pathToWCRegions, function(err, items) {
        if(err) throw err;

        items.forEach(function(item) {
            var itemLocale = item.split('.')[0];
            if(itemLocale.substr(0, 2) === 'en') {
                console.log('skipping English ' + itemLocale);
                return;
            }
            pullOneLocale(itemLocale);
        });
    });
} else {
    pullOneLocale(argLocale);
}

function pullOneLocale(locale) {
    var pathToInput = path.join(pathToWCRegions, locale + '.js');
    var pathToOutput = path.join(constants.pathToLib, 'locales', locale.toLowerCase() + '.js');

    fs.readFile(pathToInput, 'utf8', function(err, wcCode) {
        if(err) {
            throw new Error('pull_date_format failed: ' + pathToInput + ' not found');
        }

        var preStartStr = 'prototype.regionalOptions';
        var startStr = '] = {';
        var endStr = '};';

        var startIndex = wcCode.indexOf(startStr, wcCode.indexOf(preStartStr)) + startStr.length - 1;
        var endIndex = wcCode.indexOf(endStr, startIndex) + 1;

        var dataStr = wcCode.substr(startIndex, endIndex - startIndex);

        // strip out `main.substitute(Chinese)?Digits` - we don't care about the digits field for now anyway
        dataStr = dataStr.replace(/main[\.][A-Za-z]+\([^\)]*\)/g, '""');

        dataStr = cleanHTMLEntities(dataStr);
        var wcDataObj = eval('a=' + dataStr);

        fs.readFile(pathToOutput, 'utf8', function(err, existingOutputText) {
            var isNew = false;
            if(err || !existingOutputText.trim()) {
                existingOutputText = fs.readFileSync(pathToEn, 'utf8');
                isNew = true;
            }

            var outObjStartStr = 'module.exports = ';
            var outObjEndStr = '};';
            var outObjStartIndex = existingOutputText.indexOf(outObjStartStr) + outObjStartStr.length;
            var outObjEndIndex = existingOutputText.indexOf(outObjEndStr, outObjStartIndex) + 1;
            var outPrefix = existingOutputText.substr(0, outObjStartIndex);
            var outSuffix = existingOutputText.substr(outObjEndIndex);
            var objText = existingOutputText.substr(outObjStartIndex, outObjEndIndex - outObjStartIndex);
            var outObj;
            try {
                outObj = eval('a=' + objText);
            } catch(e) {
                throw new Error(locale + '--' + objText);
            }

            if(isNew) {
                outObj.name = locale;
                outObj.dictionary = {};
                outObj.format = {};
            }

            var format = outObj.format = (outObj.format || {});

            format.days = wcDataObj.dayNames;
            format.shortDays = wcDataObj.dayNamesShort;
            format.months = wcDataObj.monthNames;
            format.shortMonths = wcDataObj.monthNamesShort;
            format.date = translateDateFormat(wcDataObj.dateFormat);
            // leave out `dateTime` and `time` fields. We could include them as cmd line args later
            // for now these will get inherited from english.

            var outStr = JSON.stringify(outObj, null, 4)
                .replace(/'/g, '\\\'') // escape single quotes
                .replace(/"([A-Za-z]\w+)":/g, '$1:') // unquote simple identifier keys
                .replace(/([^\\])"/g, '$1\'') // replace unescaped doublequotes with singlequotes
                .replace(/\\"/g, '"'); // unescape escaped doublequotes

            outStr = shortenArrays(outStr);

            common.writeFile(pathToOutput, outPrefix + outStr + outSuffix, function() {
                console.log('ok pull_date_format ' + locale);
            });
        });
    });
}

/*
 * Turn HTML entities into unicode - for explicit compatibility with SVG
 * There are just a few in world-calendars that aren't already in unicode anyway.
 */
var entityMap = {
    ccedil: '\u00e7',
    auml: '\u00e4',
    '#x10C': '\u010c'
};
function cleanHTMLEntities(s) {
    return s.replace(/&([^;]+);/g, function(entity, entityID) {
        var outChar = entityMap[entityID];
        if(!outChar) {
            throw new Error('no unicode character listed for ' + entity);
        }
        return outChar;
    });
}

/*
 * Convert world-calendars date format ('dd.mm.yyyy') to d3 ('%d.%m.%Y')
 */
function translateDateFormat(wcDateFormat) {
    var out = wcDateFormat
        .replace('yyyy', '%Y')
        // bosnian (bs) uses 2-digit year in world-calendars, but I don't want to continue that!
        .replace('yy', '%Y')
        .replace('mm', '%m')
        .replace('dd', '%d')
        // gujarati (gu) uses short month name in world-calendars - keep it?
        .replace('M', '%b');

    return out;
}

/**
 * Either put the whole array on one line, split it into 2 lines,
 * or leave it as is (one line per item), whatever we can fit into 90 characters.
 * A trailing comma may still be after the 90-character limit
 */
function shortenArrays(s) {
    var maxLen = 91; // max line length plus one for the initial \n.

    return s.replace(/(\n.+\[)\n([^\]]+)\n(\s*)\]/g, function(wholeMatch, prefix, arrayStr, bracketSpaces) {
        var parts = arrayStr.trim().split(/,\n\s*/);

        var singleLine = prefix + parts.join(', ') + ']';
        if(singleLine.length <= maxLen) {
            return singleLine;
        }

        var arraySpaces = bracketSpaces + '    ';
        var splitPoint = Math.ceil(parts.length / 2);
        var line1 = arraySpaces + parts.slice(0, splitPoint).join(', ') + ',';
        var line2 = arraySpaces + parts.slice(splitPoint).join(', ');
        if(line1.length <= maxLen && line2.length <= maxLen) {
            return [prefix, line1, line2, bracketSpaces + ']'].join('\n');
        }

        return wholeMatch;
    });
}
