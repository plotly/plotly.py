var test = require('../../');

for (var i = 0; i < 11; i ++) {
    test(function (t) { t.ok(true, 'true is truthy'); t.end() });
}
