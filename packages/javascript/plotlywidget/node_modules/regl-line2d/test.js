'use strict'

const createLine = require('./')
const panZoom = require('pan-zoom')
const fps = require('fps-indicator')({css:`padding: 1.4rem`})
const random = require('gauss-random')
const rgba = require('color-rgba')
const nanoraf = require('nanoraf')
const palettes = require('nice-color-palettes')
const createScatter = require('regl-scatter2d')
const t = require('tape')
const normalize = require('array-normalize')
const extend = require('object-assign')
const arc = require('arc-to')
const curve = require('adaptive-bezier-curve')
const flatten = require('flatten-vertex-data')
const arrFrom = require('array-from')
const arrFill = require('array-fill')
const regl = require('regl')({
  attributes: { preserveDrawingBuffer: true },
  extensions: ['ANGLE_instanced_arrays', 'OES_element_index_uint']
})


// setup render
let palette = palettes[ Math.floor(Math.random() * palettes.length) ]
let span = 10
let range = [-span * .5 * innerWidth/innerHeight, -span * .5, span * .5 * innerWidth/innerHeight, span * .5]
let pan = true
let options = {
  opacity: .5,
  overlay: false,
  thickness: 20,
  color: 'rgba(0,0,255,1)',//[palette[0]],
  miterlimit: 1,
  // viewport: [200,400,800,600],
  range
}
let batch = []


let line2d = createLine(regl)
setup()



/** Test cases */
t('aligned line', t => {
  batch.push(extend({}, options, {
    positions: [ 0,0, 0.5,0, 1,0 ],
    type: 'round'
  }))

  t.end()
})

t('multiple points', t => {
  let N = 1e4
  let positions = Array(2 * N)
  for(var i=0; i<2*N; i+=2) {
    // positions[i]   = (i/N)*10.0-10.0
    positions[i] = random() * 2
    positions[i+1] = random() * 2
  }

  scale(positions, .15, .15)
  translate(positions, -5, -3)

  batch.push(extend({}, options, {
    color: 'red',
    join: 'rect',
    positions, thickness: 3, range, dash: [3, 3]
  }))

  t.end()
})

t('closed circuit', t => {
  // [0, 0.4, 0, 0.4, 0, 1, 1, 0, 1, 0, 1, 0]
  let positions = [0,0, 0,3, 3,-2, -3,-3, -6,0, -6,-2, .5,-2, 0.5,1]//, 0,0]

  scale(positions, .25, .25)
  translate(positions, -1.5, -3)

  batch.push(extend({}, options, {
    color: 'green',
    close: false,
    join: 'miter',
    positions: positions, overlay: false, thickness: 30,
    dash: [8, 2]
  }))

  t.end()
})

t('basic edge cases', t => {
  let positions = [-3,4, -3,3, -3,0, -1,0, -.7,-.5, 0,1, -.5,-.5, .5,1, 0,0, .5,.5, 1,0.5, 2,2, 5,-3, -1,-1.5, -2.5,-2, -5,-3, -4,1, -5,1, -4.5,1, -4.5,2]

  scale(positions, .25, .25)
  translate(positions, 1.5, -3)

  batch.push(extend({}, options, {overlay: true, positions: positions, thickness: 10, dash: [15, 5]}))

  t.end()
})

t('near-opposite directions / miter clipping', t => {
  let positions = [0,1, 0.25,4, .25,-4, .5,-1, .65,0]

  // normalize(positions, 2)
  // translate(positions, 2, 1)
  scale(positions, 1.75, 1)
  scale(positions, .5, .5)
  translate(positions, 5.5, -1.82)

  batch.push(extend({}, options, {overlay: true, positions: positions, thickness: 30, dash: [9, 1]}))

  t.end()
})

t('plotly linear approx', t => {
  let positions = [0.07511045655375555,0.06510416666666519,0.1281296023564065,-0.013020833333332593,0.18114874815905743,-0.2734375,0.22533136966126657,-1.0546875,0.25184094256259204,-1.9140625,0.2739322533136965,-2.916666666666665,0.2960235640648011,-4.0625,0.3136966126656848,-5.234375,0.33136966126656847,-6.2890625,0.3490427098674521,-7.3828125,0.36671575846833576,-8.4765625,0.38438880706921935,-9.53125,0.406480117820324,-10.468750000000004,0.4462444771723122,-11.640625,0.4872711971386493,-12.533482142857144,0.5434462444771723,-12.135416666666668,0.5964653902798233,-11.679687500000004,0.6494845360824743,-11.223958333333332,0.7025036818851251,-10.638020833333343,0.7555228276877761,-10.10416666666667,0.8085419734904271,-9.622395833333334,0.8615611192930782,-9.140625,0.914580265095729,-8.6328125,0.96759941089838,-8.151041666666664,1.020618556701031,-7.565104166666665,1.0736377025036818,-7.018229166666665,1.1266568483063328,-6.471354166666668,1.1796759941089838,-5.976562499999998,1.2326951399116348,-5.442708333333335,1.285714285714286,-4.908854166666666,1.3387334315169366,-4.3619791666666625,1.3917525773195876,-3.867187499999999,1.4447717231222386,-3.372395833333334,1.4977908689248896,-2.8385416666666643,1.5508100147275405,-2.304687499999999,1.6038291605301915,-1.7708333333333326,1.6568483063328423,-1.263020833333337,1.7098674521354933,-0.7291666666666663,1.7628865979381445,-0.1822916666666663,1.7614138438880704,1.2500000000000022,1.8159057437407953,0.3385416666666696,1.8689248895434465,0.8203125000000044,1.9219440353460973,1.3541666666666696,1.974963181148748,1.8359375000000022,2.0279823269513995,2.304687500000002,2.0810014727540502,2.8515624999999956,2.1340206185567006,3.320312499999998,2.1870397643593518,3.8541666666666674,2.240058910162003,4.335937499999996,2.2930780559646537,4.81770833333333,2.346097201767305,5.351562500000002,2.3991163475699557,5.820312499999998,2.452135493372607,6.289062499999993,2.5051546391752577,6.770833333333335,2.5581737849779085,7.3177083333333375,2.6111929307805597,7.91666666666667,2.6642120765832105,8.3203125,2.7172312223858617,8.671875000000002,2.770250368188513,9.088541666666664,2.823269513991163,9.531249999999998,2.8762886597938144,10.130208333333336,2.929307805596465,10.71614583333333,2.9823269513991164,11.22395833333334,3.035346097201767,11.54947916666667,3.0883652430044184,12.05729166666666,3.141384388807069,12.1875,3.1855670103092786,11.5234375,3.212076583210604,10.2734375,3.2297496318114876,9.179687500000007,3.247422680412371,8.046874999999991,3.2650957290132547,6.562500000000002,3.282768777614138,5.078124999999996,3.300441826215022,3.8671874999999933,3.3181148748159055,2.7734375000000044,3.3446244477172313,1.5039062499999978,3.38880706921944,0.7031249999999978,3.441826215022091,0.4687500000000022,3.4948453608247423,0.46875000000000444,3.547864506627393,0.4687499999999978,3.6008836524300443,0.5729166666666718,3.653902798232695,0.9114583333333259,3.7069219440353467,1.3020833333333393,3.759941089837997,1.4453125000000022,3.804123711340206,0.9570312500000022,3.8350515463917527,-0.052083333333334814,3.857142857142857,-1.250000000000001,3.874815905743741,-2.578124999999999,3.8924889543446244,-3.7500000000000036,3.9101620029455084,-5.039062499999999,3.9366715758468334,-6.523437500000004,3.949926362297496,-7.265624999999993,3.9808541973490428,-6.249999999999998,3.9985272459499264,-5.234375,4.01620029455081,-4.023437499999996,4.033873343151693,-2.6562500000000067,4.051546391752577,0.07812499999999778,4.047128129602356,-1.4062500000000044,4.060382916053019,1.9921875000000067,4.055964653902798,1.1718749999999978,4.070692194403534,4.114583333333329,4.06480117820324,2.890625,4.078055964653903,5.703125000000004,4.088365243004418,7.96875,4.082474226804123,6.796875000000009,4.095729013254786,9.492187500000002,4.1060382916053015,10.57291666666666,4.139911634756995,11.575520833333343,4.142562592047128,12.953124999999996,4.166421207658321,9.6875,4.175257731958763,8.281250000000004,4.182621502209131,6.640625,4.191458026509574,4.947916666666671,4.210603829160529,3.7499999999999956,4.228276877761414,2.5390625000000044,4.250368188512518,1.3802083333333304,4.2901325478645065,0.390625,4.343151693667157,0.09114583333332815,4.396170839469808,0.07812499999999334,4.44918998527246,0.07812500000000444,4.5022091310751104,0.07812499999999556,4.555228276877761,0.07812500000000888,4.608247422680412,0.07812499999999556,4.661266568483064,0.07812500000000888,4.714285714285714,0.14322916666667407,4.767304860088365,0.15625,4.820324005891017,0.10416666666666297,4.873343151693667,0.07812499999999556,4.926362297496317,0.07812499999999778,4.97938144329897,0.10416666666667185,5.03240058910162,0.15625000000000222,5.085419734904271,0.07812500000000888,5.1384388807069215,0.07812499999999334,5.191458026509573,0.07812500000000444,5.244477172312224,0.07812500000000444,5.297496318114875,0.07812499999999556,5.350515463917525,0.1432291666666652,5.403534609720176,0.1302083333333326,5.456553755522828,0.07812499999999556,5.509572901325479,0.07812499999999778,5.562592047128129,0.07812500000000222,5.615611192930779,0.07812499999999334,5.668630338733432,0.07812499999999334,5.721649484536082,0.07812500000000222,5.774668630338733,0.07812500000000444,5.827687776141384,0.10416666666667185,5.876288659793816,0.15625000000000666]//.slice(198,-86)

  scale(positions, 1, .12)
  // scale(positions, 2, .25)
  translate(positions, -6, 0)

  batch.push(extend({}, options, {join: 'round', positions: positions, thickness: 3, dash: null}))

  t.end()
})

t('closed path', t => {
  let positions

  positions = [0,0, 1,0, 1,1, 0,1, 0,0]
  translate(positions, 4, 2)
  batch.push(extend({}, options, {overlay: true, fill: 'green', close: true, positions: positions, thickness: 10, dash: null}))

  positions = [0,0, 1,0, .5,1]
  translate(positions, 5, 2)
  batch.push(extend({}, options, {overlay: true, fill: 'blue', close: true, positions: positions, thickness: 10, dash: null}))


  positions = circle(3.5, 2.5, .5)
  batch.push(extend({}, options, {overlay: true, fill: 'red', close: true, positions: positions, thickness: 10, dash: null}))

  t.end()
})

t('time case', t => {
  batch.push({
    type: 'rect',
    positions: [25741380000,1293840000000,25741380001,1293926400000,25741380002,1294012800000,25741380003,1294099200000,25741380004,1294185600000,1477434180000,1294272000000,1477434180001,1294358400000,1477434180002,1294444800000,1477434180003,1294531200000,1477434180004,1294617600000],
    range: [1477434179998,1293725711392.4,1477434180004,1295595888607.6],
    width: 20,
    color: 'red'
  })

  t.end()
})

t('update(1,2) after update(1,2,3) removes 3rd pass')

t.skip('disconnected', t => {
  batch.push({
    type: 'round',
    positions: [1, -2, 2, -2, 3, NaN, 4, 2, 5, 2],
    width: 20,
    color: 'red'
  })
})

t('fill', t => {
  batch.push({
    fill: '#F9F38C',
    strokeWidth: 6,
    stroke: '#D07735',
    close: false,
    positions: translate(scale([0,40, 40,40, 40,80, 80,80, 80,120, 120,120, 120,160],.015,.015), 2, -1.5),
    range
  })

  t.end()
})

t('colorscale', t => {
  let positions = translate(scale(flatten(curve([4, 4], [7, 10], [12, 2], [20, 4], 5)), .25, .25), -3, -1)
  let colors = arrFrom({ length: positions.length / 2 }).map(x => palette[Math.floor(Math.random() * palette.length)])

  translate(positions, 0, 5)
  scale(positions, .5, .5)

  batch.push({
    positions: positions,
    color: colors,
    range,
    thickness: 60
  })

  t.end()
})

t.skip('changing color', t => {
  let thickness = 100
  let positions = [0,0, 1,1]
  let colors = 'green'

  line2d.update({colors, positions, join: 'rect', thickness: 30})
  line2d.draw()

  setTimeout(() => {
    regl.clear({color: true, depth: true})
    line2d.update({colors: 'black'})
    line2d.draw()
  })

  t.end()
})

t('round join', t => {
  let thickness = 100
  let positions = [-1,-.9, -1,-1, -1,1, -.9,-.9, -.8,.8, -.7,-.6, -.5,.4, -.2,-.2, .4,0, .8,0]
  let colors = ['black', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'gray', 'blue', 'black']

  scale(positions, 1, 1)
  translate(positions, -4, 2.5)

  batch.push(extend({}, options, {color: colors, opacity: 1, join: 'round', overlay: true, positions: positions, miterlimit: 1, thickness: 30, dash: null}))

  t.end()
})

t.skip('rect line', t => {
  t.end()
})

t.skip('painting', t => {
  pan = false
  t.end()
})

t.skip('fix horizontal segments', t => {
  let positions = {
    x: [ 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,6,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,7,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,8,8.1,8.2,8.3,8.4,8.5,8.6,8.7,8.8,8.9,9,9.1,9.2,9.3,9.4,9.5,9.6,9.7,9.8,9.9,10],
    y: [ 20.392,20.388,20.386,20.374,20.384,20.384,20.384,20.38,20.384,20.384,20.384,20.372,20.388,20.384,20.386,20.376,20.38,20.384,20.38,20.386,20.382,20.378,20.372,20.378,20.386,20.384,20.386,20.394,20.388,20.38,20.384,20.384,20.374,20.36,20.378,20.384,20.378,20.378,20.384,20.38,20.384,20.386,20.378,20.384,20.386,20.384,20.384,20.384,20.386,20.384,20.38,20.374,20.384,20.384,20.384,20.384,20.384,20.384,20.378,20.384,20.384,20.38,20.372,20.384,20.374,20.38,20.384,20.378,20.394,20.384,20.384,20.384,20.376,20.38,20.378,20.378,20.384,20.372,20.384,20.378,20.384,20.384,20.378,20.378,20.384,20.38,20.376,20.38,20.38,20.384,20.384,20.378,20.38,20.384,20.38,20.394,20.384,20.384,20.378,20.372]
  }

  line2d.update({color: 'gray', positions, join: 'round', thickness: 10})
  line2d.draw()

  batch.push(extend({}, options, {
    positions,
    type: 'round',
    thickness: 10,
    color: 'gray'
  }))

  t.end()
})


function setup () {
  // FIXME: enable settings-panel
  // createPanel(options, opts => draw(opts))

  // let drawPoints = createScatter({
  //   regl, range,
  //   size: 10,
  //   borderSize: 0,
  //   color: 'rgba(255,0,0,.25)'
  // })

  function draw(opts) {
    regl.clear({ color: true, depth: true })
    line2d.update(opts)
    line2d.draw()
    // regl._refresh()
    // drawPoints(extend({}, opts[opts.length - 1], { color: 'rgba(255,0,0,.5)'}))
  }

  setTimeout(() => {
    draw(batch)
  }, 100)

  //pan-zoom interactions
  let prev = null
  let frame = nanoraf(draw)
  let cnv = regl._gl.canvas

  panZoom(cnv, e => {
    let w = cnv.offsetWidth
    let h = cnv.offsetHeight

    let rx = e.x / w
    let ry = e.y / h

    let xrange = range[2] - range[0],
      yrange = range[3] - range[1]

    if (e.dz) {
      let dz = e.dz / w
      range[0] -= rx * xrange * dz
      range[2] += (1 - rx) * xrange * dz

      range[1] -= (1 - ry) * yrange * dz
      range[3] += ry * yrange * dz
    }

    if (pan) {
      range[0] -= xrange * e.dx / w
      range[2] -= xrange * e.dx / w
      range[1] += yrange * e.dy / h
      range[3] += yrange * e.dy / h
    }

    let state = arrFill(Array(batch.length), {range: range})
    frame(state, prev)
    prev = state
  })
}

function translate (arr, x, y) {
  for (let i = 0; i < arr.length; i+=2) {
    arr[i] += x
    arr[i+1] += y
  }
  return arr
}

function scale (arr, x, y) {
  for (let i = 0; i < arr.length; i+=2) {
    arr[i] *= x
    arr[i+1] *= y
  }
  return arr
}

function circle(x, y, radius) {
  var c = arc(x, y, radius, 0, Math.PI*2, false)
  c.pop()
  return c
}
