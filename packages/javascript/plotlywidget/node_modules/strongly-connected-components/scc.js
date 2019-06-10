"use strict"

module.exports = stronglyConnectedComponents

function stronglyConnectedComponents(adjList) {
  var numVertices = adjList.length;
  var index = new Array(numVertices)
  var lowValue = new Array(numVertices)
  var active = new Array(numVertices)
  var child = new Array(numVertices)
  var scc = new Array(numVertices)
  var sccLinks = new Array(numVertices)
  
  //Initialize tables
  for(var i=0; i<numVertices; ++i) {
    index[i] = -1
    lowValue[i] = 0
    active[i] = false
    child[i] = 0
    scc[i] = -1
    sccLinks[i] = []
  }

  // The strongConnect function
  var count = 0
  var components = []
  var sccAdjList = []

  function strongConnect(v) {
    // To avoid running out of stack space, this emulates the recursive behaviour of the normal algorithm, effectively using T as the call stack.
    var S = [v], T = [v]
    index[v] = lowValue[v] = count
    active[v] = true
    count += 1
    while(T.length > 0) {
      v = T[T.length-1]
      var e = adjList[v]
      if (child[v] < e.length) { // If we're not done iterating over the children, first try finishing that.
        for(var i=child[v]; i<e.length; ++i) { // Start where we left off.
          var u = e[i]
          if(index[u] < 0) {
            index[u] = lowValue[u] = count
            active[u] = true
            count += 1
            S.push(u)
            T.push(u)
            break // First recurse, then continue here (with the same child!).
            // There is a slight change to Tarjan's algorithm here.
            // Normally, after having recursed, we set lowValue like we do for an active child (although some variants of the algorithm do it slightly differently).
            // Here, we only do so if the child we recursed on is still active.
            // The reasoning is that if it is no longer active, it must have had a lowValue equal to its own index, which means that it is necessarily higher than our lowValue.
          } else if (active[u]) {
            lowValue[v] = Math.min(lowValue[v], lowValue[u])|0
          }
          if (scc[u] >= 0) {
            // Node v is not yet assigned an scc, but once it is that scc can apparently reach scc[u].
            sccLinks[v].push(scc[u])
          }
        }
        child[v] = i // Remember where we left off.
      } else { // If we're done iterating over the children, check whether we have an scc.
        if(lowValue[v] === index[v]) { // TODO: It /might/ be true that T is always a prefix of S (at this point!!!), and if so, this could be used here.
          var component = []
          var links = [], linkCount = 0
          for(var i=S.length-1; i>=0; --i) {
            var w = S[i]
            active[w] = false
            component.push(w)
            links.push(sccLinks[w])
            linkCount += sccLinks[w].length
            scc[w] = components.length
            if(w === v) {
              S.length = i
              break
            }
          }
          components.push(component)
          var allLinks = new Array(linkCount)
          for(var i=0; i<links.length; i++) {
            for(var j=0; j<links[i].length; j++) {
              allLinks[--linkCount] = links[i][j]
            }
          }
          sccAdjList.push(allLinks)
        }
        T.pop() // Now we're finished exploring this particular node (normally corresponds to the return statement)
      }
    }
  }

  //Run strong connect starting from each vertex
  for(var i=0; i<numVertices; ++i) {
    if(index[i] < 0) {
      strongConnect(i)
    }
  }
  
  // Compact sccAdjList
  var newE
  for(var i=0; i<sccAdjList.length; i++) {
    var e = sccAdjList[i]
    if (e.length === 0) continue
    e.sort(function (a,b) { return a-b; })
    newE = [e[0]]
    for(var j=1; j<e.length; j++) {
      if (e[j] !== e[j-1]) {
        newE.push(e[j])
      }
    }
    sccAdjList[i] = newE
  }  

  return {components: components, adjacencyList: sccAdjList}
}
