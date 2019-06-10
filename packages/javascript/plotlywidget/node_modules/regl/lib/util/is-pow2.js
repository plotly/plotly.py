module.exports = function (v) {
  return !(v & (v - 1)) && (!!v)
}
