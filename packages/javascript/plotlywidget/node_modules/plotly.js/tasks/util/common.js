var fs = require('fs');
var exec = require('child_process').exec;
var falafel = require('falafel');

exports.execCmd = function(cmd, cb, errorCb) {
    cb = cb ? cb : function() {};
    errorCb = errorCb ? errorCb : function(err) { if(err) throw err; };

    exec(cmd, function(err) {
        errorCb(err);
        cb();
    })
    .stdout.pipe(process.stdout);
};

exports.writeFile = function(filePath, content, cb) {
    fs.writeFile(filePath, content, function(err) {
        if(err) throw err;
        if(cb) cb();
    });
};

exports.doesDirExist = function(dirPath) {
    try {
        if(fs.statSync(dirPath).isDirectory()) return true;
    } catch(e) {
        return false;
    }

    return false;
};

exports.doesFileExist = function(filePath) {
    try {
        if(fs.statSync(filePath).isFile()) return true;
    } catch(e) {
        return false;
    }

    return false;
};

exports.formatTime = function(date) {
    return [
        date.toLocaleDateString(),
        date.toLocaleTimeString()
    ].join(' ');
};

exports.getTimeLastModified = function(filePath) {
    if(!exports.doesFileExist(filePath)) {
        throw new Error(filePath + ' does not exist');
    }

    var stats = fs.statSync(filePath);
    var formattedTime = exports.formatTime(stats.mtime);

    return formattedTime;
};

exports.touch = function(filePath) {
    fs.closeSync(fs.openSync(filePath, 'w'));
};

exports.throwOnError = function(err) {
    if(err) throw err;
};

exports.findModuleList = function(pathToIndex) {
    var code = fs.readFileSync(pathToIndex, 'utf-8');
    // In v1.x, all partial bundles include the 'scatter' module
    var moduleList = ['scatter'];

    falafel(code, function(node) {
        if(
            node.type === 'Literal' &&
            node.parent &&
            node.parent.type === 'CallExpression' &&
            node.parent.callee &&
            node.parent.callee.type === 'Identifier' &&
            node.parent.callee.name === 'require' &&
            node.parent.parent &&
            node.parent.parent.type === 'ArrayExpression'
        ) {
            var moduleName = node.value.replace('./', '');
            moduleList.push(moduleName);
        }
    });

    return moduleList;
};

exports.formatEnumeration = function(list) {
    var len = list.length;

    return list.map(function(l, i) {
        var ending;

        if(i === len - 2) ending = ' and';
        else if(i < len - 1) ending = ',';
        else ending = '';

        return '`' + l + '`' + ending;
    }).join(' ');
};

exports.hasJasmineTestTag = function(node, tag) {
    var re = tag ?
        new RegExp('@' + tag + '\\s') :
        new RegExp('@' + '\\w');
    return re.test(node.source());
};

function isJasmineBase(block, node, tag) {
    return (
        node.type === 'Literal' &&
        node.parent &&
        node.parent.type === 'CallExpression' &&
        node.parent.callee &&
        node.parent.callee.type === 'Identifier' &&
        node.parent.callee.name === block &&
        (tag === undefined || exports.hasJasmineTestTag(node, tag))
    );
}

exports.isJasmineTestIt = function(node, tag) {
    return isJasmineBase('it', node, tag);
};

exports.isJasmineTestDescribe = function(node, tag) {
    return isJasmineBase('describe', node, tag);
};
