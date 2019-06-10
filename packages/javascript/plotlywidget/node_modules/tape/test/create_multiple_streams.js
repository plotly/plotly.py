var tape = require('../');

tape.test('createMultipleStreams', function (tt) {
    tt.plan(2);

    var th = tape.createHarness();
    th.createStream()
    th.createStream()

    var testOneComplete = false;

    th('test one', function (tht) {
        tht.plan(1);
        setTimeout( function () {
            tht.pass();
            testOneComplete = true;
        }, 100);
    });

    th('test two', function (tht) {
        tht.ok(testOneComplete, 'test 1 completed before test 2');
        tht.end();
    });

    th.onFinish(function () {
        tt.equal(th._results.count, 2, "harness test ran");
        tt.equal(th._results.fail,  0, "harness test didn't fail");
    });
});


