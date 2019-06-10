`union-find`
==========

A basic union-find data structure for node.js.  For more information, see wikipdia:

[Disjoint Set Datastructures](http://en.wikipedia.org/wiki/Disjoint-set_data_structure)


Usage
=====
Here is an example showing how to do connected component labelling.  Assume we are given a graph with `VERTEX_COUNT` vertices and a list of edges stored in array represented by pairs of vertex indices:

    //Import data structure
    var UnionFind = require('union-find');
    
    //Link all the nodes together
    var forest = new UnionFind(VERTEX_COUNT);
    for(var i=0; i<edges.length; ++i) {
      forest.link(edges[i][0], edges[i][1]);
    }
    
    //Label components
    var labels = new Array(VERTEX_COUNT);
    for(var i=0; i<VERTEX_COUNT; ++i) {
      labels[i] = forest.find(i);
    }

Installation
============

    npm install union-find
    
    
Acknowledgements
================
(c) 2013 Mikola Lysenko.  MIT License

