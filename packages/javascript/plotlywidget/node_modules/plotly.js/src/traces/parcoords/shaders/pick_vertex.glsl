precision highp float;

attribute vec4 p0, p1, p2, p3,
               p4, p5, p6, p7,
               p8, p9, pa, pb,
               pc, pd, pe;

attribute vec4 pf;

uniform mat4 dim1A, dim2A, dim1B, dim2B, dim1C, dim2C, dim1D, dim2D,
             loA, hiA, loB, hiB, loC, hiC, loD, hiD;

uniform vec2 resolution,
             viewBoxPosition,
             viewBoxSize;

uniform sampler2D mask;
uniform float maskHeight;

uniform vec2 colorClamp;

varying vec4 fragColor;

#pragma glslify: position = require("./position.glsl")

void main() {

    float prominence = abs(pf[3]);

    mat4 p[4];
    p[0] = mat4(p0, p1, p2, p3);
    p[1] = mat4(p4, p5, p6, p7);
    p[2] = mat4(p8, p9, pa, pb);
    p[3] = mat4(pc, pd, pe, abs(pf));

    gl_Position = position(
        1.0 - prominence,
        resolution, viewBoxPosition, viewBoxSize,
        p,
        sign(pf[3]),
        dim1A, dim2A, dim1B, dim2B, dim1C, dim2C, dim1D, dim2D,
        loA, hiA, loB, hiB, loC, hiC, loD, hiD,
        mask, maskHeight
    );

    fragColor = vec4(pf.rgb, 1.0);
}
