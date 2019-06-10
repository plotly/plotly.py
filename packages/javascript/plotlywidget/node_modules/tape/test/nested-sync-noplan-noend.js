var tape = require('../');
var tap = require('tap');
var concat = require('concat-stream');

tap.test('nested sync test without plan or end', function (tt) {
    tt.plan(1);

    var test = tape.createHarness();
    var tc = function (rows) {
        tt.same(rows.toString('utf8'), [
            'TAP version 13',
            '# nested without plan or end',
            '# first',
            'ok 1 should be truthy',
            '# second',
            'ok 2 should be truthy',
            '',
            '1..2',
            '# tests 2',
            '# pass  2',
            '',
            '# ok'
        ].join('\n') + '\n');
    };

    test.createStream().pipe(concat(tc));

    test('nested without plan or end', function (t) {
        t.test('first', function (q) {
            setTimeout(function first() {
                q.ok(true);
                q.end()
            }, 10);
        });
        t.test('second', function (q) {
            setTimeout(function second() {
                q.ok(true);
                q.end()
            }, 10);
        });
    });

});
