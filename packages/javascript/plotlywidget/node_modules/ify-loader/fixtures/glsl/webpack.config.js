const path = require('path')

module.exports = {
  entry: './index.js',
  output: {
    path: __dirname,
    filename: 'bundle.js'
  },
  module: {
    rules: [{
      test: /\.js/,
      use: path.join(__dirname, '..', '..')
    }]
  }
}
