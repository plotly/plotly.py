var tap = require("tap");
var tape = require("../").createHarness();

//Because this test passing depends on a failure,
//we must direct the failing output of the inner test
var noop = function () {}
var mockSink = {on:noop, removeListener:noop, emit:noop, end:noop}
tape.createStream().pipe(mockSink);

tap.test("on failure", { timeout: 1000 }, function (tt) {
    tt.plan(1);

    tape("dummy test", function (t) {
        t.fail();
        t.end();
    });

    tape.onFailure(function () {
        tt.pass("tape ended");
    });
});
