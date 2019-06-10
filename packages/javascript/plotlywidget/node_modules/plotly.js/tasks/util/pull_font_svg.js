var fs = require('fs');
var xml2js = require('xml2js');

var parser = new xml2js.Parser();
var builder = new xml2js.Builder({ headless: true, rootName: 'svg', renderOpts: {'newline': ''}});

module.exports = function pullFontSVG(data, pathOut) {
    parser.parseString(data, function(err, result) {
        if(err) throw err;

        var fontObj = result.svg.defs[0].font[0];
        var defaultWidth = Number(fontObj.$['horiz-adv-x']);
        var ascent = Number(fontObj['font-face'][0].$.ascent);
        var descent = Number(fontObj['font-face'][0].$.descent);
        var chars = {};

        fontObj.glyph.forEach(function(glyph) {
            var name = glyph.$['glyph-name'];
            var transform = name === 'spikeline' ?
                'matrix(1.5 0 0 -1.5 0 ' + ascent + ')' :
                'matrix(1 0 0 -1 0 ' + ascent + ')';

            chars[name] = {
                width: Number(glyph.$['horiz-adv-x']) || defaultWidth,
                height: ascent - descent,
                path: glyph.$.d,
                transform: transform,
            };
        });

        // Load SVG
        var svgs = result.svg.defs[0].svg;
        svgs.forEach(function(svg) {
            var name = svg.$.id;
            delete svg.$.id;
            chars[name] = {
                name: name,
                svg: builder.buildObject(svg)
            };
        });

        // turn remaining double quotes into single
        var charStr = JSON.stringify(chars, null, 4).replace(/\"/g, '\'');

        var outStr = [
            '\'use strict\';',
            '',
            'module.exports = ' + charStr + ';',
            ''
        ].join('\n');

        fs.writeFile(pathOut, outStr, function(err) {
            if(err) throw err;
        });
    });
};
