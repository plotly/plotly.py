'use strict';

function _slicedToArray(arr, i) {
  return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _nonIterableRest();
}

function _toConsumableArray(arr) {
  return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _nonIterableSpread();
}

function _arrayWithoutHoles(arr) {
  if (Array.isArray(arr)) {
    for (var i = 0, arr2 = new Array(arr.length); i < arr.length; i++) arr2[i] = arr[i];

    return arr2;
  }
}

function _arrayWithHoles(arr) {
  if (Array.isArray(arr)) return arr;
}

function _iterableToArray(iter) {
  if (Symbol.iterator in Object(iter) || Object.prototype.toString.call(iter) === "[object Arguments]") return Array.from(iter);
}

function _iterableToArrayLimit(arr, i) {
  var _arr = [];
  var _n = true;
  var _d = false;
  var _e = undefined;

  try {
    for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) {
      _arr.push(_s.value);

      if (i && _arr.length === i) break;
    }
  } catch (err) {
    _d = true;
    _e = err;
  } finally {
    try {
      if (!_n && _i["return"] != null) _i["return"]();
    } finally {
      if (_d) throw _e;
    }
  }

  return _arr;
}

function _nonIterableSpread() {
  throw new TypeError("Invalid attempt to spread non-iterable instance");
}

function _nonIterableRest() {
  throw new TypeError("Invalid attempt to destructure non-iterable instance");
}

var rgba = require('color-normalize');

var getBounds = require('array-bounds');

var colorId = require('color-id');

var cluster = require('point-cluster');

var extend = require('object-assign');

var glslify = require('glslify');

var pick = require('pick-by-alias');

var updateDiff = require('update-diff');

var flatten = require('flatten-vertex-data');

var ie = require('is-iexplorer');

var f32 = require('to-float32');

var parseRect = require('parse-rect');

var scatter = Scatter;

function Scatter(regl, options) {
  var _this = this;

  if (!(this instanceof Scatter)) return new Scatter(regl, options);

  if (typeof regl === 'function') {
    if (!options) options = {};
    options.regl = regl;
  } else {
    options = regl;
    regl = null;
  }

  if (options && options.length) options.positions = options;
  regl = options.regl; // persistent variables

  var gl = regl._gl,
      paletteTexture,
      palette = [],
      paletteIds = {},
      // state
  groups = [],
      // textures for marker keys
  markerTextures = [null],
      markerCache = [null];
  var maxColors = 255,
      maxSize = 100; // direct color buffer mode
  // IE does not support palette anyways

  this.tooManyColors = ie; // texture with color palette

  paletteTexture = regl.texture({
    data: new Uint8Array(maxColors * 4),
    width: maxColors,
    height: 1,
    type: 'uint8',
    format: 'rgba',
    wrapS: 'clamp',
    wrapT: 'clamp',
    mag: 'nearest',
    min: 'nearest'
  });
  extend(this, {
    regl: regl,
    gl: gl,
    groups: groups,
    markerCache: markerCache,
    markerTextures: markerTextures,
    palette: palette,
    paletteIds: paletteIds,
    paletteTexture: paletteTexture,
    maxColors: maxColors,
    maxSize: maxSize,
    canvas: gl.canvas
  });
  this.update(options); // common shader options

  var shaderOptions = {
    uniforms: {
      pixelRatio: regl.context('pixelRatio'),
      palette: paletteTexture,
      paletteSize: function paletteSize(ctx, prop) {
        return [_this.tooManyColors ? 0 : maxColors, paletteTexture.height];
      },
      scale: regl.prop('scale'),
      scaleFract: regl.prop('scaleFract'),
      translate: regl.prop('translate'),
      translateFract: regl.prop('translateFract'),
      opacity: regl.prop('opacity'),
      marker: regl.prop('markerTexture')
    },
    attributes: {
      // FIXME: optimize these parts
      x: function x(ctx, prop) {
        return prop.xAttr || {
          buffer: prop.positionBuffer,
          stride: 8,
          offset: 0
        };
      },
      y: function y(ctx, prop) {
        return prop.yAttr || {
          buffer: prop.positionBuffer,
          stride: 8,
          offset: 4
        };
      },
      xFract: function xFract(ctx, prop) {
        return prop.xAttr ? {
          constant: [0, 0]
        } : {
          buffer: prop.positionFractBuffer,
          stride: 8,
          offset: 0
        };
      },
      yFract: function yFract(ctx, prop) {
        return prop.yAttr ? {
          constant: [0, 0]
        } : {
          buffer: prop.positionFractBuffer,
          stride: 8,
          offset: 4
        };
      },
      size: function size(ctx, prop) {
        return prop.size.length ? {
          buffer: prop.sizeBuffer,
          stride: 2,
          offset: 0
        } : {
          constant: [Math.round(prop.size * 255 / _this.maxSize)]
        };
      },
      borderSize: function borderSize(ctx, prop) {
        return prop.borderSize.length ? {
          buffer: prop.sizeBuffer,
          stride: 2,
          offset: 1
        } : {
          constant: [Math.round(prop.borderSize * 255 / _this.maxSize)]
        };
      },
      colorId: function colorId(ctx, prop) {
        return prop.color.length ? {
          buffer: prop.colorBuffer,
          stride: _this.tooManyColors ? 8 : 4,
          offset: 0
        } : {
          constant: _this.tooManyColors ? palette.slice(prop.color * 4, prop.color * 4 + 4) : [prop.color]
        };
      },
      borderColorId: function borderColorId(ctx, prop) {
        return prop.borderColor.length ? {
          buffer: prop.colorBuffer,
          stride: _this.tooManyColors ? 8 : 4,
          offset: _this.tooManyColors ? 4 : 2
        } : {
          constant: _this.tooManyColors ? palette.slice(prop.borderColor * 4, prop.borderColor * 4 + 4) : [prop.borderColor]
        };
      },
      isActive: function isActive(ctx, prop) {
        return prop.activation === true ? {
          constant: [1]
        } : prop.activation ? prop.activation : {
          constant: [0]
        };
      }
    },
    blend: {
      enable: true,
      color: [0, 0, 0, 1],
      // photoshop blending
      func: {
        srcRGB: 'src alpha',
        dstRGB: 'one minus src alpha',
        srcAlpha: 'one minus dst alpha',
        dstAlpha: 'one'
      }
    },
    scissor: {
      enable: true,
      box: regl.prop('viewport')
    },
    viewport: regl.prop('viewport'),
    stencil: {
      enable: false
    },
    depth: {
      enable: false
    },
    elements: regl.prop('elements'),
    count: regl.prop('count'),
    offset: regl.prop('offset'),
    primitive: 'points' // draw sdf-marker

  };
  var markerOptions = extend({}, shaderOptions);
  markerOptions.frag = glslify(["precision highp float;\n#define GLSLIFY 1\n\nvarying vec4 fragColor, fragBorderColor;\nvarying float fragWidth, fragBorderColorLevel, fragColorLevel;\n\nuniform sampler2D marker;\nuniform float pixelRatio, opacity;\n\nfloat smoothStep(float x, float y) {\n  return 1.0 / (1.0 + exp(50.0*(x - y)));\n}\n\nvoid main() {\n  float dist = texture2D(marker, gl_PointCoord).r, delta = fragWidth;\n\n  // max-distance alpha\n  if (dist < 0.003) discard;\n\n  // null-border case\n  if (fragBorderColorLevel == fragColorLevel || fragBorderColor.a == 0.) {\n    float colorAmt = smoothstep(.5 - delta, .5 + delta, dist);\n    gl_FragColor = vec4(fragColor.rgb, colorAmt * fragColor.a * opacity);\n  }\n  else {\n    float borderColorAmt = smoothstep(fragBorderColorLevel - delta, fragBorderColorLevel + delta, dist);\n    float colorAmt = smoothstep(fragColorLevel - delta, fragColorLevel + delta, dist);\n\n    vec4 color = fragBorderColor;\n    color.a *= borderColorAmt;\n    color = mix(color, fragColor, colorAmt);\n    color.a *= opacity;\n\n    gl_FragColor = color;\n  }\n\n}\n"]);
  markerOptions.vert = glslify(["precision highp float;\n#define GLSLIFY 1\n\nattribute float x, y, xFract, yFract;\nattribute float size, borderSize;\nattribute vec4 colorId, borderColorId;\nattribute float isActive;\n\nuniform vec2 scale, scaleFract, translate, translateFract, paletteSize;\nuniform float pixelRatio;\nuniform sampler2D palette;\n\nconst float maxSize = 100.;\nconst float borderLevel = .5;\n\nvarying vec4 fragColor, fragBorderColor;\nvarying float fragPointSize, fragBorderRadius, fragWidth, fragBorderColorLevel, fragColorLevel;\n\nbool isDirect = (paletteSize.x < 1.);\n\nvec4 getColor(vec4 id) {\n  return isDirect ? id / 255. : texture2D(palette,\n    vec2(\n      (id.x + .5) / paletteSize.x,\n      (id.y + .5) / paletteSize.y\n    )\n  );\n}\n\nvoid main() {\n  if (isActive == 0.) return;\n\n  vec2 position = vec2(x, y);\n  vec2 positionFract = vec2(xFract, yFract);\n\n  vec4 color = getColor(colorId);\n  vec4 borderColor = getColor(borderColorId);\n\n  float size = size * maxSize / 255.;\n  float borderSize = borderSize * maxSize / 255.;\n\n  gl_PointSize = 2. * size * pixelRatio;\n  fragPointSize = size * pixelRatio;\n\n  vec2 pos = (position + translate) * scale\n      + (positionFract + translateFract) * scale\n      + (position + translate) * scaleFract\n      + (positionFract + translateFract) * scaleFract;\n\n  gl_Position = vec4(pos * 2. - 1., 0, 1);\n\n  fragColor = color;\n  fragBorderColor = borderColor;\n  fragWidth = 1. / gl_PointSize;\n\n  fragBorderColorLevel = clamp(borderLevel - borderLevel * borderSize / size, 0., 1.);\n  fragColorLevel = clamp(borderLevel + (1. - borderLevel) * borderSize / size, 0., 1.);\n}"]);
  this.drawMarker = regl(markerOptions); // draw circle

  var circleOptions = extend({}, shaderOptions);
  circleOptions.frag = glslify(["precision highp float;\n#define GLSLIFY 1\n\nvarying vec4 fragColor, fragBorderColor;\n\nuniform float opacity;\nvarying float fragBorderRadius, fragWidth;\n\nfloat smoothStep(float edge0, float edge1, float x) {\n\tfloat t;\n\tt = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0);\n\treturn t * t * (3.0 - 2.0 * t);\n}\n\nvoid main() {\n\tfloat radius, alpha = 1.0, delta = fragWidth;\n\n\tradius = length(2.0 * gl_PointCoord.xy - 1.0);\n\n\tif (radius > 1.0 + delta) {\n\t\tdiscard;\n\t}\n\n\talpha -= smoothstep(1.0 - delta, 1.0 + delta, radius);\n\n\tfloat borderRadius = fragBorderRadius;\n\tfloat ratio = smoothstep(borderRadius - delta, borderRadius + delta, radius);\n\tvec4 color = mix(fragColor, fragBorderColor, ratio);\n\tcolor.a *= alpha * opacity;\n\tgl_FragColor = color;\n}\n"]);
  circleOptions.vert = glslify(["precision highp float;\n#define GLSLIFY 1\n\nattribute float x, y, xFract, yFract;\nattribute float size, borderSize;\nattribute vec4 colorId, borderColorId;\nattribute float isActive;\n\nuniform vec2 scale, scaleFract, translate, translateFract;\nuniform float pixelRatio;\nuniform sampler2D palette;\nuniform vec2 paletteSize;\n\nconst float maxSize = 100.;\n\nvarying vec4 fragColor, fragBorderColor;\nvarying float fragBorderRadius, fragWidth;\n\nbool isDirect = (paletteSize.x < 1.);\n\nvec4 getColor(vec4 id) {\n  return isDirect ? id / 255. : texture2D(palette,\n    vec2(\n      (id.x + .5) / paletteSize.x,\n      (id.y + .5) / paletteSize.y\n    )\n  );\n}\n\nvoid main() {\n  // ignore inactive points\n  if (isActive == 0.) return;\n\n  vec2 position = vec2(x, y);\n  vec2 positionFract = vec2(xFract, yFract);\n\n  vec4 color = getColor(colorId);\n  vec4 borderColor = getColor(borderColorId);\n\n  float size = size * maxSize / 255.;\n  float borderSize = borderSize * maxSize / 255.;\n\n  gl_PointSize = (size + borderSize) * pixelRatio;\n\n  vec2 pos = (position + translate) * scale\n      + (positionFract + translateFract) * scale\n      + (position + translate) * scaleFract\n      + (positionFract + translateFract) * scaleFract;\n\n  gl_Position = vec4(pos * 2. - 1., 0, 1);\n\n  fragBorderRadius = 1. - 2. * borderSize / (size + borderSize);\n  fragColor = color;\n  fragBorderColor = borderColor.a == 0. || borderSize == 0. ? vec4(color.rgb, 0.) : borderColor;\n  fragWidth = 1. / gl_PointSize;\n}\n"]); // polyfill IE

  if (ie) {
    circleOptions.frag = circleOptions.frag.replace('smoothstep', 'smoothStep');
    markerOptions.frag = markerOptions.frag.replace('smoothstep', 'smoothStep');
  }

  this.drawCircle = regl(circleOptions);
} // single pass defaults


Scatter.defaults = {
  color: 'black',
  borderColor: 'transparent',
  borderSize: 0,
  size: 12,
  opacity: 1,
  marker: undefined,
  viewport: null,
  range: null,
  pixelSize: null,
  count: 0,
  offset: 0,
  bounds: null,
  positions: [],
  snap: 1e4 // update & redraw

};

Scatter.prototype.render = function () {
  if (arguments.length) {
    this.update.apply(this, arguments);
  }

  this.draw();
  return this;
}; // draw all groups or only indicated ones


Scatter.prototype.draw = function () {
  var _this2 = this;

  for (var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++) {
    args[_key] = arguments[_key];
  }

  var groups = this.groups; // if directly array passed - treat as passes

  if (args.length === 1 && Array.isArray(args[0]) && (args[0][0] === null || Array.isArray(args[0][0]))) {
    args = args[0];
  } // FIXME: remove once https://github.com/regl-project/regl/issues/474 resolved


  this.regl._refresh();

  if (args.length) {
    for (var i = 0; i < args.length; i++) {
      this.drawItem(i, args[i]);
    }
  } // draw all passes
  else {
      groups.forEach(function (group, i) {
        _this2.drawItem(i);
      });
    }

  return this;
}; // draw specific scatter group


Scatter.prototype.drawItem = function (id, els) {
  var groups = this.groups;
  var group = groups[id]; // debug viewport
  // let { viewport } = group
  // gl.enable(gl.SCISSOR_TEST);
  // gl.scissor(viewport.x, viewport.y, viewport.width, viewport.height);
  // gl.clearColor(0, 0, 0, .5);
  // gl.clear(gl.COLOR_BUFFER_BIT);

  if (typeof els === 'number') {
    id = els;
    group = groups[els];
    els = null;
  }

  if (!(group && group.count && group.opacity)) return; // draw circles

  if (group.activation[0]) {
    // TODO: optimize this performance by making groups and regl.this props
    this.drawCircle(this.getMarkerDrawOptions(0, group, els));
  } // draw all other available markers


  var batch = [];

  for (var i = 1; i < group.activation.length; i++) {
    if (!group.activation[i] || group.activation[i] !== true && !group.activation[i].data.length) continue;
    batch.push.apply(batch, _toConsumableArray(this.getMarkerDrawOptions(i, group, els)));
  }

  if (batch.length) {
    this.drawMarker(batch);
  }
}; // get options for the marker ids


Scatter.prototype.getMarkerDrawOptions = function (markerId, group, elements) {
  var range = group.range,
      tree = group.tree,
      viewport = group.viewport,
      activation = group.activation,
      selectionBuffer = group.selectionBuffer,
      count = group.count;
  var regl = this.regl; // direct points

  if (!tree) {
    // if elements array - draw unclustered points
    if (elements) {
      return [extend({}, group, {
        markerTexture: this.markerTextures[markerId],
        activation: activation[markerId],
        count: elements.length,
        elements: elements,
        offset: 0
      })];
    }

    return [extend({}, group, {
      markerTexture: this.markerTextures[markerId],
      activation: activation[markerId],
      offset: 0
    })];
  } // clustered points


  var batch = [];
  var lod = tree.range(range, {
    lod: true,
    px: [(range[2] - range[0]) / viewport.width, (range[3] - range[1]) / viewport.height]
  }); // enable elements by using selection buffer

  if (elements) {
    var markerActivation = activation[markerId];
    var mask = markerActivation.data;
    var data = new Uint8Array(count);

    for (var i = 0; i < elements.length; i++) {
      var id = elements[i];
      data[id] = mask ? mask[id] : 1;
    }

    selectionBuffer.subdata(data);
  }

  for (var l = lod.length; l--;) {
    var _lod$l = _slicedToArray(lod[l], 2),
        from = _lod$l[0],
        to = _lod$l[1];

    batch.push(extend({}, group, {
      markerTexture: this.markerTextures[markerId],
      activation: elements ? selectionBuffer : activation[markerId],
      offset: from,
      count: to - from
    }));
  }

  return batch;
}; // update groups options


Scatter.prototype.update = function () {
  var _this3 = this;

  for (var _len2 = arguments.length, args = new Array(_len2), _key2 = 0; _key2 < _len2; _key2++) {
    args[_key2] = arguments[_key2];
  }

  if (!args.length) return; // passes are as single array

  if (args.length === 1 && Array.isArray(args[0])) args = args[0];
  var groups = this.groups,
      gl = this.gl,
      regl = this.regl,
      maxSize = this.maxSize,
      maxColors = this.maxColors,
      palette = this.palette;
  this.groups = groups = args.map(function (options, i) {
    var group = groups[i];
    if (options === undefined) return group;
    if (options === null) options = {
      positions: null
    };else if (typeof options === 'function') options = {
      ondraw: options
    };else if (typeof options[0] === 'number') options = {
      positions: options // copy options to avoid mutation & handle aliases

    };
    options = pick(options, {
      positions: 'positions data points',
      snap: 'snap cluster lod tree',
      size: 'sizes size radius',
      borderSize: 'borderSizes borderSize border-size bordersize borderWidth borderWidths border-width borderwidth stroke-width strokeWidth strokewidth outline',
      color: 'colors color fill fill-color fillColor',
      borderColor: 'borderColors borderColor stroke stroke-color strokeColor',
      marker: 'markers marker shape',
      range: 'range dataBox databox',
      viewport: 'viewport viewPort viewBox viewbox',
      opacity: 'opacity alpha transparency',
      bounds: 'bound bounds boundaries limits',
      tooManyColors: 'tooManyColors palette paletteMode optimizePalette enablePalette'
    });
    if (options.positions === null) options.positions = [];
    if (options.tooManyColors != null) _this3.tooManyColors = options.tooManyColors;

    if (!group) {
      groups[i] = group = {
        id: i,
        scale: null,
        translate: null,
        scaleFract: null,
        translateFract: null,
        // buffers for active markers
        activation: [],
        // buffer for filtered markers
        selectionBuffer: regl.buffer({
          data: new Uint8Array(0),
          usage: 'stream',
          type: 'uint8'
        }),
        // buffers with data: it is faster to switch them per-pass
        // than provide one congregate buffer
        sizeBuffer: regl.buffer({
          data: new Uint8Array(0),
          usage: 'dynamic',
          type: 'uint8'
        }),
        colorBuffer: regl.buffer({
          data: new Uint8Array(0),
          usage: 'dynamic',
          type: 'uint8'
        }),
        positionBuffer: regl.buffer({
          data: new Uint8Array(0),
          usage: 'dynamic',
          type: 'float'
        }),
        positionFractBuffer: regl.buffer({
          data: new Uint8Array(0),
          usage: 'dynamic',
          type: 'float'
        })
      };
      options = extend({}, Scatter.defaults, options);
    } // force update triggers


    if (options.positions && !('marker' in options)) {
      options.marker = group.marker;
      delete group.marker;
    } // updating markers cause recalculating snapping


    if (options.marker && !('positions' in options)) {
      options.positions = group.positions;
      delete group.positions;
    } // global count of points


    var hasSize = 0,
        hasColor = 0;
    updateDiff(group, options, [{
      snap: true,
      size: function size(s, group) {
        if (s == null) s = Scatter.defaults.size;
        hasSize += s && s.length ? 1 : 0;
        return s;
      },
      borderSize: function borderSize(s, group) {
        if (s == null) s = Scatter.defaults.borderSize;
        hasSize += s && s.length ? 1 : 0;
        return s;
      },
      opacity: parseFloat,
      // add colors to palette, save references
      color: function color(c, group) {
        if (c == null) c = Scatter.defaults.color;
        c = _this3.updateColor(c);
        hasColor++;
        return c;
      },
      borderColor: function borderColor(c, group) {
        if (c == null) c = Scatter.defaults.borderColor;
        c = _this3.updateColor(c);
        hasColor++;
        return c;
      },
      bounds: function bounds(_bounds, group, options) {
        if (!('range' in options)) options.range = null;
        return _bounds;
      },
      positions: function positions(_positions, group, options) {
        var snap = group.snap;
        var positionBuffer = group.positionBuffer,
            positionFractBuffer = group.positionFractBuffer,
            selectionBuffer = group.selectionBuffer; // separate buffers for x/y coordinates

        if (_positions.x || _positions.y) {
          if (_positions.x.length) {
            group.xAttr = {
              buffer: regl.buffer(_positions.x),
              offset: 0,
              stride: 4,
              count: _positions.x.length
            };
          } else {
            group.xAttr = {
              buffer: _positions.x.buffer,
              offset: _positions.x.offset * 4 || 0,
              stride: (_positions.x.stride || 1) * 4,
              count: _positions.x.count
            };
          }

          if (_positions.y.length) {
            group.yAttr = {
              buffer: regl.buffer(_positions.y),
              offset: 0,
              stride: 4,
              count: _positions.y.length
            };
          } else {
            group.yAttr = {
              buffer: _positions.y.buffer,
              offset: _positions.y.offset * 4 || 0,
              stride: (_positions.y.stride || 1) * 4,
              count: _positions.y.count
            };
          }

          group.count = Math.max(group.xAttr.count, group.yAttr.count);
          return _positions;
        }

        _positions = flatten(_positions, 'float64');
        var count = group.count = Math.floor(_positions.length / 2);
        var bounds = group.bounds = count ? getBounds(_positions, 2) : null; // if range is not provided updated - recalc it

        if (!options.range && !group.range) {
          delete group.range;
          options.range = bounds;
        } // reset marker


        if (!options.marker && !group.marker) {
          delete group.marker;
          options.marker = null;
        } // build cluster tree if required


        if (snap && (snap === true || count > snap)) {
          group.tree = cluster(_positions, {
            bounds: bounds
          });
        } // existing tree instance
        else if (snap && snap.length) {
            group.tree = snap;
          }

        if (group.tree) {
          var opts = {
            primitive: 'points',
            usage: 'static',
            data: group.tree,
            type: 'uint32'
          };
          if (group.elements) group.elements(opts);else group.elements = regl.elements(opts);
        } // update position buffers


        positionBuffer({
          data: f32.float(_positions),
          usage: 'dynamic'
        });
        positionFractBuffer({
          data: f32.fract(_positions),
          usage: 'dynamic'
        }); // expand selectionBuffer

        selectionBuffer({
          data: new Uint8Array(count),
          type: 'uint8',
          usage: 'stream'
        });
        return _positions;
      }
    }, {
      // create marker ids corresponding to known marker textures
      marker: function marker(markers, group, options) {
        var activation = group.activation; // reset marker elements

        activation.forEach(function (buffer) {
          return buffer && buffer.destroy && buffer.destroy();
        });
        activation.length = 0; // single sdf marker

        if (!markers || typeof markers[0] === 'number') {
          var id = _this3.addMarker(markers);

          activation[id] = true;
        } // per-point markers use mask buffers to enable markers in vert shader
        else {
            var markerMasks = [];

            for (var _i = 0, l = Math.min(markers.length, group.count); _i < l; _i++) {
              var _id = _this3.addMarker(markers[_i]);

              if (!markerMasks[_id]) markerMasks[_id] = new Uint8Array(group.count); // enable marker by default

              markerMasks[_id][_i] = 1;
            }

            for (var _id2 = 0; _id2 < markerMasks.length; _id2++) {
              if (!markerMasks[_id2]) continue;
              var opts = {
                data: markerMasks[_id2],
                type: 'uint8',
                usage: 'static'
              };

              if (!activation[_id2]) {
                activation[_id2] = regl.buffer(opts);
              } else {
                activation[_id2](opts);
              }

              activation[_id2].data = markerMasks[_id2];
            }
          }

        return markers;
      },
      range: function range(_range, group, options) {
        var bounds = group.bounds; // FIXME: why do we need this?

        if (!bounds) return;
        if (!_range) _range = bounds;
        group.scale = [1 / (_range[2] - _range[0]), 1 / (_range[3] - _range[1])];
        group.translate = [-_range[0], -_range[1]];
        group.scaleFract = f32.fract(group.scale);
        group.translateFract = f32.fract(group.translate);
        return _range;
      },
      viewport: function viewport(vp) {
        var rect = parseRect(vp || [gl.drawingBufferWidth, gl.drawingBufferHeight]); // normalize viewport to the canvas coordinates
        // rect.y = gl.drawingBufferHeight - rect.height - rect.y

        return rect;
      }
    }]); // update size buffer, if needed

    if (hasSize) {
      var _group = group,
          count = _group.count,
          size = _group.size,
          borderSize = _group.borderSize,
          sizeBuffer = _group.sizeBuffer;
      var sizes = new Uint8Array(count * 2);

      if (size.length || borderSize.length) {
        for (var _i2 = 0; _i2 < count; _i2++) {
          // we downscale size to allow for fractions
          sizes[_i2 * 2] = Math.round((size[_i2] == null ? size : size[_i2]) * 255 / maxSize);
          sizes[_i2 * 2 + 1] = Math.round((borderSize[_i2] == null ? borderSize : borderSize[_i2]) * 255 / maxSize);
        }
      }

      sizeBuffer({
        data: sizes,
        usage: 'dynamic'
      });
    } // update color buffer if needed


    if (hasColor) {
      var _group2 = group,
          _count = _group2.count,
          color = _group2.color,
          borderColor = _group2.borderColor,
          colorBuffer = _group2.colorBuffer;
      var colors; // if too many colors - put colors to buffer directly

      if (_this3.tooManyColors) {
        if (color.length || borderColor.length) {
          colors = new Uint8Array(_count * 8);

          for (var _i3 = 0; _i3 < _count; _i3++) {
            var _colorId = color[_i3];
            colors[_i3 * 8] = palette[_colorId * 4];
            colors[_i3 * 8 + 1] = palette[_colorId * 4 + 1];
            colors[_i3 * 8 + 2] = palette[_colorId * 4 + 2];
            colors[_i3 * 8 + 3] = palette[_colorId * 4 + 3];
            var borderColorId = borderColor[_i3];
            colors[_i3 * 8 + 4] = palette[borderColorId * 4];
            colors[_i3 * 8 + 5] = palette[borderColorId * 4 + 1];
            colors[_i3 * 8 + 6] = palette[borderColorId * 4 + 2];
            colors[_i3 * 8 + 7] = palette[borderColorId * 4 + 3];
          }
        }
      } // if limited amount of colors - keep palette color picking
      // that saves significant memory
      else {
          if (color.length || borderColor.length) {
            // we need slight data increase by 2 due to vec4 borderId in shader
            colors = new Uint8Array(_count * 4 + 2);

            for (var _i4 = 0; _i4 < _count; _i4++) {
              // put color coords in palette texture
              if (color[_i4] != null) {
                colors[_i4 * 4] = color[_i4] % maxColors;
                colors[_i4 * 4 + 1] = Math.floor(color[_i4] / maxColors);
              }

              if (borderColor[_i4] != null) {
                colors[_i4 * 4 + 2] = borderColor[_i4] % maxColors;
                colors[_i4 * 4 + 3] = Math.floor(borderColor[_i4] / maxColors);
              }
            }
          }
        }

      colorBuffer({
        data: colors || new Uint8Array(0),
        type: 'uint8',
        usage: 'dynamic'
      });
    }

    return group;
  });
}; // get (and create) marker texture id


Scatter.prototype.addMarker = function (sdf) {
  var markerTextures = this.markerTextures,
      regl = this.regl,
      markerCache = this.markerCache;
  var pos = sdf == null ? 0 : markerCache.indexOf(sdf);
  if (pos >= 0) return pos; // convert sdf to 0..255 range

  var distArr;

  if (sdf instanceof Uint8Array || sdf instanceof Uint8ClampedArray) {
    distArr = sdf;
  } else {
    distArr = new Uint8Array(sdf.length);

    for (var i = 0, l = sdf.length; i < l; i++) {
      distArr[i] = sdf[i] * 255;
    }
  }

  var radius = Math.floor(Math.sqrt(distArr.length));
  pos = markerTextures.length;
  markerCache.push(sdf);
  markerTextures.push(regl.texture({
    channels: 1,
    data: distArr,
    radius: radius,
    mag: 'linear',
    min: 'linear'
  }));
  return pos;
}; // register color to palette, return it's index or list of indexes


Scatter.prototype.updateColor = function (colors) {
  var paletteIds = this.paletteIds,
      palette = this.palette,
      maxColors = this.maxColors;

  if (!Array.isArray(colors)) {
    colors = [colors];
  }

  var idx = []; // if color groups - flatten them

  if (typeof colors[0] === 'number') {
    var grouped = [];

    if (Array.isArray(colors)) {
      for (var i = 0; i < colors.length; i += 4) {
        grouped.push(colors.slice(i, i + 4));
      }
    } else {
      for (var _i5 = 0; _i5 < colors.length; _i5 += 4) {
        grouped.push(colors.subarray(_i5, _i5 + 4));
      }
    }

    colors = grouped;
  }

  for (var _i6 = 0; _i6 < colors.length; _i6++) {
    var color = colors[_i6];
    color = rgba(color, 'uint8');
    var id = colorId(color, false); // if new color - save it

    if (paletteIds[id] == null) {
      var pos = palette.length;
      paletteIds[id] = Math.floor(pos / 4);
      palette[pos] = color[0];
      palette[pos + 1] = color[1];
      palette[pos + 2] = color[2];
      palette[pos + 3] = color[3];
    }

    idx[_i6] = paletteIds[id];
  } // detect if too many colors in palette


  if (!this.tooManyColors && palette.length > maxColors * 4) this.tooManyColors = true; // limit max color

  this.updatePalette(palette); // keep static index for single-color property

  return idx.length === 1 ? idx[0] : idx;
};

Scatter.prototype.updatePalette = function (palette) {
  if (this.tooManyColors) return;
  var maxColors = this.maxColors,
      paletteTexture = this.paletteTexture;
  var requiredHeight = Math.ceil(palette.length * .25 / maxColors); // pad data

  if (requiredHeight > 1) {
    palette = palette.slice();

    for (var i = palette.length * .25 % maxColors; i < requiredHeight * maxColors; i++) {
      palette.push(0, 0, 0, 0);
    }
  } // ensure height


  if (paletteTexture.height < requiredHeight) {
    paletteTexture.resize(maxColors, requiredHeight);
  } // update full data


  paletteTexture.subimage({
    width: Math.min(palette.length * .25, maxColors),
    height: requiredHeight,
    data: palette
  }, 0, 0);
}; // remove unused stuff


Scatter.prototype.destroy = function () {
  this.groups.forEach(function (group) {
    group.sizeBuffer.destroy();
    group.positionBuffer.destroy();
    group.positionFractBuffer.destroy();
    group.colorBuffer.destroy();
    group.activation.forEach(function (b) {
      return b && b.destroy && b.destroy();
    });
    group.selectionBuffer.destroy();
    if (group.elements) group.elements.destroy();
  });
  this.groups.length = 0;
  this.paletteTexture.destroy();
  this.markerTextures.forEach(function (txt) {
    return txt && txt.destroy && txt.destroy();
  });
  return this;
};

var extend$1 = require('object-assign');

var reglScatter2d = function reglScatter2d(regl, options) {
  var scatter$$1 = new scatter(regl, options);
  var render = scatter$$1.render.bind(scatter$$1); // expose API

  extend$1(render, {
    render: render,
    update: scatter$$1.update.bind(scatter$$1),
    draw: scatter$$1.draw.bind(scatter$$1),
    destroy: scatter$$1.destroy.bind(scatter$$1),
    regl: scatter$$1.regl,
    gl: scatter$$1.gl,
    canvas: scatter$$1.gl.canvas,
    groups: scatter$$1.groups,
    markers: scatter$$1.markerCache,
    palette: scatter$$1.palette
  });
  return render;
};

module.exports = reglScatter2d;
