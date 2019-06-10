var cases = []

for(var i=1; i<4; ++i) {
  var n = Math.pow(10, i)|0
  var points = new Array(n)
  for(var j=0; j<n; ++j) {
    points[j] = [ Math.random(), Math.random() ]
  }
  cases.push({
    name: "Random, n=" + n, 
    points: points
  })
}

module.exports = cases