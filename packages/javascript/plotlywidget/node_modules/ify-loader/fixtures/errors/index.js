const fs = require('fs')

console.log(fs.readFileSync(__dirname + '/package.json', 'utf8'))
