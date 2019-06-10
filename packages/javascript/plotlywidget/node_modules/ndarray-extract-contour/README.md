ndarray-extract-contour
=======================
General purpose contour extraction routine generator.  This library has a really horrible interface, but it is pretty flexible.  It is mostly useful as an internal component, and should not be used generally unless you know what you are doing.

As an example of a nicer interface built using this module, take a look at [surface-nets](https://github.com/mikolalysenko/surface-nets).

# Example/documentation

```javascript
var generateContour = require("ndarray-extract-contour")

var getContour = generateContour({
  order: [1,0],         //Order of array iteration
  arrayArguments: 2,    //Take two arrays as input
  scalarArguments: 1,   //Take one extra scalar argument

  //Function to determine phase of a grid cell
  phase: function(a, b, s) { 

    //a = first array argument
    //b = second array argument
    //s = scalar argument

    return a
  },

  //Callback for adding vertex to array
  vertex: function(x,y, a00,a01,a10,a11,  b00,b01,b10,b11,  p00,p01,p10,p11, s) {

    //Geometry:
    //
    //   a11 ---- a10
    //    |        |
    //    |        |
    //    |        |
    //   a01 ---- a00
    //

    //Arguments:

    // x,y,...  = coordinates of vertex in grid index
    // a00,a01,...  = components of first array
    // b00,b01,...  = components of second array
    // p00,p01,...  = phase of all nearby cells
    // s,... = optional scalar arguments
    //
  },

  //Callback for adding cell
  cell: function(v0,v1,  a0,a1,  b0,b1,  p0,p1,  s) {

    // Geometry:
    //
    //       v0
    //       |
    //  p0   |    p1
    //       |
    //       v1


    //Arguments:
    //  v0,v1,...  = coordinates of vertices of cuboid cell
    //  a0,a1  = first array values on front/back cell
    //  b0,b1  = second array values on front/back cell
    //  p0,p1  = phase values for front/back cell
    //  s,... = optional scalar arguments
  }
})


//How to use it:
testContour(A, B, S)
```

# Install

```
npm install ndarray-extract-contour
```

# Credits
(c) 2014 Mikola Lysenko. MIT License