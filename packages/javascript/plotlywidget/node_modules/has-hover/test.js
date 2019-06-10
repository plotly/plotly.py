'use strict'

var hasHover = require('./')

console.log(hasHover)

if (!process.browser && hasHover) throw Error('Node should not have hover')
