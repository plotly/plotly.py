# polybooljs

Boolean operations on polygons (union, intersection, difference, xor).

# Features

1. Clips polygons for all boolean operations
2. Removes unnecessary vertices
3. Handles segments that are coincident (overlap perfectly, share vertices, one inside the other,
   etc)
4. Uses formulas that take floating point irregularities into account (via configurable epsilon)
5. Provides an API for constructing efficient sequences of operations
6. Support for GeoJSON `"Polygon"` and `"MultiPolygon"` types (experimental)

# Resources

* [Demo + Animation](https://rawgit.com/voidqk/polybooljs/master/dist/demo.html)
* [Companion Tutorial](http://syntheti.cc/article/polygon-clipping-pt2/)
* Based somewhat on the F. Martinez (2008) algorithm:
  [Paper](http://www.cs.ucr.edu/~vbz/cs230papers/martinez_boolean.pdf),
  [Code](https://github.com/akavel/martinez-src)

# Installing

`npm install polybooljs`

Or, for the browser, look in the [`dist/`](https://github.com/voidqk/polybooljs/tree/master/dist)
directory for a single file build.  When included on a page, it will expose the global `PolyBool`.

# Example

```javascript
var PolyBool = require('polybooljs');
PolyBool.intersect({
    regions: [
      [[50,50], [150,150], [190,50]],
      [[130,50], [290,150], [290,50]]
    ],
    inverted: false
  }, {
    regions: [
      [[110,20], [110,110], [20,20]],
      [[130,170], [130,20], [260,20], [260,170]]
    ],
    inverted: false
  });
===> {
  regions: [
    [[50,50], [110,50], [110,110]],
    [[178,80], [130,50], [130,130], [150,150]],
    [[178,80], [190,50], [260,50], [260,131.25]]
  ],
  inverted: false
}
```

![PolyBool Example](https://github.com/voidqk/polybooljs/raw/master/example.png)

## Basic Usage

```javascript
var poly = PolyBool.union        (poly1, poly2);
var poly = PolyBool.intersect    (poly1, poly2);
var poly = PolyBool.difference   (poly1, poly2); // poly1 - poly2
var poly = PolyBool.differenceRev(poly1, poly2); // poly2 - poly1
var poly = PolyBool.xor          (poly1, poly2);
```

Where `poly1`, `poly2`, and the return value are Polygon objects, in the format of:

```javascript
// polygon format
{
  regions: [ // list of regions
    // each region is a list of points
    [[50,50], [150,150], [190,50]],
    [[130,50], [290,150], [290,50]]
  ],
  inverted: false // is this polygon inverted?
}
```

# GeoJSON (experimental)

There are also functions for converting between the native polygon format and
[GeoJSON](https://tools.ietf.org/html/rfc7946).

Note: These functions are currently **experimental**, and I'm hoping users can provide feedback.
Please comment in [this issue on GitHub](https://github.com/voidqk/polybooljs/issues/7) -- including
letting me know if it's working as expected.  I don't use GeoJSON, but I thought I would take a
crack at conversion functions.

Use the following functions:

```javascript
var geojson = PolyBool.polygonToGeoJSON(poly);
var poly    = PolyBool.polygonFromGeoJSON(geojson);
```

Only `"Polygon"` and `"MultiPolygon"` types are supported.

# Core API

```javascript
var segments = PolyBool.segments(polygon);
var combined = PolyBool.combine(segments1, segments2);
var segments = PolyBool.selectUnion(combined);
var segments = PolyBool.selectIntersect(combined);
var segments = PolyBool.selectDifference(combined);
var segments = PolyBool.selectDifferenceRev(combined);
var segments = PolyBool.selectXor(combined);
var polygon  = PolyBool.polygon(segments);
```

Depending on your needs, it might be more efficient to construct your own sequence of operations
using the lower-level API.  Note that `PolyBool.union`, `PolyBool.intersect`, etc, are just thin
wrappers for convenience.

There are three types of objects you will encounter in the core API:

1. Polygons (discussed above, this is a list of regions and an `inverted` flag)
2. Segments
3. Combined Segments

The basic flow chart of the API is:

![PolyBool API Flow Chart](https://github.com/voidqk/polybooljs/raw/master/flowchart.png)

You start by converting Polygons to Segments using `PolyBool.segments(poly)`.

You convert Segments to Combined Segments using `PolyBool.combine(seg1, seg2)`.

You select the resulting Segments from the Combined Segments using one of the selection operators
`PolyBool.selectUnion(combined)`, `PolyBool.selectIntersect(combined)`, etc.  These selection
functions return Segments.

Once you're done, you convert the Segments back to Polygons using `PolyBool.polygon(segments)`.

Each transition is costly, so you want to navigate wisely.  The selection transition is the least
costly.

## Advanced Example 1

Suppose you wanted to union a list of polygons together.  The naive way to do it would be:

```javascript
// works but not efficient
var result = polygons[0];
for (var i = 1; i < polygons.length; i++)
  result = PolyBool.union(result, polygons[i]);
return result;
```

Instead, it's more efficient to use the core API directly, like this:

```javascript
// works AND efficient
var segments = PolyBool.segments(polygons[0]);
for (var i = 1; i < polygons.length; i++){
  var seg2 = PolyBool.segments(polygons[i]);
  var comb = PolyBool.combine(segments, seg2);
  segments = PolyBool.selectUnion(comb);
}
return PolyBool.polygon(segments);
```

## Advanced Example 2

Suppose you want to calculate all operations on two polygons.  The naive way to do it would be:

```javascript
// works but not efficient
return {
  union        : PolyBool.union        (poly1, poly2),
  intersect    : PolyBool.intersect    (poly1, poly2),
  difference   : PolyBool.difference   (poly1, poly2),
  differenceRev: PolyBool.differenceRev(poly1, poly2),
  xor          : PolyBool.xor          (poly1, poly2)
};
```

Instead, it's more efficient to use the core API directly, like this:

```javascript
// works AND efficient
var seg1 = PolyBool.segments(poly1);
var seg2 = PolyBool.segments(poly2);
var comb = PolyBool.combine(seg1, seg2);
return {
  union        : PolyBool.polygon(PolyBool.selectUnion        (comb)),
  intersect    : PolyBool.polygon(PolyBool.selectIntersect    (comb)),
  difference   : PolyBool.polygon(PolyBool.selectDifference   (comb)),
  differenceRev: PolyBool.polygon(PolyBool.selectDifferenceRev(comb)),
  xor          : PolyBool.polygon(PolyBool.selectXor          (comb))
};
```

## Advanced Example 3

As an added bonus, just going from Polygon to Segments and back performs simplification on the
polygon.

Suppose you have garbage polygon data and just want to clean it up.  The naive way to do it would
be:

```javascript
// union the polygon with nothing in order to clean up the data
// works but not efficient
var cleaned = PolyBool.union(polygon, { regions: [], inverted: false });
```

Instead, skip the combination and selection phase:

```javascript
// works AND efficient
var cleaned = PolyBool.polygon(PolyBool.segments(polygon));
```

# Epsilon

Due to the beauty of floating point reality, floating point calculations are not exactly perfect.
This is a problem when trying to detect whether lines are on top of each other, or if vertices are
exactly the same.

Normally you would expect this to work:

```javascript
if (A === B)
  /* A and B are equal */;
else
  /* A and B are not equal */;
```

But for inexact floating point math, instead we use:

```javascript
if (Math.abs(A - B) < epsilon)
  /* A and B are equal */;
else
  /* A and B are not equal */;
```

You can set the epsilon value using:

`PolyBool.epsilon(newEpsilonValue);`

Or, if you just want to get the current value:

`var currentEpsilon = PolyBool.epsilon();`

The default epsilon value is `0.0000000001`.

If your polygons are really really large or really really tiny, then you will probably have to come
up with your own epsilon value -- otherwise, the default should be fine.

If `PolyBool` detects that your epsilon is too small or too large, it will throw an error:

```
PolyBool: Zero-length segment detected; your epsilon is probably too small or too large
```

# Build Log

The library also has an option for tracking execution of the internal algorithms.  This is useful
for debugging or creating the animation on the demo page.

By default, the logging is disabled.  But you can enable or reset it via:

`var buildLog = PolyBool.buildLog(true);`

The return value is an empty list that will have log entries added to it as more API calls are made.

You can inspect the log by looking in the values:

```javascript
buildLog.forEach(function(logEntry){
  console.log(logEntry.type, logEntry.data);
});
```

Don't rely on the build log functionality to be consistent across releases.

You can disable the build log via:

`PolyBool.buildLog(false);`

You can get the current list (or `false` if disabled) via:

`var currentLog = PolyBool.buildLog();`
