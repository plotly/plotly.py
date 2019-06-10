'use strict'

module.exports = extractContour

var ndarray = require('ndarray')
var pool    = require('typedarray-pool')
var ndsort  = require('ndarray-sort')

var contourAlgorithm = require('./lib/codegen')

function getDimension(cells) {
  var numCells = cells.length
  var d = 0
  for(var i=0; i<numCells; ++i) {
    d = Math.max(d, cells[i].length)|0
  }
  return d-1
}

function getSigns(values, level) {
  var numVerts    = values.length
  var vertexSigns = pool.mallocUint8(numVerts)
  for(var i=0; i<numVerts; ++i) {
    vertexSigns[i] = (values[i] < level)|0
  }
  return vertexSigns
}

function getEdges(cells, d) {
  var numCells = cells.length
  var maxEdges = ((d * (d+1)/2) * numCells)|0
  var edges    = pool.mallocUint32(maxEdges*2)
  var ePtr     = 0
  for(var i=0; i<numCells; ++i) {
    var c = cells[i]
    var d = c.length
    for(var j=0; j<d; ++j) {
      for(var k=0; k<j; ++k) {
        var a = c[k]
        var b = c[j]
        edges[ePtr++] = Math.min(a,b)|0
        edges[ePtr++] = Math.max(a,b)|0
      }
    }
  }
  var nedges = (ePtr/2)|0
  ndsort(ndarray(edges, [nedges,2])) 
  var ptr = 2
  for(var i=2; i<ePtr; i+=2) {
    if(edges[i-2] === edges[i] &&
       edges[i-1] === edges[i+1]) {
      continue
    }
    edges[ptr++] = edges[i]
    edges[ptr++] = edges[i+1]
  }

  return ndarray(edges, [(ptr/2)|0, 2])
}

function getCrossingWeights(edges, values, signs, level) {
  var edata     = edges.data
  var numEdges  = edges.shape[0]
  var weights   = pool.mallocDouble(numEdges)
  var ptr       = 0
  for(var i=0; i<numEdges; ++i) {
    var a  = edata[2*i]
    var b  = edata[2*i+1]
    if(signs[a] === signs[b]) {
      continue
    }
    var va = values[a]
    var vb = values[b]
    edata[2*ptr]     = a
    edata[2*ptr+1]   = b
    weights[ptr++]   = (vb - level) / (vb - va)
  }
  edges.shape[0] = ptr
  return ndarray(weights, [ptr])
}

function getCascade(edges, numVerts) {
  var result   = pool.mallocInt32(numVerts*2)
  var numEdges = edges.shape[0]
  var edata    = edges.data
  result[0]    = 0
  var lastV    = 0
  for(var i=0; i<numEdges; ++i) {
    var a = edata[2*i]
    if(a !== lastV) {
      result[2*lastV+1] = i
      while(++lastV < a) {
        result[2*lastV] = i
        result[2*lastV+1] = i
      }
      result[2*lastV] = i
    }
  }
  result[2*lastV+1] = numEdges
  while(++lastV < numVerts) {
    result[2*lastV] = result[2*lastV+1] = numEdges
  }
  return result
}

function unpackEdges(edges) {
  var ne = edges.shape[0]|0
  var edata = edges.data
  var result = new Array(ne)
  for(var i=0; i<ne; ++i) {
    result[i] = [edata[2*i], edata[2*i+1]]
  }
  return result
}

function extractContour(cells, values, level, d) {
  level = level||0.0

  //If user didn't specify `d`, use brute force scan
  if(typeof d === 'undefined') {
    d = getDimension(cells)
  }

  //Count number of cells
  var numCells = cells.length
  if(numCells === 0 || d < 1) {
    return {
      cells:         [],
      vertexIds:     [],
      vertexWeights: []
    }
  }

  //Read in vertex signs
  var vertexSigns = getSigns(values, +level)

  //First get 1-skeleton, find all crossings
  var edges   = getEdges(cells, d)
  var weights = getCrossingWeights(edges, values, vertexSigns, +level)

  //Build vertex cascade to speed up binary search
  var vcascade = getCascade(edges, values.length|0)

  //Then construct cells
  var faces = contourAlgorithm(d)(cells, edges.data, vcascade, vertexSigns)

  //Unpack data into pretty format
  var uedges   = unpackEdges(edges)
  var uweights = [].slice.call(weights.data, 0, weights.shape[0])

  //Release data
  pool.free(vertexSigns)
  pool.free(edges.data)
  pool.free(weights.data)
  pool.free(vcascade)
  
  return {
    cells:         faces,
    vertexIds:     uedges,
    vertexWeights: uweights
  }
}