// @flow

import {
    LineIndexArray,
    TriangleIndexArray
} from './array_types';

/**
 * An index array stores Uint16 indicies of vertexes in a corresponding vertex array. We use
 * two kinds of index arrays: arrays storing groups of three indicies, forming triangles; and
 * arrays storing pairs of indicies, forming line segments.
 * @private
 */
export {LineIndexArray, TriangleIndexArray};
