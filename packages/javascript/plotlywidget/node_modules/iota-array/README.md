# iota-array
Fills an array with sequential integers.  Just like [C++'s `std::iota()`](http://www.sgi.com/tech/stl/iota.html) or the similarly named function in [APL](http://en.wikipedia.org/wiki/Iota).

## Install

    npm install iota-array
    
## Example

```javascript

console.log(require("iota-array")(3))

//Prints:
//
//    [0,1,2]
//

```

## `require("iota-array")(n)`
Constructs an array of length `n` of `n` sequential integers starting from 0.

* `n` the length of the array to construct

**Returns:** An array of n sequential integers starting at 0

# Credits
(c) 2013 Mikola Lysenko. MIT License
