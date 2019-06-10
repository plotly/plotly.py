var proxyquire = require('proxyquire');
var assert = require("assert");
var Module = require("module");

describe("Crypto API Test", function() {

var crypto_stub = {};
var original = Math.random;
var rng, r;

// Load seedrandom in absence of any crypto package.
it("should be able to seed without crypto", function() {
  var noncrypto_sr = proxyquire('../seedrandom', { crypto: null });
  rng = noncrypto_sr('hello.');
  assert.equal(typeof(rng), 'function', "Should return a function.");
  r = rng();
  assert.equal(r, 0.9282578795792454, "Should be 'hello.'#1");
  assert(original === Math.random, "Should not change Math.random.");
  assert(original !== rng, "PRNG should not be Math.random.");
  var noncrypto_sr = proxyquire('../seedrandom', { crypto: null });
  result = noncrypto_sr();
  assert.equal(typeof(result), 'function', "Should return function.");
  assert(original === Math.random, "Should not change Math.random.");
  r = result();
  assert(r != 0.9282578795792454, "Should not be 'hello.'#1");
  assert(r != 0.7316977468919549, "Should not be 'hello.'#3");
  assert(r != 0.23144008215179881, "Should not be '\\0'#1");
  assert(r != 0.7220382488550928, "Should not be '\\1'#1");
  // Recache original seedrandom.
  proxyquire('../seedrandom', {});
});

// Load seedrandom with zeroed-out crypto package.
it("should be able to seed ('hello.') with zero crypto", function() {
  var zerocrypto_sr = proxyquire('../seedrandom', {
    crypto: { randomBytes: function(n) {
      result = []; while (n-- > 0) { result.push(1); } return result; } }
  });
  rng = zerocrypto_sr('hello.');
  assert.equal(typeof(rng), 'function', "Should return a function.");
  r = rng();
  assert.equal(r, 0.9282578795792454 , "Should be 'hello.'#1");
  assert(original === Math.random, "Should not change Math.random.");
  assert(original !== rng, "PRNG should not be Math.random.");
  rng = zerocrypto_sr();
  assert.equal(typeof(rng), 'function', "Should return function.");
  assert(original === Math.random, "Should not change Math.random.");
  r = rng();
  assert.equal(r, 0.7220382488550928, "Should be '\\1'#1");
  r = rng();
  assert.equal(r, 0.0259971860493045, "Should be '\\1'#2");
  // Recache original seedrandom.
  proxyquire('../seedrandom', {});
});


});
