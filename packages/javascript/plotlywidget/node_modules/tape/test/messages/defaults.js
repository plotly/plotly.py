var test = require('../../');

test('default messages', function (t) {
    t.plan(7);
    t.ok(true);
    t.notOk(false);
    t.equal(true, true);
    t.notEqual(true, false);
    t.deepEqual(true, true);
    t.deepLooseEqual(true, true);
    t.notDeepLooseEqual(true, false);
});
