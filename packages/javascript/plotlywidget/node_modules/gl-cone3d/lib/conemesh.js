'use strict'

var DEFAULT_VERTEX_NORMALS_EPSILON = 1e-6; // may be too large if triangles are very small
var DEFAULT_FACE_NORMALS_EPSILON = 1e-6;

var createShader  = require('gl-shader')
var createBuffer  = require('gl-buffer')
var createVAO     = require('gl-vao')
var createTexture = require('gl-texture2d')
var normals       = require('normals')
var multiply      = require('gl-mat4/multiply')
var invert        = require('gl-mat4/invert')
var ndarray       = require('ndarray')
var colormap      = require('colormap')
var getContour    = require('simplicial-complex-contour')
var pool          = require('typedarray-pool')
var shaders       = require('./shaders')

var meshShader    = shaders.meshShader
var pickShader    = shaders.pickShader

var IDENTITY = [
  1,0,0,0,
  0,1,0,0,
  0,0,1,0,
  0,0,0,1]

function SimplicialMesh(gl
  , texture
  , triShader
  , pickShader
  , trianglePositions
  , triangleVectors
  , triangleIds
  , triangleColors
  , triangleUVs
  , triangleNormals
  , triangleVAO
  , edgePositions
  , edgeIds
  , edgeColors
  , edgeUVs
  , edgeVAO
  , pointPositions
  , pointIds
  , pointColors
  , pointUVs
  , pointSizes
  , pointVAO
  , contourPositions
  , contourVAO) {

  this.gl                = gl
  this.pixelRatio         = 1
  this.cells             = []
  this.positions         = []
  this.intensity         = []
  this.texture           = texture
  this.dirty             = true

  this.triShader         = triShader
  this.pickShader        = pickShader

  this.trianglePositions = trianglePositions
  this.triangleVectors   = triangleVectors
  this.triangleColors    = triangleColors
  this.triangleNormals   = triangleNormals
  this.triangleUVs       = triangleUVs
  this.triangleIds       = triangleIds
  this.triangleVAO       = triangleVAO
  this.triangleCount     = 0

  this.lineWidth         = 1
  this.edgePositions     = edgePositions
  this.edgeColors        = edgeColors
  this.edgeUVs           = edgeUVs
  this.edgeIds           = edgeIds
  this.edgeVAO           = edgeVAO
  this.edgeCount         = 0

  this.pointPositions    = pointPositions
  this.pointColors       = pointColors
  this.pointUVs          = pointUVs
  this.pointSizes        = pointSizes
  this.pointIds          = pointIds
  this.pointVAO          = pointVAO
  this.pointCount        = 0

  this.contourLineWidth  = 1
  this.contourPositions  = contourPositions
  this.contourVAO        = contourVAO
  this.contourCount      = 0
  this.contourColor      = [0,0,0]
  this.contourEnable     = true

  this.pickId            = 1
  this.bounds            = [
    [ Infinity, Infinity, Infinity],
    [-Infinity,-Infinity,-Infinity] ]
  this.clipBounds        = [
    [-Infinity,-Infinity,-Infinity],
    [ Infinity, Infinity, Infinity] ]

  this.lightPosition = [1e5, 1e5, 0]
  this.ambientLight  = 0.8
  this.diffuseLight  = 0.8
  this.specularLight = 2.0
  this.roughness     = 0.5
  this.fresnel       = 1.5

  this.opacity       = 1.0

  this.coneScale     = 2.0
  this.vectorScale   = 1.0
  this.coneOffset    = 1.0 / 4.0;

  this._model       = IDENTITY
  this._view        = IDENTITY
  this._projection  = IDENTITY
  this._resolution  = [1,1]
}

var proto = SimplicialMesh.prototype

proto.isOpaque = function() {
  return this.opacity >= 1
}

proto.isTransparent = function() {
  return this.opacity < 1
}

proto.pickSlots = 1

proto.setPickBase = function(id) {
  this.pickId = id
}

function genColormap(param) {
  var colors = colormap({
      colormap: param
    , nshades:  256
    , format:  'rgba'
  })

  var result = new Uint8Array(256*4)
  for(var i=0; i<256; ++i) {
    var c = colors[i]
    for(var j=0; j<3; ++j) {
      result[4*i+j] = c[j]
    }
    result[4*i+3] = c[3]*255
  }

  return ndarray(result, [256,256,4], [4,0,1])
}

function unpackIntensity(cells, numVerts, cellIntensity) {
  var result = new Array(numVerts)
  for(var i=0; i<numVerts; ++i) {
    result[i] = 0
  }
  var numCells = cells.length
  for(var i=0; i<numCells; ++i) {
    var c = cells[i]
    for(var j=0; j<c.length; ++j) {
      result[c[j]] = cellIntensity[i]
    }
  }
  return result
}

function takeZComponent(array) {
  var n = array.length
  var result = new Array(n)
  for(var i=0; i<n; ++i) {
    result[i] = array[i][2]
  }
  return result
}

proto.highlight = function(selection) {
  if(!selection || !this.contourEnable) {
    this.contourCount = 0
    return
  }
  var level = getContour(this.cells, this.intensity, selection.intensity)
  var cells         = level.cells
  var vertexIds     = level.vertexIds
  var vertexWeights = level.vertexWeights
  var numCells = cells.length
  var result = pool.mallocFloat32(2 * 3 * numCells)
  var ptr = 0
  for(var i=0; i<numCells; ++i) {
    var c = cells[i]
    for(var j=0; j<2; ++j) {
      var v = c[0]
      if(c.length === 2) {
        v = c[j]
      }
      var a = vertexIds[v][0]
      var b = vertexIds[v][1]
      var w = vertexWeights[v]
      var wi = 1.0 - w
      var pa = this.positions[a]
      var pb = this.positions[b]
      for(var k=0; k<3; ++k) {
        result[ptr++] = w * pa[k] + wi * pb[k]
      }
    }
  }
  this.contourCount = (ptr / 3)|0
  this.contourPositions.update(result.subarray(0, ptr))
  pool.free(result)
}

proto.update = function(params) {
  params = params || {}
  var gl = this.gl

  this.dirty = true

  if('contourEnable' in params) {
    this.contourEnable = params.contourEnable
  }
  if('contourColor' in params) {
    this.contourColor = params.contourColor
  }
  if('lineWidth' in params) {
    this.lineWidth = params.lineWidth
  }
  if('lightPosition' in params) {
    this.lightPosition = params.lightPosition
  }
  if('opacity' in params) {
    this.opacity = params.opacity
  }
  if('ambient' in params) {
    this.ambientLight  = params.ambient
  }
  if('diffuse' in params) {
    this.diffuseLight = params.diffuse
  }
  if('specular' in params) {
    this.specularLight = params.specular
  }
  if('roughness' in params) {
    this.roughness = params.roughness
  }
  if('fresnel' in params) {
    this.fresnel = params.fresnel
  }

  if (params.vectorScale !== undefined) {
    this.vectorScale = params.vectorScale;
  }
  if (params.coneScale !== undefined) {
    this.coneScale = params.coneScale;
  }
  if (params.coneOffset !== undefined) {
    this.coneOffset = params.coneOffset;
  }

  if(params.texture) {
    this.texture.dispose()
    this.texture = createTexture(gl, params.texture)
  } else if (params.colormap) {
    this.texture.shape = [256,256]
    this.texture.minFilter = gl.LINEAR_MIPMAP_LINEAR
    this.texture.magFilter = gl.LINEAR
    this.texture.setPixels(genColormap(params.colormap))
    this.texture.generateMipmap()
  }

  var cells = params.cells
  var positions = params.positions
  var vectors = params.vectors

  if(!positions || !cells || !vectors) {
    return
  }

  var tPos = []
  var tVec = []
  var tCol = []
  var tNor = []
  var tUVs = []
  var tIds = []

  var ePos = []
  var eCol = []
  var eUVs = []
  var eIds = []

  var pPos = []
  var pCol = []
  var pUVs = []
  var pSiz = []
  var pIds = []

  //Save geometry data for picking calculations
  this.cells     = cells
  this.positions = positions

  //Compute normals
  var vertexNormals = params.vertexNormals
  var cellNormals   = params.cellNormals
  var vertexNormalsEpsilon = params.vertexNormalsEpsilon === void(0) ? DEFAULT_VERTEX_NORMALS_EPSILON : params.vertexNormalsEpsilon
  var faceNormalsEpsilon = params.faceNormalsEpsilon === void(0) ? DEFAULT_FACE_NORMALS_EPSILON : params.faceNormalsEpsilon
  if(params.useFacetNormals && !cellNormals) {
    cellNormals = normals.faceNormals(cells, positions, faceNormalsEpsilon)
  }
  if(!cellNormals && !vertexNormals) {
    vertexNormals = normals.vertexNormals(cells, positions, vertexNormalsEpsilon)
  }

  //Compute colors
  var vertexColors    = params.vertexColors
  var cellColors      = params.cellColors
  var meshColor       = params.meshColor || [1,1,1,1]

  //UVs
  var vertexUVs       = params.vertexUVs
  var vertexIntensity = params.vertexIntensity
  var cellUVs         = params.cellUVs
  var cellIntensity   = params.cellIntensity

  var intensityLo     = Infinity
  var intensityHi     = -Infinity
  if(!vertexUVs && !cellUVs) {
    if(vertexIntensity) {
      if(params.vertexIntensityBounds) {
        intensityLo = +params.vertexIntensityBounds[0]
        intensityHi = +params.vertexIntensityBounds[1]
      } else {
        for(var i=0; i<vertexIntensity.length; ++i) {
          var f = vertexIntensity[i]
          intensityLo = Math.min(intensityLo, f)
          intensityHi = Math.max(intensityHi, f)
        }
      }
    } else if(cellIntensity) {
      for(var i=0; i<cellIntensity.length; ++i) {
        var f = cellIntensity[i]
        intensityLo = Math.min(intensityLo, f)
        intensityHi = Math.max(intensityHi, f)
      }
    } else {
      for(var i=0; i<positions.length; ++i) {
        var f = positions[i][2]
        intensityLo = Math.min(intensityLo, f)
        intensityHi = Math.max(intensityHi, f)
      }
    }
  }

  if(vertexIntensity) {
    this.intensity = vertexIntensity
  } else if(cellIntensity) {
    this.intensity = unpackIntensity(cells, positions.length, cellIntensity)
  } else {
    this.intensity = takeZComponent(positions)
  }

  //Point size
  var pointSizes      = params.pointSizes
  var meshPointSize   = params.pointSize || 1.0

  //Update bounds
  this.bounds       = [[Infinity,Infinity,Infinity], [-Infinity,-Infinity,-Infinity]]
  for(var i=0; i<positions.length; ++i) {
    var p = positions[i]
    for(var j=0; j<3; ++j) {
      if(isNaN(p[j]) || !isFinite(p[j])) {
        continue
      }
      this.bounds[0][j] = Math.min(this.bounds[0][j], p[j])
      this.bounds[1][j] = Math.max(this.bounds[1][j], p[j])
    }
  }

  //Pack cells into buffers
  var triangleCount = 0
  var edgeCount = 0
  var pointCount = 0

fill_loop:
  for(var i=0; i<cells.length; ++i) {
    var cell = cells[i]
    switch(cell.length) {
      case 1:

        var v = cell[0]
        var p = positions[v]

        //Check NaNs
        for(var j=0; j<3; ++j) {
          if(isNaN(p[j]) || !isFinite(p[j])) {
            continue fill_loop
          }
        }

        pPos.push(p[0], p[1], p[2], p[3])

        var c
        if(vertexColors) {
          c = vertexColors[v]
        } else if(cellColors) {
          c = cellColors[i]
        } else {
          c = meshColor
        }
        if(c.length === 3) {
          pCol.push(c[0], c[1], c[2], 1)
        } else {
          pCol.push(c[0], c[1], c[2], c[3])
        }

        var uv
        if(vertexUVs) {
          uv = vertexUVs[v]
        } else if(vertexIntensity) {
          uv = [
            (vertexIntensity[v] - intensityLo) /
            (intensityHi - intensityLo), 0]
        } else if(cellUVs) {
          uv = cellUVs[i]
        } else if(cellIntensity) {
          uv = [
            (cellIntensity[i] - intensityLo) /
            (intensityHi - intensityLo), 0]
        } else {
          uv = [
            (p[2] - intensityLo) /
            (intensityHi - intensityLo), 0]
        }
        pUVs.push(uv[0], uv[1])

        if(pointSizes) {
          pSiz.push(pointSizes[v])
        } else {
          pSiz.push(meshPointSize)
        }

        pIds.push(i)

        pointCount += 1
      break

      case 2:

        //Check NaNs
        for(var j=0; j<2; ++j) {
          var v = cell[j]
          var p = positions[v]
          for(var k=0; k<3; ++k) {
            if(isNaN(p[k]) || !isFinite(p[k])) {
              continue fill_loop
            }
          }
        }

        for(var j=0; j<2; ++j) {
          var v = cell[j]
          var p = positions[v]

          ePos.push(p[0], p[1], p[2])

          var c
          if(vertexColors) {
            c = vertexColors[v]
          } else if(cellColors) {
            c = cellColors[i]
          } else {
            c = meshColor
          }
          if(c.length === 3) {
            eCol.push(c[0], c[1], c[2], 1)
          } else {
            eCol.push(c[0], c[1], c[2], c[3])
          }

          var uv
          if(vertexUVs) {
            uv = vertexUVs[v]
          } else if(vertexIntensity) {
            uv = [
              (vertexIntensity[v] - intensityLo) /
              (intensityHi - intensityLo), 0]
          } else if(cellUVs) {
            uv = cellUVs[i]
          } else if(cellIntensity) {
            uv = [
              (cellIntensity[i] - intensityLo) /
              (intensityHi - intensityLo), 0]
          } else {
            uv = [
              (p[2] - intensityLo) /
              (intensityHi - intensityLo), 0]
          }
          eUVs.push(uv[0], uv[1])

          eIds.push(i)
        }
        edgeCount += 1
      break

      case 3:
        //Check NaNs
        for(var j=0; j<3; ++j) {
          var v = cell[j]
          var p = positions[v]
          for(var k=0; k<3; ++k) {
            if(isNaN(p[k]) || !isFinite(p[k])) {
              continue fill_loop
            }
          }
        }

        for(var j=0; j<3; ++j) {
          var v = cell[2 - j]

          var p = positions[v]
          tPos.push(p[0], p[1], p[2], p[3])

          var w = vectors[v]
          tVec.push(w[0], w[1], w[2]);

          var c
          if(vertexColors) {
            c = vertexColors[v]
          } else if(cellColors) {
            c = cellColors[i]
          } else {
            c = meshColor
          }
          if(c.length === 3) {
            tCol.push(c[0], c[1], c[2], 1)
          } else {
            tCol.push(c[0], c[1], c[2], c[3])
          }

          var uv
          if(vertexUVs) {
            uv = vertexUVs[v]
          } else if(vertexIntensity) {
            uv = [
              (vertexIntensity[v] - intensityLo) /
              (intensityHi - intensityLo), 0]
          } else if(cellUVs) {
            uv = cellUVs[i]
          } else if(cellIntensity) {
            uv = [
              (cellIntensity[i] - intensityLo) /
              (intensityHi - intensityLo), 0]
          } else {
            uv = [
              (p[2] - intensityLo) /
              (intensityHi - intensityLo), 0]
          }
          tUVs.push(uv[0], uv[1])

          var q
          if(vertexNormals) {
            q = vertexNormals[v]
          } else {
            q = cellNormals[i]
          }
          tNor.push(q[0], q[1], q[2])

          tIds.push(i)
        }
        triangleCount += 1
      break

      default:
      break
    }
  }

  this.pointCount     = pointCount
  this.edgeCount      = edgeCount
  this.triangleCount  = triangleCount

  this.pointPositions.update(pPos)
  this.pointColors.update(pCol)
  this.pointUVs.update(pUVs)
  this.pointSizes.update(pSiz)
  this.pointIds.update(new Uint32Array(pIds))

  this.edgePositions.update(ePos)
  this.edgeColors.update(eCol)
  this.edgeUVs.update(eUVs)
  this.edgeIds.update(new Uint32Array(eIds))

  this.trianglePositions.update(tPos)
  this.triangleVectors.update(tVec)
  this.triangleColors.update(tCol)
  this.triangleUVs.update(tUVs)
  this.triangleNormals.update(tNor)
  this.triangleIds.update(new Uint32Array(tIds))
}

proto.drawTransparent = proto.draw = function(params) {
  params = params || {}
  var gl          = this.gl
  var model       = params.model      || IDENTITY
  var view        = params.view       || IDENTITY
  var projection  = params.projection || IDENTITY

  var clipBounds = [[-1e6,-1e6,-1e6],[1e6,1e6,1e6]]
  for(var i=0; i<3; ++i) {
    clipBounds[0][i] = Math.max(clipBounds[0][i], this.clipBounds[0][i])
    clipBounds[1][i] = Math.min(clipBounds[1][i], this.clipBounds[1][i])
  }

  var uniforms = {
    model:      model,
    view:       view,
    projection: projection,
    inverseModel: IDENTITY.slice(),

    clipBounds: clipBounds,

    kambient:   this.ambientLight,
    kdiffuse:   this.diffuseLight,
    kspecular:  this.specularLight,
    roughness:  this.roughness,
    fresnel:    this.fresnel,

    eyePosition:   [0,0,0],
    lightPosition: [0,0,0],

    opacity:  this.opacity,

    vectorScale: this.vectorScale,
    coneScale: this.coneScale,
    coneOffset: this.coneOffset,

    contourColor: this.contourColor,

    texture:    0
  }

  uniforms.inverseModel = invert(uniforms.inverseModel, uniforms.model)

  gl.disable(gl.CULL_FACE)

  this.texture.bind(0)

  var invCameraMatrix = new Array(16)
  multiply(invCameraMatrix, uniforms.view, uniforms.model)
  multiply(invCameraMatrix, uniforms.projection, invCameraMatrix)
  invert(invCameraMatrix, invCameraMatrix)

  for(var i=0; i<3; ++i) {
    uniforms.eyePosition[i] = invCameraMatrix[12+i] / invCameraMatrix[15]
  }

  var w = invCameraMatrix[15]
  for(var i=0; i<3; ++i) {
    w += this.lightPosition[i] * invCameraMatrix[4*i+3]
  }
  for(var i=0; i<3; ++i) {
    var s = invCameraMatrix[12+i]
    for(var j=0; j<3; ++j) {
      s += invCameraMatrix[4*j+i] * this.lightPosition[j]
    }
    uniforms.lightPosition[i] = s / w
  }

  if(this.triangleCount > 0) {
    var shader = this.triShader
    shader.bind()
    shader.uniforms = uniforms

    this.triangleVAO.bind()
    gl.drawArrays(gl.TRIANGLES, 0, this.triangleCount*3)
    this.triangleVAO.unbind()
  }
}
proto.drawPick = function(params) {
  params = params || {}

  var gl         = this.gl

  var model      = params.model      || IDENTITY
  var view       = params.view       || IDENTITY
  var projection = params.projection || IDENTITY

  var clipBounds = [[-1e6,-1e6,-1e6],[1e6,1e6,1e6]]
  for(var i=0; i<3; ++i) {
    clipBounds[0][i] = Math.max(clipBounds[0][i], this.clipBounds[0][i])
    clipBounds[1][i] = Math.min(clipBounds[1][i], this.clipBounds[1][i])
  }

  //Save camera parameters
  this._model      = [].slice.call(model)
  this._view       = [].slice.call(view)
  this._projection = [].slice.call(projection)
  this._resolution = [gl.drawingBufferWidth, gl.drawingBufferHeight]

  var uniforms = {
    model:      model,
    view:       view,
    projection: projection,
    clipBounds: clipBounds,

    vectorScale: this.vectorScale,
    coneScale: this.coneScale,
    coneOffset: this.coneOffset,

    pickId:     this.pickId / 255.0,
  }

  var shader = this.pickShader
  shader.bind()
  shader.uniforms = uniforms

  if(this.triangleCount > 0) {
    this.triangleVAO.bind()
    gl.drawArrays(gl.TRIANGLES, 0, this.triangleCount*3)
    this.triangleVAO.unbind()
  }

  if(this.edgeCount > 0) {
    this.edgeVAO.bind()
    gl.lineWidth(this.lineWidth * this.pixelRatio)
    gl.drawArrays(gl.LINES, 0, this.edgeCount*2)
    this.edgeVAO.unbind()
  }

}


proto.pick = function(pickData) {
  if(!pickData) {
    return null
  }
  if(pickData.id !== this.pickId) {
    return null
  }

  var cellId    = pickData.value[0] + 256*pickData.value[1] + 65536*pickData.value[2]
  var cell      = this.cells[cellId]
  var pos =     this.positions[cell[1]].slice(0, 3)

  return {
    // corresponding to input indices
    index: Math.floor(cell[1] / 48),
    position: pos,
    dataCoordinate: pos
  }
}


proto.dispose = function() {
  this.texture.dispose()

  this.triShader.dispose()
  this.pickShader.dispose()

  this.triangleVAO.dispose()
  this.trianglePositions.dispose()
  this.triangleVectors.dispose()
  this.triangleColors.dispose()
  this.triangleUVs.dispose()
  this.triangleNormals.dispose()
  this.triangleIds.dispose()

  this.edgeVAO.dispose()
  this.edgePositions.dispose()
  this.edgeColors.dispose()
  this.edgeUVs.dispose()
  this.edgeIds.dispose()

  this.pointVAO.dispose()
  this.pointPositions.dispose()
  this.pointColors.dispose()
  this.pointUVs.dispose()
  this.pointSizes.dispose()
  this.pointIds.dispose()

  this.contourVAO.dispose()
  this.contourPositions.dispose()
}

function createMeshShader(gl) {
  // need to pass meshShader attributes manually,
  // to make this work on etpinard's Ubuntu Thinkpad
  var shader = createShader(gl, meshShader.vertex, meshShader.fragment, null, meshShader.attributes)
  shader.attributes.position.location = 0
  shader.attributes.color.location    = 2
  shader.attributes.uv.location       = 3
  shader.attributes.vector.location   = 5
  return shader
}


function createPickShader(gl) {
  var shader = createShader(gl, pickShader.vertex, pickShader.fragment, null, pickShader.attributes)
  shader.attributes.position.location = 0
  shader.attributes.id.location       = 1
  shader.attributes.vector.location   = 5
  return shader
}



function createSimplicialMesh(gl, params) {
  if (arguments.length === 1) {
    params = gl;
    gl = params.gl;
  }


  var triShader       = params.triShader || createMeshShader(gl)
  var pickShader      = createPickShader(gl)
  var meshTexture       = createTexture(gl,
    ndarray(new Uint8Array([255,255,255,255]), [1,1,4]))
  meshTexture.generateMipmap()
  meshTexture.minFilter = gl.LINEAR_MIPMAP_LINEAR
  meshTexture.magFilter = gl.LINEAR

  var trianglePositions = createBuffer(gl)
  var triangleVectors   = createBuffer(gl)
  var triangleColors    = createBuffer(gl)
  var triangleUVs       = createBuffer(gl)
  var triangleNormals   = createBuffer(gl)
  var triangleIds       = createBuffer(gl)
  var triangleVAO       = createVAO(gl, [
    { buffer: trianglePositions,
      type: gl.FLOAT,
      size: 4
    },
    { buffer: triangleIds,
      type: gl.UNSIGNED_BYTE,
      size: 4,
      normalized: true
    },
    { buffer: triangleColors,
      type: gl.FLOAT,
      size: 4
    },
    { buffer: triangleUVs,
      type: gl.FLOAT,
      size: 2
    },
    { buffer: triangleNormals,
      type: gl.FLOAT,
      size: 3
    },
    { buffer: triangleVectors,
      type: gl.FLOAT,
      size: 3
    }
  ])

  var edgePositions = createBuffer(gl)
  var edgeColors    = createBuffer(gl)
  var edgeUVs       = createBuffer(gl)
  var edgeIds       = createBuffer(gl)
  var edgeVAO       = createVAO(gl, [
    { buffer: edgePositions,
      type: gl.FLOAT,
      size: 3
    },
    { buffer: edgeIds,
      type: gl.UNSIGNED_BYTE,
      size: 4,
      normalized: true
    },
    { buffer: edgeColors,
      type: gl.FLOAT,
      size: 4
    },
    { buffer: edgeUVs,
      type: gl.FLOAT,
      size: 2
    }
  ])

  var pointPositions  = createBuffer(gl)
  var pointColors     = createBuffer(gl)
  var pointUVs        = createBuffer(gl)
  var pointSizes      = createBuffer(gl)
  var pointIds        = createBuffer(gl)
  var pointVAO        = createVAO(gl, [
    { buffer: pointPositions,
      type: gl.FLOAT,
      size: 3
    },
    { buffer: pointIds,
      type: gl.UNSIGNED_BYTE,
      size: 4,
      normalized: true
    },
    { buffer: pointColors,
      type: gl.FLOAT,
      size: 4
    },
    { buffer: pointUVs,
      type: gl.FLOAT,
      size: 2
    },
    { buffer: pointSizes,
      type: gl.FLOAT,
      size: 1
    }
  ])

  var contourPositions = createBuffer(gl)
  var contourVAO       = createVAO(gl, [
    { buffer: contourPositions,
      type:   gl.FLOAT,
      size:   3
    }])

  var mesh = new SimplicialMesh(gl
    , meshTexture
    , triShader
    , pickShader
    , trianglePositions
    , triangleVectors
    , triangleIds
    , triangleColors
    , triangleUVs
    , triangleNormals
    , triangleVAO
    , edgePositions
    , edgeIds
    , edgeColors
    , edgeUVs
    , edgeVAO
    , pointPositions
    , pointIds
    , pointColors
    , pointUVs
    , pointSizes
    , pointVAO
    , contourPositions
    , contourVAO)

  mesh.update(params)

  return mesh
}

module.exports = createSimplicialMesh
