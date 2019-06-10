var tap = require("tap");
var tape = require("../");

tap.test("on finish", {timeout: 1000}, function (tt) {
    tt.plan(1);
    tape.onFinish(function () {
        tt.pass('tape ended');
    });
    tape('dummy test', function (t) {
        t.end();
    });
});
