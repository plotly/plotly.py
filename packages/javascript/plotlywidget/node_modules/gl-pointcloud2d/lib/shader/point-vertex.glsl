precision mediump float;

attribute vec2 position;

uniform mat3 matrix;
uniform float pointSize;
uniform float pointCloud;

highp float rand(vec2 co) {
  highp float a = 12.9898;
  highp float b = 78.233;
  highp float c = 43758.5453;
  highp float d = dot(co.xy, vec2(a, b));
  highp float e = mod(d, 3.14);
  return fract(sin(e) * c);
}

void main() {
  vec3 hgPosition = matrix * vec3(position, 1);
  gl_Position  = vec4(hgPosition.xy, 0, hgPosition.z);
    // if we don't jitter the point size a bit, overall point cloud
    // saturation 'jumps' on zooming, which is disturbing and confusing
  gl_PointSize = pointSize * ((19.5 + rand(position)) / 20.0);
  if(pointCloud != 0.0) { // pointCloud is truthy
    // get the same square surface as circle would be
    gl_PointSize *= 0.886;
  }
}