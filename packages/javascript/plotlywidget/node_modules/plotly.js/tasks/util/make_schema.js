var fs = require('fs');
var path = require('path');
var JSDOM = require('jsdom').JSDOM;

module.exports = function makeSchema(plotlyPath, schemaPath) {
    return function() {
        var plotlyjsCode = fs.readFileSync(plotlyPath, 'utf-8');

        var w = new JSDOM('', {runScripts: 'dangerously'}).window;

        // jsdom by itself doesn't support getContext, and adding the npm canvas
        // package is annoying and platform-dependent.
        // see https://github.com/tmpvar/jsdom/issues/1782
        w.HTMLCanvasElement.prototype.getContext = function() { return null; };
        w.URL.createObjectURL = function() { return null; };

        w.eval(plotlyjsCode);

        var plotSchema = w.Plotly.PlotSchema.get();
        var plotSchemaStr = JSON.stringify(plotSchema, null, 4);
        fs.writeFileSync(schemaPath, plotSchemaStr);

        console.log('ok ' + path.basename(schemaPath));
    };
};
