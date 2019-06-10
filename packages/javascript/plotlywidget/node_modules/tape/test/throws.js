var tape = require('../');
var tap = require('tap');
var concat = require('concat-stream');

var stripFullStack = require('./common').stripFullStack;

function fn() {
    throw new TypeError('RegExp');
}

function getNonFunctionMessage(fn) {
    try {
        fn();
    } catch (e) {
        return e.message;
    }
}

var getter = function () { return 'message'; };
var messageGetterError = Object.defineProperty(
    { custom: 'error' },
    'message',
    { configurable: true, enumerable: true, get: getter }
);
var thrower = function () { throw messageGetterError; };

tap.test('failures', function (tt) {
    tt.plan(1);

    var test = tape.createHarness();
    test.createStream().pipe(concat(function (body) {
        tt.equal(
            stripFullStack(body.toString('utf8')),
            'TAP version 13\n'
            + '# non functions\n'
            + 'not ok 1 should throw\n'
            + '  ---\n'
            + '    operator: throws\n'
            + '    expected: |-\n'
            + '      undefined\n'
            + '    actual: |-\n'
            + "      { [TypeError: " + getNonFunctionMessage() + "] message: '" + getNonFunctionMessage() + "' }\n"
            + '    at: Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '    stack: |-\n'
            + '      TypeError: ' + getNonFunctionMessage(undefined) + '\n'
            + '          [... stack stripped ...]\n'
            + '          at Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '          [... stack stripped ...]\n'
            + '  ...\n'
            + 'not ok 2 should throw\n'
            + '  ---\n'
            + '    operator: throws\n'
            + '    expected: |-\n'
            + '      undefined\n'
            + '    actual: |-\n'
            + "      { [TypeError: " + getNonFunctionMessage(null) + "] message: '" + getNonFunctionMessage(null) + "' }\n"
            + '    at: Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '    stack: |-\n'
            + '      TypeError: ' + getNonFunctionMessage(null) + '\n'
            + '          [... stack stripped ...]\n'
            + '          at Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '          [... stack stripped ...]\n'
            + '  ...\n'
            + 'not ok 3 should throw\n'
            + '  ---\n'
            + '    operator: throws\n'
            + '    expected: |-\n'
            + '      undefined\n'
            + '    actual: |-\n'
            + "      { [TypeError: " + getNonFunctionMessage(true) + "] message: '" + getNonFunctionMessage(true) + "' }\n"
            + '    at: Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '    stack: |-\n'
            + '      TypeError: ' + getNonFunctionMessage(true) + '\n'
            + '          [... stack stripped ...]\n'
            + '          at Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '          [... stack stripped ...]\n'
            + '  ...\n'
            + 'not ok 4 should throw\n'
            + '  ---\n'
            + '    operator: throws\n'
            + '    expected: |-\n'
            + '      undefined\n'
            + '    actual: |-\n'
            + "      { [TypeError: " + getNonFunctionMessage(false) + "] message: '" + getNonFunctionMessage(false) + "' }\n"
            + '    at: Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '    stack: |-\n'
            + '      TypeError: ' + getNonFunctionMessage(false) + '\n'
            + '          [... stack stripped ...]\n'
            + '          at Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '          [... stack stripped ...]\n'
            + '  ...\n'
            + 'not ok 5 should throw\n'
            + '  ---\n'
            + '    operator: throws\n'
            + '    expected: |-\n'
            + '      undefined\n'
            + '    actual: |-\n'
            + "      { [TypeError: " + getNonFunctionMessage('abc') + "] message: '" + getNonFunctionMessage('abc') + "' }\n"
            + '    at: Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '    stack: |-\n'
            + '      TypeError: ' + getNonFunctionMessage('abc') + '\n'
            + '          [... stack stripped ...]\n'
            + '          at Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '          [... stack stripped ...]\n'
            + '  ...\n'
            + 'not ok 6 should throw\n'
            + '  ---\n'
            + '    operator: throws\n'
            + '    expected: |-\n'
            + '      undefined\n'
            + '    actual: |-\n'
            + "      { [TypeError: " + getNonFunctionMessage(/a/g) + "] message: '" + getNonFunctionMessage(/a/g) + "' }\n"
            + '    at: Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '    stack: |-\n'
            + '      TypeError: ' + getNonFunctionMessage(/a/g) + '\n'
            + '          [... stack stripped ...]\n'
            + '          at Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '          [... stack stripped ...]\n'
            + '  ...\n'
            + 'not ok 7 should throw\n'
            + '  ---\n'
            + '    operator: throws\n'
            + '    expected: |-\n'
            + '      undefined\n'
            + '    actual: |-\n'
            + "      { [TypeError: " + getNonFunctionMessage([]) + "] message: '" + getNonFunctionMessage([]) + "' }\n"
            + '    at: Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '    stack: |-\n'
            + '      TypeError: ' + getNonFunctionMessage([]) + '\n'
            + '          [... stack stripped ...]\n'
            + '          at Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '          [... stack stripped ...]\n'
            + '  ...\n'
            + 'not ok 8 should throw\n'
            + '  ---\n'
            + '    operator: throws\n'
            + '    expected: |-\n'
            + '      undefined\n'
            + '    actual: |-\n'
            + "      { [TypeError: " + getNonFunctionMessage({}) + "] message: '" + getNonFunctionMessage({}) + "' }\n"
            + '    at: Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '    stack: |-\n'
            + '      TypeError: ' + getNonFunctionMessage({}) + '\n'
            + '          [... stack stripped ...]\n'
            + '          at Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '          [... stack stripped ...]\n'
            + '  ...\n'
            + '# function\n'
            + 'not ok 9 should throw\n'
            + '  ---\n'
            + '    operator: throws\n'
            + '    expected: undefined\n'
            + '    actual:   undefined\n'
            + '    at: Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '    stack: |-\n'
            + '      Error: should throw\n'
            + '          [... stack stripped ...]\n'
            + '          at Test.<anonymous> ($TEST/throws.js:$LINE:$COL)\n'
            + '          [... stack stripped ...]\n'
            + '  ...\n'
            + '# custom error messages\n'
            + 'ok 10 "message" is enumerable\n'
            + "ok 11 { custom: 'error', message: 'message' }\n"
            + 'ok 12 getter is still the same\n'
            + '# throws null\n'
            + 'ok 13 throws null\n'
            + '\n1..13\n'
            + '# tests 13\n'
            + '# pass  4\n'
            + '# fail  9\n'
        );
    }));

    test('non functions', function (t) {
        t.plan(8);
        t.throws();
        t.throws(null);
        t.throws(true);
        t.throws(false);
        t.throws('abc');
        t.throws(/a/g);
        t.throws([]);
        t.throws({});
    });

    test('function', function (t) {
        t.plan(1);
        t.throws(function () {});
    });

    test('custom error messages', function (t) {
        t.plan(3);
        t.equal(Object.prototype.propertyIsEnumerable.call(messageGetterError, 'message'), true, '"message" is enumerable');
        t.throws(thrower, "{ custom: 'error', message: 'message' }");
        t.equal(Object.getOwnPropertyDescriptor(messageGetterError, 'message').get, getter, 'getter is still the same');
    });

    test('throws null', function (t) {
        t.plan(1);
        t.throws(function () { throw null; }, 'throws null');
        t.end();
    });
});
