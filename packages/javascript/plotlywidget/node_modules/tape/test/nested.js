var falafel = require('falafel');
var tape = require('../');
var tap = require('tap');
var concat = require('concat-stream');

tap.test('array test', function (tt) {
    tt.plan(1);

    var test = tape.createHarness();
    var tc = function (rows) {
        tt.same(rows.toString('utf8'), [
            'TAP version 13',
            '# nested array test',
            'ok 1 should be equivalent',
            'ok 2 should be equivalent',
            'ok 3 should be equivalent',
            'ok 4 should be equivalent',
            'ok 5 should be equivalent',
            '# inside test',
            'ok 6 should be truthy',
            'ok 7 should be truthy',
            '# another',
            'ok 8 should be truthy',
            '',
            '1..8',
            '# tests 8',
            '# pass  8',
            '',
            '# ok'
        ].join('\n') + '\n');
    };

    test.createStream().pipe(concat(tc));

    test('nested array test', function (t) {
        t.plan(6);

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

        t.test('inside test', function (q) {
            q.plan(2);
            q.ok(true);

            setTimeout(function () {
                q.ok(true);
            }, 100);
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

    test('another', function (t) {
        t.plan(1);
        setTimeout(function () {
            t.ok(true);
        }, 50);
    });
});
