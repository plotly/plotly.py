"use strict"

var nextafter = require("../nextafter")

var x = 0.1
console.log("The number", x, "is between", nextafter(x, -Infinity), "and", nextafter(x, Infinity))