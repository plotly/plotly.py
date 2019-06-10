"use strict";

var V = require('gl-vec3');

var vec3 = function(x, y, z) {
	var v = V.create();
	if (x !== undefined) {
		V.set(v, x, y, z);
	}
	return v;
}

var createPositionsForMeshgrid = function(meshgrid) {
	var xs = meshgrid[0], ys = meshgrid[1], zs = meshgrid[2];
	var positions = [];
	for (var z=0; z<zs.length; z++) {
		for (var y=0; y<ys.length; y++) {
			for (var x=0; x<xs.length; x++) {
				positions.push([zs[z], ys[y], xs[x]]);
			}
		}
	}
	return positions;
};

var findLastSmallerIndex = function(points, v) {
	for (var i=0; i<points.length; i++) {
		if (points[i] >= v) {
			return i-1;
		}
	}
	return i;
};

var tmp = V.create();
var tmp2 = V.create();

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
		return V.create();
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

	var result = V.create();

	// Average samples according to distance to point.
	V.lerp(result, v000, v001, xf);
	V.lerp(tmp, v010, v011, xf);
	V.lerp(result, result, tmp, yf);
	V.lerp(tmp, v100, v101, xf);
	V.lerp(tmp2, v110, v111, xf);
	V.lerp(tmp, tmp, tmp2, yf);
	V.lerp(result, result, tmp, zf);

	return result;
};

var getOrthogonalVector = function(dst, v) {
	// Return up-vector for only-z vector.
	if (v[0] === 0 && v[1] === 0) {
		V.set(dst, 0, 1, 0);
	} else {
		// Return ax + by + cz = 0, a point that lies on the plane that has v as a normal and that isn't (0,0,0).
		// From the above if-statement we have ||a|| > 0  U  ||b|| > 0.
		// Assign z = 0, x = -b, y = a:
		// a*-b + b*a + c*0 = -ba + ba + 0 = 0
		V.set(dst, -v[1], v[0], 0);
	}
	return dst;
};

module.exports = function(vectorfield, bounds) {
	var positions;
	if (vectorfield.positions) {
		positions = vectorfield.positions;
	} else {
		positions = createPositionsForMeshgrid(vectorfield.meshgrid);
	}
	var meshgrid = vectorfield.meshgrid;
	var vectors = vectorfield.vectors;
	var geo = {
		positions: [],
		vertexIntensity: [],
		vertexIntensityBounds: vectorfield.vertexIntensityBounds,
		vertexNormals: [],
		vectors: [],
		cells: [],
		coneOffset: vectorfield.coneOffset,
		colormap: vectorfield.colormap
	};

	if (vectorfield.positions.length === 0) {
		if (bounds) {
			bounds[0] = [0,0,0];
			bounds[1] = [0,0,0];
		}
		return geo;
	}

	// Compute bounding box for the dataset.
	// Compute maximum velocity for the dataset to use for scaling the cones.
	var maxNorm = 0;
	var minX = 1/0, maxX = -1/0;
	var minY = 1/0, maxY = -1/0;
	var minZ = 1/0, maxZ = -1/0;
	var p2 = null;
	var u2 = null;
	var positionVectors = [];
	var vectorScale = 1/0;
	for (var i = 0; i < positions.length; i++) {
		var p = positions[i];
		minX = Math.min(p[0], minX);
		maxX = Math.max(p[0], maxX);
		minY = Math.min(p[1], minY);
		maxY = Math.max(p[1], maxY);
		minZ = Math.min(p[2], minZ);
		maxZ = Math.max(p[2], maxZ);
		var u;
		if (meshgrid) {
			u = sampleMeshgrid(p, vectors, meshgrid, true);
		} else {
			u = vectors[i];
		}
		if (V.length(u) > maxNorm) {
			maxNorm = V.length(u);
		}
		if (i) {
			// Find vector scale [w/ units of time] using "successive" positions
			// (not "adjacent" with would be O(n^2)),
			//
			// The vector scale corresponds to the minimum "time" to travel across two
			// two adjacent positions at the average velocity of those two adjacent positions
			vectorScale = Math.min(vectorScale,
				2 * V.distance(p2, p) / (V.length(u2) + V.length(u))
			);
		}
		p2 = p;
		u2 = u;
		positionVectors.push(u);
	}
	var minV = [minX, minY, minZ];
	var maxV = [maxX, maxY, maxZ];
	if (bounds) {
		bounds[0] = minV;
		bounds[1] = maxV;
	}
	if (maxNorm === 0) {
		maxNorm = 1;
	}

	// Inverted max norm would map vector with norm maxNorm to 1 coord space units in length
	var invertedMaxNorm = 1 / maxNorm;

	if (!isFinite(vectorScale) || isNaN(vectorScale)) {
		vectorScale = 1.0;
	}
	geo.vectorScale = vectorScale;

	var nml = vec3(0,1,0);

	var coneScale = vectorfield.coneSize || 0.5;

	if (vectorfield.absoluteConeSize) {
		coneScale = vectorfield.absoluteConeSize * invertedMaxNorm;
	}

	geo.coneScale = coneScale;

	// Build the cone model.
	for (var i = 0, j = 0; i < positions.length; i++) {
		var p = positions[i];
		var x = p[0], y = p[1], z = p[2];
		var d = positionVectors[i];
		var intensity = V.length(d) * invertedMaxNorm;
		for (var k = 0, l = 8; k < l; k++) {
			geo.positions.push([x, y, z, j++]);
			geo.positions.push([x, y, z, j++]);
			geo.positions.push([x, y, z, j++]);
			geo.positions.push([x, y, z, j++]);
			geo.positions.push([x, y, z, j++]);
			geo.positions.push([x, y, z, j++]);

			geo.vectors.push(d);
			geo.vectors.push(d);
			geo.vectors.push(d);
			geo.vectors.push(d);
			geo.vectors.push(d);
			geo.vectors.push(d);

			geo.vertexIntensity.push(intensity, intensity, intensity);
			geo.vertexIntensity.push(intensity, intensity, intensity);

			geo.vertexNormals.push(nml, nml, nml);
			geo.vertexNormals.push(nml, nml, nml);

			var m = geo.positions.length;
			geo.cells.push([m-6, m-5, m-4], [m-3, m-2, m-1]);
		}
	}

	return geo;
};

module.exports.createConeMesh = require('./lib/conemesh');
