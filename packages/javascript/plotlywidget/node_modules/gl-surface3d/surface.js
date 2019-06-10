'use strict'

module.exports = createSurfacePlot

var bits = require('bit-twiddle')
var createBuffer = require('gl-buffer')
var createVAO = require('gl-vao')
var createTexture = require('gl-texture2d')
var pool = require('typedarray-pool')
var colormap = require('colormap')
var ops = require('ndarray-ops')
var pack = require('ndarray-pack')
var ndarray = require('ndarray')
var surfaceNets = require('surface-nets')
var multiply = require('gl-mat4/multiply')
var invert = require('gl-mat4/invert')
var bsearch = require('binary-search-bounds')
var gradient = require('ndarray-gradient')
var shaders = require('./lib/shaders')

var createShader = shaders.createShader
var createContourShader = shaders.createContourShader
var createPickShader = shaders.createPickShader
var createPickContourShader = shaders.createPickContourShader

var SURFACE_VERTEX_SIZE = 4 * (4 + 3 + 3)

var IDENTITY = [
  1, 0, 0, 0,
  0, 1, 0, 0,
  0, 0, 1, 0,
  0, 0, 0, 1 ]

var QUAD = [
  [0, 0],
  [0, 1],
  [1, 0],
  [1, 1],
  [1, 0],
  [0, 1]
]

var PERMUTATIONS = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

;(function () {
  for (var i = 0; i < 3; ++i) {
    var p = PERMUTATIONS[i]
    var u = (i + 1) % 3
    var v = (i + 2) % 3
    p[u + 0] = 1
    p[v + 3] = 1
    p[i + 6] = 1
  }
})()

function SurfacePickResult (position, index, uv, level, dataCoordinate) {
  this.position = position
  this.index = index
  this.uv = uv
  this.level = level
  this.dataCoordinate = dataCoordinate
}

var N_COLORS = 256

function genColormap (name) {
  var x = pack([colormap({
    colormap: name,
    nshades: N_COLORS,
    format: 'rgba'
  }).map(function (c) {
    return [c[0], c[1], c[2], 255 * c[3]]
  })])
  ops.divseq(x, 255.0)
  return x
}

function SurfacePlot (
  gl,
  shape,
  bounds,
  shader,
  pickShader,
  coordinates,
  vao,
  colorMap,
  contourShader,
  contourPickShader,
  contourBuffer,
  contourVAO,
  dynamicBuffer,
  dynamicVAO,
  objectOffset) {
  this.gl = gl
  this.shape = shape
  this.bounds = bounds
  this.objectOffset = objectOffset
  this.intensityBounds = []

  this._shader = shader
  this._pickShader = pickShader
  this._coordinateBuffer = coordinates
  this._vao = vao
  this._colorMap = colorMap

  this._contourShader = contourShader
  this._contourPickShader = contourPickShader
  this._contourBuffer = contourBuffer
  this._contourVAO = contourVAO
  this._contourOffsets = [[], [], []]
  this._contourCounts = [[], [], []]
  this._vertexCount = 0

  this._pickResult = new SurfacePickResult([0, 0, 0], [0, 0], [0, 0], [0, 0, 0], [0, 0, 0])

  this._dynamicBuffer = dynamicBuffer
  this._dynamicVAO = dynamicVAO
  this._dynamicOffsets = [0, 0, 0]
  this._dynamicCounts = [0, 0, 0]

  this.contourWidth = [ 1, 1, 1 ]
  this.contourLevels = [[1], [1], [1]]
  this.contourTint = [0, 0, 0]
  this.contourColor = [[0.5, 0.5, 0.5, 1], [0.5, 0.5, 0.5, 1], [0.5, 0.5, 0.5, 1]]

  this.showContour = true
  this.showSurface = true

  this.enableHighlight = [true, true, true]
  this.highlightColor = [[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
  this.highlightTint = [ 1, 1, 1 ]
  this.highlightLevel = [-1, -1, -1]

  // Dynamic contour options
  this.enableDynamic = [ true, true, true ]
  this.dynamicLevel = [ NaN, NaN, NaN ]
  this.dynamicColor = [ [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1] ]
  this.dynamicTint = [ 1, 1, 1 ]
  this.dynamicWidth = [ 1, 1, 1 ]

  this.axesBounds = [[Infinity, Infinity, Infinity], [-Infinity, -Infinity, -Infinity]]
  this.surfaceProject = [ false, false, false ]
  this.contourProject = [[ false, false, false ],
    [ false, false, false ],
    [ false, false, false ]]

  this.colorBounds = [ false, false ]

  // Store xyz fields, need this for picking
  this._field = [
    ndarray(pool.mallocFloat(1024), [0, 0]),
    ndarray(pool.mallocFloat(1024), [0, 0]),
    ndarray(pool.mallocFloat(1024), [0, 0]) ]

  this.pickId = 1
  this.clipBounds = [[-Infinity, -Infinity, -Infinity], [Infinity, Infinity, Infinity]]

  this.snapToData = false

  this.pixelRatio = 1

  this.opacity = 1.0

  this.lightPosition = [10, 10000, 0]
  this.ambientLight = 0.8
  this.diffuseLight = 0.8
  this.specularLight = 2.0
  this.roughness = 0.5
  this.fresnel = 1.5
  this.vertexColor = 0

  this.dirty = true
}

var proto = SurfacePlot.prototype

proto.isTransparent = function () {
  return this.opacity < 1
}

proto.isOpaque = function () {
  if (this.opacity >= 1) {
    return true
  }
  for (var i = 0; i < 3; ++i) {
    if (this._contourCounts[i].length > 0 || this._dynamicCounts[i] > 0) {
      return true
    }
  }
  return false
}

proto.pickSlots = 1

proto.setPickBase = function (id) {
  this.pickId = id
}

var ZERO_VEC = [0, 0, 0]

var PROJECT_DATA = {
  showSurface: false,
  showContour: false,
  projections: [IDENTITY.slice(), IDENTITY.slice(), IDENTITY.slice()],
  clipBounds: [
    [[0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0]]]
}

function computeProjectionData (camera, obj) {
  var i, j, k

  // Compute cube properties
  var cubeAxis = (obj.axes && obj.axes.lastCubeProps.axis) || ZERO_VEC

  var showSurface = obj.showSurface
  var showContour = obj.showContour

  for (i = 0; i < 3; ++i) {
    showSurface = showSurface || obj.surfaceProject[i]
    for (j = 0; j < 3; ++j) {
      showContour = showContour || obj.contourProject[i][j]
    }
  }

  for (i = 0; i < 3; ++i) {
    // Construct projection onto axis
    var axisSquish = PROJECT_DATA.projections[i]
    for (j = 0; j < 16; ++j) {
      axisSquish[j] = 0
    }
    for (j = 0; j < 4; ++j) {
      axisSquish[5 * j] = 1
    }
    axisSquish[5 * i] = 0
    axisSquish[12 + i] = obj.axesBounds[+(cubeAxis[i] > 0)][i]
    multiply(axisSquish, camera.model, axisSquish)

    var nclipBounds = PROJECT_DATA.clipBounds[i]
    for (k = 0; k < 2; ++k) {
      for (j = 0; j < 3; ++j) {
        nclipBounds[k][j] = camera.clipBounds[k][j]
      }
    }
    nclipBounds[0][i] = -1e8
    nclipBounds[1][i] = 1e8
  }

  PROJECT_DATA.showSurface = showSurface
  PROJECT_DATA.showContour = showContour

  return PROJECT_DATA
}

var UNIFORMS = {
  model: IDENTITY,
  view: IDENTITY,
  projection: IDENTITY,
  inverseModel: IDENTITY.slice(),
  lowerBound: [0, 0, 0],
  upperBound: [0, 0, 0],
  colorMap: 0,
  clipBounds: [[0, 0, 0], [0, 0, 0]],
  height: 0.0,
  contourTint: 0,
  contourColor: [0, 0, 0, 1],
  permutation: [1, 0, 0, 0, 1, 0, 0, 0, 1],
  zOffset: -1e-4,
  objectOffset: [0, 0, 0],
  kambient: 1,
  kdiffuse: 1,
  kspecular: 1,
  lightPosition: [1000, 1000, 1000],
  eyePosition: [0, 0, 0],
  roughness: 1,
  fresnel: 1,
  opacity: 1,
  vertexColor: 0
}

var MATRIX_INVERSE = IDENTITY.slice()
var DEFAULT_PERM = [1, 0, 0, 0, 1, 0, 0, 0, 1]

function drawCore (params, transparent) {
  params = params || {}
  var gl = this.gl

  gl.disable(gl.CULL_FACE)

  this._colorMap.bind(0)

  var uniforms = UNIFORMS
  uniforms.model = params.model || IDENTITY
  uniforms.view = params.view || IDENTITY
  uniforms.projection = params.projection || IDENTITY
  uniforms.lowerBound = [this.bounds[0][0], this.bounds[0][1], this.colorBounds[0] || this.bounds[0][2]]
  uniforms.upperBound = [this.bounds[1][0], this.bounds[1][1], this.colorBounds[1] || this.bounds[1][2]]
  uniforms.objectOffset = this.objectOffset
  uniforms.contourColor = this.contourColor[0]

  uniforms.inverseModel = invert(uniforms.inverseModel, uniforms.model)

  for (var i = 0; i < 2; ++i) {
    var clipClamped = uniforms.clipBounds[i]
    for (var j = 0; j < 3; ++j) {
      clipClamped[j] = Math.min(Math.max(this.clipBounds[i][j], -1e8), 1e8)
    }
  }

  uniforms.kambient = this.ambientLight
  uniforms.kdiffuse = this.diffuseLight
  uniforms.kspecular = this.specularLight

  uniforms.roughness = this.roughness
  uniforms.fresnel = this.fresnel
  uniforms.opacity = this.opacity

  uniforms.height = 0.0
  uniforms.permutation = DEFAULT_PERM

  uniforms.vertexColor = this.vertexColor

  // Compute camera matrix inverse
  var invCameraMatrix = MATRIX_INVERSE
  multiply(invCameraMatrix, uniforms.view, uniforms.model)
  multiply(invCameraMatrix, uniforms.projection, invCameraMatrix)
  invert(invCameraMatrix, invCameraMatrix)

  for (i = 0; i < 3; ++i) {
    uniforms.eyePosition[i] = invCameraMatrix[12 + i] / invCameraMatrix[15]
  }

  var w = invCameraMatrix[15]
  for (i = 0; i < 3; ++i) {
    w += this.lightPosition[i] * invCameraMatrix[4 * i + 3]
  }
  for (i = 0; i < 3; ++i) {
    var s = invCameraMatrix[12 + i]
    for (j = 0; j < 3; ++j) {
      s += invCameraMatrix[4 * j + i] * this.lightPosition[j]
    }
    uniforms.lightPosition[i] = s / w
  }

  var projectData = computeProjectionData(uniforms, this)

  if (projectData.showSurface && (transparent === (this.opacity < 1))) {
    // Set up uniforms
    this._shader.bind()
    this._shader.uniforms = uniforms

    // Draw it
    this._vao.bind()

    if (this.showSurface && this._vertexCount) {
      this._vao.draw(gl.TRIANGLES, this._vertexCount)
    }

    // Draw projections of surface
    for (i = 0; i < 3; ++i) {
      if (!this.surfaceProject[i] || !this.vertexCount) {
        continue
      }
      this._shader.uniforms.model = projectData.projections[i]
      this._shader.uniforms.clipBounds = projectData.clipBounds[i]
      this._vao.draw(gl.TRIANGLES, this._vertexCount)
    }

    this._vao.unbind()
  }

  if (projectData.showContour && !transparent) {
    var shader = this._contourShader

    // Don't apply lighting to contours
    uniforms.kambient = 1.0
    uniforms.kdiffuse = 0.0
    uniforms.kspecular = 0.0
    uniforms.opacity = 1.0

    shader.bind()
    shader.uniforms = uniforms

    // Draw contour lines
    var vao = this._contourVAO
    vao.bind()

    // Draw contour levels
    for (i = 0; i < 3; ++i) {
      shader.uniforms.permutation = PERMUTATIONS[i]
      gl.lineWidth(this.contourWidth[i] * this.pixelRatio)

      for (j = 0; j < this.contourLevels[i].length; ++j) {
        if (j === this.highlightLevel[i]) {
          shader.uniforms.contourColor = this.highlightColor[i]
          shader.uniforms.contourTint = this.highlightTint[i]
        } else if (j === 0 || (j - 1) === this.highlightLevel[i]) {
          shader.uniforms.contourColor = this.contourColor[i]
          shader.uniforms.contourTint = this.contourTint[i]
        }
        if (!this._contourCounts[i][j]) {
          continue
        }

        shader.uniforms.height = this.contourLevels[i][j]
        vao.draw(gl.LINES, this._contourCounts[i][j], this._contourOffsets[i][j])
      }
    }

    // Draw projections of surface
    for (i = 0; i < 3; ++i) {
      shader.uniforms.model = projectData.projections[i]
      shader.uniforms.clipBounds = projectData.clipBounds[i]
      for (j = 0; j < 3; ++j) {
        if (!this.contourProject[i][j]) {
          continue
        }
        shader.uniforms.permutation = PERMUTATIONS[j]
        gl.lineWidth(this.contourWidth[j] * this.pixelRatio)
        for (var k = 0; k < this.contourLevels[j].length; ++k) {
          if (k === this.highlightLevel[j]) {
            shader.uniforms.contourColor = this.highlightColor[j]
            shader.uniforms.contourTint = this.highlightTint[j]
          } else if (k === 0 || (k - 1) === this.highlightLevel[j]) {
            shader.uniforms.contourColor = this.contourColor[j]
            shader.uniforms.contourTint = this.contourTint[j]
          }
          if (!this._contourCounts[j][k]) {
            continue
          }

          shader.uniforms.height = this.contourLevels[j][k]
          vao.draw(gl.LINES, this._contourCounts[j][k], this._contourOffsets[j][k])
        }
      }
    }

    vao.unbind()

    // Draw dynamic contours
    vao = this._dynamicVAO
    vao.bind()

    // Draw contour levels
    for (i = 0; i < 3; ++i) {
      if (this._dynamicCounts[i] === 0) {
        continue
      }

      shader.uniforms.model = uniforms.model
      shader.uniforms.clipBounds = uniforms.clipBounds
      shader.uniforms.permutation = PERMUTATIONS[i]
      gl.lineWidth(this.dynamicWidth[i] * this.pixelRatio)

      shader.uniforms.contourColor = this.dynamicColor[i]
      shader.uniforms.contourTint = this.dynamicTint[i]
      shader.uniforms.height = this.dynamicLevel[i]
      vao.draw(gl.LINES, this._dynamicCounts[i], this._dynamicOffsets[i])

      for (j = 0; j < 3; ++j) {
        if (!this.contourProject[j][i]) {
          continue
        }

        shader.uniforms.model = projectData.projections[j]
        shader.uniforms.clipBounds = projectData.clipBounds[j]
        vao.draw(gl.LINES, this._dynamicCounts[i], this._dynamicOffsets[i])
      }
    }

    vao.unbind()
  }
}

proto.draw = function (params) {
  return drawCore.call(this, params, false)
}

proto.drawTransparent = function (params) {
  return drawCore.call(this, params, true)
}

var PICK_UNIFORMS = {
  model: IDENTITY,
  view: IDENTITY,
  projection: IDENTITY,
  inverseModel: IDENTITY,
  clipBounds: [[0, 0, 0], [0, 0, 0]],
  height: 0.0,
  shape: [0, 0],
  pickId: 0,
  lowerBound: [0, 0, 0],
  upperBound: [0, 0, 0],
  zOffset: 0.0,
  objectOffset: [0, 0, 0],
  permutation: [1, 0, 0, 0, 1, 0, 0, 0, 1],
  lightPosition: [0, 0, 0],
  eyePosition: [0, 0, 0]
}

proto.drawPick = function (params) {
  params = params || {}
  var gl = this.gl
  gl.disable(gl.CULL_FACE)

  var uniforms = PICK_UNIFORMS
  uniforms.model = params.model || IDENTITY
  uniforms.view = params.view || IDENTITY
  uniforms.projection = params.projection || IDENTITY
  uniforms.shape = this._field[2].shape
  uniforms.pickId = this.pickId / 255.0
  uniforms.lowerBound = this.bounds[0]
  uniforms.upperBound = this.bounds[1]
  uniforms.objectOffset = this.objectOffset
  uniforms.permutation = DEFAULT_PERM

  for (var i = 0; i < 2; ++i) {
    var clipClamped = uniforms.clipBounds[i]
    for (var j = 0; j < 3; ++j) {
      clipClamped[j] = Math.min(Math.max(this.clipBounds[i][j], -1e8), 1e8)
    }
  }

  var projectData = computeProjectionData(uniforms, this)

  if (projectData.showSurface) {
    // Set up uniforms
    this._pickShader.bind()
    this._pickShader.uniforms = uniforms

    // Draw it
    this._vao.bind()
    this._vao.draw(gl.TRIANGLES, this._vertexCount)

    // Draw projections of surface
    for (i = 0; i < 3; ++i) {
      if (!this.surfaceProject[i]) {
        continue
      }
      this._pickShader.uniforms.model = projectData.projections[i]
      this._pickShader.uniforms.clipBounds = projectData.clipBounds[i]
      this._vao.draw(gl.TRIANGLES, this._vertexCount)
    }

    this._vao.unbind()
  }

  if (projectData.showContour) {
    var shader = this._contourPickShader

    shader.bind()
    shader.uniforms = uniforms

    var vao = this._contourVAO
    vao.bind()

    for (j = 0; j < 3; ++j) {
      gl.lineWidth(this.contourWidth[j] * this.pixelRatio)
      shader.uniforms.permutation = PERMUTATIONS[j]
      for (i = 0; i < this.contourLevels[j].length; ++i) {
        if (this._contourCounts[j][i]) {
          shader.uniforms.height = this.contourLevels[j][i]
          vao.draw(gl.LINES, this._contourCounts[j][i], this._contourOffsets[j][i])
        }
      }
    }

    // Draw projections of surface
    for (i = 0; i < 3; ++i) {
      shader.uniforms.model = projectData.projections[i]
      shader.uniforms.clipBounds = projectData.clipBounds[i]

      for (j = 0; j < 3; ++j) {
        if (!this.contourProject[i][j]) {
          continue
        }

        shader.uniforms.permutation = PERMUTATIONS[j]
        gl.lineWidth(this.contourWidth[j] * this.pixelRatio)
        for (var k = 0; k < this.contourLevels[j].length; ++k) {
          if (this._contourCounts[j][k]) {
            shader.uniforms.height = this.contourLevels[j][k]
            vao.draw(gl.LINES, this._contourCounts[j][k], this._contourOffsets[j][k])
          }
        }
      }
    }

    vao.unbind()
  }
}

proto.pick = function (selection) {
  if (!selection) {
    return null
  }

  if (selection.id !== this.pickId) {
    return null
  }

  var shape = this._field[2].shape

  var result = this._pickResult

  // Compute uv coordinate
  var x = shape[0] * (selection.value[0] + (selection.value[2] >> 4) / 16.0) / 255.0
  var ix = Math.floor(x)
  var fx = x - ix

  var y = shape[1] * (selection.value[1] + (selection.value[2] & 15) / 16.0) / 255.0
  var iy = Math.floor(y)
  var fy = y - iy

  ix += 1
  iy += 1

  // Compute xyz coordinate
  var pos = result.position
  pos[0] = pos[1] = pos[2] = 0
  for (var dx = 0; dx < 2; ++dx) {
    var s = dx ? fx : 1.0 - fx
    for (var dy = 0; dy < 2; ++dy) {
      var t = dy ? fy : 1.0 - fy

      var r = ix + dx
      var c = iy + dy
      var w = s * t

      for (var i = 0; i < 3; ++i) {
        pos[i] += this._field[i].get(r, c) * w
      }
    }
  }

  // Find closest level
  var levelIndex = this._pickResult.level
  for (var j = 0; j < 3; ++j) {
    levelIndex[j] = bsearch.le(this.contourLevels[j], pos[j])
    if (levelIndex[j] < 0) {
      if (this.contourLevels[j].length > 0) {
        levelIndex[j] = 0
      }
    } else if (levelIndex[j] < this.contourLevels[j].length - 1) {
      var a = this.contourLevels[j][levelIndex[j]]
      var b = this.contourLevels[j][levelIndex[j] + 1]
      if (Math.abs(a - pos[j]) > Math.abs(b - pos[j])) {
        levelIndex[j] += 1
      }
    }
  }

  result.index[0] = fx < 0.5 ? ix : (ix + 1)
  result.index[1] = fy < 0.5 ? iy : (iy + 1)

  result.uv[0] = x / shape[0]
  result.uv[1] = y / shape[1]

  for (i = 0; i < 3; ++i) {
    result.dataCoordinate[i] = this._field[i].get(result.index[0], result.index[1])
  }

  return result
}

proto.padField = function(dstField, srcField) {
  var srcShape = srcField.shape.slice()
  var dstShape = dstField.shape.slice()

  // Center
  ops.assign(dstField.lo(1, 1).hi(srcShape[0], srcShape[1]), srcField)

  // Edges
  ops.assign(dstField.lo(1).hi(srcShape[0], 1),
    srcField.hi(srcShape[0], 1))
  ops.assign(dstField.lo(1, dstShape[1] - 1).hi(srcShape[0], 1),
    srcField.lo(0, srcShape[1] - 1).hi(srcShape[0], 1))
  ops.assign(dstField.lo(0, 1).hi(1, srcShape[1]),
    srcField.hi(1))
  ops.assign(dstField.lo(dstShape[0] - 1, 1).hi(1, srcShape[1]),
    srcField.lo(srcShape[0] - 1))
  // Corners
  dstField.set(0, 0, srcField.get(0, 0))
  dstField.set(0, dstShape[1] - 1, srcField.get(0, srcShape[1] - 1))
  dstField.set(dstShape[0] - 1, 0, srcField.get(srcShape[0] - 1, 0))
  dstField.set(dstShape[0] - 1, dstShape[1] - 1, srcField.get(srcShape[0] - 1, srcShape[1] - 1))
}

function handleArray (param, ctor) {
  if (Array.isArray(param)) {
    return [ ctor(param[0]), ctor(param[1]), ctor(param[2]) ]
  }
  return [ ctor(param), ctor(param), ctor(param) ]
}

function toColor (x) {
  if (Array.isArray(x)) {
    if (x.length === 3) {
      return [x[0], x[1], x[2], 1]
    }
    return [x[0], x[1], x[2], x[3]]
  }
  return [0, 0, 0, 1]
}

function handleColor (param) {
  if (Array.isArray(param)) {
    if (Array.isArray(param)) {
      return [
        toColor(param[0]),
        toColor(param[1]),
        toColor(param[2]) ]
    } else {
      var c = toColor(param)
      return [
        c.slice(),
        c.slice(),
        c.slice() ]
    }
  }
}

proto.update = function (params) {
  params = params || {}

  this.objectOffset = params.objectOffset || this.objectOffset

  this.dirty = true

  if ('contourWidth' in params) {
    this.contourWidth = handleArray(params.contourWidth, Number)
  }
  if ('showContour' in params) {
    this.showContour = handleArray(params.showContour, Boolean)
  }
  if ('showSurface' in params) {
    this.showSurface = !!params.showSurface
  }
  if ('contourTint' in params) {
    this.contourTint = handleArray(params.contourTint, Boolean)
  }
  if ('contourColor' in params) {
    this.contourColor = handleColor(params.contourColor)
  }
  if ('contourProject' in params) {
    this.contourProject = handleArray(params.contourProject, function (x) {
      return handleArray(x, Boolean)
    })
  }
  if ('surfaceProject' in params) {
    this.surfaceProject = params.surfaceProject
  }
  if ('dynamicColor' in params) {
    this.dynamicColor = handleColor(params.dynamicColor)
  }
  if ('dynamicTint' in params) {
    this.dynamicTint = handleArray(params.dynamicTint, Number)
  }
  if ('dynamicWidth' in params) {
    this.dynamicWidth = handleArray(params.dynamicWidth, Number)
  }
  if ('opacity' in params) {
    this.opacity = params.opacity
  }
  if ('colorBounds' in params) {
    this.colorBounds = params.colorBounds
  }
  if ('vertexColor' in params) {
    this.vertexColor = params.vertexColor ? 1 : 0;
  }

  var field = params.field || (params.coords && params.coords[2]) || null
  var levelsChanged = false

  if (!field) {
    if (this._field[2].shape[0] || this._field[2].shape[2]) {
      field = this._field[2].lo(1, 1).hi(this._field[2].shape[0] - 2, this._field[2].shape[1] - 2)
    } else {
      field = this._field[2].hi(0, 0)
    }
  }

  // Update field
  if ('field' in params || 'coords' in params) {
    var fsize = (field.shape[0] + 2) * (field.shape[1] + 2)

    // Resize if necessary
    if (fsize > this._field[2].data.length) {
      pool.freeFloat(this._field[2].data)
      this._field[2].data = pool.mallocFloat(bits.nextPow2(fsize))
    }

    // Pad field
    this._field[2] = ndarray(this._field[2].data, [field.shape[0] + 2, field.shape[1] + 2])
    this.padField(this._field[2], field)

    // Save shape of field
    this.shape = field.shape.slice()
    var shape = this.shape

    // Resize coordinate fields if necessary
    for (var i = 0; i < 2; ++i) {
      if (this._field[2].size > this._field[i].data.length) {
        pool.freeFloat(this._field[i].data)
        this._field[i].data = pool.mallocFloat(this._field[2].size)
      }
      this._field[i] = ndarray(this._field[i].data, [shape[0] + 2, shape[1] + 2])
    }

    // Generate x/y coordinates
    if (params.coords) {
      var coords = params.coords
      if (!Array.isArray(coords) || coords.length !== 3) {
        throw new Error('gl-surface: invalid coordinates for x/y')
      }
      for (i = 0; i < 2; ++i) {
        var coord = coords[i]
        for (j = 0; j < 2; ++j) {
          if (coord.shape[j] !== shape[j]) {
            throw new Error('gl-surface: coords have incorrect shape')
          }
        }
        this.padField(this._field[i], coord)
      }
    } else if (params.ticks) {
      var ticks = params.ticks
      if (!Array.isArray(ticks) || ticks.length !== 2) {
        throw new Error('gl-surface: invalid ticks')
      }
      for (i = 0; i < 2; ++i) {
        var tick = ticks[i]
        if (Array.isArray(tick) || tick.length) {
          tick = ndarray(tick)
        }
        if (tick.shape[0] !== shape[i]) {
          throw new Error('gl-surface: invalid tick length')
        }
        // Make a copy view of the tick array
        var tick2 = ndarray(tick.data, shape)
        tick2.stride[i] = tick.stride[0]
        tick2.stride[i ^ 1] = 0

        // Fill in field array
        this.padField(this._field[i], tick2)
      }
    } else {
      for (i = 0; i < 2; ++i) {
        var offset = [0, 0]
        offset[i] = 1
        this._field[i] = ndarray(this._field[i].data, [shape[0] + 2, shape[1] + 2], offset, 0)
      }
      this._field[0].set(0, 0, 0)
      for (var j = 0; j < shape[0]; ++j) {
        this._field[0].set(j + 1, 0, j)
      }
      this._field[0].set(shape[0] + 1, 0, shape[0] - 1)
      this._field[1].set(0, 0, 0)
      for (j = 0; j < shape[1]; ++j) {
        this._field[1].set(0, j + 1, j)
      }
      this._field[1].set(0, shape[1] + 1, shape[1] - 1)
    }

    // Save shape
    var fields = this._field

    // Compute surface normals
    var dfields = ndarray(pool.mallocFloat(fields[2].size * 3 * 2), [3, shape[0] + 2, shape[1] + 2, 2])
    for (i = 0; i < 3; ++i) {
      gradient(dfields.pick(i), fields[i], 'mirror')
    }
    var normals = ndarray(pool.mallocFloat(fields[2].size * 3), [shape[0] + 2, shape[1] + 2, 3])
    for (i = 0; i < shape[0] + 2; ++i) {
      for (j = 0; j < shape[1] + 2; ++j) {
        var dxdu = dfields.get(0, i, j, 0)
        var dxdv = dfields.get(0, i, j, 1)
        var dydu = dfields.get(1, i, j, 0)
        var dydv = dfields.get(1, i, j, 1)
        var dzdu = dfields.get(2, i, j, 0)
        var dzdv = dfields.get(2, i, j, 1)

        var nx = dydu * dzdv - dydv * dzdu
        var ny = dzdu * dxdv - dzdv * dxdu
        var nz = dxdu * dydv - dxdv * dydu

        var nl = Math.sqrt(nx * nx + ny * ny + nz * nz)
        if (nl < 1e-8) {
          nl = Math.max(Math.abs(nx), Math.abs(ny), Math.abs(nz))
          if (nl < 1e-8) {
            nz = 1.0
            ny = nx = 0.0
            nl = 1.0
          } else {
            nl = 1.0 / nl
          }
        } else {
          nl = 1.0 / Math.sqrt(nl)
        }

        normals.set(i, j, 0, nx * nl)
        normals.set(i, j, 1, ny * nl)
        normals.set(i, j, 2, nz * nl)
      }
    }
    pool.free(dfields.data)

    // Initialize surface
    var lo = [ Infinity, Infinity, Infinity ]
    var hi = [ -Infinity, -Infinity, -Infinity ]
    var lo_intensity = Infinity
    var hi_intensity = -Infinity
    var count = (shape[0] - 1) * (shape[1] - 1) * 6
    var tverts = pool.mallocFloat(bits.nextPow2(10 * count))
    var tptr = 0
    var vertexCount = 0
    for (i = 0; i < shape[0] - 1; ++i) {
      j_loop:
      for (j = 0; j < shape[1] - 1; ++j) {
        // Test for NaNs
        for (var dx = 0; dx < 2; ++dx) {
          for (var dy = 0; dy < 2; ++dy) {
            for (var k = 0; k < 3; ++k) {
              var f = this._field[k].get(1 + i + dx, 1 + j + dy)
              if (isNaN(f) || !isFinite(f)) {
                continue j_loop
              }
            }
          }
        }
        for (k = 0; k < 6; ++k) {
          var r = i + QUAD[k][0]
          var c = j + QUAD[k][1]

          var tx = this._field[0].get(r + 1, c + 1)
          var ty = this._field[1].get(r + 1, c + 1)
          f =      this._field[2].get(r + 1, c + 1)

          nx = normals.get(r + 1, c + 1, 0)
          ny = normals.get(r + 1, c + 1, 1)
          nz = normals.get(r + 1, c + 1, 2)

          if (params.intensity) {
            vf = params.intensity.get(r, c)
          }

          var vf = (params.intensity) ?
            params.intensity.get(r, c) :
            f + this.objectOffset[2];

          tverts[tptr++] = r
          tverts[tptr++] = c
          tverts[tptr++] = tx
          tverts[tptr++] = ty
          tverts[tptr++] = f
          tverts[tptr++] = 0
          tverts[tptr++] = vf
          tverts[tptr++] = nx
          tverts[tptr++] = ny
          tverts[tptr++] = nz

          lo[0] = Math.min(lo[0], tx + this.objectOffset[0])
          lo[1] = Math.min(lo[1], ty + this.objectOffset[1])
          lo[2] = Math.min(lo[2], f  + this.objectOffset[2])
          lo_intensity = Math.min(lo_intensity, vf)

          hi[0] = Math.max(hi[0], tx + this.objectOffset[0])
          hi[1] = Math.max(hi[1], ty + this.objectOffset[1])
          hi[2] = Math.max(hi[2], f  + this.objectOffset[2])
          hi_intensity = Math.max(hi_intensity, vf)

          vertexCount += 1
        }
      }
    }

    if (params.intensityBounds) {
      lo_intensity = +params.intensityBounds[0]
      hi_intensity = +params.intensityBounds[1]
    }

    // Scale all vertex intensities
    for (i = 6; i < tptr; i += 10) {
      tverts[i] = (tverts[i] - lo_intensity) / (hi_intensity - lo_intensity)
    }

    this._vertexCount = vertexCount
    this._coordinateBuffer.update(tverts.subarray(0, tptr))
    pool.freeFloat(tverts)
    pool.free(normals.data)

    // Update bounds
    this.bounds = [lo, hi]

    // Save intensity
    this.intensity = params.intensity || this._field[2]

    if(this.intensityBounds[0] !== lo_intensity || this.intensityBounds[1] !== hi_intensity) {
        levelsChanged = true
    }

    // Save intensity bound
    this.intensityBounds = [lo_intensity, hi_intensity]
  }

  // Update level crossings
  if ('levels' in params) {
    var levels = params.levels
    if (!Array.isArray(levels[0])) {
      levels = [ [], [], levels ]
    } else {
      levels = levels.slice()
    }
    for (i = 0; i < 3; ++i) {
      levels[i] = levels[i].slice()
      levels[i].sort(function (a, b) {
        return a - b
      })
    }
    for (i = 0; i < 3; ++i) {
      for (j = 0; j < levels[i].length; ++j) {
        levels[i][j] -= this.objectOffset[i]
      }
    }
    change_test:
    for (i = 0; i < 3; ++i) {
      if (levels[i].length !== this.contourLevels[i].length) {
        levelsChanged = true
        break
      }
      for (j = 0; j < levels[i].length; ++j) {
        if (levels[i][j] !== this.contourLevels[i][j]) {
          levelsChanged = true
          break change_test
        }
      }
    }
    this.contourLevels = levels
  }

  if (levelsChanged) {
    fields = this._field
    shape = this.shape

    // Update contour lines
    var contourVerts = []

    for (var dim = 0; dim < 3; ++dim) {
      var contourLevel = this.contourLevels[dim]

      var levelOffsets = []
      var levelCounts = []

      var parts = [0, 0, 0]

      for (i = 0; i < contourLevel.length; ++i) {
        var graph = surfaceNets(this._field[dim], contourLevel[i])

        levelOffsets.push((contourVerts.length / 5) | 0)
        vertexCount = 0

        edge_loop:
        for (j = 0; j < graph.cells.length; ++j) {
          var e = graph.cells[j]
          for (k = 0; k < 2; ++k) {
            var p = graph.positions[e[k]]

            var x = p[0]
            var ix = Math.floor(x) | 0
            var fx = x - ix

            var y = p[1]
            var iy = Math.floor(y) | 0
            var fy = y - iy

            var hole = false
            axis_loop:
            for (var axis = 0; axis < 3; ++axis) {
              parts[axis] = 0.0
              var iu = (dim + axis + 1) % 3
              for (dx = 0; dx < 2; ++dx) {
                var s = dx ? fx : 1.0 - fx
                r = Math.min(Math.max(ix + dx, 0), shape[0]) | 0
                for (dy = 0; dy < 2; ++dy) {
                  var t = dy ? fy : 1.0 - fy
                  c = Math.min(Math.max(iy + dy, 0), shape[1]) | 0

                  if (axis < 2) {
                    f = this._field[iu].get(r, c)
                  } else {
                    f = (this.intensity.get(r, c) - this.intensityBounds[0]) / (this.intensityBounds[1] - this.intensityBounds[0])
                  }
                  if (!isFinite(f) || isNaN(f)) {
                    hole = true
                    break axis_loop
                  }

                  var w = s * t
                  parts[axis] += w * f
                }
              }
            }

            if (!hole) {
              contourVerts.push(
                parts[0],
                parts[1],
                p[0],
                p[1],
                parts[2]
              )
              vertexCount += 1
            } else {
              if (k > 0) {
                // If we already added first edge, pop off verts
                for (var l = 0; l < 5; ++l) {
                  contourVerts.pop()
                }
                vertexCount -= 1
              }
              continue edge_loop
            }
          }
        }
        levelCounts.push(vertexCount)
      }

      // Store results
      this._contourOffsets[dim] = levelOffsets
      this._contourCounts[dim] = levelCounts

    }

    var floatBuffer = pool.mallocFloat(contourVerts.length)
    for (i = 0; i < contourVerts.length; ++i) {
      floatBuffer[i] = contourVerts[i]
    }
    this._contourBuffer.update(floatBuffer)
    pool.freeFloat(floatBuffer)
  }

  if (params.colormap) {
    this._colorMap.setPixels(genColormap(params.colormap))
  }
}

proto.dispose = function () {
  this._shader.dispose()
  this._vao.dispose()
  this._coordinateBuffer.dispose()
  this._colorMap.dispose()
  this._contourBuffer.dispose()
  this._contourVAO.dispose()
  this._contourShader.dispose()
  this._contourPickShader.dispose()
  this._dynamicBuffer.dispose()
  this._dynamicVAO.dispose()
  for (var i = 0; i < 3; ++i) {
    pool.freeFloat(this._field[i].data)
  }
}

proto.highlight = function (selection) {
  var i

  if (!selection) {
    this._dynamicCounts = [0, 0, 0]
    this.dyanamicLevel = [NaN, NaN, NaN]
    this.highlightLevel = [-1, -1, -1]
    return
  }

  for (i = 0; i < 3; ++i) {
    if (this.enableHighlight[i]) {
      this.highlightLevel[i] = selection.level[i]
    } else {
      this.highlightLevel[i] = -1
    }
  }

  var levels
  if (this.snapToData) {
    levels = selection.dataCoordinate
  } else {
    levels = selection.position
  }
  for (i = 0; i < 3; ++i) {
    levels[i] -= this.objectOffset[i]
  }
  if ((!this.enableDynamic[0] || levels[0] === this.dynamicLevel[0]) &&
    (!this.enableDynamic[1] || levels[1] === this.dynamicLevel[1]) &&
    (!this.enableDynamic[2] || levels[2] === this.dynamicLevel[2])) {
    return
  }

  var vertexCount = 0
  var shape = this.shape
  var scratchBuffer = pool.mallocFloat(12 * shape[0] * shape[1])

  for (var d = 0; d < 3; ++d) {
    if (!this.enableDynamic[d]) {
      this.dynamicLevel[d] = NaN
      this._dynamicCounts[d] = 0
      continue
    }

    this.dynamicLevel[d] = levels[d]

    var u = (d + 1) % 3
    var v = (d + 2) % 3

    var f = this._field[d]
    var g = this._field[u]
    var h = this._field[v]

    var graph = surfaceNets(f, levels[d])
    var edges = graph.cells
    var positions = graph.positions

    this._dynamicOffsets[d] = vertexCount

    for (i = 0; i < edges.length; ++i) {
      var e = edges[i]
      for (var j = 0; j < 2; ++j) {
        var p = positions[e[j]]

        var x = +p[0]
        var ix = x | 0
        var jx = Math.min(ix + 1, shape[0]) | 0
        var fx = x - ix
        var hx = 1.0 - fx

        var y = +p[1]
        var iy = y | 0
        var jy = Math.min(iy + 1, shape[1]) | 0
        var fy = y - iy
        var hy = 1.0 - fy

        var w00 = hx * hy
        var w01 = hx * fy
        var w10 = fx * hy
        var w11 = fx * fy

        var cu = w00 * g.get(ix, iy) +
          w01 * g.get(ix, jy) +
          w10 * g.get(jx, iy) +
          w11 * g.get(jx, jy)

        var cv = w00 * h.get(ix, iy) +
          w01 * h.get(ix, jy) +
          w10 * h.get(jx, iy) +
          w11 * h.get(jx, jy)

        if (isNaN(cu) || isNaN(cv)) {
          if (j) {
            vertexCount -= 1
          }
          break
        }

        scratchBuffer[2 * vertexCount + 0] = cu
        scratchBuffer[2 * vertexCount + 1] = cv

        vertexCount += 1
      }
    }

    this._dynamicCounts[d] = vertexCount - this._dynamicOffsets[d]
  }

  this._dynamicBuffer.update(scratchBuffer.subarray(0, 2 * vertexCount))
  pool.freeFloat(scratchBuffer)
}

function createSurfacePlot (params) {
  var gl = params.gl

  var shader = createShader(gl)
  var pickShader = createPickShader(gl)
  var contourShader = createContourShader(gl)
  var contourPickShader = createPickContourShader(gl)

  var coordinateBuffer = createBuffer(gl)
  var vao = createVAO(gl, [
    { buffer: coordinateBuffer,
      size: 4,
      stride: SURFACE_VERTEX_SIZE,
      offset: 0
    },
    { buffer: coordinateBuffer,
      size: 3,
      stride: SURFACE_VERTEX_SIZE,
      offset: 16
    },
    {
      buffer: coordinateBuffer,
      size: 3,
      stride: SURFACE_VERTEX_SIZE,
      offset: 28
    }
  ])

  var contourBuffer = createBuffer(gl)
  var contourVAO = createVAO(gl, [
    {
      buffer: contourBuffer,
      size: 4,
      stride: 20,
      offset: 0
    },
    {
      buffer: contourBuffer,
      size: 1,
      stride: 20,
      offset: 16
    }
  ])

  var dynamicBuffer = createBuffer(gl)
  var dynamicVAO = createVAO(gl, [
    {
      buffer: dynamicBuffer,
      size: 2,
      type: gl.FLOAT
    }])

  var cmap = createTexture(gl, 1, N_COLORS, gl.RGBA, gl.UNSIGNED_BYTE)
  cmap.minFilter = gl.LINEAR
  cmap.magFilter = gl.LINEAR

  var surface = new SurfacePlot(
    gl,
    [0, 0], // shape
    [[0, 0, 0], [0, 0, 0]], // bounds
    shader,
    pickShader,
    coordinateBuffer,
    vao,
    cmap,
    contourShader,
    contourPickShader,
    contourBuffer,
    contourVAO,
    dynamicBuffer,
    dynamicVAO,
    [0, 0, 0] // objectOffset
  )

  var nparams = {
    levels: [[], [], []]
  }
  for (var id in params) {
    nparams[id] = params[id]
  }
  nparams.colormap = nparams.colormap || 'jet'

  surface.update(nparams)

  return surface
}
