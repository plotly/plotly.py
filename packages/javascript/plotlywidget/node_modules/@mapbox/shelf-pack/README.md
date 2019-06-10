[![npm version](https://badge.fury.io/js/%40mapbox%2Fshelf-pack.svg)](https://badge.fury.io/js/%40mapbox%2Fshelf-pack)
[![Build Status](https://secure.travis-ci.org/mapbox/shelf-pack.svg)](http://travis-ci.org/mapbox/shelf-pack)
[![Coverage Status](https://coveralls.io/repos/github/mapbox/shelf-pack/badge.svg?branch=master)](https://coveralls.io/github/mapbox/shelf-pack?branch=master)

## shelf-pack

A 2D rectangular [bin packing](https://en.wikipedia.org/wiki/Bin_packing_problem)
data structure that uses the Shelf Best Height Fit heuristic.


### What is it?

`shelf-pack` is a library for packing little rectangles into a big rectangle.  This sounds simple enough,
but finding an optimal packing is a problem with [NP-Complete](https://en.wikipedia.org/wiki/NP-completeness)
complexity.  One useful application of bin packing is to assemble icons or glyphs into a sprite texture.

There are many ways to approach the bin packing problem, but `shelf-pack` uses the Shelf Best
Height Fit heuristic.  It works by dividing the total space into "shelves", each with a certain height.
The allocator packs rectangles onto whichever shelf minimizes the amount of wasted vertical space.

`shelf-pack` is simple, fast, and works best when the rectangles have similar heights (icons and glyphs
are like this).  It is not a generalized bin packer, and can potentially waste a lot of space if the
rectangles vary significantly in height.


### How fast is it?

Really fast!  `shelf-pack` is several orders of magnitude faster than the more general
[`bin-pack`](https://www.npmjs.com/package/bin-pack) library.

```bash
> npm run bench

ShelfPack single allocate fixed size bins x 1,610 ops/sec ±1.21% (90 runs sampled)
ShelfPack single allocate random width bins x 1,475 ops/sec ±1.00% (89 runs sampled)
ShelfPack single allocate random height bins x 1,458 ops/sec ±1.00% (90 runs sampled)
ShelfPack single allocate random height and width bins x 1,346 ops/sec ±0.96% (89 runs sampled)
ShelfPack batch allocate fixed size bins x 1,522 ops/sec ±1.06% (86 runs sampled)
ShelfPack batch allocate random width bins x 1,427 ops/sec ±1.06% (89 runs sampled)
ShelfPack batch allocate random height bins x 1,350 ops/sec ±1.63% (90 runs sampled)
ShelfPack batch allocate random height and width bins x 1,257 ops/sec ±1.02% (89 runs sampled)
BinPack batch allocate fixed size bins x 2.21 ops/sec ±6.60% (10 runs sampled)
BinPack batch allocate random width bins x 0.50 ops/sec ±2.25% (6 runs sampled)
BinPack batch allocate random height bins x 0.51 ops/sec ±1.97% (6 runs sampled)
BinPack batch allocate random height and width bins x 0.51 ops/sec ±1.37% (6 runs sampled)
```


### Usage

#### Basic Usage

```js
var ShelfPack = require('@mapbox/shelf-pack');

// Initialize the sprite with a width and height..
var sprite = new ShelfPack(64, 64);

// Pack bins one at a time..
for (var i = 0; i < 5; i++) {
    // packOne() accepts parameters: `width`, `height`, `id`
    // and returns a single allocated Bin object..
    // `id` is optional - if you skip it, shelf-pack will make up a number for you..
    // (Protip: numeric ids are much faster than string ids)

    var bin = sprite.packOne(32, 32);
    console.log(bin || 'out of space');
}

/* output:
Bin { id: 1, x: 0, y: 0, w: 32, h: 32, maxw: 32, maxh: 32, refcount: 1 }
Bin { id: 2, x: 32, y: 0, w: 32, h: 32, maxw: 32, maxh: 32, refcount: 1 }
Bin { id: 3, x: 0, y: 32, w: 32, h: 32, maxw: 32, maxh: 32, refcount: 1 }
Bin { id: 4, x: 32, y: 32, w: 32, h: 32, maxw: 32, maxh: 32, refcount: 1 }
out of space
*/

// Clear sprite and start over..
sprite.clear();

// Or, resize sprite by passing larger dimensions..
sprite.resize(128, 128);   // width, height

```


#### Batch packing

```js
var ShelfPack = require('@mapbox/shelf-pack');

// If you don't want to think about the size of the sprite,
// the `autoResize` option will allow it to grow as needed..
var sprite = new ShelfPack(10, 10, { autoResize: true });

// Bins can be allocated in batches..
// Each requested bin should have `w`, `h` (or `width`, `height`) properties..
var requests = [
    { id: 'a', width: 10, height: 10 },
    { id: 'b', width: 10, height: 12 },
    { id: 'c', w: 10, h: 12 },
    { id: 'd', w: 10, h: 10 }
];

// pack() returns an Array of packed Bin objects..
var results = sprite.pack(requests);

results.forEach(function(bin) {
    console.log(bin);
});

/* output:
Bin { id: 'a', x: 0, y: 0, w: 10, h: 10, maxw: 10, maxh: 10, refcount: 1 }
Bin { id: 'b', x: 0, y: 10, w: 10, h: 12, maxw: 10, maxh: 12, refcount: 1 }
Bin { id: 'c', x: 10, y: 10, w: 10, h: 12, maxw: 10, maxh: 12, refcount: 1 }
Bin { id: 'd', x: 10, y: 0, w: 10, h: 10, maxw: 10, maxh: 10, refcount: 1 }
*/

// If you don't mind letting ShelfPack modify your objects,
// the `inPlace` option will decorate your bin objects with `x` and `y` properties.
// Fancy!
var myBins = [
    { id: 'e', width: 12, height: 24 },
    { id: 'f', width: 12, height: 12 },
    { id: 'g', w: 10, h: 10 }
];

sprite.pack(myBins, { inPlace: true });
myBins.forEach(function(bin) {
    console.log(bin);
});

/* output:
{ id: 'e', width: 12, height: 24, x: 0, y: 22 }
{ id: 'f', width: 12, height: 12, x: 20, y: 10 }
{ id: 'g', w: 10, h: 10, x: 20, y: 0 }
*/

```

#### Reference Counting

```js
var ShelfPack = require('@mapbox/shelf-pack');

// Initialize the sprite with a width and height..
var sprite = new ShelfPack(64, 64);

// Allocated bins are automatically reference counted.
// They start out having a refcount of 1.
[100, 101, 102].forEach(function(id) {
    var bin = sprite.packOne(16, 16, id);
    console.log(bin);
});

/* output:
Bin { id: 100, x: 0, y: 0, w: 16, h: 16, maxw: 16, maxh: 16, refcount: 1 }
Bin { id: 101, x: 16, y: 0, w: 16, h: 16, maxw: 16, maxh: 16, refcount: 1 }
Bin { id: 102, x: 32, y: 0, w: 16, h: 16, maxw: 16, maxh: 16, refcount: 1 }
*/

// If you try to pack the same id again, shelf-pack will not re-pack it.
// Instead, it will increment the reference count automatically..
var bin102 = sprite.packOne(16, 16, 102);
console.log(bin102);

/* output:
Bin { id: 102, x: 32, y: 0, w: 16, h: 16, maxw: 16, maxh: 16, refcount: 2 }
*/

// You can also manually increment the reference count..
var bin101 = sprite.getBin(101);
sprite.ref(bin101);
console.log(bin101);

/* output:
Bin { id: 101, x: 16, y: 0, w: 16, h: 16, maxw: 16, maxh: 16, refcount: 2 }
*/

// ...and decrement it!
var bin100 = sprite.getBin(100);
sprite.unref(bin100);
console.log(bin100);

/* output:
Bin { id: 100, x: 0, y: 0, w: 16, h: 16, maxw: 16, maxh: 16, refcount: 0 }
*/

// Bins with a refcount of 0 are considered free space.
// Next time a bin is packed, shelf-back tries to reuse free space first.
// See how Bin 103 gets allocated at [0,0] - Bin 100's old spot!
var bin103 = sprite.packOne(16, 15, 103);
console.log(bin103);

/* output:
Bin { id: 103, x: 0, y: 0, w: 16, h: 15, maxw: 16, maxh: 16, refcount: 1 }
*/

// Bin 103 may be smaller (16x15) but it knows 16x16 was its original size.
// If that space becomes free again, a 16x16 bin will still fit there.
sprite.unref(bin103)
var bin104 = sprite.packOne(16, 16, 104);
console.log(bin104);

/* output:
Bin { id: 104, x: 0, y: 0, w: 16, h: 16, maxw: 16, maxh: 16, refcount: 1 }
*/

```


### Documentation

Complete API documentation is here:  http://mapbox.github.io/shelf-pack/


### See also

J. Jylänky, "A Thousand Ways to Pack the Bin - A Practical
Approach to Two-Dimensional Rectangle Bin Packing,"
http://clb.demon.fi/files/RectangleBinPack.pdf, 2010
