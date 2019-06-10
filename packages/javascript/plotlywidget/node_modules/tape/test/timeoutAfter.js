var tape = require('../');
var tap = require('tap');
var concat = require('concat-stream');

var stripFullStack = require('./common').stripFullStack;

tap.test('timeoutAfter test', function (tt) {
    tt.plan(1);

    var test = tape.createHarness();
    var tc = function (rows) {
        tt.same(stripFullStack(rows.toString('utf8')), [
            'TAP version 13',
            '# timeoutAfter',
            'not ok 1 test timed out after 1ms',
            '  ---',
            '    operator: fail',
            '    stack: |-',
            '      Error: test timed out after 1ms',
            '          [... stack stripped ...]',
            '  ...',
            '',
            '1..1',
            '# tests 1',
            '# pass  0',
            '# fail  1'
        ].join('\n') + '\n');
    };

    test.createStream().pipe(concat(tc));

    test('timeoutAfter', function (t) {
        t.plan(1);
        t.timeoutAfter(1);
    });
});
