var test = require("tape")
  , invert = require("../index.js")

function check_array(t, a, b) {
  var a_str = invert(a).join(",")
  var b_str = b.join(",")
  t.equals(a_str, b_str)
}


test("0", function(t) {
  check_array(t, [], [])
  t.end()
})

test("1", function(t) {
  check_array(t, [0], [0])
  t.end()
})


test("2", function(t) {
  check_array(t, [0,1], [0,1])
  check_array(t, [1,0], [1,0])
  t.end()
})

test("3", function(t) {
  check_array(t, [0,1,2], [0,1,2])
  check_array(t, [2,1,0], [2,1,0])
  check_array(t, [1,2,0], [2,0,1])
  t.end()
})

