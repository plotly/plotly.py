precision highp float;

#pragma glslify: outOfRange = require(glsl-out-of-range)

attribute vec3 position;
attribute vec4 color;
attribute vec2 glyph;
attribute vec4 id;

uniform vec4 highlightId;
uniform float highlightScale;
uniform mat4 model, view, projection;
uniform vec3 clipBounds[2];

varying vec4 interpColor;
varying vec4 pickId;
varying vec3 dataCoordinate;

void main() {
  if (outOfRange(clipBounds[0], clipBounds[1], position)) {

    gl_Position = vec4(0,0,0,0);
  } else {
    float scale = 1.0;
    if(distance(highlightId, id) < 0.0001) {
      scale = highlightScale;
    }

    vec4 worldPosition = model * vec4(position, 1);
    vec4 viewPosition = view * worldPosition;
    viewPosition = viewPosition / viewPosition.w;
    vec4 clipPosition = projection * (viewPosition + scale * vec4(glyph.x, -glyph.y, 0, 0));

    gl_Position = clipPosition;
    interpColor = color;
    pickId = id;
    dataCoordinate = position;
  }
}