var concat = require('concat-stream');
var tap = require('tap');
var tape = require('../');

// Exploratory test to ascertain proper output when no t.comment() call
// is made.
tap.test('no comment', function (assert) {
    assert.plan(1);

    var verify = function (output) {
        assert.equal(output.toString('utf8'), [
            'TAP version 13',
            '# no comment',
            '',
            '1..0',
            '# tests 0',
            '# pass  0',
            '',
            '# ok',
            ''
        ].join('\n'));
    };

    var test = tape.createHarness();
    test.createStream().pipe(concat(verify));
    test('no comment', function (t) {
        t.end();
    });
});

// Exploratory test, can we call t.comment() passing nothing?
tap.test('missing argument', function (assert) {
    assert.plan(1);
    var test = tape.createHarness();
    test.createStream();
    test('missing argument', function (t) {
        try {
            t.comment();
            t.end();
        } catch (err) {
            assert.equal(err.constructor, TypeError);
        } finally {
            assert.end();
        }
    });
});

// Exploratory test, can we call t.comment() passing nothing?
tap.test('null argument', function (assert) {
    assert.plan(1);
    var test = tape.createHarness();
    test.createStream();
    test('null argument', function (t) {
        try {
            t.comment(null);
            t.end();
        } catch (err) {
            assert.equal(err.constructor, TypeError);
        } finally {
            assert.end();
        }
    });
});


// Exploratory test, how is whitespace treated?
tap.test('whitespace', function (assert) {
    assert.plan(1);

    var verify = function (output) {
        assert.equal(output.toString('utf8'), [
            'TAP version 13',
            '# whitespace',
            '# ',
            '# a',
            '# a',
            '# a',
            '',
            '1..0',
            '# tests 0',
            '# pass  0',
            '',
            '# ok',
            ''
        ].join('\n'));
    };

    var test = tape.createHarness();
    test.createStream().pipe(concat(verify));
    test('whitespace', function (t) {
        t.comment(' ');
        t.comment(' a');
        t.comment('a ');
        t.comment(' a ');
        t.end();
    });
});

// Exploratory test, how about passing types other than strings?
tap.test('non-string types', function (assert) {
    assert.plan(1);

    var verify = function (output) {
        assert.equal(output.toString('utf8'), [
            'TAP version 13',
            '# non-string types',
            '# true',
            '# false',
            '# 42',
            '# 6.66',
            '# [object Object]',
            '# [object Object]',
            '# [object Object]',
            '# function ConstructorFunction() {}',
            '',
            '1..0',
            '# tests 0',
            '# pass  0',
            '',
            '# ok',
            ''
        ].join('\n'));
    };

    var test = tape.createHarness();
    test.createStream().pipe(concat(verify));
    test('non-string types', function (t) {
        t.comment(true);
        t.comment(false);
        t.comment(42);
        t.comment(6.66);
        t.comment({});
        t.comment({"answer": 42});
        function ConstructorFunction() {}
        t.comment(new ConstructorFunction());
        t.comment(ConstructorFunction);
        t.end();
    });
});

tap.test('multiline string', function (assert) {
    assert.plan(1);

    var verify = function (output) {
        assert.equal(output.toString('utf8'), [
            'TAP version 13',
            '# multiline strings',
            '# a',
            '# b',
            '# c',
            '# d',
            '',
            '1..0',
            '# tests 0',
            '# pass  0',
            '',
            '# ok',
            ''
        ].join('\n'));
    };

    var test = tape.createHarness();
    test.createStream().pipe(concat(verify));
    test('multiline strings', function (t) {
        t.comment([
            'a',
            'b',
        ].join('\n'));
        t.comment([
            'c',
            'd',
        ].join('\r\n'));
        t.end();
    });
});
