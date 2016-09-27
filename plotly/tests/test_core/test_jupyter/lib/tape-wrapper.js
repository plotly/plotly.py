'use strict';

var test = require('tape');
var xhr = require('xhr');
var domready = require('domready');

var cnt = 0;
var noop = function() {};

var post = function(query, data) {
    var opts = data ? { body: data } : {};
    xhr.post('/?' + query + '&' + (cnt++), opts, noop);
};

var ws = test.createStream();

ws.on('data', function(data) {
    post('data', data)
});

test.onFinish(function() {
    post('done');
});

test('should not crash browser', function(t) {
    t.plan(1);

    domready(function() {
        t.pass('domready');
    });
});

module.exports = test;
