var tap = require('tap');
var tape = require('../');
var concat = require('concat-stream');

var common = require('./common');
var stripFullStack = common.stripFullStack;

tap.test('tape todo test', function (assert) {
    var test = tape.createHarness({ exit: false });
    assert.plan(1);

    test.createStream().pipe(concat(function (body) {
        assert.equal(
            stripFullStack(body.toString('utf8')),
            'TAP version 13\n'
            + '# success\n'
            + 'ok 1 this test runs\n'
            + '# failure\n'
            + 'not ok 2 should never happen # TODO\n'
            + '  ---\n'
            + '    operator: fail\n'
            + '    at: Test.<anonymous> ($TEST/todo.js:$LINE:$COL)\n'
            + '  ...\n'
            + '\n'
            + '1..2\n'
            + '# tests 2\n'
            + '# pass  2\n'
            + '\n'
            + '# ok\n'
        )
    }));

    test('success', function (t) {
        t.equal(true, true, 'this test runs');
        t.end();
    });

    test('failure', { todo: true }, function (t) {
        t.fail('should never happen');
        t.end();
    });
});
