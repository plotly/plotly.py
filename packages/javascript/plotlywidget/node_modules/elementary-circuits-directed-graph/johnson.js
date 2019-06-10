var tarjan = require('strongly-connected-components');

module.exports = function findCircuits(edges) {
    var circuits = []; // Output

    var stack = [];
    var blocked = [];
    var B = {};
    var Ak = [];
    var s;

    function unblock(u) {
        blocked[u] = false;
        if(B.hasOwnProperty(u)) {
            Object.keys(B[u]).forEach(function(w) {
                delete B[u][w];
                if(blocked[w]) {unblock(w);}
            });
        }
    }

    function circuit(v) {
        var found = false;

        stack.push(v);
        blocked[v] = true;

        // L1
        var i;
        var w;
        for(i = 0; i < Ak[v].length; i++) {
            w = Ak[v][i];
            if(w === s) {
                output(s, stack);
                found = true;
            } else if(!blocked[w]) {
                found = circuit(w);
            }
        }

        // L2
        if(found) {
            unblock(v);
        } else {
            for(i = 0; i < Ak[v].length; i++) {
                w = Ak[v][i];
                var entry = B[w];

                if(!entry) {
                    entry = {};
                    B[w] = entry;
                }

                entry[w] = true;
            }
        }
        stack.pop();
        return found;
    }

    function output(start, stack) {
        var cycle = [].concat(stack).concat(start);
        circuits.push(cycle);
    }

    function subgraph(minId) {
      // Remove edges with indice smaller than minId
        for(var i = 0; i < edges.length; i++) {
            if(i < minId) edges[i] = [];
            edges[i] = edges[i].filter(function(i) {
                return i >= minId;
            });
        }
    }

    function adjacencyStructureSCC(from) {
      // Make subgraph starting from vertex minId
        subgraph(from);
        var g = edges;

      // Find strongly connected components using Tarjan algorithm
        var sccs = tarjan(g);

      // Filter out trivial connected components (ie. made of one node)
        var ccs = sccs.components.filter(function(scc) {
            return scc.length > 1;
        });

      // Find least vertex
        var leastVertex = Infinity;
        var leastVertexComponent;
        for(var i = 0; i < ccs.length; i++) {
            for(var j = 0; j < ccs[i].length; j++) {
                if(ccs[i][j] < leastVertex) {
                    leastVertex = ccs[i][j];
                    leastVertexComponent = i;
                }
            }
        }

        var cc = ccs[leastVertexComponent];

        if(!cc) return false;

      // Return the adjacency list of first component
        var adjList = edges.map(function(l, index) {
            if(cc.indexOf(index) === -1) return [];
            return l.filter(function(i) {
                return cc.indexOf(i) !== -1;
            });
        });

        return {
            leastVertex: leastVertex,
            adjList: adjList
        };
    }

    s = 0;
    var n = edges.length;
    while(s < n) {
        // find strong component with least vertex in
        // subgraph starting from vertex `s`
        var p = adjacencyStructureSCC(s);

        // Its least vertex
        s = p.leastVertex;
        // Its adjacency list
        Ak = p.adjList;

        if(Ak) {
            for(var i = 0; i < Ak.length; i++) {
                for(var j = 0; j < Ak[i].length; j++) {
                    var vertexId = Ak[i][j];
                    blocked[+vertexId] = false;
                    B[vertexId] = {};
                }
            }
            circuit(s);
            s = s + 1;
        } else {
            s = n;
        }

    }

    return circuits;
};
