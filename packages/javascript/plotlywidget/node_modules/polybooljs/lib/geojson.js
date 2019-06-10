// (c) Copyright 2017, Sean Connelly (@voidqk), http://syntheti.cc
// MIT License
// Project Home: https://github.com/voidqk/polybooljs

//
// convert between PolyBool polygon format and GeoJSON formats (Polygon and MultiPolygon)
//

var GeoJSON = {
	// convert a GeoJSON object to a PolyBool polygon
	toPolygon: function(PolyBool, geojson){

		// converts list of LineString's to segments
		function GeoPoly(coords){
			// check for empty coords
			if (coords.length <= 0)
				return PolyBool.segments({ inverted: false, regions: [] });

			// convert LineString to segments
			function LineString(ls){
				// remove tail which should be the same as head
				var reg = ls.slice(0, ls.length - 1);
				return PolyBool.segments({ inverted: false, regions: [reg] });
			}

			// the first LineString is considered the outside
			var out = LineString(coords[0]);

			// the rest of the LineStrings are considered interior holes, so subtract them from the
			// current result
			for (var i = 1; i < coords.length; i++)
				out = PolyBool.selectDifference(PolyBool.combine(out, LineString(coords[i])));

			return out;
		}

		if (geojson.type === 'Polygon'){
			// single polygon, so just convert it and we're done
			return PolyBool.polygon(GeoPoly(geojson.coordinates));
		}
		else if (geojson.type === 'MultiPolygon'){
			// multiple polygons, so union all the polygons together
			var out = PolyBool.segments({ inverted: false, regions: [] });
			for (var i = 0; i < geojson.coordinates.length; i++)
				out = PolyBool.selectUnion(PolyBool.combine(out, GeoPoly(geojson.coordinates[i])));
			return PolyBool.polygon(out);
		}
		throw new Error('PolyBool: Cannot convert GeoJSON object to PolyBool polygon');
	},

	// convert a PolyBool polygon to a GeoJSON object
	fromPolygon: function(PolyBool, eps, poly){
		// make sure out polygon is clean
		poly = PolyBool.polygon(PolyBool.segments(poly));

		// test if r1 is inside r2
		function regionInsideRegion(r1, r2){
			// we're guaranteed no lines intersect (because the polygon is clean), but a vertex
			// could be on the edge -- so we just average pt[0] and pt[1] to produce a point on the
			// edge of the first line, which cannot be on an edge
			return eps.pointInsideRegion([
				(r1[0][0] + r1[1][0]) * 0.5,
				(r1[0][1] + r1[1][1]) * 0.5
			], r2);
		}

		// calculate inside heirarchy
		//
		//  _____________________   _______    roots -> A       -> F
		// |          A          | |   F   |            |          |
		// |  _______   _______  | |  ___  |            +-- B      +-- G
		// | |   B   | |   C   | | | |   | |            |   |
		// | |  ___  | |  ___  | | | |   | |            |   +-- D
		// | | | D | | | | E | | | | | G | |            |
		// | | |___| | | |___| | | | |   | |            +-- C
		// | |_______| |_______| | | |___| |                |
		// |_____________________| |_______|                +-- E

		function newNode(region){
			return {
				region: region,
				children: []
			};
		}

		var roots = newNode(null);

		function addChild(root, region){
			// first check if we're inside any children
			for (var i = 0; i < root.children.length; i++){
				var child = root.children[i];
				if (regionInsideRegion(region, child.region)){
					// we are, so insert inside them instead
					addChild(child, region);
					return;
				}
			}

			// not inside any children, so check to see if any children are inside us
			var node = newNode(region);
			for (var i = 0; i < root.children.length; i++){
				var child = root.children[i];
				if (regionInsideRegion(child.region, region)){
					// oops... move the child beneath us, and remove them from root
					node.children.push(child);
					root.children.splice(i, 1);
					i--;
				}
			}

			// now we can add ourselves
			root.children.push(node);
		}

		// add all regions to the root
		for (var i = 0; i < poly.regions.length; i++){
			var region = poly.regions[i];
			if (region.length < 3) // regions must have at least 3 points (sanity check)
				continue;
			addChild(roots, region);
		}

		// with our heirarchy, we can distinguish between exterior borders, and interior holes
		// the root nodes are exterior, children are interior, children's children are exterior,
		// children's children's children are interior, etc

		// while we're at it, exteriors are counter-clockwise, and interiors are clockwise

		function forceWinding(region, clockwise){
			// first, see if we're clockwise or counter-clockwise
			// https://en.wikipedia.org/wiki/Shoelace_formula
			var winding = 0;
			var last_x = region[region.length - 1][0];
			var last_y = region[region.length - 1][1];
			var copy = [];
			for (var i = 0; i < region.length; i++){
				var curr_x = region[i][0];
				var curr_y = region[i][1];
				copy.push([curr_x, curr_y]); // create a copy while we're at it
				winding += curr_y * last_x - curr_x * last_y;
				last_x = curr_x;
				last_y = curr_y;
			}
			// this assumes Cartesian coordinates (Y is positive going up)
			var isclockwise = winding < 0;
			if (isclockwise !== clockwise)
				copy.reverse();
			// while we're here, the last point must be the first point...
			copy.push([copy[0][0], copy[0][1]]);
			return copy;
		}

		var geopolys = [];

		function addExterior(node){
			var poly = [forceWinding(node.region, false)];
			geopolys.push(poly);
			// children of exteriors are interior
			for (var i = 0; i < node.children.length; i++)
				poly.push(getInterior(node.children[i]));
		}

		function getInterior(node){
			// children of interiors are exterior
			for (var i = 0; i < node.children.length; i++)
				addExterior(node.children[i]);
			// return the clockwise interior
			return forceWinding(node.region, true);
		}

		// root nodes are exterior
		for (var i = 0; i < roots.children.length; i++)
			addExterior(roots.children[i]);

		// lastly, construct the approrpriate GeoJSON object

		if (geopolys.length <= 0) // empty GeoJSON Polygon
			return { type: 'Polygon', coordinates: [] };
		if (geopolys.length == 1) // use a GeoJSON Polygon
			return { type: 'Polygon', coordinates: geopolys[0] };
		return { // otherwise, use a GeoJSON MultiPolygon
			type: 'MultiPolygon',
			coordinates: geopolys
		};
	}
};

module.exports = GeoJSON;
