
/**
 * Module dependencies.
 */

var duplexer = require('duplexer2');
var Stream = require('stream');

/**
 * Slice reference.
 */

var slice = [].slice;

/**
 * Duplexer options.
 */

var opts = {
  bubbleErrors: false,
  objectMode: true
};

/**
 * Expose `pipe`.
 */

module.exports = pipe;

/**
 * Pipe.
 *
 * @param streams Array[Stream,...]
 * @param cb [Function]
 * @return {Stream}
 * @api public
 */

function pipe(streams, cb){
  if (!Array.isArray(streams)) {
    streams = slice.call(arguments);
    cb = null;
  }

  if ('function' == typeof streams[streams.length - 1]) {
    cb = streams.splice(-1)[0];
  }
  var first = streams[0];
  var last = streams[streams.length - 1];
  var ret;

  if (!first) {
    if (cb) process.nextTick(cb);
    return new Stream;
  }
  
  if (first.writable && last.readable) ret = duplexer(opts, first, last);
  else if (streams.length == 1) ret = streams[0];
  else if (first.writable) ret = first;
  else if (last.readable) ret = last;
  else ret = new Stream;
  
  streams.forEach(function(stream, i){
    var next = streams[i+1];
    if (next) stream.pipe(next);
    if (stream != ret) stream.on('error', ret.emit.bind(ret, 'error'));
  });

  if (cb) {
    var ended = false;
    ret.on('error', end);
    last.on('finish', end);
    last.on('close', end);
    function end(err){
      if (ended) return;
      ended = true;
      cb(err);
    }
  }

  return ret;
}

