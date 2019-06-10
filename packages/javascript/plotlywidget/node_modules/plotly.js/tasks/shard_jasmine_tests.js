var fs = require('fs');
var path = require('path');

var falafel = require('falafel');
var glob = require('glob');
var minimist = require('minimist');

var pathToJasmineTests = require('./util/constants').pathToJasmineTests;
var isJasmineTestIt = require('./util/common').isJasmineTestIt;

var argv = minimist(process.argv.slice(2), {
    string: ['tag', 'limit'],
    alias: {
        tag: ['t'],
        limit: ['l'],
    },
    default: {
        limit: 20
    }
});

var tag = argv.tag;
var limit = argv.limit;

glob(path.join(pathToJasmineTests, '*.js'), function(err, files) {
    if(err) throw err;

    var file2cnt = {};

    files.forEach(function(file) {
        var code = fs.readFileSync(file, 'utf-8');
        var bn = path.basename(file);

        falafel(code, function(node) {
            if(isJasmineTestIt(node, tag)) {
                if(file2cnt[bn]) {
                    file2cnt[bn]++;
                } else {
                    file2cnt[bn] = 1;
                }
            }
        });
    });

    var ranking = Object.keys(file2cnt);
    var runs = [];

    // if 'it' count in file greater than threshold,
    // run only this file separately,
    // don't try to shard within file
    Object.keys(file2cnt).forEach(function(f) {
        if(file2cnt[f] > limit) {
            runs.push(f);
            ranking.splice(ranking.indexOf(f), 1);
        }
    });

    // sort ranking in decreasing order
    ranking.sort(function(a, b) { return file2cnt[b] - file2cnt[a]; });

    var runi;
    var cnt;

    function newRun() {
        var r0 = ranking[0];
        runi = [r0];
        cnt = file2cnt[r0];
        ranking.shift();
    }

    function concat() {
        runs.push(runi.join(','));
    }

    // try to match files with many tests with files not-that-many,
    // by matching first rank with one or multiple trailing ranks.
    newRun();
    while(ranking.length) {
        var rn = ranking[ranking.length - 1];

        if((cnt + file2cnt[rn]) > limit) {
            concat();
            newRun();
        } else {
            runi.push(rn);
            cnt += file2cnt[rn];
            ranking.pop();
        }
    }
    concat();

    // print result to stdout
    console.log(runs.join('\n'));
});
