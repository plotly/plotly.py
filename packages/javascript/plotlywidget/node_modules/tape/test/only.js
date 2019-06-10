var tap = require('tap');
var tape = require('../');
var concat = require('concat-stream');

tap.test('tape only test', function (tt) {
    var test = tape.createHarness({ exit: false });
    var ran = [];

    var tc = function (rows) {
        tt.deepEqual(rows.toString('utf8'), [
            'TAP version 13',
            '# run success',
            'ok 1 assert name',
            '',
            '1..1',
            '# tests 1',
            '# pass  1',
            '',
            '# ok'
        ].join('\n') + '\n');
        tt.deepEqual(ran, [ 3 ]);

        tt.end()
    };

    test.createStream().pipe(concat(tc));

    test("never run fail", function (t) {
        ran.push(1);
        t.equal(true, false)
        t.end()
    })

    test("never run success", function (t) {
        ran.push(2);
        t.equal(true, true)
        t.end()
    })

    test.only("run success", function (t) {
        ran.push(3);
        t.ok(true, "assert name")
        t.end()
    })
})
