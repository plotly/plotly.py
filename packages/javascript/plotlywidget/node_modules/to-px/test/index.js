'use strict'

var tape = require('tape')
var toPX = require('../')
var parseUnit = require('parse-unit')
var almostEqual = require('almost-equal')

var units = ['em', 'ch', 'ex', 'rem', 'px', 'vw', 'vh', 'vmin', 'vmax', 'in', 'cm', 'mm', 'pt', 'pc']

var fontSizes = ['20px', '10px', '1em', '3in']

tape('test to-px', function(t) {
  if (typeof document === 'undefined') return t.end()

  function testUnitsEmpirically(element) {
    var testDiv = document.createElement('div')
    element.appendChild(testDiv)
    for(var i=0; i<units.length; ++i) {
      testDiv.style['height'] = '128' + units[i]
      testDiv.style.position = 'absolute'
      testDiv.style.width = '1px'
      var expected = parseUnit(getComputedStyle(testDiv).getPropertyValue('height'))[0]/128
      var value = units[i]
      var actual = toPX(units[i], element)

      t.ok(almostEqual(actual, expected, 0.005, almostEqual.FLT_EPSILON),
        'testing: ' + units[i] + ' ' + actual + ' ~ ' + expected)

      value = '1' + units[i]
      actual = toPX(value, element)
      t.ok(almostEqual(actual, expected, 0.005, almostEqual.FLT_EPSILON),
        'testing: ' + value + ' ' + actual + ' ~ ' + expected)

      value = Math.PI + units[i]
      actual = toPX(value, element)
      expected *= Math.PI
      t.ok(almostEqual(actual, expected, 0.005, almostEqual.FLT_EPSILON),
        'testing: ' + value + ' ' + actual + ' ~ ' + expected)
    }
    element.removeChild(testDiv)
  }

  testUnitsEmpirically(document.body)

  var container = document.createElement('div')
  document.body.appendChild(container)
  for(var i=0; i<fontSizes.length; ++i) {
    container.style['font-size'] = fontSizes[i]
    testUnitsEmpirically(container)
  }

  var header = document.createElement('h1')
  document.body.appendChild(header)
  testUnitsEmpirically(header)

  t.end()
})

tape('edge cases', function (t) {
  t.equal(toPX(), null, 'no value')
  t.equal(toPX(''), null, 'empty string')
  t.equal(toPX(null), null, 'null value')
  t.equal(toPX('abc'), null, 'unknown units')
  t.equal(toPX('5def'), null, 'wrong units')
  t.equal(toPX('10'), null, 'number no units')
  t.equal(toPX(10), null, 'number value')

  t.end()
})
