var tape = require('../..');

tape.test('module-a', function (t) {
    t.plan(1)
    t.pass('loaded module a')
})

global.module_a = true
