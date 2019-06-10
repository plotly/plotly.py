'use strict'

var createTexture = require('gl-texture2d')

module.exports = createFBO

var colorAttachmentArrays = null
var FRAMEBUFFER_UNSUPPORTED
var FRAMEBUFFER_INCOMPLETE_ATTACHMENT
var FRAMEBUFFER_INCOMPLETE_DIMENSIONS
var FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT

function saveFBOState(gl) {
  var fbo = gl.getParameter(gl.FRAMEBUFFER_BINDING)
  var rbo = gl.getParameter(gl.RENDERBUFFER_BINDING)
  var tex = gl.getParameter(gl.TEXTURE_BINDING_2D)
  return [fbo, rbo, tex]
}

function restoreFBOState(gl, data) {
  gl.bindFramebuffer(gl.FRAMEBUFFER, data[0])
  gl.bindRenderbuffer(gl.RENDERBUFFER, data[1])
  gl.bindTexture(gl.TEXTURE_2D, data[2])
}

function lazyInitColorAttachments(gl, ext) {
  var maxColorAttachments = gl.getParameter(ext.MAX_COLOR_ATTACHMENTS_WEBGL)
  colorAttachmentArrays = new Array(maxColorAttachments + 1)
  for(var i=0; i<=maxColorAttachments; ++i) {
    var x = new Array(maxColorAttachments)
    for(var j=0; j<i; ++j) {
      x[j] = gl.COLOR_ATTACHMENT0 + j
    }
    for(var j=i; j<maxColorAttachments; ++j) {
      x[j] = gl.NONE
    }
    colorAttachmentArrays[i] = x
  }
}

//Throw an appropriate error
function throwFBOError(status) {
  switch(status){
    case FRAMEBUFFER_UNSUPPORTED:
      throw new Error('gl-fbo: Framebuffer unsupported')
    case FRAMEBUFFER_INCOMPLETE_ATTACHMENT:
      throw new Error('gl-fbo: Framebuffer incomplete attachment')
    case FRAMEBUFFER_INCOMPLETE_DIMENSIONS:
      throw new Error('gl-fbo: Framebuffer incomplete dimensions')
    case FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT:
      throw new Error('gl-fbo: Framebuffer incomplete missing attachment')
    default:
      throw new Error('gl-fbo: Framebuffer failed for unspecified reason')
  }
}

//Initialize a texture object
function initTexture(gl, width, height, type, format, attachment) {
  if(!type) {
    return null
  }
  var result = createTexture(gl, width, height, format, type)
  result.magFilter = gl.NEAREST
  result.minFilter = gl.NEAREST
  result.mipSamples = 1
  result.bind()
  gl.framebufferTexture2D(gl.FRAMEBUFFER, attachment, gl.TEXTURE_2D, result.handle, 0)
  return result
}

//Initialize a render buffer object
function initRenderBuffer(gl, width, height, component, attachment) {
  var result = gl.createRenderbuffer()
  gl.bindRenderbuffer(gl.RENDERBUFFER, result)
  gl.renderbufferStorage(gl.RENDERBUFFER, component, width, height)
  gl.framebufferRenderbuffer(gl.FRAMEBUFFER, attachment, gl.RENDERBUFFER, result)
  return result
}

//Rebuild the frame buffer
function rebuildFBO(fbo) {

  //Save FBO state
  var state = saveFBOState(fbo.gl)

  var gl = fbo.gl
  var handle = fbo.handle = gl.createFramebuffer()
  var width = fbo._shape[0]
  var height = fbo._shape[1]
  var numColors = fbo.color.length
  var ext = fbo._ext
  var useStencil = fbo._useStencil
  var useDepth = fbo._useDepth
  var colorType = fbo._colorType

  //Bind the fbo
  gl.bindFramebuffer(gl.FRAMEBUFFER, handle)

  //Allocate color buffers
  for(var i=0; i<numColors; ++i) {
    fbo.color[i] = initTexture(gl, width, height, colorType, gl.RGBA, gl.COLOR_ATTACHMENT0 + i)
  }
  if(numColors === 0) {
    fbo._color_rb = initRenderBuffer(gl, width, height, gl.RGBA4, gl.COLOR_ATTACHMENT0)
    if(ext) {
      ext.drawBuffersWEBGL(colorAttachmentArrays[0])
    }
  } else if(numColors > 1) {
    ext.drawBuffersWEBGL(colorAttachmentArrays[numColors])
  }

  //Allocate depth/stencil buffers
  var WEBGL_depth_texture = gl.getExtension('WEBGL_depth_texture')
  if(WEBGL_depth_texture) {
    if(useStencil) {
      fbo.depth = initTexture(gl, width, height,
                          WEBGL_depth_texture.UNSIGNED_INT_24_8_WEBGL,
                          gl.DEPTH_STENCIL,
                          gl.DEPTH_STENCIL_ATTACHMENT)
    } else if(useDepth) {
      fbo.depth = initTexture(gl, width, height,
                          gl.UNSIGNED_SHORT,
                          gl.DEPTH_COMPONENT,
                          gl.DEPTH_ATTACHMENT)
    }
  } else {
    if(useDepth && useStencil) {
      fbo._depth_rb = initRenderBuffer(gl, width, height, gl.DEPTH_STENCIL, gl.DEPTH_STENCIL_ATTACHMENT)
    } else if(useDepth) {
      fbo._depth_rb = initRenderBuffer(gl, width, height, gl.DEPTH_COMPONENT16, gl.DEPTH_ATTACHMENT)
    } else if(useStencil) {
      fbo._depth_rb = initRenderBuffer(gl, width, height, gl.STENCIL_INDEX, gl.STENCIL_ATTACHMENT)
    }
  }

  //Check frame buffer state
  var status = gl.checkFramebufferStatus(gl.FRAMEBUFFER)
  if(status !== gl.FRAMEBUFFER_COMPLETE) {

    //Release all partially allocated resources
    fbo._destroyed = true

    //Release all resources
    gl.bindFramebuffer(gl.FRAMEBUFFER, null)
    gl.deleteFramebuffer(fbo.handle)
    fbo.handle = null
    if(fbo.depth) {
      fbo.depth.dispose()
      fbo.depth = null
    }
    if(fbo._depth_rb) {
      gl.deleteRenderbuffer(fbo._depth_rb)
      fbo._depth_rb = null
    }
    for(var i=0; i<fbo.color.length; ++i) {
      fbo.color[i].dispose()
      fbo.color[i] = null
    }
    if(fbo._color_rb) {
      gl.deleteRenderbuffer(fbo._color_rb)
      fbo._color_rb = null
    }

    restoreFBOState(gl, state)

    //Throw the frame buffer error
    throwFBOError(status)
  }

  //Everything ok, let's get on with life
  restoreFBOState(gl, state)
}

function Framebuffer(gl, width, height, colorType, numColors, useDepth, useStencil, ext) {

  //Handle and set properties
  this.gl = gl
  this._shape = [width|0, height|0]
  this._destroyed = false
  this._ext = ext

  //Allocate buffers
  this.color = new Array(numColors)
  for(var i=0; i<numColors; ++i) {
    this.color[i] = null
  }
  this._color_rb = null
  this.depth = null
  this._depth_rb = null

  //Save depth and stencil flags
  this._colorType = colorType
  this._useDepth = useDepth
  this._useStencil = useStencil

  //Shape vector for resizing
  var parent = this
  var shapeVector = [width|0, height|0]
  Object.defineProperties(shapeVector, {
    0: {
      get: function() {
        return parent._shape[0]
      },
      set: function(w) {
        return parent.width = w
      }
    },
    1: {
      get: function() {
        return parent._shape[1]
      },
      set: function(h) {
        return parent.height = h
      }
    }
  })
  this._shapeVector = shapeVector

  //Initialize all attachments
  rebuildFBO(this)
}

var proto = Framebuffer.prototype

function reshapeFBO(fbo, w, h) {
  //If fbo is invalid, just skip this
  if(fbo._destroyed) {
    throw new Error('gl-fbo: Can\'t resize destroyed FBO')
  }

  //Don't resize if no change in shape
  if( (fbo._shape[0] === w) &&
      (fbo._shape[1] === h) ) {
    return
  }

  var gl = fbo.gl

  //Check parameter ranges
  var maxFBOSize = gl.getParameter(gl.MAX_RENDERBUFFER_SIZE)
  if( w < 0 || w > maxFBOSize ||
      h < 0 || h > maxFBOSize) {
    throw new Error('gl-fbo: Can\'t resize FBO, invalid dimensions')
  }

  //Update shape
  fbo._shape[0] = w
  fbo._shape[1] = h

  //Save framebuffer state
  var state = saveFBOState(gl)

  //Resize framebuffer attachments
  for(var i=0; i<fbo.color.length; ++i) {
    fbo.color[i].shape = fbo._shape
  }
  if(fbo._color_rb) {
    gl.bindRenderbuffer(gl.RENDERBUFFER, fbo._color_rb)
    gl.renderbufferStorage(gl.RENDERBUFFER, gl.RGBA4, fbo._shape[0], fbo._shape[1])
  }
  if(fbo.depth) {
    fbo.depth.shape = fbo._shape
  }
  if(fbo._depth_rb) {
    gl.bindRenderbuffer(gl.RENDERBUFFER, fbo._depth_rb)
    if(fbo._useDepth && fbo._useStencil) {
      gl.renderbufferStorage(gl.RENDERBUFFER, gl.DEPTH_STENCIL, fbo._shape[0], fbo._shape[1])
    } else if(fbo._useDepth) {
      gl.renderbufferStorage(gl.RENDERBUFFER, gl.DEPTH_COMPONENT16, fbo._shape[0], fbo._shape[1])
    } else if(fbo._useStencil) {
      gl.renderbufferStorage(gl.RENDERBUFFER, gl.STENCIL_INDEX, fbo._shape[0], fbo._shape[1])
    }
  }

  //Check FBO status after resize, if something broke then die in a fire
  gl.bindFramebuffer(gl.FRAMEBUFFER, fbo.handle)
  var status = gl.checkFramebufferStatus(gl.FRAMEBUFFER)
  if(status !== gl.FRAMEBUFFER_COMPLETE) {
    fbo.dispose()
    restoreFBOState(gl, state)
    throwFBOError(status)
  }

  //Restore framebuffer state
  restoreFBOState(gl, state)
}

Object.defineProperties(proto, {
  'shape': {
    get: function() {
      if(this._destroyed) {
        return [0,0]
      }
      return this._shapeVector
    },
    set: function(x) {
      if(!Array.isArray(x)) {
        x = [x|0, x|0]
      }
      if(x.length !== 2) {
        throw new Error('gl-fbo: Shape vector must be length 2')
      }

      var w = x[0]|0
      var h = x[1]|0
      reshapeFBO(this, w, h)

      return [w, h]
    },
    enumerable: false
  },
  'width': {
    get: function() {
      if(this._destroyed) {
        return 0
      }
      return this._shape[0]
    },
    set: function(w) {
      w = w|0
      reshapeFBO(this, w, this._shape[1])
      return w
    },
    enumerable: false
  },
  'height': {
    get: function() {
      if(this._destroyed) {
        return 0
      }
      return this._shape[1]
    },
    set: function(h) {
      h = h|0
      reshapeFBO(this, this._shape[0], h)
      return h
    },
    enumerable: false
  }
})

proto.bind = function() {
  if(this._destroyed) {
    return
  }
  var gl = this.gl
  gl.bindFramebuffer(gl.FRAMEBUFFER, this.handle)
  gl.viewport(0, 0, this._shape[0], this._shape[1])
}

proto.dispose = function() {
  if(this._destroyed) {
    return
  }
  this._destroyed = true
  var gl = this.gl
  gl.deleteFramebuffer(this.handle)
  this.handle = null
  if(this.depth) {
    this.depth.dispose()
    this.depth = null
  }
  if(this._depth_rb) {
    gl.deleteRenderbuffer(this._depth_rb)
    this._depth_rb = null
  }
  for(var i=0; i<this.color.length; ++i) {
    this.color[i].dispose()
    this.color[i] = null
  }
  if(this._color_rb) {
    gl.deleteRenderbuffer(this._color_rb)
    this._color_rb = null
  }
}

function createFBO(gl, width, height, options) {

  //Update frame buffer error code values
  if(!FRAMEBUFFER_UNSUPPORTED) {
    FRAMEBUFFER_UNSUPPORTED = gl.FRAMEBUFFER_UNSUPPORTED
    FRAMEBUFFER_INCOMPLETE_ATTACHMENT = gl.FRAMEBUFFER_INCOMPLETE_ATTACHMENT
    FRAMEBUFFER_INCOMPLETE_DIMENSIONS = gl.FRAMEBUFFER_INCOMPLETE_DIMENSIONS
    FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = gl.FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT
  }

  //Lazily initialize color attachment arrays
  var WEBGL_draw_buffers = gl.getExtension('WEBGL_draw_buffers')
  if(!colorAttachmentArrays && WEBGL_draw_buffers) {
    lazyInitColorAttachments(gl, WEBGL_draw_buffers)
  }

  //Special case: Can accept an array as argument
  if(Array.isArray(width)) {
    options = height
    height = width[1]|0
    width = width[0]|0
  }

  if(typeof width !== 'number') {
    throw new Error('gl-fbo: Missing shape parameter')
  }

  //Validate width/height properties
  var maxFBOSize = gl.getParameter(gl.MAX_RENDERBUFFER_SIZE)
  if(width < 0 || width > maxFBOSize || height < 0 || height > maxFBOSize) {
    throw new Error('gl-fbo: Parameters are too large for FBO')
  }

  //Handle each option type
  options = options || {}

  //Figure out number of color buffers to use
  var numColors = 1
  if('color' in options) {
    numColors = Math.max(options.color|0, 0)
    if(numColors < 0) {
      throw new Error('gl-fbo: Must specify a nonnegative number of colors')
    }
    if(numColors > 1) {
      //Check if multiple render targets supported
      if(!WEBGL_draw_buffers) {
        throw new Error('gl-fbo: Multiple draw buffer extension not supported')
      } else if(numColors > gl.getParameter(WEBGL_draw_buffers.MAX_COLOR_ATTACHMENTS_WEBGL)) {
        throw new Error('gl-fbo: Context does not support ' + numColors + ' draw buffers')
      }
    }
  }

  //Determine whether to use floating point textures
  var colorType = gl.UNSIGNED_BYTE
  var OES_texture_float = gl.getExtension('OES_texture_float')
  if(options.float && numColors > 0) {
    if(!OES_texture_float) {
      throw new Error('gl-fbo: Context does not support floating point textures')
    }
    colorType = gl.FLOAT
  } else if(options.preferFloat && numColors > 0) {
    if(OES_texture_float) {
      colorType = gl.FLOAT
    }
  }

  //Check if we should use depth buffer
  var useDepth = true
  if('depth' in options) {
    useDepth = !!options.depth
  }

  //Check if we should use a stencil buffer
  var useStencil = false
  if('stencil' in options) {
    useStencil = !!options.stencil
  }

  return new Framebuffer(
    gl,
    width,
    height,
    colorType,
    numColors,
    useDepth,
    useStencil,
    WEBGL_draw_buffers)
}
