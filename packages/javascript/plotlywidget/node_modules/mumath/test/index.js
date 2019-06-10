var m = require('../index');
var assert = require('assert');

// assert.equal(m.min(0,2),0);
// assert.equal(m.max(0,2),2);
// assert.deepEqual(m.min([0,0],[2,-2]),[0,-2]);

assert.equal(m.clamp(-100, 0, 100), 0);
assert.equal(m.clamp(-100, 100, 0), 0);
assert.equal(m.clamp(-Infinity, -100, 0), -100);

//limit arrays
assert.deepEqual(m.clamp([-100, -200], -100, 100),  [-100, -100]);
assert.deepEqual(m.clamp([-101, 101], [-50, -100], [100, 50]), [-50, 50]);

//limit objects
assert.deepEqual(m.clamp({top: 120, bottom: -10}, 0, 100), {top: 100, bottom: 0});
assert.deepEqual(m.clamp({top: 120, bottom: -10}, {top: 0, bottom:0},  {top: 100, bottom: 100}), {top: 100, bottom: 0});

//normalize
assert.equal(m.normalize(-0.4999999999999998), -.5);
assert.equal(m.normalize(1.5000000000000002), 1.5);
assert.equal(m.normalize(10.5000000000000002), 10.5);
assert.equal(m.normalize(-0.7999999999999996), -.8);


//precisions
assert.equal(m.precision(1.0000000000000005e+33), 0);
assert.equal(m.precision(3.0000000000000004), 0);
assert.equal(m.precision(1.9999999999999998), 0);
assert.equal(m.precision(0.02), 2);
assert.equal(m.precision(100), 0);
assert.equal(m.precision(1e-1), 1);
assert.equal(m.precision(1e-5), 5);
assert.equal(m.precision(1e-19), 19);
assert.equal(m.precision(1.0000000000000001e+33), 0);
assert.equal(m.precision(-0.4999999999999998), 1);
assert.equal(m.precision(1.5000000000000002), 1);
assert.equal(m.precision(-0.7999999999999996), 1);


assert.equal(m.round(0.3, .5), .5);

//multiple
assert.equal(m.isMultiple(100,10), true);
assert.equal(m.isMultiple(100.1,10, .1), true);

//loop
assert.equal(m.mod(10, 100), 10);

assert.equal(m.mod(110, 100), 10);
assert.equal(m.mod(110, 90), 20);

assert.equal(m.mod(-110, 100), 90);

assert.equal(m.mod(110, 0, 100), 10);
assert.equal(m.mod(110, -10, 100), 0);
assert.equal(m.mod(110, -10, 90), 10);
assert.equal(m.mod(-110, -100, 0), -10);
assert.equal(m.mod(-110, -100, 10), 0);
assert.equal(m.mod(-110, -90, 10), -10);

//lg
assert.equal(m.log10(100), 2);
assert.equal(m.log10(10), 1);
assert.equal(m.log10(1), 0);
assert.equal(Math.round(m.log10(0.1)), -1);

//len
assert.equal(m.len(3,4), 5);

//closest
assert.equal(m.closest(0.2, [0.01, 0.1, 1, 10, 100]), 0.1);

//order
assert.equal(m.order(123), 100);
assert.equal(m.order(0.000213), 0.0001);
assert.equal(m.order(-123), 100);
assert.equal(m.order(-0.0000123), 0.00001);

assert(m.within(1, 0, 2));
assert(m.within(1, 2, 0));
assert(!m.within(0, 2, 1));


assert.equal(m.lerp(1,0,.5), .5);


//step
assert.equal(m.scale(.1, [1, 2, 5]), .1);
assert.equal(m.scale(.1, [1, 2, 5]), .1);



//formatting
// assert.equal(m.pretty(1.9999999999999998), '2');
// assert.equal(m.pretty(1.0000000000000005e+33), '1e+33');
// assert.equal(m.pretty(0.1), '0.1');
// assert.equal(m.pretty(3.0000000000000004), '3');
// assert.equal(m.pretty(7.0000000000000036, 2), '7');
// assert.equal(m.pretty(3.885780586188048e-16), '0');
// assert.equal(m.pretty(-1.9999999999999993), '-2');
// assert.equal(m.pretty(-0.9999999999999996), '-1');
// assert.equal(m.pretty(1.5000000000000002), '1.5');
// assert.equal(m.pretty(-0.4999999999999998), '-0.5');
// assert.equal(m.pretty(-0.7999999999999996), '-0.8');
// assert.equal(m.pretty(500), '500');
// assert.equal(m.pretty(0.4000000000000002), '0.4');
