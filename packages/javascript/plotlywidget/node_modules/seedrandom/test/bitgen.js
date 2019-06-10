#!/usr/bin/env node
var seedrandom = require('../seedrandom');

// process.on('SIGPIPE', process.exit);
function epipeBomb(stream, callback) {
  if (stream == null) stream = process.stdout;
  if (callback == null) callback = process.exit;

  function epipeFilter(err) {
    if (err.code === 'EPIPE') return callback();

    // If there's more than one error handler (ie, us),
    // then the error won't be bubbled up anyway
    if (stream.listeners('error').length <= 1) {
      stream.removeAllListeners();    // Pretend we were never here
      stream.emit('error', err);      // Then emit as if we were never here
      stream.on('error', epipeFilter);// Reattach, ready for the next error!
    }
  }

  stream.on('error', epipeFilter);
}

epipeBomb();

var bufsize = 1024 * 256,
    buf = new Buffer(bufsize * 4),
    prng = seedrandom(0),
    count = parseInt(process.argv[2]) || Infinity;
function dowrite() {
  while (count > 0) {
    for (var j = 0; j < bufsize; ++j) {
      buf.writeUInt32BE(Math.floor(
          prng() * 256 * 256 * 256 * 256
      ), j * 4);
    }
    count -= bufsize * 32;
    if (!process.stdout.write(buf)) {
      process.stdout.once('drain', function() { setTimeout(dowrite, 0) });
      return;
    }
  }
}

dowrite();
