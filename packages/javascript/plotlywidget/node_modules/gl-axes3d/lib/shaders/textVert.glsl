precision highp float;

attribute vec3 position;

uniform mat4 model, view, projection;
uniform vec3 offset, axis, alignDir, alignOpt;
uniform float scale, angle, pixelScale;
uniform vec2 resolution;

vec3 project(vec3 p) {
  vec4 pp = projection * view * model * vec4(p, 1.0);
  return pp.xyz / max(pp.w, 0.0001);
}

float computeViewAngle(vec3 a, vec3 b) {
  vec3 A = project(a);
  vec3 B = project(b);

  return atan(
    (B.y - A.y) * resolution.y,
    (B.x - A.x) * resolution.x
  );
}

const float PI = 3.141592;
const float TWO_PI = 2.0 * PI;
const float HALF_PI = 0.5 * PI;
const float ONE_AND_HALF_PI = 1.5 * PI;

int option = int(floor(alignOpt.x + 0.001));
float hv_ratio =       alignOpt.y;
bool enableAlign =    (alignOpt.z != 0.0);

float mod_angle(float a) {
  return mod(a, PI);
}

float positive_angle(float a) {
  return mod_angle((a < 0.0) ?
    a + TWO_PI :
    a
  );
}

float look_upwards(float a) {
  float b = positive_angle(a);
  return ((b > HALF_PI) && (b <= ONE_AND_HALF_PI)) ?
    b - PI :
    b;
}

float look_horizontal_or_vertical(float a, float ratio) {
  // ratio controls the ratio between being horizontal to (vertical + horizontal)
  // if ratio is set to 0.5 then it is 50%, 50%.
  // when using a higher ratio e.g. 0.75 the result would
  // likely be more horizontal than vertical.

  float b = positive_angle(a);

  return
    (b < (      ratio) * HALF_PI) ? 0.0 :
    (b < (2.0 - ratio) * HALF_PI) ? -HALF_PI :
    (b < (2.0 + ratio) * HALF_PI) ? 0.0 :
    (b < (4.0 - ratio) * HALF_PI) ? HALF_PI :
                                    0.0;
}

float roundTo(float a, float b) {
  return float(b * floor((a + 0.5 * b) / b));
}

float look_round_n_directions(float a, int n) {
  float b = positive_angle(a);
  float div = TWO_PI / float(n);
  float c = roundTo(b, div);
  return look_upwards(c);
}

float applyAlignOption(float rawAngle, float delta) {
  return
    (option >  2) ? look_round_n_directions(rawAngle + delta, option) :       // option 3-n: round to n directions
    (option == 2) ? look_horizontal_or_vertical(rawAngle + delta, hv_ratio) : // horizontal or vertical
    (option == 1) ? rawAngle + delta :       // use free angle, and flip to align with one direction of the axis
    (option == 0) ? look_upwards(rawAngle) : // use free angle, and stay upwards
    (option ==-1) ? 0.0 :                    // useful for backward compatibility, all texts remains horizontal
                    rawAngle;                // otherwise return back raw input angle
}

bool isAxisTitle = (axis.x == 0.0) &&
                   (axis.y == 0.0) &&
                   (axis.z == 0.0);

void main() {
  //Compute world offset
  float axisDistance = position.z;
  vec3 dataPosition = axisDistance * axis + offset;

  float beta = angle; // i.e. user defined attributes for each tick

  float axisAngle;
  float clipAngle;
  float flip;

  if (enableAlign) {
    axisAngle = (isAxisTitle) ? HALF_PI :
                      computeViewAngle(dataPosition, dataPosition + axis);
    clipAngle = computeViewAngle(dataPosition, dataPosition + alignDir);

    axisAngle += (sin(axisAngle) < 0.0) ? PI : 0.0;
    clipAngle += (sin(clipAngle) < 0.0) ? PI : 0.0;

    flip = (dot(vec2(cos(axisAngle), sin(axisAngle)),
                vec2(sin(clipAngle),-cos(clipAngle))) > 0.0) ? 1.0 : 0.0;

    beta += applyAlignOption(clipAngle, flip * PI);
  }

  //Compute plane offset
  vec2 planeCoord = position.xy * pixelScale;

  mat2 planeXform = scale * mat2(
     cos(beta), sin(beta),
    -sin(beta), cos(beta)
  );

  vec2 viewOffset = 2.0 * planeXform * planeCoord / resolution;

  //Compute clip position
  vec3 clipPosition = project(dataPosition);

  //Apply text offset in clip coordinates
  clipPosition += vec3(viewOffset, 0.0);

  //Done
  gl_Position = vec4(clipPosition, 1.0);
}