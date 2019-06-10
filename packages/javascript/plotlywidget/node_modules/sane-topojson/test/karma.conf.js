var isCI = process.env.CI

module.exports = function (config) {
  config.set({
    basePath: '.',

    files: [
      'https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.js',
      'test.js'
    ],

    frameworks: ['jasmine', 'browserify'],

    preprocessors: { 'test.js': ['browserify'] },

    browsers: ['Firefox'],

    autoWatch: !isCI,

    singleRun: isCI,

    browserNoActivityTimeout: 100000,

    browserify: {
      watch: true,
      debug: true
    }
  })
}
