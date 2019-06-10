var test = require('tap').test;
var path = require('path');
var concat = require('concat-stream');
var spawn = require('child_process').spawn;

var stripFullStack = require('./common').stripFullStack;

test(function (t) {
    t.plan(2);
    var ps = spawn(process.execPath, [path.join(__dirname, 'double_end', 'double.js')]);
    ps.on('exit', function (code) {
        t.equal(code, 1);
    });
    ps.stdout.pipe(concat(function (body) {
        // The implementation of node's timer library has changed over time. We
        // need to reverse engineer the error we expect to see.

        // This code is unfortunately by necessity highly coupled to node
        // versions, and may require tweaking with future versions of the timers
        // library.
        function doEnd() { throw new Error() };
        var to = setTimeout(doEnd, 5000);
        clearTimeout(to);
        to._onTimeout = doEnd;

        var stackExpected;
        var atExpected;
        try {
            to._onTimeout();
        }
        catch (e) {
            stackExpected = stripFullStack(e.stack).split('\n')[1];
            stackExpected = stackExpected.replace('double_end.js', 'double_end/double.js');
            stackExpected = stackExpected.trim();
            atExpected = stackExpected.replace(/^at\s+/, 'at: ');
        }

        var stripped = stripFullStack(body.toString('utf8'));
        t.equal(stripped, [
            'TAP version 13',
            '# double end',
            'ok 1 should be equal',
            'not ok 2 .end() called twice',
            '  ---',
            '    operator: fail',
            '    ' + atExpected,
            '    stack: |-',
            '      Error: .end() called twice',
            '          [... stack stripped ...]',
            '          ' + stackExpected,
            '          [... stack stripped ...]',
            '  ...',
            '',
            '1..2',
            '# tests 2',
            '# pass  1',
            '# fail  1',
        ].join('\n') + '\n\n');
    }));
});
