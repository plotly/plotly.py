var preprocessPolygon = require("point-in-big-polygon")
var classifyPoint = preprocessPolygon([
  [ [-10, -10], [-10, 10], [10, 10], [10, -10] ],
  [ [-1, -1], [1, -1], [1, 1], [-1, 1] ]
])

var img = []
for(var y=-12; y<=12; y+=0.5) {
  var row = []
  for(var x=-12; x<=12; x+=0.5) {
    var v = classifyPoint([x, y])
    if(v < 0) {
      row.push('-')
    } else if(v === 0) {
      row.push('o')
    } else {
      row.push('+')
    }
  }
  img.push(row.join(''))
}
console.log(img.join('\n'))