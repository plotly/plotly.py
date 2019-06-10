var test = require('tape')

var createStore = require('../create-store.js')

test('can create store', function (assert) {
    var privates = createStore()

    var key = {}
    var value = privates(key)

    value.foo = 'bar'

    var value2 = privates(key)

    assert.equal(value, value2)
    assert.equal(value2.foo, 'bar')
    assert.deepEqual(Object.keys(key), [])

    assert.end()
})

test('cannot call valueOf() to access store', function (assert) {
    var privates = createStore()

    var key = { foo: 'bar' }
    privates(key)

    var obj = key.valueOf()

    assert.equal(obj, key)
    assert.equal(obj.foo, 'bar')

    assert.end()
})
