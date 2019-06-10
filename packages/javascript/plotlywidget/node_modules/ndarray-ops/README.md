ndarray-ops
===========
A collection of common mathematical operations for [ndarrays](http://github.com/mikolalysenko/ndarray).  Implemented using [cwise](http://github.com/mikolalysenko/cwise)

Usage
=====
First, install the library using npm:

    npm install ndarray-ops
    
Then you can import the library by doing:

    var ops = require("ndarray-ops")

Then you can use the functions as in the following example:

```javascript
//First, import libraries
var ndarray = require("ndarray")
  , ops = require("ndarray-ops")


//Next, create some arrays
var a = ndarray(new Float32Array(128*128))
  , b = ndarray(new Float32Array(128*128))
  , c = ndarray(new Float32Array(128*128))

//Initialize b with some random numbers:
ops.random(b)

//Set c to a constant 1
ops.assigns(c, 1.0)

//Add b and c, store result in a:
ops.add(a, b, c)

//Multiply a by 0.5 in place
ops.mulseq(a, 0.5)

//Print some statistics about a:
console.log(
  "inf(a) = ", ops.inf(a),
  "sup(a) = ", ops.sup(a),
  "argmin(a) = ", ops.argmin(a),
  "argmax(a) = ", ops.argmax(a),
  "norm1(a) = ", ops.norm1(a))
```

Conventions
===========
This library implements component-wise operations for all of the operators and Math.* functions in JS, along with a few commonly used aggregate operations.  Most of the functions in the library work by applying some symmetric binary operator to a pair of arrays. You call them like this:

```javascript
ops.add(dest, arg1, arg2)
```

Which translates into code that works (approximately) like this:

```javascript
for(var i=0; i<dest.shape[0]; ++i) {
  dest[i] = arg1[i] + arg2[i]
}
```

It is up to you to specify where the result gets store.  This library does not create new arrays for you to avoid performing expensive intermediate allocations.  There are also a few other variations:

```javascript
ops.addeq(dest, arg1)
```
Operators with the -eq suffix perform an assignment.

```javascript
for(var i=0; i<dest.shape[0]; ++i) {
  dest[i] += arg1[i]
}
```

```javascript
ops.adds(dest, arg1, 1.0)
```
The -s suffix denotes scalar/broadcast operations; so the above would translate to:

```javascript
for(var i=0; i<dest.shape[0]; ++i) {
  dest[i] = arg1[i] + 1.0
}
```

```javascript
ops.addseq(dest, 1.0)
```
The -seq suffix is basically the combination of the above, and translates to:

```javascript
for(var i=0; i<dest.shape[0]; ++i) {
  dest[i] += 1.0
}
```

The following operators follow this rule:

* add[,s,eq,seq] - Addition, `+`
* sub[,s,eq,seq] - Subtraction, `-`
* mul[,s,eq,seq] - Multiplication, `*`
* div[,s,eq,seq] - Division, `/`
* mod[,s,eq,seq] - Modulo, `%`
* band[,s,eq,seq] - Bitwise And, `&`
* bor[,s,eq,seq] - Bitwise Or, `&`
* bxor[,s,eq,seq] - Bitwise Xor, `^`
* lshift[,s,eq,seq] - Left shift, `<<`
* rshift[,s,eq,seq] - Signed right shift, `>>`
* rrshift[,s,eq,seq] - Unsigned right shift, `>>>`
* lt[,s,eq,seq] - Less than, `<`
* gt[,s,eq,seq] - Greater than, `>`
* leq[,s,eq,seq] - Less than or equal, `<=`
* geq[,s,eq,seq] - Greater than or equal `>=`
* eq[,s,eq,seq] - Equals, `===`
* neq[,s,eq,seq] - Not equals, `!==`
* and[,s,eq,seq] - Boolean And, `&&`
* or[,s,eq,seq] - Boolean Or, `||`
* max[,s,eq,seq] - Maximum, `Math.max`
* min[,s,eq,seq] - Minimum, `Math.min`


Special Cases
-------------
There are a few corner cases that follow slightly different rules.  These can be grouped using the following general categories:

### Assignment

There are two assignment operators:

* assign
* assigns

`op.assign(dest, src)` copies one array into another, while `op.assigns(dest, val)` broadcasts a scalar to all elements of an array.

### Nullary operators
Nullary operators only take on argument for the array they are assigning to, and don't have any variations.  Currently there is only one of these:

* random - Sets each element of an array to a random scalar between 0 and 1, `Math.random()`

### Unary operators
Unary operators have one of two forms, they can be written as either:

```javascript
op.abs(dest, arg)
```

Or:

```javascript
op.abseq(dest)
```

The former version sets dest = |arg|, while in the latter the operation is applied in place.  ndarray-ops exposes the following unary operators:

* not[,eq] - Boolean not, `!`
* bnot[,eq] - Bitwise not, `~`
* neg[,eq] - Negative, `-`
* recip[,eq] - Reciprocal, `1.0/`
* abs[,eq] - Absolute value, `Math.abs`
* acos[,eq] - Inverse cosine, `Math.acos`
* asin[,eq] - Inverse sine, `Math.asin`
* atan[,eq] - Inverse tangent, `Math.atan`
* ceil[,eq] - Ceiling, `Math.ceil`
* cos[,eq] - Cosine, `Math.cos`
* exp[,eq] - Exponent, `Math.exp`
* floor[,eq] - Floor, `Math.floor`
* log[,eq] - Logarithm, `Math.log`
* round[,eq] - Round, `Math.round`
* sin[,eq] - Sine, `Math.sin`
* sqrt[,eq] - Square root, `Math.sqrt`
* tan[,eq] - Tangent, `Math.tan`

### Non-symmetric binary operators
There are also a few non-symmetric binary operators.  These operators have an extra suffix `op` which flips the order of the arguments.  There are only two of these:

* atan2[,s,eq,seq,op,sop,opeq,sopeq]
* pow[,s,eq,seq,op,sop,opeq,sopeq]

### Map-reduce (aggregate) operators
Finally, there are aggregate operators that take an array as input and compute some aggregate result or summary.  These functions don't have any special suffixes and all of them take a single array as input.

* equals - Check if two ndarrays are equal
* any - Check if any element of the array is truthy
* all - Checks if any element of the array is falsy
* sum - Sums all elements of the array
* prod - Multiplies all elements of the array
* norm2squared - Computes the squared L2 norm
* norm2 - Computes the L2 norm
* norminf - Computes the L-infinity norm
* norm1 - Computs the L1 norm
* sup - Max element in array
* inf - Min element in array
* argmin - Index of min element
* argmax - Index of max element

Credits
=======
(c) 2013 Mikola Lysenko. MIT License
