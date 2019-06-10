// @flow

// We use brfs, a browserify transform, to inline shader sources during bundling. As a result:
// - readFileSync calls must be written out long-form
// - this module must use CommonJS rather than ES2015 syntax
/* eslint-disable prefer-template, no-path-concat, import/unambiguous, import/no-commonjs */

const fs = require('fs');

const shaders: {[string]: {fragmentSource: string, vertexSource: string}} = {
    prelude: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/_prelude.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/_prelude.vertex.glsl', 'utf8')
    },
    background: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/background.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/background.vertex.glsl', 'utf8')
    },
    backgroundPattern: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/background_pattern.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/background_pattern.vertex.glsl', 'utf8')
    },
    circle: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/circle.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/circle.vertex.glsl', 'utf8')
    },
    clippingMask: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/clipping_mask.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/clipping_mask.vertex.glsl', 'utf8')
    },
    heatmap: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/heatmap.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/heatmap.vertex.glsl', 'utf8')
    },
    heatmapTexture: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/heatmap_texture.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/heatmap_texture.vertex.glsl', 'utf8')
    },
    collisionBox: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/collision_box.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/collision_box.vertex.glsl', 'utf8')
    },
    collisionCircle: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/collision_circle.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/collision_circle.vertex.glsl', 'utf8')
    },
    debug: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/debug.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/debug.vertex.glsl', 'utf8')
    },
    fill: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/fill.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/fill.vertex.glsl', 'utf8')
    },
    fillOutline: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/fill_outline.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/fill_outline.vertex.glsl', 'utf8')
    },
    fillOutlinePattern: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/fill_outline_pattern.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/fill_outline_pattern.vertex.glsl', 'utf8')
    },
    fillPattern: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/fill_pattern.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/fill_pattern.vertex.glsl', 'utf8')
    },
    fillExtrusion: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/fill_extrusion.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/fill_extrusion.vertex.glsl', 'utf8')
    },
    fillExtrusionPattern: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/fill_extrusion_pattern.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/fill_extrusion_pattern.vertex.glsl', 'utf8')
    },
    extrusionTexture: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/extrusion_texture.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/extrusion_texture.vertex.glsl', 'utf8')
    },
    hillshadePrepare: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/hillshade_prepare.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/hillshade_prepare.vertex.glsl', 'utf8')
    },
    hillshade: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/hillshade.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/hillshade.vertex.glsl', 'utf8')
    },
    line: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/line.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/line.vertex.glsl', 'utf8')
    },
    lineGradient: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/line_gradient.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/line_gradient.vertex.glsl', 'utf8')
    },
    linePattern: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/line_pattern.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/line_pattern.vertex.glsl', 'utf8')
    },
    lineSDF: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/line_sdf.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/line_sdf.vertex.glsl', 'utf8')
    },
    raster: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/raster.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/raster.vertex.glsl', 'utf8')
    },
    symbolIcon: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/symbol_icon.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/symbol_icon.vertex.glsl', 'utf8')
    },
    symbolSDF: {
        fragmentSource: fs.readFileSync(__dirname + '/../shaders/symbol_sdf.fragment.glsl', 'utf8'),
        vertexSource: fs.readFileSync(__dirname + '/../shaders/symbol_sdf.vertex.glsl', 'utf8')
    }
};

// Expand #pragmas to #ifdefs.

const re = /#pragma mapbox: ([\w]+) ([\w]+) ([\w]+) ([\w]+)/g;

for (const programName in shaders) {
    const program = shaders[programName];
    const fragmentPragmas: {[string]: boolean} = {};

    program.fragmentSource = program.fragmentSource.replace(re, (match: string, operation: string, precision: string, type: string, name: string) => {
        fragmentPragmas[name] = true;
        if (operation === 'define') {
            return `
#ifndef HAS_UNIFORM_u_${name}
varying ${precision} ${type} ${name};
#else
uniform ${precision} ${type} u_${name};
#endif
`;
        } else /* if (operation === 'initialize') */ {
            return `
#ifdef HAS_UNIFORM_u_${name}
    ${precision} ${type} ${name} = u_${name};
#endif
`;
        }
    });

    program.vertexSource = program.vertexSource.replace(re, (match: string, operation: string, precision: string, type: string, name: string) => {
        const attrType = type === 'float' ? 'vec2' : 'vec4';
        if (fragmentPragmas[name]) {
            if (operation === 'define') {
                return `
#ifndef HAS_UNIFORM_u_${name}
uniform lowp float a_${name}_t;
attribute ${precision} ${attrType} a_${name};
varying ${precision} ${type} ${name};
#else
uniform ${precision} ${type} u_${name};
#endif
`;
            } else /* if (operation === 'initialize') */ {
                return `
#ifndef HAS_UNIFORM_u_${name}
    ${name} = unpack_mix_${attrType}(a_${name}, a_${name}_t);
#else
    ${precision} ${type} ${name} = u_${name};
#endif
`;
            }
        } else {
            if (operation === 'define') {
                return `
#ifndef HAS_UNIFORM_u_${name}
uniform lowp float a_${name}_t;
attribute ${precision} ${attrType} a_${name};
#else
uniform ${precision} ${type} u_${name};
#endif
`;
            } else /* if (operation === 'initialize') */ {
                return `
#ifndef HAS_UNIFORM_u_${name}
    ${precision} ${type} ${name} = unpack_mix_${attrType}(a_${name}, a_${name}_t);
#else
    ${precision} ${type} ${name} = u_${name};
#endif
`;
            }
        }
    });
}

module.exports = shaders;
