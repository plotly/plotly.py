var crypto = require('crypto')
/* istanbul ignore next */
if (crypto && (!crypto.pbkdf2Sync || crypto.pbkdf2Sync.toString().indexOf('keylen, digest') === -1)) {
  exports.pbkdf2 = require('./lib/async')
  exports.pbkdf2Sync = require('./lib/sync')
} else {
  exports.pbkdf2Sync = crypto.pbkdf2Sync
  exports.pbkdf2 = crypto.pbkdf2
}
