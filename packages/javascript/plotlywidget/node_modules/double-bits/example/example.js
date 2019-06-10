var db = require("../double")

//Get higher order word
console.log(db.hi(1.0).toString(16))    //Prints out: 3ff00000

//Get lower order word
console.log(db.lo(1.0).toString(16))    //Prints out: 0

//Combine two words into a double
console.log(db.pack(0, 0x3ff00000))     //Prints out: 1.0

//More sophisticated example:  Print out base 2 representation
var pad = require("pad")
function base2Str(n) {
  var f = db.fraction(n)
  return (db.sign(n) ? "-" : "") +
    "2^" + (db.exponent(n)+1) +
    " * 0." + pad(f[1].toString(2), 21, "0") + 
              pad(f[0].toString(2), 32, "0")
}

console.log(base2Str(1.0))