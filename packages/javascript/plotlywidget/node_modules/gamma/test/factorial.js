var test = require('tape');
var gamma = require('../');

test('factorials', function (t) {
    // gamma(n) = (n - 1)!
    
    var facts = [];
    var f = 1;
    for (var i = 1; i < 12; i++) facts.push(f *= i);
    
    for (var n = 0; n < facts.length; n++) {
        var res = gamma(n + 2);
        t.equal(facts[n], Math.round(res * 1e6) / 1e6);
    }
    
    t.end();
});
