var test = require("tap").test
  , top = require("../topology.js");

function arr_equals(t, a, b) {
  console.log(a, "---", b);
  t.equals(a.length, b.length, "length match");
  for(var i=0; i<a.length; ++i) {
    t.equals(top.compareCells(a[i], b[i]), 0, "cells["+i+"]: " + a[i] + ", " + b[i]);
  }
}

test("dimension", function(t) {
  t.equals(top.dimension([
    [0],
    [],
    [1,2,3],
    [4,5]
  ]), 2);
  t.end();
});

test("countVertices", function(t) {

  t.equals(top.countVertices([
    [1,2,3],
    [5, 6],
    [1000, 1]
  ]), 1001);
  
  t.equals(top.countVertices([]), 0)
  
  t.end();
});

test("cloneCells", function(t) {

  var a = [[1,2,3],[2,5]];
  var b = top.cloneCells(a);
  
  b[0][0] = 10;
  
  t.equals(a[0][0], 1);

  t.end();
});

test("compareCells", function(t) {
  t.ok(!!top.compareCells([], [1]));
  t.ok(!!top.compareCells([1,3,5], [1,3,5,7]));
  
  t.ok(!!top.compareCells([2], [3]) );
  t.ok( !top.compareCells([0], [0]) );
  
  t.ok(!!top.compareCells([4,3],[7,0]));
  t.ok( !top.compareCells([10,11], [11,10]));
  
  t.ok(!!top.compareCells([2,0,5], [3,0,4]));
  t.ok( !top.compareCells([0,1,2], [2,0,1]));
  t.ok( !top.compareCells([0,1,2], [1,2,0]));
  t.ok( !top.compareCells([0,1,2], [1,0,2]));

  t.ok(!!top.compareCells([2,4,5,6], [6,7,8,9]));
  t.ok(!!top.compareCells([1,2,3,6], [1,2,3,7]));
  t.ok( !top.compareCells([0,1,2,3], [3,1,2,0]));

  t.end();
});

test("normalize", function(t) {
  var r = [[6, 2, 3], [1, 2, 4], [0, 5, 1], [1], [5,0,1]]
    , s = top.cloneCells(r);
  top.normalize(s);
  
  for(var i=1; i<r.length; ++i) {
    var x = r[i]
      , j = Math.floor(Math.random() * i);
    r[i] = r[j];
    r[j] = x;
  }
  top.normalize(r);
  
  arr_equals(t, s, r);
  
  t.end();
});

test("skeleton", function(t) {

  var r = [[1,2,3]];
  arr_equals(t, top.unique(top.normalize(top.skeleton(r,1))), [
    [1,2],
    [1,3],
    [2,3]
  ]);
  
  var h = [[1,2,3],[2,3,4]];
  arr_equals(t, top.unique(top.normalize(top.skeleton(h, 1))), [
    [1,2],
    [1,3],
    [2,3],
    [2,4],
    [3,4]
  ]);
  
  var k = [[1,2,3,4,5,6,7,8]];
  arr_equals(t, top.normalize(top.skeleton(k, 0)), [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
  ]);

  var s = [[0,1,2,3]];
  arr_equals(t, top.skeleton(s, 2), [
    [0,1,2],
    [0,1,3],
    [0,2,3],
    [1,2,3]
  ]);

  t.end();
});

test("findCell", function(t) {

  var tris = [
    [1,2,3],
    [4,5,6],
    [6,7,8],
    [0],
    [1,2,5]
  ];

  top.normalize(tris);
  
  
  t.equals(top.findCell(tris, [6,4,6]), -1);
  t.equals(top.findCell(tris, []), -1);
  t.equals(top.findCell(tris, [10000,1000,1000,10000]), -1);
  t.equals(top.findCell(tris, [-1000]), -1);

  //Test central item
  var idx = top.findCell(tris, [6,4,5]);
  t.ok(idx > 0);
  t.equals(tris[idx][0], 4);
  t.equals(tris[idx][1], 5);
  t.equals(tris[idx][2], 6);

  //Test lower extreme
  t.equals(top.findCell(tris, [0], true), 0);
  
  //Test upper extreme
  t.equals(top.findCell(tris, [6,7,8]), tris.length-1);

  t.end();
});

test("buildIndex", function(t) {
  var from_cells = top.normalize([
    [0,1],
    [0,2],
    [1,2],
    [1,3],
    [2,3]
  ]);
  var to_cells = top.normalize([
    [0,1,2],
    [0,1,3],
    [0,2,3],
    [1,2,3]
  ]);
  
  var index = top.incidence(from_cells, to_cells);
  t.equals(index.length, from_cells.length);
  
  console.log(from_cells, to_cells);
  
  for(var i=0; i<from_cells.length; ++i) {
    var idx = index[i];
    console.log(from_cells[i], idx);
  }
  
  t.end();
});


test("dual", function(t) {
  
  var cells = top.normalize([
    [1,2,3],
    [0],
    [5,6,7],
    [8,3],
    [4,6],
    [2,5],
    [2,7],
    [2,0]
  ]);
  
  //Compute vertex stars
  console.log("Cells = ", cells);
  var stars = top.dual(cells);
  console.log("Dual (sparse) = ", stars);
  
  var tstars = top.dual(cells, 9);
  console.log("Dual (dense) = ", tstars);
  arr_equals(t, stars, tstars);
  
  t.end();
});

test("boundary", function(t) {

  var tris = top.normalize([
    [0,1,2],
    [0,1,3],
    [0,2,3],
    [1,2,3]
  ]);
  
  var tetra = [[0,1,2,3]];
  arr_equals(t,top.normalize(top.boundary(tetra,2)), tris);
  
  t.end();
});

test("explode", function(t) {

  var e = top.normalize(top.explode([[0,1,2]]))
  console.log(e)
  
  arr_equals(t, e, top.normalize([
    [0],
    [1],
    [2],
    [0,1],
    [1,2],
    [2,0],
    [0,1,2]
  ]))
  

  t.end()
})



test("connectedComponents", function(t) {

  var graph = top.normalize([
    [0,1],
    [1,2],
    [2,3],
    [5,6],
    [4],
    [4,7,8]
  ]);
  
  console.log(top.connectedComponents(graph));
  console.log(top.connectedComponents(graph,9));
  
  t.end();
});



