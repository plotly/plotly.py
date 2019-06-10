'use strict'

module.exports = getPolygonizer

var pool = require('typedarray-pool')
var createMSTable = require('marching-simplex-table')

var CACHE = {}

function createCellPolygonizer(d) {
  var maxCellSize = 0
  var tables = new Array(d+1)
  tables[0] = [ [] ]
  for(var i=1; i<=d; ++i) {
    var tab = tables[i] = createMSTable(i)
    for(var j=0; j<tab.length; ++j) {
      maxCellSize = Math.max(maxCellSize, tab[i].length)
    }
  }

  var code  = [
  'function B(C,E,i,j){',
    'var a=Math.min(i,j)|0,b=Math.max(i,j)|0,l=C[2*a],h=C[2*a+1];',
    'while(l<h){',
      'var m=(l+h)>>1,v=E[2*m+1];',
      'if(v===b){return m}',
      'if(b<v){h=m}else{l=m+1}',
    '}',
    'return l;',
  '};',
  'function getContour', d, 'd(F,E,C,S){',
    'var n=F.length,R=[];',
    'for(var i=0;i<n;++i){var c=F[i],l=c.length;'
  ]

  function generateCase(facets) {
    if(facets.length <= 0) {
      return
    }
    code.push('R.push(')
    for(var i=0; i<facets.length; ++i) {
      var facet = facets[i]
      if(i > 0) {
        code.push(',')
      }
      code.push('[')
      for(var j=0; j<facet.length; ++j) {
        var f = facet[j]
        if(j > 0) {
          code.push(',')
        }
        code.push('B(C,E,c[', f[0], '],c[', f[1], '])')
      }
      code.push(']')
    }
    code.push(');')
  }

  for(var i=d+1; i>1; --i) {
    if(i < d+1) {
      code.push('else ')
    }
    code.push('if(l===', i, '){')

    //Generate mask
    var maskStr = []
    for(var j=0; j<i; ++j) {
      maskStr.push('(S[c['+j+']]<<'+j+')')
    }

    //Perform table look up
    code.push('var M=', maskStr.join('+'), 
      ';if(M===0||M===', (1<<i)-1, 
        '){continue}switch(M){')

    var tab = tables[i-1]
    for(var j=0; j<tab.length; ++j) {
      code.push('case ', j, ':')
      generateCase(tab[j])
      code.push('break;')
    }
    code.push('}}')
  }
  code.push('}return R;};return getContour', d, 'd')

  var proc = new Function('pool', code.join(''))
  return proc(pool)
}

function getPolygonizer(d) {
  var alg = CACHE[d]
  if(!alg) {
    alg = CACHE[d] = createCellPolygonizer(d) 
  }
  return alg
}