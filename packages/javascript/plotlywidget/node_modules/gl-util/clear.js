'use strict'

module.exports = function clear (gl, o) {
	// TODO: add bg color setup gl.clearColor(r, g, b, a)

	var mask = gl.COLOR_BUFFER_BIT
	if (!o || o.depth) {
		mask |= gl.DEPTH_BUFFER_BIT
	}
	if (!o || o.stencil) {
		mask |= gl.STENCIL_BUFFER_BIT
	}

	var scissor
	if (!o || (o.viewport || o.scissor)) {
		// save scissor
		scissor = gl.getParameter(gl.SCISSOR_BOX)

		var vp = this.viewport
		gl.enable(gl.SCISSOR_TEST)
		gl.scissor(vp.x, vp.y, vp.width, vp.height)
	}

	gl.clear(mask)

	// restore scissor
	if (scissor) {
		gl.scissor.apply(gl, scissor);
	}
}
