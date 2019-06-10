var fs = require('fs');

var falafel = require('falafel');

var pkg = require('../../package.json');


module.exports = function updateVersion(pathToFile) {
    fs.readFile(pathToFile, 'utf-8', function(err, code) {
        var out = falafel(code, function(node) {
            if(isVersionNode(node)) node.update('\'' + pkg.version + '\'');
        });

        fs.writeFile(pathToFile, out, function(err) {
            if(err) throw err;
        });
    });
};

function isVersionNode(node) {
    return (
        node.type === 'Literal' &&
        node.parent &&
        node.parent.type === 'AssignmentExpression' &&
        node.parent.left &&
        node.parent.left.object &&
        node.parent.left.property &&
        node.parent.left.property.name === 'version'
    );
}
