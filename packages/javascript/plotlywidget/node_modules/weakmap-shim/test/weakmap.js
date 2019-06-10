var test = require('tape')

var weakMap = require('../index')

test('weakMap is a function', function (assert) {
    assert.equal(typeof weakMap, 'function')
    assert.end()
})

test('weakMap returns a map', function (assert) {
    var map = weakMap();

    var key = {}
    var v = map.get(key);
    var v2 = map.get(key, 'default');

    map.set(key, 'bar');

    var v3 = map.get(key);

    assert.equal(v, undefined);
    assert.equal(v2, 'default');
    assert.equal(v3, 'bar');

    assert.end();
})

test('weakMap does not work with string keys', function (assert) {
    var map = weakMap();

    assert.throws(function () {
        map.get('foo')
    }, /Key must be object/)

    assert.end()
})

test('weakMap set returns self', function (assert) {
    var map = weakMap();

    assert.equal(map.set({}, 'bar'), map);

    assert.end();
})

test('weakMap has()', function (assert) {
    var map = weakMap()

    var key = {}
    var key2 = {}

    var bool = map.has(key);
    var bool2 = map.has(key2)

    map.set(key, 'foobar')

    var bool3 = map.has(key)
    var bool4 = map.has(key2)

    assert.equal(bool, false)
    assert.equal(bool2, false)
    assert.equal(bool3, true)
    assert.equal(bool4, false)

    assert.end()
});

test('weakMap delete()', function (assert) {
    var key = {}
    var map = weakMap()

    map.set(key, 'foo')

    var bool = map.has(key)
    var value = map.get(key)

    map.delete(key)

    var bool2 = map.has(key)
    var value2 = map.get(key)

    assert.equal(bool, true)
    assert.equal(value, 'foo')

    assert.equal(bool2, false)
    assert.equal(value2, undefined)

    assert.end()
})
