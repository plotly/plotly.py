'use strict'

var cmp = require('./cmp')

module.exports = equals

function equals(a, b) {
    return cmp(a, b) === 0
}
