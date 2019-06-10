module.exports = function atob(str) {
  return new Buffer(str, 'base64').toString('utf8')
}
