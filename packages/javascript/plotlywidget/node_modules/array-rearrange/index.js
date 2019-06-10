'use strict'

module.exports = reorder


function reorder(arr, index, stride) {
    var n = index.length

    if (!stride) {
        stride = Math.floor(arr.length / index.length);
    }

    if (arr.length !== n * stride) {
        throw Error('Bad length of index array')
    }

    if (stride === 1) {
        reorderSimple()
    }
    else {
        reorderStride(stride)
    }


    function reorderSimple () {
        for (var start = 0; start < n; start++) {
            var currId, pickId = index[start]

            if (start === pickId) continue

            while (pickId !== start) {
                currId = pickId
                pickId = index[currId]

                var v = arr[pickId]
                arr[pickId] = arr[currId]
                arr[currId] = v

                index[currId] = currId
            }
        }
    }

    function reorderStride (stride) {
        for (var start = 0; start < n; start++) {
            var currId, pickId = index[start]

            if (start === pickId) continue

            while (pickId !== start) {
                currId = pickId
                pickId = index[currId]

                for (var j = 0; j < stride; j++) {
                    var value  = arr[pickId * stride + j];
                    arr[pickId * stride + j] = arr[currId * stride + j];
                    arr[currId * stride + j]   = value;
                }

                index[currId] = currId
            }

        }
    }

    return arr
}
