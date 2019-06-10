#pragma glslify: axisY = require("./y.glsl", mats=mats)

#pragma glslify: export(position)

const int bitsPerByte = 8;

int mod2(int a) {
    return a - 2 * (a / 2);
}

int mod8(int a) {
    return a - 8 * (a / 8);
}

vec4 zero = vec4(0, 0, 0, 0);
vec4 unit = vec4(1, 1, 1, 1);
vec2 xyProjection = vec2(1, 1);

mat4 mclamp(mat4 m, mat4 lo, mat4 hi) {
    return mat4(clamp(m[0], lo[0], hi[0]),
                clamp(m[1], lo[1], hi[1]),
                clamp(m[2], lo[2], hi[2]),
                clamp(m[3], lo[3], hi[3]));
}

bool mshow(mat4 p, mat4 lo, mat4 hi) {
    return mclamp(p, lo, hi) == p;
}

bool withinBoundingBox(
        mat4 d[4],
        mat4 loA, mat4 hiA, mat4 loB, mat4 hiB, mat4 loC, mat4 hiC, mat4 loD, mat4 hiD
    ) {

    return mshow(d[0], loA, hiA) &&
           mshow(d[1], loB, hiB) &&
           mshow(d[2], loC, hiC) &&
           mshow(d[3], loD, hiD);
}

bool withinRasterMask(mat4 d[4], sampler2D mask, float height) {
    bool result = true;
    int bitInByteStepper;
    float valY, valueY, scaleX;
    int hit, bitmask, valX;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                bitInByteStepper = mod8(j * 4 + k);
                valX = i * 2 + j / 2;
                valY = d[i][j][k];
                valueY = valY * (height - 1.0) + 0.5;
                scaleX = (float(valX) + 0.5) / 8.0;
                hit = int(texture2D(mask, vec2(scaleX, (valueY + 0.5) / height))[3] * 255.0) / int(pow(2.0, float(bitInByteStepper)));
                result = result && mod2(hit) == 1;
            }
        }
    }
    return result;
}

vec4 position(
        float depth,
        vec2 resolution, vec2 viewBoxPosition, vec2 viewBoxSize,
        mat4 dims[4],
        float signum,
        mat4 dim1A, mat4 dim2A, mat4 dim1B, mat4 dim2B, mat4 dim1C, mat4 dim2C, mat4 dim1D, mat4 dim2D,
        mat4 loA, mat4 hiA, mat4 loB, mat4 hiB, mat4 loC, mat4 hiC, mat4 loD, mat4 hiD,
        sampler2D mask, float maskHeight
    ) {

    float x = 0.5 * signum + 0.5;
    float y = axisY(x, dims, dim1A, dim2A, dim1B, dim2B, dim1C, dim2C, dim1D, dim2D);

    float show = float(
                            withinBoundingBox(dims, loA, hiA, loB, hiB, loC, hiC, loD, hiD)
                         && withinRasterMask(dims, mask, maskHeight)
                      );

    vec2 viewBoxXY = viewBoxPosition + viewBoxSize * vec2(x, y);
    float depthOrHide = depth + 2.0 * (1.0 - show);

    return vec4(
        xyProjection * (2.0 * viewBoxXY / resolution - 1.0),
        depthOrHide,
        1.0
    );
}
