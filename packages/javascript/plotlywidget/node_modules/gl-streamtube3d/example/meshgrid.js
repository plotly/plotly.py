
var meshgridCoords = function(xs) {
  if (typeof xs === 'number') {
    return {start: xs, end: xs, step: 1};

  } else if (xs instanceof Array) {
    var obj = {start: xs[0], end: xs[0], step: 1};
    if (xs.length === 2) {
      obj.end = xs[1];
    }
    if (xs.length === 3) {
      obj.step = xs[1] || 1; // Force non-zero step
      obj.end = xs[2];
    }
    return obj;
  }

  var parsed = {start: xs.start, end: xs.end, step: xs.step};
  if (!parsed.step) { // Force non-zero step
    parsed.step = 1;
  }
  if (parsed.end === undefined) {
    parsed.end = parsed.start;
  }
  return parsed;
};

var meshgridExpand = function(xs) {
  var res = [];
  var step = xs.step;
  if (xs.start > xs.end && step > 0) {
    step = -step; // Use negative step when start is larger than end.
  }
  var count = (xs.end - xs.start) / step;

  res.push(xs.start); // Include start
  for (var i = 1; i < count; i++) {
    res.push(xs.start + i * step); // Interpolate values without accumulating error
  }
  if (xs.start !== xs.end) {
    res.push(xs.end); // Include end if it differs from start
  }

  return res;
}

var meshgrid = function(xs, ys, zs) {
  xs = meshgridCoords(xs);
  ys = meshgridCoords(ys);
  zs = meshgridCoords(zs);
  return [
    meshgridExpand(xs),
    meshgridExpand(ys),
    meshgridExpand(zs)
  ];
};

meshgrid.getBounds = function(mg) {
  return [
    mg.map(function(m) { return m[0]; }), 
    mg.map(function(m) { return m[m.length-1]; })
  ];
};

meshgrid.toPoints = function(mg) {
  var res = [];
  for (var z=0; z<mg[2].length; z++) {
    var mz = mg[2][z];
    for (var y=0; y<mg[1].length; y++) {
      var my = mg[1][y];
      for (var x=0; x<mg[0].length; x++) {
        var mx = mg[0][x];
        res.push([mx, my, mz]);
      }
    }
  }
  return res;
};

module.exports = meshgrid;