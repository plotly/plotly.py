var barycentric = require("../barycentric.js")

require("tap").test("barycentric", function(t) {
  t.equals(barycentric([
    [0, 0],
    [1, 0],
    [0, 1]],
    [0.5, 0.5]).join(),
    [0, 0.5,0.5].join())

  t.end()
})