var test = require('tape');
var gamma = require('../');

test('integrate', function (t) {
    // gamma(z) = integral(0, inf, e^(-t)*t^(z - 1))
    
    var zs = [ 0.84, 1.31, 2.54, 3.01, 5.2, 6.1 ];
    
    for (var i = 0; i < zs.length; i++) {
        // integration by rectangles
        var res = 0;
        var dx = 0.0001;
        for (var x = 0.000001; x < 40; x += dx) {
            res += Math.exp(-x) * Math.pow(x, zs[i] - 1) * dx;
        }
        
        t.equal(
            Math.round(res * 10) / 10,
            Math.round(gamma(zs[i]) * 10) / 10,
            'z = ' + zs[i]
        );
    }
    
    t.end();
});
