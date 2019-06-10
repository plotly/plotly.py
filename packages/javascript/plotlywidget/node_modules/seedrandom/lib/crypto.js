// mimic a subset of node's crypto API for the browser

function randomBytes(width) {
  var out = new Uint8Array(width);
  (global.crypto || global.msCrypto).getRandomValues(out);
  return out;
}

module.exports = {
  randomBytes: randomBytes
}
