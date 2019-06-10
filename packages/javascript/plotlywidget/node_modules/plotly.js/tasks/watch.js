var makeWatchifiedBundle = require('./util/watchified_bundle');
var noop = function() {};

// make a watchified bundle for plotly.js and run it!
var watchifiedBundle = makeWatchifiedBundle(noop);
watchifiedBundle();
