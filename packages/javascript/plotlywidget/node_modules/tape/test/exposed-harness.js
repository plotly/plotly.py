var tape = require('../');
var tap = require('tap');

tap.test('main harness object is exposed', function (assert) {

    assert.equal(typeof tape.getHarness, 'function', 'tape.getHarness is a function')

    assert.equal(tape.getHarness()._results.pass, 0)

    assert.end()

})
