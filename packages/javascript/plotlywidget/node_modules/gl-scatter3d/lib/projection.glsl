precision highp float;

#pragma glslify: outOfRange = require(glsl-out-of-range)

attribute vec3 position;
attribute vec4 color;
attribute vec2 glyph;
attribute vec4 id;

uniform float highlightScale;
uniform vec4 highlightId;
uniform vec3 axes[2];
uniform mat4 model, view, projection;
uniform vec2 screenSize;
uniform vec3 clipBounds[2];
uniform float scale, pixelRatio;

varying vec4 interpColor;
varying vec4 pickId;
varying vec3 dataCoordinate;

void main() {
  if (outOfRange(clipBounds[0], clipBounds[1], position)) {

    gl_Position = vec4(0,0,0,0);
  } else {
    float lscale = pixelRatio * scale;
    if(distance(highlightId, id) < 0.0001) {
      lscale *= highlightScale;
    }

    vec4 clipCenter   = projection * view * model * vec4(position, 1);
    vec3 dataPosition = position + 0.5*lscale*(axes[0] * glyph.x + axes[1] * glyph.y) * clipCenter.w * screenSize.y;
    vec4 clipPosition = projection * view * model * vec4(dataPosition, 1);

    gl_Position = clipPosition;
    interpColor = color;
    pickId = id;
    dataCoordinate = dataPosition;
  }
}
