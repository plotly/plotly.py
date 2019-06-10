var falafel = require('falafel');
var tape = require('../');
var tap = require('tap');
var concat = require('concat-stream');

var stripFullStack = require('./common').stripFullStack;

tap.test('array test', function (tt) {
    tt.plan(1);

    var test = tape.createHarness({ exit : false });
    var tc = function (rows) {
        tt.same(stripFullStack(rows.toString('utf8')), [
            'TAP version 13',
            '# array',
            'ok 1 should be equivalent',
            'ok 2 should be equivalent',
            'ok 3 should be equivalent',
            'ok 4 should be equivalent',
            'not ok 5 plan != count',
            '  ---',
            '    operator: fail',
            '    expected: 3',
            '    actual:   4',
            '    at: <anonymous> ($TEST/too_many.js:$LINE:$COL)',
            '    stack: |-',
            '      Error: plan != count',
            '          [... stack stripped ...]',
            '          at $TEST/too_many.js:$LINE:$COL',
            '          at eval (eval at <anonymous> ($TEST/too_many.js:$LINE:$COL))',
            '          at eval (eval at <anonymous> ($TEST/too_many.js:$LINE:$COL))',
            '          at Test.<anonymous> ($TEST/too_many.js:$LINE:$COL)',
            '          [... stack stripped ...]',
            '  ...',
            'ok 6 should be equivalent',
            '',
            '1..6',
            '# tests 6',
            '# pass  5',
            '# fail  1'
        ].join('\n') + '\n');
    };

    test.createStream().pipe(concat(tc));

    test('array', function (t) {
        t.plan(3);

        var src = '(' + function () {
            var xs = [ 1, 2, [ 3, 4 ] ];
            var ys = [ 5, 6 ];
            g([ xs, ys ]);
        } + ')()';

        var output = falafel(src, function (node) {
            if (node.type === 'ArrayExpression') {
                node.update('fn(' + node.source() + ')');
            }
        });

        var arrays = [
            [ 3, 4 ],
            [ 1, 2, [ 3, 4 ] ],
            [ 5, 6 ],
            [ [ 1, 2, [ 3, 4 ] ], [ 5, 6 ] ],
        ];

        Function(['fn','g'], output)(
            function (xs) {
                t.same(arrays.shift(), xs);
                return xs;
            },
            function (xs) {
                t.same(xs, [ [ 1, 2, [ 3, 4 ] ], [ 5, 6 ] ]);
            }
        );
    });
});
