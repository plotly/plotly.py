var test = require('./lib/tape-wrapper');

test('should have the correct number of script tags', function(t) {
    t.plan(1);

    var nodes = document.querySelectorAll('script');
    t.equal(nodes.length, 8);
});

test('should have one plotly.js graph', function(t) {
    t.plan(1);

    var nodes = document.querySelectorAll('.js-plotly-plot');
    t.equal(nodes.length, 1);
});
