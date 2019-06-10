module.exports = function (obj) {
  return Object.keys(obj).map(function (key) { return obj[key] })
}
