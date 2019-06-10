"use strict"

module.exports = simplifyPolygon

var orient = require("robust-orientation")
var sc = require("simplicial-complex")

function errorWeight(base, a, b) {
  var area = Math.abs(orient(base, a, b))
  var perim = Math.sqrt(Math.pow(a[0] - b[0], 2) + Math.pow(a[1]-b[1], 2))
  return area / perim
}

function simplifyPolygon(cells, positions, minArea) {

  var n = positions.length
  var nc = cells.length
  var inv = new Array(n)
  var outv = new Array(n)
  var weights = new Array(n)
  var dead = new Array(n)
  
  //Initialize tables
  for(var i=0; i<n; ++i) {
    inv[i] = outv[i] = -1
    weights[i] = Infinity
    dead[i] = false
  }

  //Compute neighbors
  for(var i=0; i<nc; ++i) {
    var c = cells[i]
    if(c.length !== 2) {
      throw new Error("Input must be a graph")
    }
    var s = c[1]
    var t = c[0]
    if(outv[t] !== -1) {
      outv[t] = -2
    } else {
      outv[t] = s
    }
    if(inv[s] !== -1) {
      inv[s] = -2
    } else {
      inv[s] = t
    }
  }

  //Updates the weight for vertex i
  function computeWeight(i) {
    if(dead[i]) {
      return Infinity
    }
    //TODO: Check that the line segment doesn't cross once simplified
    var s = inv[i]
    var t = outv[i]
    if((s<0) || (t<0)) {
      return Infinity
    } else {
      return errorWeight(positions[i], positions[s], positions[t])
    }
  }

  //Swaps two nodes on the heap (i,j) are the index of the nodes
  function heapSwap(i,j) {
    var a = heap[i]
    var b = heap[j]
    heap[i] = b
    heap[j] = a
    index[a] = j
    index[b] = i
  }

  //Returns the weight of node i on the heap
  function heapWeight(i) {
    return weights[heap[i]]
  }

  function heapParent(i) {
    if(i & 1) {
      return (i - 1) >> 1
    }
    return (i >> 1) - 1
  }

  //Bubble element i down the heap
  function heapDown(i) {
    var w = heapWeight(i)
    while(true) {
      var tw = w
      var left  = 2*i + 1
      var right = 2*(i + 1)
      var next = i
      if(left < heapCount) {
        var lw = heapWeight(left)
        if(lw < tw) {
          next = left
          tw = lw
        }
      }
      if(right < heapCount) {
        var rw = heapWeight(right)
        if(rw < tw) {
          next = right
        }
      }
      if(next === i) {
        return i
      }
      heapSwap(i, next)
      i = next      
    }
  }

  //Bubbles element i up the heap
  function heapUp(i) {
    var w = heapWeight(i)
    while(i > 0) {
      var parent = heapParent(i)
      if(parent >= 0) {
        var pw = heapWeight(parent)
        if(w < pw) {
          heapSwap(i, parent)
          i = parent
          continue
        }
      }
      return i
    }
  }

  //Pop minimum element
  function heapPop() {
    if(heapCount > 0) {
      var head = heap[0]
      heapSwap(0, heapCount-1)
      heapCount -= 1
      heapDown(0)
      return head
    }
    return -1
  }

  //Update heap item i
  function heapUpdate(i, w) {
    var a = heap[i]
    if(weights[a] === w) {
      return i
    }
    weights[a] = -Infinity
    heapUp(i)
    heapPop()
    weights[a] = w
    heapCount += 1
    return heapUp(heapCount-1)
  }

  //Kills a vertex (assume vertex already removed from heap)
  function kill(i) {
    if(dead[i]) {
      return
    }
    //Kill vertex
    dead[i] = true
    //Fixup topology
    var s = inv[i]
    var t = outv[i]
    if(inv[t] >= 0) {
      inv[t] = s
    }
    if(outv[s] >= 0) {
      outv[s] = t
    }

    //Update weights on s and t
    if(index[s] >= 0) {
      heapUpdate(index[s], computeWeight(s))
    }
    if(index[t] >= 0) {
      heapUpdate(index[t], computeWeight(t))
    }
  }

  //Initialize weights and heap
  var heap = []
  var index = new Array(n)
  for(var i=0; i<n; ++i) {
    var w = weights[i] = computeWeight(i)
    if(w < Infinity) {
      index[i] = heap.length
      heap.push(i)
    } else {
      index[i] = -1
    }
  }
  var heapCount = heap.length
  for(var i=heapCount>>1; i>=0; --i) {
    heapDown(i)
  }
  
  //Kill vertices
  while(true) {
    var hmin = heapPop()
    if((hmin < 0) || (weights[hmin] > minArea)) {
      break
    }
    kill(hmin)
  }

  //Build collapsed vertex table
  var npositions = []
  for(var i=0; i<n; ++i) {
    if(!dead[i]) {
      index[i] = npositions.length
      npositions.push(positions[i].slice())
    }
  }
  var nv = npositions.length

  function tortoiseHare(seq, start) {
    if(seq[start] < 0) {
      return start
    }
    var t = start
    var h = start
    do {
      //Walk two steps with h
      var nh = seq[h]
      if(!dead[h] || nh < 0 || nh === h) {
        break
      }
      h = nh
      nh = seq[h]
      if(!dead[h] || nh < 0 || nh === h) {
        break
      }
      h = nh

      //Walk one step with t
      t = seq[t]
    } while(t !== h)
    //Compress cycles
    for(var v=start; v!==h; v = seq[v]) {
      seq[v] = h
    }
    return h
  }

  var ncells = []
  cells.forEach(function(c) {
    var tin = tortoiseHare(inv, c[0])
    var tout = tortoiseHare(outv, c[1])
    if(tin >= 0 && tout >= 0 && tin !== tout) {
      var cin = index[tin]
      var cout = index[tout]
      if(cin !== cout) {
        ncells.push([ cin, cout ])
      }
    }
  })

  //Normalize result
  sc.unique(sc.normalize(ncells))

  //Return final list of cells
  return {
    positions: npositions,
    edges: ncells
  }
}