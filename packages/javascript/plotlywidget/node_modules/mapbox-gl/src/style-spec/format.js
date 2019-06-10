
import reference from './reference/latest.js';
import sortObject from 'sort-object';

function sameOrderAs(reference) {
    const keyOrder = {};

    Object.keys(reference).forEach((k, i) => {
        keyOrder[k] = i + 1;
    });

    return {
        sort: function (a, b) {
            return (keyOrder[a] || Infinity) -
                   (keyOrder[b] || Infinity);
        }
    };
}

/**
 * Format a Mapbox GL Style.  Returns a stringified style with its keys
 * sorted in the same order as the reference style.
 *
 * The optional `space` argument is passed to
 * [`JSON.stringify`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)
 * to generate formatted output.
 *
 * If `space` is unspecified, a default of `2` spaces will be used.
 *
 * @private
 * @param {Object} style a Mapbox GL Style
 * @param {number} [space] space argument to pass to `JSON.stringify`
 * @returns {string} stringified formatted JSON
 * @example
 * var fs = require('fs');
 * var format = require('mapbox-gl-style-spec').format;
 * var style = fs.readFileSync('./source.json', 'utf8');
 * fs.writeFileSync('./dest.json', format(style));
 * fs.writeFileSync('./dest.min.json', format(style, 0));
 */
function format(style, space) {
    if (space === undefined) space = 2;
    style = sortObject(style, sameOrderAs(reference.$root));

    if (style.layers) {
        style.layers = style.layers.map((layer) => {
            return sortObject(layer, sameOrderAs(reference.layer));
        });
    }

    return JSON.stringify(style, null, space);
}

export default format;
