var test = require('../');

var asyncFunction = function (callback) {
    setTimeout(callback, Math.random * 50);
};

test('master test', function (t) {
    t.test('subtest 1', function (st) {
        st.pass('subtest 1 before async call');
        asyncFunction(function () {
            st.pass('subtest 1 in async callback');
            st.end();
        })
    });

    t.test('subtest 2', function (st) {
        st.pass('subtest 2 before async call');
        asyncFunction(function () {
            st.pass('subtest 2 in async callback');
            st.end();
        })
    });

    t.end();
});
