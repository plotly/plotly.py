var test = require('tape').test

var mat = require('gl-mat4')
var decompose = require('./')

test("decompose a 3D matrix", function(t) {
    var m = mat.create() 
    var translate = [0,0,0],
        scale = [0,0,0],
        skew = [0,0,0],
        perspective = [0,0,0,1],
        quaternion = [0,0,0,1]

    var valid = decompose(m)
    t.equal(valid, true, 'can be decomposed')

    mat.identity(m)
    mat.translate(m, m, [-5, 2, 10])
    decompose(m, translate)
    t.deepEqual(translate, [-5, 2, 10], 'extracts translation')

    mat.identity(m)
    mat.scale(m, m, [1, 0, 5])
    decompose(m, translate, scale)
    t.deepEqual(scale, [1, 0, 5], 'extracts scale')

    mat.identity(m)
    mat.rotateX(m, m, Math.PI)
    decompose(m, translate, scale, skew, perspective, quaternion)
    t.deepEqual(quaternion, [1, 0, 0, 0], 'extracts rotation x')

    mat.identity(m)
    mat.rotateY(m, m, -Math.PI)
    decompose(m, translate, scale, skew, perspective, quaternion)
    t.deepEqual(quaternion, [0, -1, 0, 0], 'extracts rotation y')

    mat.identity(m)
    mat.rotateZ(m, m, -Math.PI)
    decompose(m, translate, scale, skew, perspective, quaternion)
    t.deepEqual(quaternion, [0, 0, -1, 0], 'extracts rotation z')
    t.deepEqual(skew, [0,0,0], 'extracts skew')

    mat.identity(m)
    mat.translate(m, m, [10, 5, -50])
    mat.scale(m, m, [0.25, 0.5, -0.5])
    mat.rotateZ(m, m, -Math.PI)
    decompose(m, translate, scale, skew, perspective, quaternion)
    t.deepEqual(translate, [10,5,-50], 'extracts translation')
    t.deepEqual(perspective, [0,0,0,1], 'extracts perspective')
    t.deepEqual(scale, [-0.25,-0.5,-0.5], 'extracts scale')
    t.deepEqual(quaternion, [0,0,0,1], 'extracts rotation')

    t.end()
})