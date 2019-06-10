'use strict'

var hasPassiveEvents = require('./')

console.log(hasPassiveEvents)

if (!process.browser && hasPassiveEvents) throw Error('Node should not have hover')
