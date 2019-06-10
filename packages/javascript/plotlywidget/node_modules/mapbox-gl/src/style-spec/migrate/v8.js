
import Reference from '../reference/v8.json';
import URL from 'url';

function getPropertyReference(propertyName) {
    for (let i = 0; i < Reference.layout.length; i++) {
        for (const key in Reference[Reference.layout[i]]) {
            if (key === propertyName) return Reference[Reference.layout[i]][key];
        }
    }
    for (let i = 0; i < Reference.paint.length; i++) {
        for (const key in Reference[Reference.paint[i]]) {
            if (key === propertyName) return Reference[Reference.paint[i]][key];
        }
    }
}

function eachSource(style, callback) {
    for (const k in style.sources) {
        callback(style.sources[k]);
    }
}

function eachLayer(style, callback) {
    for (const k in style.layers) {
        callback(style.layers[k]);
        eachLayer(style.layers[k], callback);
    }
}

function eachLayout(layer, callback) {
    for (const k in layer) {
        if (k.indexOf('layout') === 0) {
            callback(layer[k], k);
        }
    }
}

function eachPaint(layer, callback) {
    for (const k in layer) {
        if (k.indexOf('paint') === 0) {
            callback(layer[k], k);
        }
    }
}

function resolveConstant(style, value) {
    if (typeof value === 'string' && value[0] === '@') {
        return resolveConstant(style, style.constants[value]);
    } else {
        return value;
    }
}

function eachProperty(style, options, callback) {
    if (arguments.length === 2) {
        callback = options;
        options = {};
    }

    options.layout = options.layout === undefined ? true : options.layout;
    options.paint = options.paint === undefined ? true : options.paint;

    function inner(layer, properties) {
        Object.keys(properties).forEach((key) => {
            callback({
                key: key,
                value: properties[key],
                reference: getPropertyReference(key),
                set: function(x) {
                    properties[key] = x;
                }
            });
        });
    }

    eachLayer(style, (layer) => {
        if (options.paint) {
            eachPaint(layer, (paint) => {
                inner(layer, paint);
            });
        }
        if (options.layout) {
            eachLayout(layer, (layout) => {
                inner(layer, layout);
            });
        }
    });
}

function isFunction(value) {
    return Array.isArray(value.stops);
}

function renameProperty(obj, from, to) {
    obj[to] = obj[from]; delete obj[from];
}

export default function(style) {
    style.version = 8;

    // Rename properties, reverse coordinates in source and layers
    eachSource(style, (source) => {
        if (source.type === 'video' && source.url !== undefined) {
            renameProperty(source, 'url', 'urls');
        }
        if (source.type === 'video') {
            source.coordinates.forEach((coord) => {
                return coord.reverse();
            });
        }
    });

    eachLayer(style, (layer) => {
        eachLayout(layer, (layout) => {
            if (layout['symbol-min-distance'] !== undefined) {
                renameProperty(layout, 'symbol-min-distance', 'symbol-spacing');
            }
        });

        eachPaint(layer, (paint) => {
            if (paint['background-image'] !== undefined) {
                renameProperty(paint, 'background-image', 'background-pattern');
            }
            if (paint['line-image'] !== undefined) {
                renameProperty(paint, 'line-image', 'line-pattern');
            }
            if (paint['fill-image'] !== undefined) {
                renameProperty(paint, 'fill-image', 'fill-pattern');
            }
        });
    });

    // Inline Constants
    eachProperty(style, (property) => {
        const value = resolveConstant(style, property.value);

        if (isFunction(value)) {
            value.stops.forEach((stop) => {
                stop[1] = resolveConstant(style, stop[1]);
            });
        }

        property.set(value);
    });
    delete style.constants;

    eachLayer(style, (layer) => {
        // get rid of text-max-size, icon-max-size
        // turn text-size, icon-size into layout properties
        // https://github.com/mapbox/mapbox-gl-style-spec/issues/255

        eachLayout(layer, (layout) => {
            delete layout['text-max-size'];
            delete layout['icon-max-size'];
        });

        eachPaint(layer, (paint) => {
            if (paint['text-size']) {
                if (!layer.layout) layer.layout = {};
                layer.layout['text-size'] = paint['text-size'];
                delete paint['text-size'];
            }

            if (paint['icon-size']) {
                if (!layer.layout) layer.layout = {};
                layer.layout['icon-size'] = paint['icon-size'];
                delete paint['icon-size'];
            }
        });
    });

    function migrateFontstackURL(input) {
        const inputParsed = URL.parse(input);
        const inputPathnameParts = inputParsed.pathname.split('/');

        if (inputParsed.protocol !== 'mapbox:') {
            return input;

        } else if (inputParsed.hostname === 'fontstack') {
            assert(decodeURI(inputParsed.pathname) === '/{fontstack}/{range}.pbf');
            return 'mapbox://fonts/mapbox/{fontstack}/{range}.pbf';

        } else if (inputParsed.hostname === 'fonts') {
            assert(inputPathnameParts[1] === 'v1');
            assert(decodeURI(inputPathnameParts[3]) === '{fontstack}');
            assert(decodeURI(inputPathnameParts[4]) === '{range}.pbf');
            return `mapbox://fonts/${inputPathnameParts[2]}/{fontstack}/{range}.pbf`;

        } else {
            assert(false);
        }

        function assert(predicate) {
            if (!predicate) {
                throw new Error(`Invalid font url: "${input}"`);
            }
        }
    }

    if (style.glyphs) {
        style.glyphs = migrateFontstackURL(style.glyphs);
    }

    function migrateFontStack(font) {
        function splitAndTrim(string) {
            return string.split(',').map((s) => {
                return s.trim();
            });
        }

        if (Array.isArray(font)) {
            // Assume it's a previously migrated font-array.
            return font;

        } else if (typeof font === 'string') {
            return splitAndTrim(font);

        } else if (typeof font === 'object') {
            font.stops.forEach((stop) => {
                stop[1] = splitAndTrim(stop[1]);
            });
            return font;

        } else {
            throw new Error("unexpected font value");
        }
    }

    eachLayer(style, (layer) => {
        eachLayout(layer, (layout) => {
            if (layout['text-font']) {
                layout['text-font'] = migrateFontStack(layout['text-font']);
            }
        });
    });

    // Reverse order of symbol layers. This is an imperfect migration.
    //
    // The order of a symbol layer in the layers list affects two things:
    // - how it is drawn relative to other layers (like oneway arrows below bridges)
    // - the placement priority compared to other layers
    //
    // It's impossible to reverse the placement priority without breaking the draw order
    // in some cases. This migration only reverses the order of symbol layers that
    // are above all other types of layers.
    //
    // Symbol layers that are at the top of the map preserve their priority.
    // Symbol layers that are below another type (line, fill) of layer preserve their draw order.

    let firstSymbolLayer = 0;
    for (let i = style.layers.length - 1; i >= 0; i--) {
        const layer = style.layers[i];
        if (layer.type !== 'symbol') {
            firstSymbolLayer = i + 1;
            break;
        }
    }

    const symbolLayers = style.layers.splice(firstSymbolLayer);
    symbolLayers.reverse();
    style.layers = style.layers.concat(symbolLayers);

    return style;
}
