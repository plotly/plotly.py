vec2 xyProjection = vec2(1, 1);

#pragma glslify: axisY = require("./y.glsl", mats=mats)

#pragma glslify: export(position)
vec4 position(
        float depth,
        vec2 resolution, vec2 viewBoxPosition, vec2 viewBoxSize,
        mat4 dims[4],
        float signum,
        mat4 dim1A, mat4 dim2A, mat4 dim1B, mat4 dim2B, mat4 dim1C, mat4 dim2C, mat4 dim1D, mat4 dim2D
    ) {

    float x = 0.5 * signum + 0.5;
    float y = axisY(x, dims, dim1A, dim2A, dim1B, dim2B, dim1C, dim2C, dim1D, dim2D);

    vec2 viewBoxXY = viewBoxPosition + viewBoxSize * vec2(x, y);

    return vec4(
        xyProjection * (2.0 * viewBoxXY / resolution - 1.0),
        depth,
        1.0
    );
}
