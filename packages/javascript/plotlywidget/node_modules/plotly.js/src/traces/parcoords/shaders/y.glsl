vec4 unit = vec4(1, 1, 1, 1);

float val(mat4 p, mat4 v) {
    return dot(matrixCompMult(p, v) * unit, unit);
}

#pragma glslify: export(axisY)
float axisY(
        float x,
        mat4 d[4],
        mat4 dim1A, mat4 dim2A, mat4 dim1B, mat4 dim2B, mat4 dim1C, mat4 dim2C, mat4 dim1D, mat4 dim2D
    ) {

    float y1 = val(d[0], dim1A) + val(d[1], dim1B) + val(d[2], dim1C) + val(d[3], dim1D);
    float y2 = val(d[0], dim2A) + val(d[1], dim2B) + val(d[2], dim2C) + val(d[3], dim2D);
    return y1 * (1.0 - x) + y2 * x;
}
