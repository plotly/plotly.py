var tape = require('../..');

tape.test('module-b', function (t) {
    t.plan(1)
    t.pass('loaded module b')
})

global.module_b = true
