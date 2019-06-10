"use strict"

module.exports = createGLStateStack

var uniq = require("uniq")

function createGLStateStack(gl, variables) {
  //By default SAVE EVERYTHING
  if(!variables) {
    variables = [
      gl.ACTIVE_TEXTURE,
      gl.ARRAY_BUFFER_BINDING,
      gl.BLEND,
      gl.BLEND_COLOR,
      gl.BLEND_SRC_ALPHA,
      gl.BLEND_SRC_RGB,
      gl.BLEND_DST_ALPHA,
      gl.BLEND_DST_RGB,
      gl.BLEND_EQUATION_ALPHA,
      gl.BLEND_EQUATION_RGB,
      gl.COLOR_WRITEMASK,
      gl.COLOR_CLEAR_VALUE,
      gl.CULL_FACE,
      gl.CULL_FACE_MODE,
      gl.CURRENT_PROGRAM,
      gl.DEPTH_CLEAR_VALUE,
      gl.DEPTH_FUNC,
      gl.DEPTH_RANGE,
      gl.DEPTH_WRITEMASK,
      gl.DITHER,
      gl.ELEMENT_ARRAY_BUFFER_BINDING,
      gl.FRAMEBUFFER_BINDING,
      gl.FRONT_FACE,
      gl.GENERATE_MIPMAP_HINT,
      gl.LINE_WIDTH,
      gl.PACK_ALIGNMENT,
      gl.POLYGON_OFFSET_FACTOR,
      gl.POLYGON_OFFSET_FILL,
      gl.POLYGON_OFFSET_UNITS,
      gl.RENDERBUFFER_BINDING,
      gl.SAMPLE_COVERAGE,
      gl.SAMPLE_COVERAGE_INVERT,
      gl.SAMPLE_COVERAGE_VALUE,
      gl.SCISSOR_BOX,
      gl.SCISSOR_TEST,
      gl.STENCIL_BACK_FAIL,
      gl.STENCIL_BACK_FUNC,
      gl.STENCIL_BACK_PASS_DEPTH_FAIL,
      gl.STENCIL_BACK_PASS_DEPTH_PASS,
      gl.STENCIL_BACK_REF,
      gl.STENCIL_BACK_VALUE_MASK,
      gl.STENCIL_BACK_WRITEMASK,
      gl.STENCIL_CLEAR_VALUE,
      gl.STENCIL_FAIL,
      gl.STENCIL_FUNC,
      gl.STENCIL_PASS_DEPTH_FAIL,
      gl.STENCIL_PASS_DEPTH_PASS,
      gl.STENCIL_REF,
      gl.STENCIL_TEST,
      gl.STENCIL_VALUE_MASK,
      gl.STENCIL_WRITEMASK,
      gl.TEXTURE,
      gl.UNPACK_ALIGNMENT,
      gl.UNPACK_COLORSPACE_CONVERSION_WEBGL,
      gl.UNPACK_FLIP_Y_WEBGL,
      gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL,
      gl.VIEWPORT
    ]
  }

  var ctorBody = [
    "'use strict'\nfunction StateStack(gl){this.gl=gl;"
  ]

  var pushBody = [
    "proto.push=function(){var gl=this.gl;"
  ]

  var popBody = [
    "proto.pop=function(){var gl=this.gl;"
  ]

  //Compute a collection of state variables
  var nvariables = variables.slice()
  nvariables.sort(function(a,b) {
    return a-b
  })
  uniq(nvariables, undefined, true)


  //Check if texture state needs to be saved
  var textureTypes = [gl.TEXTURE, 
      gl.TEXTURE_2D, 
      gl.TEXTURE_CUBE_MAP,
      gl.TEXTURE_BINDING_2D, 
      gl.TEXTURE_BINDING_CUBE_MAP]
  if(textureTypes.some(function(v) {
        return nvariables.indexOf(v) >= 0
      })) {
    //Generate code for saving texture state
    var numTextures = gl.getParameter(gl.MAX_TEXTURE_IMAGE_UNITS)
    ctorBody.push("this.textures=[];")

    //Generate save state for textures
    pushBody.push("var curTex=gl.getParameter(", gl.ACTIVE_TEXTURE, "),texState=new Array(",numTextures,");")
    for(var i=0; i<numTextures; ++i) {
      pushBody.push("gl.activeTexture(", gl.TEXTURE0+i, ");texState[",i,"]=[gl.getParameter(",
        gl.TEXTURE_BINDING_2D, "),gl.getParameter(",
        gl.TEXTURE_BINDING_CUBE_MAP, ")];")
    }
    pushBody.push("this.textures.push(texState);gl.activeTexture(curTex);")

    //Generate restore state for textures
    popBody.push("var texState=this.textures.pop();")
    var restoreActive = nvariables.indexOf(gl.ACTIVE_TEXTURE) < 0
    if(restoreActive) {
      popBody.push("var curTex=gl.getParameter(", gl.ACTIVE_TEXTURE, ");")
    }
    for(var i=0; i<numTextures; ++i) {
      popBody.push(
        "gl.activeTexture(", gl.TEXTURE0+i, ");",
        "gl.bindTexture(", gl.TEXTURE_2D, ",texState[", i, "][0]);",
        "gl.bindTexture(", gl.TEXTURE_CUBE_MAP, ",texState[", i, "][1]);")
    }
    if(restoreActive) {
      popBody.push("gl.activeTexture(curTex);")
    }
  }

  //Multiparameter state functions
  var specialVars = {
    blendEquationSeparate: [
      gl.BLEND_EQUATION_ALPHA,
      gl.BLEND_EQUATION_RGB
    ],
    blendFuncSeparate: [
      gl.BLEND_SRC_RGB,
      gl.BLEND_DST_RGB,
      gl.BLEND_SRC_ALPHA,
      gl.BLEND_DST_ALPHA
    ],
    sampleCoverage: [
      gl.SAMPLE_COVERAGE_INVERT,
      gl.SAMPLE_COVERAGE_VALUE
    ],
    polygonOffset: [
      gl.POLYGON_OFFSET_FACTOR,
      gl.POLYGON_OFFSET_UNITS
    ],
    stencilFuncSeparate_FRONT: [
      gl.STENCIL_FUNC,
      gl.STENCIL_REF,
      gl.STENCIL_VALUE_MASK
    ],
    stencilFuncSeparate_BACK: [
      gl.STENCIL_BACK_FUNC,
      gl.STENCIL_BACK_REF,
      gl.STENCIL_BACK_VALUE_MASK
    ],
    stencilOpSeparate_FRONT: [
      gl.STENCIL_FAIL,
      gl.STENCIL_PASS_DEPTH_FAIL,
      gl.STENCIL_PASS_DEPTH_PASS
    ],
    stencilOpSeparate_BACK: [
      gl.STENCIL_BACK_FAIL,
      gl.STENCIL_BACK_PASS_DEPTH_FAIL,
      gl.STENCIL_BACK_PASS_DEPTH_PASS
    ]
  }

  //Decorate all multiparameter fields
  for(var id in specialVars) {
    var params = specialVars[id]
    var variables = []
    var snippets = []
    for(var i=0; i<params.length; ++i) {
      var name = "v" + params[i]
      var snip = [name, "=gl.getParameter(", params[i], ");"].join("")
      variables.push(name)
      snippets.push(snip)

    }
    specialVars[id] = {
      present: false,
      variables: variables,
      snippets: snippets,
      parameters: params
    }
  }

main_loop:
  for(var i=0; i<nvariables.length; ++i) {
    var type = nvariables[i]
    //Textures handled separately
    if(textureTypes.indexOf(type) >= 0) {
      continue
    }
    var stateStack = "this[" + type + "]"
    ctorBody.push(stateStack, "=[];")

    //Generate save code
    switch(type) {
      case gl.SAMPLE_COVERAGE:
        //HACK: This is broken in the webgl specification
        pushBody.push(stateStack, ".push(gl.isEnabled(", gl.SAMPLE_COVERAGE, "));")
      break
      default:
        pushBody.push(stateStack, ".push(gl.getParameter(", type, "));")
      break
    }

    //Generate restore code
    var sv = stateStack + ".pop()"
    switch(type) {
      case gl.ACTIVE_TEXTURE:
        popBody.push("gl.activeTexture(", sv, ");")
      break
      case gl.ARRAY_BUFFER_BINDING:
        popBody.push("gl.bindBuffer(", gl.ARRAY_BUFFER, ",", sv, ");")
      break
      case gl.BLEND_COLOR:
        popBody.push("var c=", sv, ";gl.blendColor(c[0], c[1], c[2], c[3]);")
      break
      case gl.COLOR_CLEAR_VALUE:
        popBody.push("var c=", sv, ";gl.clearColor(c[0], c[1], c[2], c[3]);")
      break
      case gl.COLOR_WRITEMASK:
        popBody.push("var c=", sv, ";gl.colorMask(c[0], c[1], c[2], c[3]);")
      break
      case gl.CULL_FACE_MODE:
        popBody.push("gl.cullFace(", sv, ");")
      break
      case gl.CURRENT_PROGRAM:
        popBody.push("gl.useProgram(", sv, ");")
      break
      case gl.DEPTH_CLEAR_VALUE:
        popBody.push("gl.clearDepth(", sv, ");")
      break
      case gl.DEPTH_FUNC:
        popBody.push("gl.depthFunc(", sv, ");")
      break
      case gl.DEPTH_RANGE:
        popBody.push("var z=", sv, ";gl.depthRange(z[0], z[1]);")
      break
      case gl.DEPTH_WRITEMASK:
        popBody.push("gl.depthMask(", sv, ");")
      break
      case gl.ELEMENT_ARRAY_BUFFER_BINDING:
        popBody.push("gl.bindBuffer(", gl.ELEMENT_ARRAY_BUFFER, ",", sv, ");")
      break
      case gl.FRAMEBUFFER_BINDING:
        popBody.push("gl.bindFramebuffer(", gl.FRAMEBUFFER, ",", sv, ");")
      break
      case gl.FRONT_FACE:
        popBody.push("gl.frontFace(", sv, ");")
      break
      case gl.LINE_WIDTH:
        popBody.push("gl.lineWidth(", sv, ");")
      break
      case gl.RENDERBUFFER_BINDING:
        popBody.push("gl.bindRenderbuffer(", gl.RENDERBUFFER, ",", sv, ");")
      break
      case gl.SCISSOR_BOX:
        popBody.push("var c=", sv, ";gl.scissor(c[0],c[1],c[2],c[3]);")
      break
      case gl.STENCIL_WRITEMASK:
        popBody.push("gl.stencilMaskSeparate(", gl.FRONT, ",", sv, ");")
      break
      case gl.STENCIL_BACK_WRITEMASK:
        popBody.push("gl.stencilMaskSeparate(", gl.BACK, ",", sv, ");")
      break
      case gl.STENCIL_CLEAR_VALUE:
        popBody.push("gl.clearStencil(", sv, ");")
      break
      case gl.VIEWPORT:
        popBody.push("var c=", sv, ";gl.viewport(c[0],c[1],c[2],c[3]);")
      break

      //Pixel storage
      case gl.PACK_ALIGNMENT:
      case gl.UNPACK_ALIGNMENT:
      case gl.UNPACK_COLORSPACE_CONVERSION_WEBGL:
      case gl.UNPACK_FLIP_Y_WEBGL:
      case gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL:
        popBody.push("gl.pixelStorei(", type, ",", sv, ");")
      break

      //Flags
      case gl.BLEND:
      case gl.CULL_FACE:
      case gl.DEPTH_TEST:
      case gl.DITHER:
      case gl.POLYGON_OFFSET_FILL:
      case gl.SAMPLE_COVERAGE:
      case gl.SCISSOR_TEST:
      case gl.STENCIL_TEST:
        popBody.push("if(", sv, "){gl.enable(", type, ")}else{gl.disable(", type, ")}")
      break

      //Hints
      case gl.GENERATE_MIPMAP_HINT:
        popBody.push("gl.hint(", type, ",", sv, ");")
      break

      default:
        //Check if special variable present
        for(var id in specialVars) {
          var special = specialVars[id]
          var index = special.parameters.indexOf(type)
          if(index < 0) {
            continue
          }
          special.present = true
          special.snippets[index] = "var " + special.variables[index] + "=" + sv + ";"
          continue main_loop
        }
        throw new Error("gl-state: Error, unknown state parameter " + type)
    }
  }

  //Handle multiparameter functions
  for(var id in specialVars) {
    var data = specialVars[id]
    if(data.present) {
      popBody.push.apply(popBody, data.snippets)
      var parts = id.split("_")
      if(parts.length === 1) {
        popBody.push("gl.", parts[0], "(", data.variables.join(","), ");")
      } else {
        popBody.push("gl.", parts[0], "(gl.", parts[1], ",", data.variables.join(","), ");")
      }
    }
  }

  //Compile procedure
  var code = [ctorBody.join(""),
    "};var proto=StateStack.prototype;",
    pushBody.join(""), "};",
    popBody.join(""), "};",
    "return new StateStack(gl);"].join("")
  var proc = new Function("gl", code)
  return proc(gl)
}