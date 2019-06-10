var path = require('path');
var exec = require('child_process').exec;
var glob = require('glob');
var runSeries = require('run-series');

var constants = require('./util/constants');
var pathToJasmineBundleTests = constants.pathToJasmineBundleTests;

/**
 * Run all jasmine 'bundle' test in series
 *
 * To run specific bundle tests, use
 *
 * $ npm run test-jasmine -- --bundleTest=<name-of-suite>
 */
glob(pathToJasmineBundleTests + '/*.js', function(err, files) {
    var tasks = files.map(function(file) {
        return function(cb) {
            var cmd = [
                'karma', 'start',
                path.join(constants.pathToRoot, 'test', 'jasmine', 'karma.conf.js'),
                '--bundleTest=' + path.basename(file),
                '--nowatch'
            ].join(' ');

            console.log('Running: ' + cmd);

            exec(cmd, function(err) {
                cb(null, err);
            }).stdout.pipe(process.stdout);
        };
    });

    var mathjaxTestFirefox = function(cb) {
        var cmd = [
            'karma', 'start',
            path.join(constants.pathToRoot, 'test', 'jasmine', 'karma.conf.js'),
            '--FF',
            '--bundleTest=mathjax',
            '--nowatch'
        ].join(' ');

        console.log('Running: ' + cmd);

        exec(cmd, function(err) {
            cb(null, err);
        }).stdout.pipe(process.stdout);
    };
    tasks.push(mathjaxTestFirefox);

    runSeries(tasks, function(err, results) {
        if(err) throw err;

        var failed = results.filter(function(r) { return r; });

        if(failed.length) {
            console.log('\ntest-bundle summary:');
            failed.forEach(function(r) { console.warn('- ' + r.cmd + ' failed'); });
            console.log('');
            process.exit(1);
        }
    });
});
