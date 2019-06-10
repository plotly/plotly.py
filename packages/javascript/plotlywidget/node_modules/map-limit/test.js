var test = require('tape')
var mapl = require('./')

test('basic', function(t) {
  var items = [1, 2, 3, 4, 5]
  var goals = [2, 4, 6, 8,10]

  t.plan(2)

  mapl(items, 5, function(item, next) {
    next(null, item * 2)
  }, function(err, results) {
    t.ifError(err)
    t.deepEqual(results, goals)
  })
})

test('stalled', function(t) {
  var items = [1, 2, 3, 4, 5, 6, 7, 8]
  var goals = [2, 4, 6, 8,10,12,14,16]
  var n = 0

  t.plan(6)

  mapl(items, 2, function(item, next) {
    setTimeout(function() {
      n += 1
      next(null, item * 2)
    }, 150)
  }, function(err, results) {
    t.ifError(err)
    t.deepEqual(results, goals)
  })

  setTimeout(function() { t.equal(n, 2) }, 225)
  setTimeout(function() { t.equal(n, 4) }, 350)
  setTimeout(function() { t.equal(n, 6) }, 475)
  setTimeout(function() { t.equal(n, 8) }, 625)
})
