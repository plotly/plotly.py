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
