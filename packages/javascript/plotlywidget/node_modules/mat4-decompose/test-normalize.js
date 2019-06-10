var decomposeMat4 = require('./')
var test = require('tape').test

var mat = require('gl-mat4')
var normalize = require('./normalize')

test("normalize a 3D matrix", function(t) {
    var m = Array.prototype.slice.call(mat.create())
    mat.scale(m, m, [2, 2, 2])
    mat.translate(m, m, [4, 5, 2])
    m[15] = 2

    var out = []
    var n = normalize(out, m)
    t.equal(n, true, 'can normalize')
    t.deepEqual(out, [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, 5, 2, 1 ])

    m[15] = 0
    n = normalize(out, m)
    t.equal(n, false, 'cannot normalize')

    t.end()
})