"use strict";

var vec3 = require('gl-vec3');
var vec4 = require('gl-vec4');

var streamToTube = function(stream, maxDivergence, minDistance, maxNorm) {
	var points = stream.points;
	var velocities = stream.velocities;
	var divergences = stream.divergences;

	var p, fwd, r, u, v, up;
	up = vec3.set(vec3.create(), 0, 1, 0);
	u = vec3.create();
	v = vec3.create();
	var p2 = vec3.create();

	var verts = [];
	var faces = [];
	var vectors = [];
	var previousVerts = [];
	var currentVerts = [];
	var intensities = [];
	var previousIntensity = 0;
	var currentIntensity = 0;
	var currentVector = vec4.create();
	var previousVector = vec4.create();

	var facets = 8;

	for (var i = 0; i < points.length; i++) {
		p = points[i];
		fwd = velocities[i];
		r = divergences[i];
		if (maxDivergence === 0) {
			r = minDistance * 0.05;
		}
		currentIntensity = vec3.length(fwd) / maxNorm;
		currentVector = vec4.create();
		vec3.copy(currentVector, fwd);
		currentVector[3] = r;
		
		for (var a = 0; a < facets; a++) {
			currentVerts[a] = [p[0], p[1], p[2], a];
		}
		if (previousVerts.length > 0) {
			for (var a = 0; a < facets; a++) {
				var a1 = (a+1) % facets;
				verts.push(
					previousVerts[a],
					currentVerts[a],
					currentVerts[a1],

					currentVerts[a1],
					previousVerts[a1],
					previousVerts[a]
				);
				vectors.push(
					previousVector,
					currentVector,
					currentVector,

					currentVector,
					previousVector,
					previousVector
				);
				intensities.push(
					previousIntensity,
					currentIntensity,
					currentIntensity,

					currentIntensity,
					previousIntensity,
					previousIntensity
				);
				faces.push(
					[verts.length-6, verts.length-5, verts.length-4],
					[verts.length-3, verts.length-2, verts.length-1]
				);
			}
		}
		var tmp = previousVerts;
		previousVerts = currentVerts;
		currentVerts = tmp;
		tmp = previousVector;
		previousVector = currentVector;
		currentVector = tmp;
		tmp = previousIntensity;
		previousIntensity = currentIntensity;
		currentIntensity = tmp;
	}
	return {
		positions: verts,
		cells: faces,
		vectors: vectors,
		vertexIntensity: intensities
	};

};

var createTubes = function(streams, colormap, maxDivergence, minDistance) {

	var maxNorm = 0;
	for (var i=0; i<streams.length; i++) {
		var velocities = streams[i].velocities;
		for (var j=0; j<velocities.length; j++) {
			var norm = vec3.length(velocities[j]);
			if (norm > maxNorm) {
				maxNorm = norm;
			}
		}
	}

	var tubes = streams.map(function(s) {
		return streamToTube(s, maxDivergence, minDistance, maxNorm);
	});

	var positions = [];
	var cells = [];
	var vectors = [];
	var vertexIntensity = [];
	for (var i=0; i < tubes.length; i++) {
		var tube = tubes[i];
		var offset = positions.length;
		positions = positions.concat(tube.positions);
		vectors = vectors.concat(tube.vectors);
		vertexIntensity = vertexIntensity.concat(tube.vertexIntensity);
		for (var j=0; j<tube.cells.length; j++) {
			var cell = tube.cells[j];
			var newCell = [];
			cells.push(newCell);
			for (var k=0; k<cell.length; k++) {
				newCell.push(cell[k] + offset);
			}
		}
	}
	return {
		positions: positions,
		cells: cells,
		vectors: vectors,
		vertexIntensity: vertexIntensity,
		colormap: colormap
	};
};

var defaultGetDivergence = function(p, v0) {
	var dp = vec3.create();
	var e = 1/10000;

	vec3.add(dp, p, [e, 0, 0]);
	var vx = this.getVelocity(dp);
	vec3.subtract(vx, vx, v0);
	vec3.scale(vx, vx, 1/e);

	vec3.add(dp, p, [0, e, 0]);
	var vy = this.getVelocity(dp);
	vec3.subtract(vy, vy, v0);
	vec3.scale(vy, vy, 1/e);

	vec3.add(dp, p, [0, 0, e]);
	var vz = this.getVelocity(dp);
	vec3.subtract(vz, vz, v0);
	vec3.scale(vz, vz, 1/e);

	vec3.add(dp, vx, vy);
	vec3.add(dp, dp, vz);
	return dp;
};

var defaultGetVelocity = function(p) {
    var u = sampleMeshgrid(p, this.vectors, this.meshgrid, this.clampBorders);
    return u;
};


var findLastSmallerIndex = function(points, v) {
  for (var i=0; i<points.length; i++) {
  	var p = points[i];
  	if (p === v) return i;
    if (p > v) return i-1;
  }
  return i;
};

var tmp = vec3.create();
var tmp2 = vec3.create();

var clamp = function(v, min, max) {
	return v < min ? min : (v > max ? max : v);
};

var sampleMeshgrid = function(point, array, meshgrid, clampOverflow) {
	var x = point[0];
	var y = point[1];
	var z = point[2];

	var w = meshgrid[0].length;
	var h = meshgrid[1].length;
	var d = meshgrid[2].length;

	// Find the index of the nearest smaller value in the meshgrid for each coordinate of (x,y,z).
	// The nearest smaller value index for x is the index x0 such that
	// meshgrid[0][x0] < x and for all x1 > x0, meshgrid[0][x1] >= x.
	var x0 = findLastSmallerIndex(meshgrid[0], x);
	var y0 = findLastSmallerIndex(meshgrid[1], y);
	var z0 = findLastSmallerIndex(meshgrid[2], z);

	// Get the nearest larger meshgrid value indices.
	// From the above "nearest smaller value", we know that
	//   meshgrid[0][x0] < x
	//   meshgrid[0][x0+1] >= x
	var x1 = x0 + 1;
	var y1 = y0 + 1;
	var z1 = z0 + 1;

	if (meshgrid[0][x0] === x) x1 = x0;
	if (meshgrid[1][y0] === y) y1 = y0;
	if (meshgrid[2][z0] === z) z1 = z0;

	if (clampOverflow) {
		x0 = clamp(x0, 0, w-1);
		x1 = clamp(x1, 0, w-1);
		y0 = clamp(y0, 0, h-1);
		y1 = clamp(y1, 0, h-1);
		z0 = clamp(z0, 0, d-1);
		z1 = clamp(z1, 0, d-1);
	}

	// Reject points outside the meshgrid, return a zero vector.
	if (x0 < 0 || y0 < 0 || z0 < 0 || x1 >= w || y1 >= h || z1 >= d) {
		return vec3.create();
	}

	// Normalize point coordinates to 0..1 scaling factor between x0 and x1.
	var xf = (x - meshgrid[0][x0]) / (meshgrid[0][x1] - meshgrid[0][x0]);
	var yf = (y - meshgrid[1][y0]) / (meshgrid[1][y1] - meshgrid[1][y0]);
	var zf = (z - meshgrid[2][z0]) / (meshgrid[2][z1] - meshgrid[2][z0]);

	if (xf < 0 || xf > 1 || isNaN(xf)) xf = 0;
	if (yf < 0 || yf > 1 || isNaN(yf)) yf = 0;
	if (zf < 0 || zf > 1 || isNaN(zf)) zf = 0;

	var z0off = z0*w*h;
	var z1off = z1*w*h;

	var y0off = y0*w;
	var y1off = y1*w;

	var x0off = x0;
	var x1off = x1;

	// Sample data array around the (x,y,z) point.
	//  vZYX = array[zZoff + yYoff + xXoff]
	var v000 = array[y0off + z0off + x0off];
	var v001 = array[y0off + z0off + x1off];
	var v010 = array[y1off + z0off + x0off];
	var v011 = array[y1off + z0off + x1off];
	var v100 = array[y0off + z1off + x0off];
	var v101 = array[y0off + z1off + x1off];
	var v110 = array[y1off + z1off + x0off];
	var v111 = array[y1off + z1off + x1off];

	var result = vec3.create();

	// Average samples according to distance to point.
	vec3.lerp(result, v000, v001, xf);
	vec3.lerp(tmp, v010, v011, xf);
	vec3.lerp(result, result, tmp, yf);
	vec3.lerp(tmp, v100, v101, xf);
	vec3.lerp(tmp2, v110, v111, xf);
	vec3.lerp(tmp, tmp, tmp2, yf);
	vec3.lerp(result, result, tmp, zf);

	return result;
};


var vabs = function(dst, v) {
	var x = v[0];
	var y = v[1];
	var z = v[2];
	dst[0] = x >= 0 ? x : -x;
	dst[1] = y >= 0 ? y : -y;
	dst[2] = z >= 0 ? z : -z;
	return dst;
};

var findMinSeparation = function(xs) {
	var minSeparation = 1/0;
	xs.sort(function(a, b) { return a - b; });
	for (var i=1; i<xs.length; i++) {
		var d = Math.abs(xs[i] - xs[i-1]);
		if (d < minSeparation) {
			minSeparation = d;
		}
	}
	return minSeparation;
};

// Finds the minimum per-component distance in positions.
// 
var calculateMinPositionDistance = function(positions) {
	var xs = [], ys = [], zs = [];
	var xi = {}, yi = {}, zi = {};
	for (var i=0; i<positions.length; i++) {
		var p = positions[i];
		var x = p[0], y = p[1], z = p[2];

		// Split the positions array into arrays of unique component values.
		//
		// Why go through the trouble of using a uniqueness hash table vs
		// sort and uniq: 
		//
		// Suppose you've got a million positions in a 100x100x100 grid.
		//
		// Using a uniqueness hash table, you're doing 1M array reads, 
		// 3M hash table lookups from 100-element hashes, 300 hash table inserts, then
		// sorting three 100-element arrays and iterating over them.
		// Roughly, 1M + 3M * ln(100) + 300 * ln(100/2) + 3 * 100 * ln(100) + 3 * 100 = 
		//          1M + 13.8M + 0.0012M +  0.0014M + 0.0003M 
		//          =~ 15M
		//
		// Sort and uniq solution would do 1M array reads, 3M array inserts,
		// sort three 1M-element arrays and iterate over them.
		// Roughly, 1M + 3M + 3 * 1M * ln(1M) + 3 * 1M = 
		//          1M + 3M + 41.4M + 3M 
		//          =~ 48.4M
		//
		// Guessing that a hard-coded sort & uniq would be faster due to not having
		// to run a hashing function on everything. More memory usage though 
		// (bunch of small hash tables vs. duplicating the input array.)
		//
		// In JS-land, who knows. Maybe xi[x] casts x to string and destroys perf, 
		// maybe numeric keys get special-cased, maybe the object lookups run at near O(1)-speeds.
		// Maybe the sorting comparison function is expensive to call, maybe it gets inlined or special-cased.
		//
		// ... You're probably not going to call this with more than 10k positions anyhow, so this is very academic.
		//
		if (!xi[x]) {
			xs.push(x);
			xi[x] = true;
		}
		if (!yi[y]) {
			ys.push(y);
			yi[y] = true;
		}
		if (!zi[z]) {
			zs.push(z);
			zi[z] = true;
		}
	}
	var xSep = findMinSeparation(xs);
	var ySep = findMinSeparation(ys);
	var zSep = findMinSeparation(zs);
	var minSeparation = Math.min(xSep, ySep, zSep);
	if (!isFinite(minSeparation)) {
		return 1;
	}
	return minSeparation;
};

module.exports = function(vectorField, bounds) {
	var positions = vectorField.startingPositions;
	var maxLength = vectorField.maxLength || 1000;
	var tubeSize = vectorField.tubeSize || 1;
	var absoluteTubeSize = vectorField.absoluteTubeSize;

	if (!vectorField.getDivergence) {
		vectorField.getDivergence = defaultGetDivergence;
	}

	if (!vectorField.getVelocity) {
		vectorField.getVelocity = defaultGetVelocity;
	}

	if (vectorField.clampBorders === undefined) {
		vectorField.clampBorders = true;
	}

	var streams = [];

	var minX = bounds[0][0], minY = bounds[0][1], minZ = bounds[0][2];
	var maxX = bounds[1][0], maxY = bounds[1][1], maxZ = bounds[1][2];

	var inBounds = function(bounds, p) {
		var x = p[0];
		var y = p[1];
		var z = p[2];
		return (
			x >= minX && x <= maxX &&
			y >= minY && y <= maxY &&
			z >= minZ && z <= maxZ
		);
	};

	var boundsSize = vec3.distance(bounds[0], bounds[1]);
	var maxStepSize = 10 * boundsSize / maxLength;
	var maxStepSizeSq = maxStepSize * maxStepSize;

	var minDistance = 1;
	var maxDivergence = 0; // For component-wise divergence vec3.create();
	var tmp = vec3.create();

	if (positions.length >= 2) {
		minDistance = calculateMinPositionDistance(positions);
	}

	for (var i = 0; i < positions.length; i++) {
		var p = vec3.create();
		vec3.copy(p, positions[i]);

		var stream = [p];
		var velocities = [];
		var v = vectorField.getVelocity(p);
		var op = p;
		velocities.push(v);

		var divergences = [];

		var dv = vectorField.getDivergence(p, v);
		var dvLength = vec3.length(dv);
		if (dvLength > maxDivergence && !isNaN(dvLength) && isFinite(dvLength)) {
			maxDivergence = dvLength;
		}
		// In case we need to do component-wise divergence visualization
		// vec3.max(maxDivergence, maxDivergence, vabs(tmp, dv));
		divergences.push(dvLength);

		streams.push({points: stream, velocities: velocities, divergences: divergences});

		var j = 0;

		while (j < maxLength * 100 && stream.length < maxLength && inBounds(bounds, p)) {
			j++;
			var np = vec3.clone(v);
			var sqLen = vec3.squaredLength(np);
			if (sqLen === 0) {
				break;
			} else if (sqLen > maxStepSizeSq) {
				vec3.scale(np, np, maxStepSize / Math.sqrt(sqLen));
			}
			vec3.add(np, np, p);

			v = vectorField.getVelocity(np);

			if (vec3.squaredDistance(op, np) - maxStepSizeSq > -0.0001 * maxStepSizeSq) {
				stream.push(np);
				op = np;
				velocities.push(v);
				var dv = vectorField.getDivergence(np, v);
				var dvLength = vec3.length(dv);
				if (dvLength > maxDivergence && !isNaN(dvLength) && isFinite(dvLength)) {
					maxDivergence = dvLength;
				}
				// In case we need to do component-wise divergence visualization
				//vec3.max(maxDivergence, maxDivergence, vabs(tmp, dv));
				divergences.push(dvLength);
			}

			p = np;
		}
	}

	// Replace NaNs and Infinities with non-NaN, finite maxDivergence
	for (var i=0; i<divergences.length; i++) {
		var dvLength = divergences[i];
		if (isNaN(dvLength) || !isFinite(dvLength)) {
			divergences[i] = maxDivergence;
		}
	}

	var tubes = createTubes(streams, vectorField.colormap, maxDivergence, minDistance);

	if (absoluteTubeSize) {
		tubes.tubeScale = absoluteTubeSize;
	} else {
		// Avoid division by zero.
		if (maxDivergence === 0) {
			maxDivergence = 1;
		}
		tubes.tubeScale = tubeSize * 0.5 * minDistance / maxDivergence;
	}

	return tubes;
};

module.exports.createTubeMesh = require('./lib/tubemesh');
