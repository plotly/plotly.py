var tape = require('../..');

tape.test('test-b', function (t) {
    t.ok(global.module_b, 'module-b loaded in same context')
    t.pass('test ran after module-b was loaded')
    t.end()
})
