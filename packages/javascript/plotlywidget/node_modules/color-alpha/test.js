const assert = require('assert');
const α = require('./');

assert.equal(α('white', .1), 'rgba(255,255,255,0.1)');
assert.equal(α('rgba(244,244,244, .3)', 1), 'rgba(244,244,244,1)');
assert.equal(α('hsla(1,2%,3%, .3)', 1), 'hsla(1,2%,3%,1)');