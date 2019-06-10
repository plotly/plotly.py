var rat = require('../index')

//Construct a pair of rational numbers;
//   a = 1/10
//   b = 2/10
var a = rat(1, 10)
var b = rat(2, 10)

//Compute their sum
var add = require('../add')
var c = add(a, b)

//Print out sum
var toString = require('../to-string')
console.log('a+b=', toString(c))

//And also convert to a number
var toFloat = require('../to-float')
console.log('exact rational result:', toFloat(c))

//For comparison, here is the same computation performed with floats
var x = 0.1
var y = 0.2
console.log('approximate float result:', x + y)
