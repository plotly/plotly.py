var test = require('tape')
var path = require('path')

var through = require('through2')
var from = require('../')

function fromStrings() {
  return from.obj(['a', 'b', 'c'])
}

function fromObjects() {
  return from.obj([{
    name:'a'},{
    name:'b'},{
    name:'c'}])
}

test('from2 string array', function(t) {
  var stream = fromStrings()

  var arr = []
  stream
    .pipe(through.obj(function(chunk, enc, cb){
      arr.push(chunk)
      cb()
    }, function(){
      t.equal(arr.length, 3)
      t.equal(arr[0], 'a')
      t.equal(arr[1], 'b')
      t.equal(arr[2], 'c')
      t.end()
    }))
})

test('from2 object array', function(t) {
  var stream = fromObjects()

  var arr = []
  stream
    .pipe(through.obj(function(chunk, enc, cb){
      arr.push(chunk)
      cb()
    }, function(){
      t.equal(arr.length, 3)
      t.equal(arr[0].name, 'a')
      t.equal(arr[1].name, 'b')
      t.equal(arr[2].name, 'c')
      t.end()
    }))
})
