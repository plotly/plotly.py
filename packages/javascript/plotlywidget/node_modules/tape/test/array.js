var falafel = require('falafel');
var tape = require('../');
var tap = require('tap');
var concat = require('concat-stream');

tap.test('array test', function (tt) {
    tt.plan(1);

    var test = tape.createHarness();

    test.createStream().pipe(concat(function (rows) {
        tt.same(rows.toString('utf8'), [
            'TAP version 13',
            '# array',
            'ok 1 should be equivalent',
            'ok 2 should be equivalent',
            'ok 3 should be equivalent',
            'ok 4 should be equivalent',
            'ok 5 should be equivalent',
            '',
            '1..5',
            '# tests 5',
            '# pass  5',
            '',
            '# ok'
        ].join('\n') + '\n');
    }));

    test('array', function (t) {
        t.plan(5);

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
