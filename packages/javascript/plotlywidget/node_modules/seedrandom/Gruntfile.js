module.exports = function(grunt) {
  "use strict";

  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),
    bowercopy: {
      options: {
        clean: true
      },
      test: {
        options: {
          destPrefix: "test/lib"
        },
        files: {
          "qunit.js" : "qunit/qunit/qunit.js",
          "qunit.css" : "qunit/qunit/qunit.css",
          "require.js" : "requirejs/require.js"
        }
      }
    },
    uglify: {
      all: {
        files: {
          "<%= pkg.name %>.min.js": [ "<%= pkg.name %>.js" ],
          "lib/alea.min.js": [ "lib/alea.js" ],
          "lib/tychei.min.js": [ "lib/tychei.js" ],
          "lib/xor4096.min.js": [ "lib/xor4096.js" ],
          "lib/xorshift7.min.js": [ "lib/xorshift7.js" ],
          "lib/xorwow.min.js": [ "lib/xorwow.js" ],
          "lib/xor128.min.js": [ "lib/xor128.js" ]
        },
        options: {
          preserveComments: false,
          report: "min",
          output: {
            ascii_only: true
          }
        }
      }
    },
    qunit: {
      options: {
        noGlobals: true,
        httpBase: 'http://localhost:8192'
      },
      all: ["test/*.html"]
    },
    connect: {
      server: {
        options: {
          port: 8192,
          base: '.'
        }
      }
    },
    browserify: {
      test: {
        files: {
          'test/browserified.js': ['test/nodetest.js'],
        },
        options: {
          ignore: ['requirejs', 'process'],
          alias: {
            'assert': './test/qunitassert.js'
          }
        }
      }
    },
    mochacov: {
      options: {
        files: [
          'test/cryptotest.js',
          'test/nodetest.js',
          'test/prngtest.js'
       ]
      },
      coverage: {
        options: {
          coveralls: true
        }
      },
      test: {
        options: {
          reporter: 'dot'
        }
      }
    },
    release: {
      options: {
        bump: false
      }
    }
  });

  grunt.loadNpmTasks('grunt-bowercopy');
  grunt.loadNpmTasks('grunt-contrib-connect');
  grunt.loadNpmTasks('grunt-contrib-qunit');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-mocha-cov');
  grunt.loadNpmTasks('grunt-release');
  grunt.loadNpmTasks('grunt-browserify');

  grunt.registerTask("test",
      ["browserify", "connect", "qunit", "mochacov:test"]);
  grunt.registerTask("default", ["uglify", "test"]);
  grunt.registerTask("travis", ["default", "mochacov:coverage"]);
};

