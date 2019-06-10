precision highp float;

uniform sampler2D dashPattern;
uniform float dashSize, pixelRatio, thickness, opacity, id, miterMode;

varying vec4 fragColor;
varying vec2 tangent;
varying vec4 startCutoff, endCutoff;
varying vec2 startCoord, endCoord;
varying float enableStartMiter, enableEndMiter;

float distToLine(vec2 p, vec2 a, vec2 b) {
	vec2 diff = b - a;
	vec2 perp = normalize(vec2(-diff.y, diff.x));
	return dot(p - a, perp);
}

void main() {
	float alpha = 1., distToStart, distToEnd;
	float cutoff = thickness * .5;

	//bevel miter
	if (miterMode == 1.) {
		if (enableStartMiter == 1.) {
			distToStart = distToLine(gl_FragCoord.xy, startCutoff.xy, startCutoff.zw);
			if (distToStart < -1.) {
				discard;
				return;
			}
			alpha *= min(max(distToStart + 1., 0.), 1.);
		}

		if (enableEndMiter == 1.) {
			distToEnd = distToLine(gl_FragCoord.xy, endCutoff.xy, endCutoff.zw);
			if (distToEnd < -1.) {
				discard;
				return;
			}
			alpha *= min(max(distToEnd + 1., 0.), 1.);
		}
	}

	// round miter
	else if (miterMode == 2.) {
		if (enableStartMiter == 1.) {
			distToStart = distToLine(gl_FragCoord.xy, startCutoff.xy, startCutoff.zw);
			if (distToStart < 0.) {
				float radius = length(gl_FragCoord.xy - startCoord);

				if(radius > cutoff + .5) {
					discard;
					return;
				}

				alpha -= smoothstep(cutoff - .5, cutoff + .5, radius);
			}
		}

		if (enableEndMiter == 1.) {
			distToEnd = distToLine(gl_FragCoord.xy, endCutoff.xy, endCutoff.zw);
			if (distToEnd < 0.) {
				float radius = length(gl_FragCoord.xy - endCoord);

				if(radius > cutoff + .5) {
					discard;
					return;
				}

				alpha -= smoothstep(cutoff - .5, cutoff + .5, radius);
			}
		}
	}

	float t = fract(dot(tangent, gl_FragCoord.xy) / dashSize) * .5 + .25;
	float dash = texture2D(dashPattern, vec2(t, .5)).r;

	gl_FragColor = fragColor;
	gl_FragColor.a *= alpha * opacity * dash;
}
