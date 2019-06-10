var test = require('../');

test('only4 duplicate test name', function (t) {
    t.fail('not 1');
    t.end();
});

test.only('only4 duplicate test name', function (t) {
    t.end();
});
