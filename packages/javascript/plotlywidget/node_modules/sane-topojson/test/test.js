/* global d3:false */
/* global describe:false, it:false, expect:false fail:false beforeEach:false, afterEach:false */

/*
 * N.B. these test assert ./index.js which itself requires dist/*,
 * so make sure to run `npm start` before `npm test` to test new topojson files
 *
 */

var saneTopojson = require('../')
var assets = require('./assets')
var topojson = require('topojson')
var diff = require('fast-array-diff').diff

describe('sane topojson general', () => {
  it('should have correct test environments', () => {
    expect(d3.version).toEqual('3.5.17')
    expect(Object.keys(saneTopojson)).toEqual(Object.keys(assets.GEOMETRY_COUNT))
  })

  it('should have all the correct layers', () => {
    Object.keys(saneTopojson).forEach((k) => {
      var saneTopojsonItem = saneTopojson[k]

      expect(Object.keys(saneTopojsonItem)).toEqual([
        'type', 'objects', 'arcs', 'transform', 'bbox'
      ])

      expect(Object.keys(saneTopojsonItem.objects)).toEqual([
        'coastlines', 'land', 'ocean', 'lakes',
        'rivers', 'countries', 'subunits'
      ])

      var objs = saneTopojsonItem.objects
      Object.keys(objs).forEach((l) => {
        expect(Object.keys(objs[l])).toEqual(['type', 'geometries'])
      })
    })
  })

  it('should have correct number of geometries per layer', () => {
    Object.keys(saneTopojson).forEach((k) => {
      var objs = saneTopojson[k].objects

      Object.keys(objs).forEach((l) => {
        expect(objs[l].geometries.length).toBe(assets.GEOMETRY_COUNT[k][l], [k, l])
      })
    })
  })

  it('should have a minimal set of *properties*', () => {
    Object.keys(saneTopojson).forEach((k) => {
      var objs = saneTopojson[k].objects

      Object.keys(objs).forEach((l) => {
        var o = objs[l]
        var list = []

        switch (l) {
          case 'coastlines':
          case 'land':
          case 'ocean':
          case 'lakes':
          case 'rivers':
            o.geometries.forEach(function (g, i) {
              var msg = [k, l, i]

              expect(Object.keys(g).length).toBe(2, 'just two fields| ' + msg)
              expect(Array.isArray(g.arcs)).toBe(true, '*arcs* is an array| ' + msg)
              expect(typeof g.type === 'string').toBe(true, '*type* is a string |' + msg)
            })
            break
          case 'countries':
          case 'subunits':
            var expNumOfProps = { countries: 1, subunits: 2 }[l]

            o.geometries.forEach(function (g, i) {
              var msg = [k, l, i]
              var p = g.properties

              if (p) {
                expect(Object.keys(g).length).toBe(4, 'four fields| ' + msg)
                expect(typeof g.id === 'string').toBe(true, '*id* is a string| ' + msg)

                var pLen = Object.keys(p).length
                expect(pLen).toBe(expNumOfProps, '# properties field| ' + msg)
                expect(Array.isArray(p.ct)).toBe(true, '*properties.ct* is an array| ' + msg)
                if (pLen > 1) {
                  expect(typeof p.gu === 'string').toBe(true, '*properties.gu* is a string| ' + msg)
                }

                list.push(g.id)
              } else {
                expect(Object.keys(g).length).toBe(2, 'just two fields| ' + msg)
              }

              expect(Array.isArray(g.arcs)).toBe(true, '*arcs* is an array| ' + msg)
              expect(typeof g.type === 'string').toBe(true, '*type* is a string| ' + msg)
            })
            break
          default:
            fail('Unknown layer ' + l + ' in topojson ' + k)
            break
        }

        switch (l) {
          case 'countries':
            expect(list.length).toBe(assets.COUNTRIES_CNT[k], '# of countries| ' + [k, l])
            break
          case 'subunits':
            expect(list.length).toBe(assets.SUBUNITS_CNT[k], '# of subunits| ' + [k, l])
            break
        }
      })
    })
  })

  it('should have correct set of country IDs', () => {
    Object.keys(saneTopojson).forEach((k) => {
      var actual = saneTopojson[k].objects.countries.geometries
        .map(g => g.id).filter(Boolean).sort()
      var d = diff(assets.COUNTRY_LIST[k], actual)
      expect(d.removed).withContext('removed country for list| ' + k).toEqual([])
      expect(d.added).withContext('added country for list| ' + k).toEqual([])
    })
  })

  it('should have correct set of subunit IDs', () => {
    Object.keys(saneTopojson).forEach((k) => {
      var actual = saneTopojson[k].objects.subunits.geometries
        .map(g => g.id).filter(Boolean).sort()
      var d = diff(assets.SUBUNITS_LIST[k], actual)
      expect(d.removed).withContext('removed subunit for list| ' + k).toEqual([])
      expect(d.added).withContext('added subunit for list| ' + k).toEqual([])
    })
  })
})

describe('sane topojson with d3-geo & topojson', () => {
  beforeEach(() => {
    this.svg = d3.select('body').append('svg')
      .attr('width', 960)
      .attr('height', 500)
  })

  afterEach(() => {
    document.body.removeChild(this.svg.node())
  })

  describe('should be able to draw path all layers', () => {
    Object.keys(saneTopojson).forEach((k) => {
      var saneTopojsonItem = saneTopojson[k]

      Object.keys(d3.geo).forEach((p) => {
        var projFunc = d3.geo[p]

        if (!(
          typeof projFunc === 'function' &&
                    projFunc.raw !== undefined
        )) return

        it('in topojson ' + k + ' using projection function ' + p, () => {
          appendLayers(this.svg, projFunc, saneTopojsonItem)

          var paths = this.svg.selectAll('path')

          expect(paths.size()).toEqual(7)

          paths.each(function () {
            var path = d3.select(this)

            var l = path.attr('id')

            if (
              l === 'subunits' &&
                            assets.ITEM_WITH_NO_SUBUNITS.indexOf(k) !== -1
            ) {
              expect(path.attr('d')).toBe(null)
            } else {
              expect(path.attr('d').length > 1).toBe(true)
            }
          })
        })
      })
    })
  })
})

function appendLayers (svg, projFunc, saneTopojsonItem) {
  var width = +svg.attr('width')
  var height = svg.attr('height')

  var projection = projFunc()
    .translate([width / 2, height / 2])
    .precision(0.1)

  var path = d3.geo.path().projection(projection)

  Object.keys(saneTopojsonItem.objects).forEach((l) => {
    var datum = topojson.feature(
      saneTopojsonItem,
      saneTopojsonItem.objects[l]
    )

    svg.append('path')
      .datum(datum)
      .attr('d', path)
      .attr('id', l)
  })
}
