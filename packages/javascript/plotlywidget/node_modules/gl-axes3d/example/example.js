//Load shell
var shell = require("gl-now")({ clearColor: [0,0,0,0] })
var camera = require("game-shell-orbit-camera")(shell)

//Mesh creation tools
var createMesh = require("gl-mesh3d")
var polygonize = require("isosurface").surfaceNets
var createAxes = require("../axes")

//Matrix math
var mat4 = require("gl-matrix").mat4

//Bounds on function to plot
var bounds = [[-5,-5,-5], [5,5,5]]

//Plot level set of f = 0
function f(x,y,z) {
  return x*x + y*y + z*z - 2.0
}

//State variables
var mesh, axes

shell.on("gl-init", function() {
  var gl = shell.gl

  //Set up camera
  camera.lookAt(bounds[1], [0,0,0], [0, 1, 0])

  //Create mesh
  mesh = createMesh(gl, polygonize([64, 64, 64], f, bounds))

  //Create axes object
  axes = createAxes(gl, {
    bounds: bounds
  })

  axes.update({
    bounds: [[-10,-10,-10], [10,10,10]]
  })
})

shell.on("gl-render", function() {
  var gl = shell.gl
  gl.enable(gl.DEPTH_TEST)

  //Compute camera parameters
  var cameraParameters = {
    view: camera.view(),
    projection: mat4.perspective(
        mat4.create(),
        Math.PI/4.0,
        shell.width/shell.height,
        0.1,
        1000.0)
  }

  //Draw mesh
  mesh.draw(cameraParameters)

  //Draw axes
  axes.draw(cameraParameters)
})
