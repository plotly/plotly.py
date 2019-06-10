var util = require('util')
var tape = require('tape')

var createIntervalTree = require('../interval-tree.js')

function cmpInterval(a, b) {
  var d = a[0] - b[0]
  if(d) { return d }
  return a[1] - b[1]
}

tape('fuzz test', function(t) {
  function verifyTree(tree, intervals) {
    function testInterval(x) {
      var expected = []
      if(x[0] <= x[1])
      for(var j=0; j<intervals.length; ++j) {
        var y = intervals[j]
        if(x[1] >= y[0] && y[1] >= x[0]) {
          expected.push(y)
        }
      }
      expected.sort(cmpInterval)

      var actual = []
      tree.queryInterval(x[0], x[1], function(j) {
        actual.push(j)
      })
      actual.sort(cmpInterval)

      t.same(actual, expected, 'query interval: ' + x)
    }
    for(var i=0; i<intervals.length; ++i) {
      testInterval(intervals[i])
    }
    testInterval([-Infinity, Infinity])
    testInterval([0,0])
    testInterval([Infinity, -Infinity])
    for(var i=0; i<100; ++i) {
      testInterval([Math.random(), 2*Math.random()])
    }

    //Verify queryPoint
    function testPoint(p) {
      var expected = []
      for(var j=0; j<intervals.length; ++j) {
        var y = intervals[j]
        if(y[0] <= p && p <= y[1]) {
          expected.push(y)
        }
      }
      expected.sort(cmpInterval)

      var actual = []
      tree.queryPoint(p, function(y) {
        actual.push(y)
      })
      actual.sort(cmpInterval)

      t.same(actual, expected, 'query point: ' + p)
    }
    for(var i=0; i<intervals.length; ++i) {
      testPoint(intervals[i][0])
      testPoint(intervals[i][1])
    }
    testPoint(0)
    testPoint(-1)
    testPoint(1)
    testPoint(-Infinity)
    testPoint(Infinity)
    for(var i=0; i<100; ++i) {
      testPoint(Math.random())
    }

    //Check tree contents
    t.equals(tree.count, intervals.length, 'interval count ok')
    var treeIntervals = tree.intervals.slice()
    treeIntervals.sort(cmpInterval)
    var expectedIntervals = intervals.slice()
    expectedIntervals.sort(cmpInterval)
    t.same(treeIntervals, expectedIntervals, 'intervals same')

    //Check tree invariants
    function verifyNode(node, left, right) {
      if(!node) {
        return 0
      }
      var midp = node.mid
      t.ok(left < midp && midp < right, 'mid point in range: ' + node.mid + ' in ' + [left,right])

      //Verify left end points in ascending order
      var leftP = node.leftPoints.slice()
      for(var i=0; i<leftP.length; ++ i) {
        if(i > 0) {
          t.ok(leftP[i][0] >= leftP[i-1][0], 'order ok')
        }
        var y = leftP[i]
        t.ok(y[0] <= midp && midp <= y[1], 'interval ok')
      }

      //Verify right end points in ascending order
      var rightP = node.rightPoints.slice()
      for(var i=0; i<rightP.length; ++ i) {
        if(i > 0) {
          t.ok(rightP[i][1] >= rightP[i-1][1], 'order ok')
        }
        var y = rightP[i]
        t.ok(y[0] <= midp && midp <= y[1], 'interval ok')
      }

      leftP.sort(cmpInterval)
      rightP.sort(cmpInterval)
      t.same(leftP, rightP, 'intervals are consistent')

      var leftCount = verifyNode(node.left, left, node.mid)
      var rightCount = verifyNode(node.right, node.mid, right)
      var actualCount = leftCount + rightCount + leftP.length
      t.equals(node.count, actualCount, 'node count consistent')

      return actualCount
    }
    verifyNode(tree.root, -Infinity, Infinity)
  }

  //Check empty tree
  verifyTree(createIntervalTree(), [])

  //Try trees with uniformly distributed end points
  for(var count=0; count<10; ++count) {
    //Create empty tree and insert 100 intervals
    var intervals = []
    var tree = createIntervalTree()
    for(var i=0; i<100; ++i) {
      var a = Math.random()
      var b = a + Math.random()
      var x = [a,b]
      intervals.push(x)
      tree.insert(x)
    }
    verifyTree(tree, intervals)

    //Remove half the intervals
    for(var i=99; i>=50; --i) {
      tree.remove(intervals.pop())
    }
    verifyTree(tree, intervals)
  }

  //Trees with quantized end points
  for(var count=0; count<10; ++count) {
    //Create empty tree and insert 100 intervals
    var intervals = []
    var tree = createIntervalTree()
    for(var i=0; i<100; ++i) {
      var a = Math.floor(8.0*Math.random())/8.0
      var b = Math.max(a + Math.floor(8.0*Math.random())/8.0, 1.0)
      var x = [a,b]
      intervals.push(x)
      tree.insert(x)
    }
    verifyTree(tree, intervals)

    //Remove half the intervals
    for(var i=99; i>=50; --i) {
      tree.remove(intervals.pop())
    }
    verifyTree(tree, intervals)
  }

  var stackIntervals = []
  for(var i=0; i<100; ++i) {
    stackIntervals.push([i/200, 1.0-(i/200)])
  }
  var tree = createIntervalTree(stackIntervals)
  verifyTree(tree, stackIntervals)

  t.end()
})

tape('containment', function(t) {
  var tree = createIntervalTree([[0, 100]])
  var count = 0
  function incr() { count++ }

  tree.queryInterval(10, 20, incr)
  t.equals(count, 1)

  count = 0;
  tree.queryInterval(100, 100, incr)
  t.equals(count, 1)

  count = 0;
  tree.queryInterval(110, 111, incr)
  t.equals(count, 0)

  var tree = createIntervalTree([[0, 20], [30, 50]])
  count = 0
  tree.queryInterval(10, 15, incr)
  t.equals(count, 1)

  count = 0
  tree.queryInterval(25, 26, incr)
  t.equals(count, 0)

  count = 0
  tree.queryInterval(35, 40, incr)
  t.equals(count, 1)

  t.end()
})