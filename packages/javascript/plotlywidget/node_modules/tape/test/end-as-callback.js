var tap = require("tap");
var forEach = require("for-each");
var tape = require("../");
var concat = require('concat-stream');

tap.test("tape assert.end as callback", function (tt) {
    var test = tape.createHarness({ exit: false })

    test.createStream().pipe(concat(function (rows) {
        tt.equal(rows.toString('utf8'), [
            'TAP version 13',
            '# do a task and write',
            'ok 1 null',
            'ok 2 should be equal',
            '# do a task and write fail',
            'ok 3 null',
            'ok 4 should be equal',
            'not ok 5 Error: fail',
            getStackTrace(rows), // tap error stack
            '',
            '1..5',
            '# tests 5',
            '# pass  4',
            '# fail  1'
        ].join('\n') + '\n');
        tt.end()
    }));

    test("do a task and write", function (assert) {
        fakeAsyncTask("foo", function (err, value) {
            assert.ifError(err)
            assert.equal(value, "taskfoo")

            fakeAsyncWrite("bar", assert.end)
        })
    })

    test("do a task and write fail", function (assert) {
        fakeAsyncTask("bar", function (err, value) {
            assert.ifError(err)
            assert.equal(value, "taskbar")

            fakeAsyncWriteFail("baz", assert.end)
        })
    })
})

function fakeAsyncTask(name, cb) {
    cb(null, "task" + name)
}

function fakeAsyncWrite(name, cb) {
    cb(null)
}

function fakeAsyncWriteFail(name, cb) {
    cb(new Error("fail"))
}

/**
 * extract the stack trace for the failed test.
 * this will change dependent on the environment
 * so no point hard-coding it in the test assertion
 * see: https://git.io/v6hGG for example
 * @param String rows - the tap output lines
 * @returns String stacktrace - just the error stack part
 */
function getStackTrace(rows) {
    var stacktrace = '  ---\n';
    var extract = false;
    forEach(rows.toString('utf8').split('\n'), function (row) {
        if (!extract) {
            if (row.indexOf('---') > -1) { // start of stack trace
                extract = true;
            }
        } else {
            if (row.indexOf('...') > -1) { // end of stack trace
                extract = false;
                stacktrace += '  ...';
            } else {
                stacktrace += row + '\n';
            }

        }
    });
    // console.log(stacktrace);
    return stacktrace;
}
