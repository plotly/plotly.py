var mat4 = require('gl-mat4')
var style = require('dom-css')
var stringify = require('matrix-to-css')
var tweenr = require('tweenr')()

var mix = require('./')

require('domready')(function() {
    var div = createBox()

    var start = mat4.create()
    var end = mat4.create()
    var out = mat4.create()

    //our intial transform
    mat4.rotateY(start, start, Math.PI/2)
    mat4.translate(start, start, [100, 20, 0])
    mat4.scale(start, start, [0.5, 0.25, 1])
    mat4.rotateZ(start, start, Math.PI)

    //our ending transform
    mat4.translate(end, end, [240, 50, 0])

    //apply the initial transformation
    style(div, 'transform', stringify(start))

    // function loop() {
    //     animate()
    // }

    function animate() {
        var tween = { value: 0 }
        //Note we aren't handling non-invertible edge 
        //cases here (e.g. scale = 0)
        tweenr.to(tween, { value: 1, duration: 3, delay: 0.5, ease: 'expoOut' })
            .on('update', function() {
                //interpolate matrices
                mix(out, start, end, tween.value)

                //apply new matrix
                style(div, 'transform', stringify(out))
            })
            .on('complete', animate)
    }

    animate()
})

function createBox() {
    var div = document.createElement('div')

    var parent = document.createElement('div')
    parent.appendChild(div)
    document.body.appendChild(parent)

    style(parent, {
        perspective: 1000,
        transformStyle: 'preserve-3d',
        width: 100,
        height: 100,
        display: 'inline-block'
    })

    style(div, {
        position: 'absolute',
        top: 0,
        left: 0,
        width: 100,
        height: 100,
        background: 'blue'
    })
    return div
}