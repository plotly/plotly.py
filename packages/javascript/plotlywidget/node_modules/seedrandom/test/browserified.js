require=(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){

},{}],2:[function(require,module,exports){
arguments[4][1][0].apply(exports,arguments)
},{"dup":1}],3:[function(require,module,exports){
/*
Copyright 2014 David Bau.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

*/

(function (pool, math) {
//
// The following constants are related to IEEE 754 limits.
//

// Detect the global object, even if operating in strict mode.
// http://stackoverflow.com/a/14387057/265298
var global = (0, eval)('this'),
    width = 256,        // each RC4 output is 0 <= x < 256
    chunks = 6,         // at least six RC4 outputs for each double
    digits = 52,        // there are 52 significant digits in a double
    rngname = 'random', // rngname: name for Math.random and Math.seedrandom
    startdenom = math.pow(width, chunks),
    significance = math.pow(2, digits),
    overflow = significance * 2,
    mask = width - 1,
    nodecrypto;         // node.js crypto module, initialized at the bottom.

//
// seedrandom()
// This is the seedrandom function described above.
//
function seedrandom(seed, options, callback) {
  var key = [];
  options = (options == true) ? { entropy: true } : (options || {});

  // Flatten the seed string or build one from local entropy if needed.
  var shortseed = mixkey(flatten(
    options.entropy ? [seed, tostring(pool)] :
    (seed == null) ? autoseed() : seed, 3), key);

  // Use the seed to initialize an ARC4 generator.
  var arc4 = new ARC4(key);

  // This function returns a random double in [0, 1) that contains
  // randomness in every bit of the mantissa of the IEEE 754 value.
  var prng = function() {
    var n = arc4.g(chunks),             // Start with a numerator n < 2 ^ 48
        d = startdenom,                 //   and denominator d = 2 ^ 48.
        x = 0;                          //   and no 'extra last byte'.
    while (n < significance) {          // Fill up all significant digits by
      n = (n + x) * width;              //   shifting numerator and
      d *= width;                       //   denominator and generating a
      x = arc4.g(1);                    //   new least-significant-byte.
    }
    while (n >= overflow) {             // To avoid rounding up, before adding
      n /= 2;                           //   last byte, shift everything
      d /= 2;                           //   right using integer math until
      x >>>= 1;                         //   we have exactly the desired bits.
    }
    return (n + x) / d;                 // Form the number within [0, 1).
  };

  prng.int32 = function() { return arc4.g(4) | 0; }
  prng.quick = function() { return arc4.g(4) / 0x100000000; }
  prng.double = prng;

  // Mix the randomness into accumulated entropy.
  mixkey(tostring(arc4.S), pool);

  // Calling convention: what to return as a function of prng, seed, is_math.
  return (options.pass || callback ||
      function(prng, seed, is_math_call, state) {
        if (state) {
          // Load the arc4 state from the given state if it has an S array.
          if (state.S) { copy(state, arc4); }
          // Only provide the .state method if requested via options.state.
          prng.state = function() { return copy(arc4, {}); }
        }

        // If called as a method of Math (Math.seedrandom()), mutate
        // Math.random because that is how seedrandom.js has worked since v1.0.
        if (is_math_call) { math[rngname] = prng; return seed; }

        // Otherwise, it is a newer calling convention, so return the
        // prng directly.
        else return prng;
      })(
  prng,
  shortseed,
  'global' in options ? options.global : (this == math),
  options.state);
}
math['seed' + rngname] = seedrandom;

//
// ARC4
//
// An ARC4 implementation.  The constructor takes a key in the form of
// an array of at most (width) integers that should be 0 <= x < (width).
//
// The g(count) method returns a pseudorandom integer that concatenates
// the next (count) outputs from ARC4.  Its return value is a number x
// that is in the range 0 <= x < (width ^ count).
//
function ARC4(key) {
  var t, keylen = key.length,
      me = this, i = 0, j = me.i = me.j = 0, s = me.S = [];

  // The empty key [] is treated as [0].
  if (!keylen) { key = [keylen++]; }

  // Set up S using the standard key scheduling algorithm.
  while (i < width) {
    s[i] = i++;
  }
  for (i = 0; i < width; i++) {
    s[i] = s[j = mask & (j + key[i % keylen] + (t = s[i]))];
    s[j] = t;
  }

  // The "g" method returns the next (count) outputs as one number.
  (me.g = function(count) {
    // Using instance members instead of closure state nearly doubles speed.
    var t, r = 0,
        i = me.i, j = me.j, s = me.S;
    while (count--) {
      t = s[i = mask & (i + 1)];
      r = r * width + s[mask & ((s[i] = s[j = mask & (j + t)]) + (s[j] = t))];
    }
    me.i = i; me.j = j;
    return r;
    // For robust unpredictability, the function call below automatically
    // discards an initial batch of values.  This is called RC4-drop[256].
    // See http://google.com/search?q=rsa+fluhrer+response&btnI
  })(width);
}

//
// copy()
// Copies internal state of ARC4 to or from a plain object.
//
function copy(f, t) {
  t.i = f.i;
  t.j = f.j;
  t.S = f.S.slice();
  return t;
};

//
// flatten()
// Converts an object tree to nested arrays of strings.
//
function flatten(obj, depth) {
  var result = [], typ = (typeof obj), prop;
  if (depth && typ == 'object') {
    for (prop in obj) {
      try { result.push(flatten(obj[prop], depth - 1)); } catch (e) {}
    }
  }
  return (result.length ? result : typ == 'string' ? obj : obj + '\0');
}

//
// mixkey()
// Mixes a string seed into a key that is an array of integers, and
// returns a shortened string seed that is equivalent to the result key.
//
function mixkey(seed, key) {
  var stringseed = seed + '', smear, j = 0;
  while (j < stringseed.length) {
    key[mask & j] =
      mask & ((smear ^= key[mask & j] * 19) + stringseed.charCodeAt(j++));
  }
  return tostring(key);
}

//
// autoseed()
// Returns an object for autoseeding, using window.crypto and Node crypto
// module if available.
//
function autoseed() {
  try {
    var out;
    if (nodecrypto && (out = nodecrypto.randomBytes)) {
      // The use of 'out' to remember randomBytes makes tight minified code.
      out = out(width);
    } else {
      out = new Uint8Array(width);
      (global.crypto || global.msCrypto).getRandomValues(out);
    }
    return tostring(out);
  } catch (e) {
    var browser = global.navigator,
        plugins = browser && browser.plugins;
    return [+new Date, global, plugins, global.screen, tostring(pool)];
  }
}

//
// tostring()
// Converts an array of charcodes to a string
//
function tostring(a) {
  return String.fromCharCode.apply(0, a);
}

//
// When seedrandom.js is loaded, we immediately mix a few bits
// from the built-in RNG into the entropy pool.  Because we do
// not want to interfere with deterministic PRNG state later,
// seedrandom will not call math.random on its own again after
// initialization.
//
mixkey(math.random(), pool);

//
// Nodejs and AMD support: export the implementation as a module using
// either convention.
//
if ((typeof module) == 'object' && module.exports) {
  module.exports = seedrandom;
  // When in node.js, try using crypto package for autoseeding.
  try {
    nodecrypto = require('crypto');
  } catch (ex) {}
} else if ((typeof define) == 'function' && define.amd) {
  define(function() { return seedrandom; });
}

// End anonymous scope, and pass initial values.
})(
  [],     // pool: entropy pool starts empty
  Math    // math: package containing random, pow, and seedrandom
);

},{"crypto":1}],4:[function(require,module,exports){
(function (__dirname){
var assert = require("assert");
var seedrandom = require("../seedrandom");
var requirejs = require("requirejs");

// Stub out requirejs if in the browser via browserify.
if (!requirejs.config) {
  requirejs = require;
} else {
  requirejs.config({
    baseUrl: __dirname
  });
}

describe("Nodejs API Test", function() {

it('should pass basic tests.', function() {
  var original = Math.random,
      result, r, xprng, obj, as2, as3, autoseed1, myrng,
      firstprng, secondprng, thirdprng, rng;

  result = Math.seedrandom('hello.');
  firstprng = Math.random;
  assert.ok(original !== firstprng, "Should change Math.random.");
  assert.equal(result, "hello.", "Should return short seed.");
  r = Math.random();
  assert.equal(r, 0.9282578795792454, "Should be 'hello.'#1");
  r = Math.random();
  assert.equal(r, 0.3752569768646784, "Should be 'hello.'#2");

  // should be able to autoseed
  result = Math.seedrandom();
  secondprng = Math.random;
  assert.ok(original !== secondprng, "Should change Math.random.");
  assert.ok(firstprng !== secondprng, "Should change Math.random.");
  assert.equal(result.length, 256, "Should return short seed.");
  r = Math.random();
  assert.ok(r > 0, "Should be posititive.");
  assert.ok(r < 1, "Should be less than 1.");
  assert.ok(r != 0.9282578795792454, "Should not be 'hello.'#1");
  assert.ok(r != 0.3752569768646784, "Should not be 'hello.'#2");
  assert.ok(r != 0.7316977468919549, "Should not be 'hello.'#3");
  autoseed1 = r;

  // should be able to add entropy.
  result = Math.seedrandom('added entropy.', { entropy:true });
  assert.equal(result.length, 256, "Should return short seed.");
  thirdprng = Math.random;
  assert.ok(thirdprng !== secondprng, "Should change Math.random.");
  r = Math.random();
  assert.ok(r != 0.597067214994467, "Should not be 'added entropy.'#1");

  // Reset to original Math.random.
  Math.random = original;
  // should be able to use new Math.seedrandom('hello.')
  myrng = new Math.seedrandom('hello.');
  assert.ok(original === Math.random, "Should not change Math.random.");
  assert.ok(original !== myrng, "PRNG should not be Math.random.");
  r = myrng();
  assert.equal(r, 0.9282578795792454, "Should be 'hello.'#1");

  // should be able to use seedrandom('hello.')"
  rng = seedrandom('hello.');
  assert.equal(typeof(rng), 'function', "Should return a function.");
  r = rng();
  assert.equal(r, 0.9282578795792454, "Should be 'hello.'#1");
  assert.ok(original === Math.random, "Should not change Math.random.");
  assert.ok(original !== rng, "PRNG should not be Math.random.");

  // Global PRNG: set Math.random.
  // should be able to use seedrandom('hello.', { global: true })
  result = seedrandom('hello.', { global: true });
  assert.equal(result, 'hello.', "Should return short seed.");
  assert.ok(original != Math.random, "Should change Math.random.");
  r = Math.random();
  assert.equal(r, 0.9282578795792454, "Should be 'hello.'#1");

  // Autoseeded non-global
  Math.random = original;
  // should be able to use seedrandom()
  result = seedrandom();
  assert.equal(typeof(result), 'function', "Should return function.");
  assert.ok(original === Math.random, "Should not change Math.random.");
  r = result();
  // got " + r);
  assert.ok(r != autoseed1, "Should not repeat previous autoseed.");
  assert.ok(r != 0.9282578795792454, "Should not be 'hello.'#1");
  assert.ok(r != 0.7316977468919549, "Should not be 'hello.'#3");

  // Mixing accumulated entropy.
  // should be able to use seedrandom('added entropy.', { entropy: true })
  rng = seedrandom('added entropy.', { entropy: true });
  r = result();
  // got " + r);
  assert.ok(r != autoseed1, "Should not repeat previous autoseed.");
  assert.ok(r != 0.597067214994467, "Should not be 'added entropy.'#1");

  // Legacy calling convention for mixing accumulated entropy.
  // should be able to use seedrandom('added entropy.', true)
  rng = seedrandom('added entropy.', true);
  r = result();
  // got " + r);
  assert.ok(r != autoseed1, "Should not repeat previous autoseed.");
  assert.ok(r != 0.597067214994467, "Should not be 'added entropy.'#1");

  // The pass option
  // should be able to use Math.seedrandom(null, { pass: ...
  obj = Math.seedrandom(null, { pass: function(prng, seed) {
    return { random: prng, seed: seed };
  }});
  assert.ok(original === Math.random, "Should not change Math.random.");
  assert.ok(original !== obj.random, "Should be different from Math.random.");
  assert.equal(typeof(obj.random), 'function', "Should return a PRNG function.");
  assert.equal(typeof(obj.seed), 'string', "Should return a seed.");
  as2 = obj.random();
  assert.ok(as2 != 0.9282578795792454, "Should not be 'hello.'#1");
  rng = seedrandom(obj.seed);
  as3 = rng();
  assert.equal(as2, as3, "Should be reproducible when using the seed.");

  // Exercise pass again, with explicit seed and global
  // should be able to use Math.seedrandom('hello.', { pass: ...
  result = Math.seedrandom('hello.', {
    global: 'abc',
    pass: function(prng, seed, global) {
      assert.equal(typeof(prng), 'function', "Callback arg #1 assert");
      assert.equal(seed, 'hello.', "Callback arg #2 assert");
      assert.equal(global, 'abc', "Callback arg #3 passed through.");
      assert.equal(prng(), 0.9282578795792454, "Should be 'hello.'#1");
      return 'def';
  }});
  assert.equal(result, 'def', "Should return value from callback.");
  assert.ok(original === Math.random, "Should not change Math.random.");

  // Legacy third argument callback argument:
  // should be able to use Math.seedrandom('hello.', { global: 50 }, callback)
  result = Math.seedrandom('hello.', { global: 50 },
    function(prng, seed, global) {
      assert.equal(typeof(prng), 'function', "Callback arg #1 assert");
      assert.equal(seed, 'hello.', "Callback arg #2 assert");
      assert.equal(global, 50, "Callback arg #3 assert");
      assert.equal(prng(), 0.9282578795792454, "Should be 'hello.'#1");
      return 'zzz';
  });
  assert.equal(result, 'zzz', "Should return value from callback.");
  assert.ok(original === Math.random, "Should not change Math.random.");

  // Global: false.
  // should be able to use new Math.seedrandom('hello.', {global: false})
  myrng = new Math.seedrandom('hello.', {global:false});
  assert.equal(typeof(myrng), 'function', "Should return a PRNG funciton.");
  assert.ok(original === Math.random, "Should not change Math.random.");
  assert.ok(original !== myrng, "PRNG should not be Math.random.");
  r = myrng();
  assert.equal(r, 0.9282578795792454, "Should be 'hello.'#1");

  // options = {} when a method of Math.
  // should be able to use Math.seedrandom('hello.', {})
  result = Math.seedrandom('hello.');
  xprng = Math.random;
  assert.ok(original !== xprng, "Should change Math.random.");
  assert.equal(result, "hello.", "Should return short seed.");
  r = Math.random();
  assert.equal(r, 0.9282578795792454, "Should be 'hello.'#1");
  r = Math.random();
  assert.equal(r, 0.3752569768646784, "Should be 'hello.'#2");
  Math.random = original;

  // options = {} when not a method of Math
  // should be able to use seedrandom('hello.', {})
  rng = seedrandom('hello.', {});
  assert.equal(typeof(rng), 'function', "Should return a function.");
  r = rng();
  assert.equal(r, 0.9282578795792454, "Should be 'hello.'#1");
  assert.ok(original === Math.random, "Should not change Math.random.");
  assert.ok(original !== rng, "PRNG should not be Math.random.");
});

it('should support state api.', function() {
  // Verify that there is no state method
  var dummy = seedrandom('hello');
  var unexpected = -1;
  var expected = -1;
  try {
    unexpected = dummy.state();
  } catch(e) {
    expected = 1;
  }
  assert.equal(unexpected, -1);
  assert.equal(expected, 1);
  var count = 0;
  for (var x in dummy) {
    if (x == 'state') count += 1;
  }
  assert.equal(count, 0);

  // Verify that a state method can be added
  var saveable = seedrandom("secret-seed", {state: true});
  var ordinary = seedrandom("secret-seed");
  for (var j = 0; j < 1e2; ++j) {
    assert.equal(ordinary(), saveable());
  }
  var virgin = seedrandom("secret-seed");
  var saved = saveable.state();
  var replica = seedrandom("", {state: saved});
  for (var j = 0; j < 1e2; ++j) {
    var r = replica();
    assert.equal(r, saveable());
    assert.equal(r, ordinary());
    assert.ok(r != virgin());
  }
});

it('should support requirejs in node.', function() {
  var original = Math.random;
  var rsr = requirejs('../seedrandom');
  var rng = rsr('hello.');
  assert.equal(typeof(rng), 'function', "Should return a function.");
  var r = rng();
  assert.equal(r, 0.9282578795792454, "Should be 'hello.'#1");
  assert.ok(original === Math.random, "Should not change Math.random.");
  assert.ok(original !== rng, "PRNG should not be Math.random.");
});

// End of test.

});

}).call(this,"/test")
},{"../seedrandom":3,"assert":"assert","requirejs":2}],"assert":[function(require,module,exports){
// Use QUnit.assert to mimic node.assert.

module.exports = QUnit.assert;

},{}]},{},[4]);
