barycentric
===========
Computes the location of a point in a simplex in [barycentric coordinates](http://en.wikipedia.org/wiki/Barycentric_coordinate_system#Generalized_barycentric_coordinates) (aka [areal coordinates](http://mathworld.wolfram.com/BarycentricCoordinates.html)).

Usage
=====
Install using npm:

    npm install barycentric
    
And then use as follows:

```javascript
var barycentric = require("barycentric")

console.log(barycentric([[0,0], [0,1], [1,0]], [0.5, 0.5]))
//Prints:
//
//  [0, 0.5, 0.5]
//
```

Credits
=======
(c) 2013 Mikola Lysenko. MIT License