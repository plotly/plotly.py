import * as vec3 from './vec3';
import * as vec4 from './vec4';
import * as mat2 from './mat2';
import * as mat3 from './mat3';
import * as mat4 from './mat4';

export default {
    vec3: {
        transformMat3: vec3.transformMat3
    },
    vec4: {
        transformMat4: vec4.transformMat4
    },
    mat2: {
        create: mat2.create,
        rotate: mat2.rotate,
        scale: mat2.scale
    },
    mat3: {
        create: mat3.create,
        fromRotation: mat3.fromRotation
    },
    mat4: {
        create: mat4.create,
        identity: mat4.identity,
        translate: mat4.translate,
        scale: mat4.scale,
        multiply: mat4.multiply,
        perspective: mat4.perspective,
        rotateX: mat4.rotateX,
        rotateZ: mat4.rotateZ,
        invert: mat4.invert,
        ortho: mat4.ortho
    }
};
