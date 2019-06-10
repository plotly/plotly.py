var fs = require('fs');


module.exports = function pullCSS(data, pathOut) {
    var rules = {};

    data.split(/\s*\}\s*/).forEach(function(chunk) {
        if(!chunk) return;

        var parts = chunk.split(/\s*\{\s*/);
        var selectorList = parts[0];
        var rule = parts[1];

        // take off ".js-plotly-plot .plotly", which should be on every selector
        selectorList.split(/,\s*/).forEach(function(selector) {
            if(!selector.match(/^([\.]js-plotly-plot [\.]plotly|[\.]plotly-notifier)/)) {
                throw new Error('all plotlyjs-style selectors must start ' +
                    '.js-plotly-plot .plotly or .plotly-notifier\n' +
                    'found: ' + selectorList);
            }
        });

        selectorList = selectorList
            .replace(/[\.]js-plotly-plot [\.]plotly/g, 'X')
            .replace(/[\.]plotly-notifier/g, 'Y');

        // take out newlines in rule, and make sure it ends in a semicolon
        rule = rule.replace(/;\s*/g, ';').replace(/;?\s*$/, ';');

        // omit blank rules (why do we get these occasionally?)
        if(rule.match(/^[\s;]*$/)) return;

        rules[selectorList] = rules[selectorList] || '' + rule;
    });

    var rulesStr = JSON.stringify(rules, null, 4).replace(/\"(\w+)\":/g, '$1:');

    var outStr = [
        '\'use strict\';',
        '',
        'var Lib = require(\'../src/lib\');',
        'var rules = ' + rulesStr + ';',
        '',
        'for(var selector in rules) {',
        '    var fullSelector = selector.replace(/^,/,\' ,\')',
        '        .replace(/X/g, \'.js-plotly-plot .plotly\')',
        '        .replace(/Y/g, \'.plotly-notifier\');',
        '    Lib.addStyleRule(fullSelector, rules[selector]);',
        '}',
        ''
    ].join('\n');

    fs.writeFile(pathOut, outStr, function(err) {
        if(err) throw err;
    });
};
