precision highp float;

varying vec4 fragColor, fragBorderColor;

uniform float opacity;
varying float fragBorderRadius, fragWidth;

float smoothStep(float edge0, float edge1, float x) {
	float t;
	t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0);
	return t * t * (3.0 - 2.0 * t);
}

void main() {
	float radius, alpha = 1.0, delta = fragWidth;

	radius = length(2.0 * gl_PointCoord.xy - 1.0);

	if (radius > 1.0 + delta) {
		discard;
	}

	alpha -= smoothstep(1.0 - delta, 1.0 + delta, radius);

	float borderRadius = fragBorderRadius;
	float ratio = smoothstep(borderRadius - delta, borderRadius + delta, radius);
	vec4 color = mix(fragColor, fragBorderColor, ratio);
	color.a *= alpha * opacity;
	gl_FragColor = color;
}
