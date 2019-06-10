"use strict"

var tape = require("tape")
var db = require("../double.js")

tape("double-bits", function(t) {

  t.equals(db.lo(1.0), 0)
  t.equals(db.hi(1.0), 0x3ff00000)
  t.equals(db.pack(0, 0x3ff00000), 1.0)
  t.same(db(1.0), [0, 0x3ff00000])
  t.same(db.fraction(1.0), [0, 1<<20])
  t.equals(db.exponent(1), 0)
  t.equals(db.sign(1), 0)
  t.equals(db.sign(-1), 1)
  t.equals(db.exponent(0.5), -1)

  t.ok(db.denormalized(Math.pow(2, -1024)))
  t.ok(!db.denormalized(1))
  t.ok(db.denormalized(Math.pow(2, -1023)))
  t.ok(!db.denormalized(Math.pow(2, -1022)))

  t.end()
})