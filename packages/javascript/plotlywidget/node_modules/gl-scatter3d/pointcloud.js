'use strict'

var isAllBlank      = require('is-string-blank')
var createBuffer    = require('gl-buffer')
var createVAO       = require('gl-vao')
var pool            = require('typedarray-pool')
var mat4mult        = require('gl-mat4/multiply')
var shaders         = require('./lib/shaders')
var getGlyph        = require('./lib/glyphs')
var getSimpleString = require('./lib/get-simple-string')

var IDENTITY = [1,0,0,0,
                0,1,0,0,
                0,0,1,0,
                0,0,0,1]

module.exports = createPointCloud

function transformMat4(x, m) {
  var x0 = x[0]
  var x1 = x[1]
  var x2 = x[2]
  var x3 = x[3]
  x[0] = m[0] * x0 + m[4] * x1 + m[8]  * x2 + m[12] * x3
  x[1] = m[1] * x0 + m[5] * x1 + m[9]  * x2 + m[13] * x3
  x[2] = m[2] * x0 + m[6] * x1 + m[10] * x2 + m[14] * x3
  x[3] = m[3] * x0 + m[7] * x1 + m[11] * x2 + m[15] * x3
  return x
}

function project(p, v, m, x) {
  transformMat4(x, x, m)
  transformMat4(x, x, v)
  return transformMat4(x, x, p)
}

function ScatterPlotPickResult(index, position) {
  this.index = index
  this.dataCoordinate = this.position = position
}

function fixOpacity(a) {
  if(a === true) return 1
  if(a > 1) return 1
  return a
}

function PointCloud(
  gl,
  shader,
  orthoShader,
  projectShader,
  pointBuffer,
  colorBuffer,
  glyphBuffer,
  idBuffer,
  vao,
  pickPerspectiveShader,
  pickOrthoShader,
  pickProjectShader) {

  this.gl              = gl

  this.pixelRatio      = 1

  this.shader          = shader
  this.orthoShader     = orthoShader
  this.projectShader   = projectShader

  this.pointBuffer     = pointBuffer
  this.colorBuffer     = colorBuffer
  this.glyphBuffer     = glyphBuffer
  this.idBuffer        = idBuffer
  this.vao             = vao
  this.vertexCount     = 0
  this.lineVertexCount = 0

  this.opacity         = 1
  this.hasAlpha        = false

  this.lineWidth       = 0
  this.projectScale    = [2.0/3.0, 2.0/3.0, 2.0/3.0]
  this.projectOpacity  = [1, 1, 1]
  this.projectHasAlpha  = false

  this.pickId                = 0
  this.pickPerspectiveShader = pickPerspectiveShader
  this.pickOrthoShader       = pickOrthoShader
  this.pickProjectShader     = pickProjectShader
  this.points                = []

  this._selectResult = new ScatterPlotPickResult(0, [0,0,0])

  this.useOrtho = true
  this.bounds   = [[ Infinity,Infinity,Infinity],
                   [-Infinity,-Infinity,-Infinity]]

  //Axes projections
  this.axesProject = [ true, true, true ]
  this.axesBounds = [[-Infinity,-Infinity,-Infinity],
                     [ Infinity, Infinity, Infinity]]

  this.highlightId    = [1,1,1,1]
  this.highlightScale = 2

  this.clipBounds = [[-Infinity,-Infinity,-Infinity],
                     [ Infinity, Infinity, Infinity]]

  this.dirty = true
}

var proto = PointCloud.prototype

proto.pickSlots = 1

proto.setPickBase = function(pickBase) {
  this.pickId = pickBase
}

proto.isTransparent = function() {
  if(this.hasAlpha)  {
    return true
  }
  for(var i=0; i<3; ++i) {
    if(this.axesProject[i] && this.projectHasAlpha) {
      return true
    }
  }
  return false
}

proto.isOpaque = function() {
  if(!this.hasAlpha)  {
    return true
  }
  for(var i=0; i<3; ++i) {
    if(this.axesProject[i] && !this.projectHasAlpha) {
      return true
    }
  }
  return false
}

var VIEW_SHAPE = [0,0]
var U_VEC = [0,0,0]
var V_VEC = [0,0,0]
var MU_VEC = [0,0,0,1]
var MV_VEC = [0,0,0,1]
var SCRATCH_MATRIX = IDENTITY.slice()
var SCRATCH_VEC = [0,0,0]
var CLIP_BOUNDS = [[0,0,0], [0,0,0]]

function zeroVec(a) {
  a[0] = a[1] = a[2] = 0
  return a
}

function augment(hg, af) {
  hg[0] = af[0]
  hg[1] = af[1]
  hg[2] = af[2]
  hg[3] = 1
  return hg
}

function setComponent(out, v, i, x) {
  out[0] = v[0]
  out[1] = v[1]
  out[2] = v[2]
  out[i] = x
  return out
}

function getClipBounds(bounds) {
  var result = CLIP_BOUNDS
  for(var i=0; i<2; ++i) {
    for(var j=0; j<3; ++j) {
      result[i][j] = Math.max(Math.min(bounds[i][j], 1e8), -1e8)
    }
  }
  return result
}

function drawProject(shader, points, camera, pixelRatio) {
  var axesProject = points.axesProject

  var gl         = points.gl
  var uniforms   = shader.uniforms
  var model      = camera.model      || IDENTITY
  var view       = camera.view       || IDENTITY
  var projection = camera.projection || IDENTITY
  var bounds     = points.axesBounds
  var clipBounds = getClipBounds(points.clipBounds)

  var cubeAxis
  if(points.axes && points.axes.lastCubeProps) {
    cubeAxis = points.axes.lastCubeProps.axis
  } else {
    cubeAxis = [1,1,1]
  }

  VIEW_SHAPE[0] = 2.0/gl.drawingBufferWidth
  VIEW_SHAPE[1] = 2.0/gl.drawingBufferHeight

  shader.bind()
  uniforms.view           = view
  uniforms.projection     = projection
  uniforms.screenSize     = VIEW_SHAPE
  uniforms.highlightId    = points.highlightId
  uniforms.highlightScale = points.highlightScale
  uniforms.clipBounds     = clipBounds
  uniforms.pickGroup      = points.pickId / 255.0
  uniforms.pixelRatio     = pixelRatio

  for(var i=0; i<3; ++i) {
    if(!axesProject[i]) {
      continue
    }

    uniforms.scale          = points.projectScale[i]
    uniforms.opacity        = points.projectOpacity[i]

    //Project model matrix
    var pmodel = SCRATCH_MATRIX
    for(var j=0; j<16; ++j) {
      pmodel[j] = 0
    }
    for(var j=0; j<4; ++j) {
      pmodel[5*j] = 1
    }
    pmodel[5*i] = 0
    if(cubeAxis[i] < 0) {
      pmodel[12+i] = bounds[0][i]
    } else {
      pmodel[12+i] = bounds[1][i]
    }
    mat4mult(pmodel, model, pmodel)
    uniforms.model = pmodel

    //Compute initial axes
    var u = (i+1)%3
    var v = (i+2)%3
    var du = zeroVec(U_VEC)
    var dv = zeroVec(V_VEC)
    du[u] = 1
    dv[v] = 1

    //Align orientation relative to viewer
    var mdu = project(projection, view, model, augment(MU_VEC, du))
    var mdv = project(projection, view, model, augment(MV_VEC, dv))
    if(Math.abs(mdu[1]) > Math.abs(mdv[1])) {
      var tmp = mdu
      mdu = mdv
      mdv = tmp
      tmp = du
      du = dv
      dv = tmp
      var t = u
      u = v
      v = t
    }
    if(mdu[0] < 0) {
      du[u] = -1
    }
    if(mdv[1] > 0) {
      dv[v] = -1
    }
    var su = 0.0
    var sv = 0.0
    for(var j=0; j<4; ++j) {
      su += Math.pow(model[4*u+j], 2)
      sv += Math.pow(model[4*v+j], 2)
    }
    du[u] /= Math.sqrt(su)
    dv[v] /= Math.sqrt(sv)
    uniforms.axes[0] = du
    uniforms.axes[1] = dv

    //Update fragment clip bounds
    uniforms.fragClipBounds[0] = setComponent(SCRATCH_VEC, clipBounds[0], i, -1e8)
    uniforms.fragClipBounds[1] = setComponent(SCRATCH_VEC, clipBounds[1], i, 1e8)

    points.vao.bind()

    //Draw interior
    points.vao.draw(gl.TRIANGLES, points.vertexCount)

    //Draw edges
    if(points.lineWidth > 0) {
      gl.lineWidth(points.lineWidth * pixelRatio)
      points.vao.draw(gl.LINES, points.lineVertexCount, points.vertexCount)
    }

    points.vao.unbind()
  }
}


var NEG_INFINITY3 = [-1e8, -1e8, -1e8]
var POS_INFINITY3 = [1e8, 1e8, 1e8]
var CLIP_GROUP    = [NEG_INFINITY3, POS_INFINITY3]

function drawFull(shader, pshader, points, camera, pixelRatio, transparent, forceDraw) {
  var gl = points.gl

  if(transparent === points.projectHasAlpha || forceDraw) {
    drawProject(pshader, points, camera, pixelRatio)
  }

  if(transparent === points.hasAlpha || forceDraw) {

    shader.bind()
    var uniforms = shader.uniforms

    uniforms.model      = camera.model      || IDENTITY
    uniforms.view       = camera.view       || IDENTITY
    uniforms.projection = camera.projection || IDENTITY

    VIEW_SHAPE[0]       = 2.0/gl.drawingBufferWidth
    VIEW_SHAPE[1]       = 2.0/gl.drawingBufferHeight
    uniforms.screenSize = VIEW_SHAPE

    uniforms.highlightId    = points.highlightId
    uniforms.highlightScale = points.highlightScale

    uniforms.fragClipBounds = CLIP_GROUP
    uniforms.clipBounds     = points.axes.bounds

    uniforms.opacity    = points.opacity
    uniforms.pickGroup  = points.pickId / 255.0

    uniforms.pixelRatio = pixelRatio

    points.vao.bind()

    //Draw interior
    points.vao.draw(gl.TRIANGLES, points.vertexCount)

    //Draw edges
    if(points.lineWidth > 0) {
      gl.lineWidth(points.lineWidth * pixelRatio)
      points.vao.draw(gl.LINES, points.lineVertexCount, points.vertexCount)
    }

    points.vao.unbind()
  }


}

proto.draw = function(camera) {
  var shader = this.useOrtho ? this.orthoShader : this.shader
  drawFull(shader, this.projectShader, this, camera, this.pixelRatio, false, false)
}

proto.drawTransparent = function(camera) {
  var shader = this.useOrtho ? this.orthoShader : this.shader
  drawFull(shader, this.projectShader, this, camera, this.pixelRatio, true, false)
}

proto.drawPick = function(camera) {
  var shader = this.useOrtho ? this.pickOrthoShader : this.pickPerspectiveShader
  drawFull(shader, this.pickProjectShader, this, camera, 1, true, true)
}

proto.pick = function(selected) {
  if(!selected) {
    return null
  }
  if(selected.id !== this.pickId) {
    return null
  }
  var x = selected.value[2] + (selected.value[1]<<8) + (selected.value[0]<<16)
  if(x >= this.pointCount || x < 0) {
    return null
  }

  //Unpack result
  var coord = this.points[x]
  var result = this._selectResult
  result.index = x
  for(var i=0; i<3; ++i) {
    result.position[i] = result.dataCoordinate[i] = coord[i]
  }
  return result
}

proto.highlight = function(selection) {
  if(!selection) {
    this.highlightId = [1,1,1,1]
  } else {
    var pointId = selection.index
    var a0 =  pointId     &0xff
    var a1 = (pointId>>8) &0xff
    var a2 = (pointId>>16)&0xff
    this.highlightId = [a0/255.0, a1/255.0, a2/255.0, 0]
  }
}

function get_glyphData(glyphs, index, font, pixelRatio) {
  var str

  // use the data if presented in an array
  if(Array.isArray(glyphs)) {
    if(index < glyphs.length) {
      str = glyphs[index]
    } else {
      str = undefined
    }
  } else {
    str = glyphs
  }

  str = getSimpleString(str) // this would handle undefined cases

  var visible = true
  if(isAllBlank(str)) {
    str = '▼' // Note: this special character may have minimum number of surfaces
    visible = false
  }

  var glyph = getGlyph(str, font, pixelRatio)

  return { mesh:glyph[0],
          lines:glyph[1],
         bounds:glyph[2],
        visible:visible };
}



proto.update = function(options) {

  options = options || {}

  if('perspective' in options) {
    this.useOrtho = !options.perspective
  }
  if('orthographic' in options) {
    this.useOrtho = !!options.orthographic
  }
  if('lineWidth' in options) {
    this.lineWidth = options.lineWidth
  }
  if('project' in options) {
    if(Array.isArray(options.project)) {
      this.axesProject = options.project
    } else {
      var v = !!options.project
      this.axesProject = [v,v,v]
    }
  }
  if('projectScale' in options) {
    if(Array.isArray(options.projectScale)) {
      this.projectScale = options.projectScale.slice()
    } else {
      var s = +options.projectScale
      this.projectScale = [s,s,s]
    }
  }

  this.projectHasAlpha = false // default to no transparent draw
  if('projectOpacity' in options) {
    if(Array.isArray(options.projectOpacity)) {
      this.projectOpacity = options.projectOpacity.slice()
    } else {
      var s = +options.projectOpacity
      this.projectOpacity = [s,s,s]
    }
    for(var i=0; i<3; ++i) {
      this.projectOpacity[i] = fixOpacity(this.projectOpacity[i]);
      if(this.projectOpacity[i] < 1) {
        this.projectHasAlpha = true;
      }
    }
  }

  this.hasAlpha = false // default to no transparent draw
  if('opacity' in options) {
    this.opacity = fixOpacity(options.opacity)
    if(this.opacity < 1) {
      this.hasAlpha = true;
    }
  }

  //Set dirty flag
  this.dirty = true

  //Create new buffers
  var points = options.position

  //Text font
  var font      = options.font      || 'normal'
  var alignment = options.alignment || [0,0]

  var alignmentX;
  var alignmentY;
  if (alignment.length === 2) {
    alignmentX = alignment[0]
    alignmentY = alignment[1]
  } else {
    alignmentX = []
    alignmentY = []
    for (var i = 0; i < alignment.length; ++i) {
      alignmentX[i] = alignment[i][0]
      alignmentY[i] = alignment[i][1]
    }
  }

  //Bounds
  var lowerBound = [ Infinity, Infinity, Infinity]
  var upperBound = [-Infinity,-Infinity,-Infinity]

  //Unpack options
  var glyphs     = options.glyph
  var colors     = options.color
  var sizes      = options.size
  var angles     = options.angle
  var lineColors = options.lineColor

  //Picking geometry
  var pickCounter = -1

  //First do pass to compute buffer sizes
  var triVertexCount  = 0
  var lineVertexCount = 0

  var numPoints = 0;

  if(points.length) {

    //Count number of points and buffer size
    numPoints = points.length

  count_loop:
    for(var i=0; i<numPoints; ++i) {
      var x = points[i]
      for(var j=0; j<3; ++j) {
        if(isNaN(x[j]) || !isFinite(x[j])) {
          continue count_loop
        }
      }

      var glyphData = get_glyphData(glyphs, i, font, this.pixelRatio)

      var glyphMesh   = glyphData.mesh
      var glyphLines  = glyphData.lines
      var glyphBounds = glyphData.bounds

      triVertexCount  += glyphMesh.cells.length * 3
      lineVertexCount += glyphLines.edges.length * 2
    }
  }

  var vertexCount   = triVertexCount + lineVertexCount

  //Preallocate data
  var positionArray = pool.mallocFloat(3*vertexCount)
  var colorArray    = pool.mallocFloat(4*vertexCount)
  var glyphArray    = pool.mallocFloat(2*vertexCount)
  var idArray       = pool.mallocUint32(vertexCount)

  if(vertexCount > 0) {
    var triOffset  = 0
    var lineOffset = triVertexCount
    var color      = [0,0,0,1]
    var lineColor  = [0,0,0,1]

    var isColorArray      = Array.isArray(colors)     && Array.isArray(colors[0])
    var isLineColorArray  = Array.isArray(lineColors) && Array.isArray(lineColors[0])

  fill_loop:
    for(var i=0; i<numPoints; ++i) {
      //Increment pickCounter
      pickCounter += 1

      var x = points[i]
      for(var j=0; j<3; ++j) {
        if(isNaN(x[j]) || !isFinite(x[j])) {
          continue fill_loop
        }

        upperBound[j] = Math.max(upperBound[j], x[j])
        lowerBound[j] = Math.min(lowerBound[j], x[j])
      }

      var glyphData = get_glyphData(glyphs, i, font, this.pixelRatio)

      var glyphMesh   = glyphData.mesh
      var glyphLines  = glyphData.lines
      var glyphBounds = glyphData.bounds
      var glyphVisible = glyphData.visible

      //Get color
      if(!glyphVisible) color = [1,1,1,0]
      else if(Array.isArray(colors)) {
        var c
        if(isColorArray) {
          if(i < colors.length) {
            c = colors[i]
          } else {
            c = [0,0,0,0]
          }
        } else {
          c = colors
        }

        if(c.length === 3) {
          for(var j=0; j<3; ++j) {
            color[j] = c[j]
          }
          color[3] = 1
        } else if(c.length === 4) {
          for(var j=0; j<4; ++j) {
            color[j] = c[j]
          }
          if(!this.hasAlpha && c[3] < 1) this.hasAlpha = true
        }
      } else {
        color[0] = color[1] = color[2] = 0
        color[3] = 1
      }


      //Get lineColor
      if(!glyphVisible) lineColor = [1,1,1,0]
      else if(Array.isArray(lineColors)) {
        var c
        if(isLineColorArray) {
          if(i < lineColors.length) {
            c = lineColors[i]
          } else {
            c = [0,0,0,0]
          }
        } else {
          c = lineColors
        }

        if(c.length === 3) {
          for(var j=0; j<3; ++j) {
            lineColor[j] = c[j]
          }
          lineColor[j] = 1
        } else if(c.length === 4) {
          for(var j=0; j<4; ++j) {
            lineColor[j] = c[j]
          }
          if(!this.hasAlpha && c[3] < 1) this.hasAlpha = true
        }
      } else {
        lineColor[0] = lineColor[1] = lineColor[2] = 0
        lineColor[3] = 1
      }


      var size = 0.5
      if(!glyphVisible) size = 0.0
      else if(Array.isArray(sizes)) {
        if(i < sizes.length) {
          size = +sizes[i]
        } else {
          size = 12
        }
      } else if(sizes) {
        size = +sizes
      } else if(this.useOrtho) {
        size = 12
      }


      var angle = 0
      if(Array.isArray(angles)) {
        if(i < angles.length) {
          angle = +angles[i]
        } else {
          angle = 0
        }
      } else if(angles) {
        angle = +angles
      }

      //Loop through markers and append to buffers
      var cos = Math.cos(angle)
      var sin = Math.sin(angle)

      var x = points[i]
      for(var j=0; j<3; ++j) {
        upperBound[j] = Math.max(upperBound[j], x[j])
        lowerBound[j] = Math.min(lowerBound[j], x[j])
      }

      //Calculate text offset
      var textOffsetX = alignmentX
      var textOffsetY = alignmentY

      var textOffsetX = 0
      if(Array.isArray(alignmentX)) {
        if(i < alignmentX.length) {
          textOffsetX = alignmentX[i]
        } else {
          textOffsetX = 0
        }
      } else if(alignmentX) {
        textOffsetX = alignmentX
      }

      var textOffsetY = 0
      if(Array.isArray(alignmentY)) {
        if(i < alignmentY.length) {
          textOffsetY = alignmentY[i]
        } else {
          textOffsetY = 0
        }
      } else if(alignmentY) {
        textOffsetY = alignmentY
      }

      textOffsetX *= (textOffsetX > 0) ? (1 - glyphBounds[0][0]) :
                     (textOffsetX < 0) ? (1 + glyphBounds[1][0]) : 1;

      textOffsetY *= (textOffsetY > 0) ? (1 - glyphBounds[0][1]) :
                     (textOffsetY < 0) ? (1 + glyphBounds[1][1]) : 1;

      var textOffset = [textOffsetX, textOffsetY]

      //Write out inner marker
      var cells = glyphMesh.cells || []
      var verts = glyphMesh.positions || []

      for(var j=0; j<cells.length; ++j) {
        var cell = cells[j]
        for(var k=0; k<3; ++k) {
          for(var l=0; l<3; ++l) {
            positionArray[3*triOffset+l] = x[l]
          }
          for(var l=0; l<4; ++l) {
            colorArray[4*triOffset+l] = color[l]
          }
          idArray[triOffset] = pickCounter
          var p = verts[cell[k]]
          glyphArray[2*triOffset]   = size * (cos*p[0] - sin*p[1] + textOffset[0])
          glyphArray[2*triOffset+1] = size * (sin*p[0] + cos*p[1] + textOffset[1])
          triOffset += 1
        }
      }

      var cells = glyphLines.edges
      var verts = glyphLines.positions

      for(var j=0; j<cells.length; ++j) {
        var cell = cells[j]
        for(var k=0; k<2; ++k) {
          for(var l=0; l<3; ++l) {
            positionArray[3*lineOffset+l] = x[l]
          }
          for(var l=0; l<4; ++l) {
            colorArray[4*lineOffset+l] = lineColor[l]
          }
          idArray[lineOffset] = pickCounter
          var p = verts[cell[k]]
          glyphArray[2*lineOffset]   = size * (cos*p[0] - sin*p[1] + textOffset[0])
          glyphArray[2*lineOffset+1] = size * (sin*p[0] + cos*p[1] + textOffset[1])
          lineOffset += 1
        }
      }

    }



  }

  //Update bounds
  this.bounds = [lowerBound, upperBound]

  //Save points
  this.points = points

  //Save number of points
  this.pointCount = points.length

  //Update vertex counts
  this.vertexCount      = triVertexCount
  this.lineVertexCount  = lineVertexCount

  this.pointBuffer.update(positionArray)
  this.colorBuffer.update(colorArray)
  this.glyphBuffer.update(glyphArray)
  //this.idBuffer.update(new Uint32Array(idArray))
  this.idBuffer.update(idArray)

  pool.free(positionArray)
  pool.free(colorArray)
  pool.free(glyphArray)
  pool.free(idArray)
}

proto.dispose = function() {
  //Shaders
  this.shader.dispose()
  this.orthoShader.dispose()
  this.pickPerspectiveShader.dispose()
  this.pickOrthoShader.dispose()

  //Vertex array
  this.vao.dispose()

  //Buffers
  this.pointBuffer.dispose()
  this.colorBuffer.dispose()
  this.glyphBuffer.dispose()
  this.idBuffer.dispose()
}

function createPointCloud(options) {
  var gl = options.gl

  var shader                = shaders.createPerspective(gl)
  var orthoShader           = shaders.createOrtho(gl)
  var projectShader         = shaders.createProject(gl)
  var pickPerspectiveShader = shaders.createPickPerspective(gl)
  var pickOrthoShader       = shaders.createPickOrtho(gl)
  var pickProjectShader     = shaders.createPickProject(gl)

  var pointBuffer = createBuffer(gl)
  var colorBuffer = createBuffer(gl)
  var glyphBuffer = createBuffer(gl)
  var idBuffer    = createBuffer(gl)
  var vao = createVAO(gl, [
    {
      buffer: pointBuffer,
      size: 3,
      type: gl.FLOAT
    },
    {
      buffer: colorBuffer,
      size: 4,
      type: gl.FLOAT
    },
    {
      buffer: glyphBuffer,
      size: 2,
      type: gl.FLOAT
    },
    {
      buffer: idBuffer,
      size: 4,
      type: gl.UNSIGNED_BYTE,
      normalized: true
    }
  ])

  var pointCloud = new PointCloud(
    gl,
    shader,
    orthoShader,
    projectShader,
    pointBuffer,
    colorBuffer,
    glyphBuffer,
    idBuffer,
    vao,
    pickPerspectiveShader,
    pickOrthoShader,
    pickProjectShader)

  pointCloud.update(options)

  return pointCloud
}
