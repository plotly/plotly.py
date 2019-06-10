var test = require('../');

test('deep strict equal', function (t) {
    t.notDeepEqual(
        [ { a: '3' } ],
        [ { a: 3 } ]
    );
    t.end();
});

test('deep loose equal', function (t) {
    t.deepLooseEqual(
        [ { a: '3' } ],
        [ { a: 3 } ]
    );
    t.end();
});
