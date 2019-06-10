module.exports = function now() {
  var time = process.hrtime()
  return time[0] * 1e3 + time[1] / 1e6
}
