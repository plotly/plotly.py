circumcenter
============
Computes the [circumcenter](http://en.wikipedia.org/wiki/Circumcenter) of a simplex.  That is, it is the center of an [n-sphere](http://en.wikipedia.org/wiki/N-sphere) passing through n+1 points.

[![testling badge](https://ci.testling.com/mikolalysenko/circumcenter.png)](https://ci.testling.com/mikolalysenko/circumcenter)

[![build status](https://secure.travis-ci.org/mikolalysenko/circumcenter.png)](http://travis-ci.org/mikolalysenko/circumcenter)

#Usage

First install using npm:

    npm install circumcenter
    
Then you can call it like so:

```javascript
var circumcenter = require("circumcenter")

console.log(circumcenter([[0,0], [0,1], [1,1]]))

//Prints:
//
//    [0.5, 0.5]
//
```

#### `require("circumcenter")(points)`
Computes the circumcenter of a collection of points

#### `require("circumcenter").barycentric(points)`
Computes the circumcenter in barycentric coordinates

Credits
=======
(c) 2013 Mikola Lysenko. MIT License
