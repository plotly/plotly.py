precision highp float;

attribute float x, y, xFract, yFract;
attribute float size, borderSize;
attribute vec4 colorId, borderColorId;
attribute float isActive;

uniform vec2 scale, scaleFract, translate, translateFract, paletteSize;
uniform float pixelRatio;
uniform sampler2D palette;

const float maxSize = 100.;
const float borderLevel = .5;

varying vec4 fragColor, fragBorderColor;
varying float fragPointSize, fragBorderRadius, fragWidth, fragBorderColorLevel, fragColorLevel;

bool isDirect = (paletteSize.x < 1.);

vec4 getColor(vec4 id) {
  return isDirect ? id / 255. : texture2D(palette,
    vec2(
      (id.x + .5) / paletteSize.x,
      (id.y + .5) / paletteSize.y
    )
  );
}

void main() {
  if (isActive == 0.) return;

  vec2 position = vec2(x, y);
  vec2 positionFract = vec2(xFract, yFract);

  vec4 color = getColor(colorId);
  vec4 borderColor = getColor(borderColorId);

  float size = size * maxSize / 255.;
  float borderSize = borderSize * maxSize / 255.;

  gl_PointSize = 2. * size * pixelRatio;
  fragPointSize = size * pixelRatio;

  vec2 pos = (position + translate) * scale
      + (positionFract + translateFract) * scale
      + (position + translate) * scaleFract
      + (positionFract + translateFract) * scaleFract;

  gl_Position = vec4(pos * 2. - 1., 0, 1);

  fragColor = color;
  fragBorderColor = borderColor;
  fragWidth = 1. / gl_PointSize;

  fragBorderColorLevel = clamp(borderLevel - borderLevel * borderSize / size, 0., 1.);
  fragColorLevel = clamp(borderLevel + (1. - borderLevel) * borderSize / size, 0., 1.);
}