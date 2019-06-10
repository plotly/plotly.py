var test = require('../');
var ran = 0;

test('timeout', function (t) {
    t.pass('this should run');
    ran++;
    setTimeout(function () {
        t.end();
    }, 100);
});

test('should still run', { timeout: 50 }, function (t) {
    t.equal(ran, 1);
    t.end();
});
