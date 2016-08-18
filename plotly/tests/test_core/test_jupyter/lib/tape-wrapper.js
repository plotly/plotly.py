var test = require('tape');
var xhr = require('xhr');

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

module.exports = test;
