var shell = require("gl-now")()
var createStateStack = require("../savestate")

var stack

shell.on("gl-init", function() {

  //Create stack for saving state
  stack = createStateStack(shell.gl)

  //Push variables onto stack here
  stack.push()
  //... clobber stuff here ...
  shell.gl.clearColor(1, 0, 1, 0);

  //Context states can also be nested
  stack.push()
  // ... clobbber more stuff
  shell.gl.clearColor(0, 1, 0, 1)
  stack.pop()

  //Color back to previous value
  console.log(shell.gl.getParameter(shell.gl.COLOR_CLEAR_VALUE))

  //Restore state
  stack.pop()

  //Now state is completely restored
})