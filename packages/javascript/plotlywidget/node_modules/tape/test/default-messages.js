var tap = require('tap');
var path = require('path');
var spawn = require('child_process').spawn;
var concat = require('concat-stream');

tap.test('default messages', function (t) {
    t.plan(1);

    var ps = spawn(process.execPath, [path.join(__dirname, 'messages', 'defaults.js')]);

    ps.stdout.pipe(concat(function (rows) {

        t.same(rows.toString('utf8'), [
            'TAP version 13',
            '# default messages',
            'ok 1 should be truthy',
            'ok 2 should be falsy',
            'ok 3 should be equal',
            'ok 4 should not be equal',
            'ok 5 should be equivalent',
            'ok 6 should be equivalent',
            'ok 7 should be equivalent',
            '',
            '1..7',
            '# tests 7',
            '# pass  7',
            '',
            '# ok'
        ].join('\n') + '\n\n');
    }));
});
