var fs = require('fs');
var path = require('path');

var through = require('through2');
var Readable = require('readable-stream').Readable;

var concat = require('concat-stream');
var duplexer = require('duplexer2');
var falafel = require('falafel');
var unparse = require('escodegen').generate;
var inspect = require('object-inspect');
var evaluate = require('static-eval');
var copy = require('shallow-copy');
var has = require('has');

module.exports = function parse (modules, opts) {
    if (!opts) opts = {};
    var vars = opts.vars || {};
    var varNames = opts.varNames || {};
    var varModules = opts.varModules || {};
    var skip = opts.skip || {};
    var skipOffset = opts.skipOffset || 0;
    var updates = [];
    
    var output = through();
    var body;
    return duplexer(concat(function (buf) {
        try {
            body = buf.toString('utf8').replace(/^#!/, '//#!');
            falafel(body, { ecmaVersion: 8 }, walk);
        }
        catch (err) { return error(err) }
        finish(body);
    }), output);
    
    function finish (src) {
        var pos = 0;
        src = String(src);
        
        (function next () {
            if (updates.length === 0) return done();
            var s = updates.shift();

            output.push(src.slice(pos, s.start));
            pos = s.start + s.offset;

            s.stream.pipe(output, { end: false });
            s.stream.on('end', next);
        })();
        
        function done () {
            output.push(src.slice(pos));
            output.push(null);
        }
    }
    
    function error (msg) {
        var err = typeof msg === 'string' ? new Error(msg) : msg;
        output.emit('error', err);
    }
    
    function walk (node) {
        var isreq = isRequire(node);
        var isreqm = false, isreqv = false, reqid;
        if (isreq) {
            reqid = node.arguments[0].value;
            isreqm = has(modules, reqid);
            isreqv = has(varModules, reqid);
        }
        
        if (isreqv && node.parent.type === 'VariableDeclarator'
        && node.parent.id.type === 'Identifier') {
            vars[node.parent.id.name] = varModules[reqid];
        }
        else if (isreqv && node.parent.type === 'AssignmentExpression'
        && node.parent.left.type === 'Identifier') {
            vars[node.parent.left.name] = varModules[reqid];
        }
        else if (isreqv && node.parent.type === 'MemberExpression'
        && isStaticProperty(node.parent.property)
        && node.parent.parent.type === 'VariableDeclarator'
        && node.parent.parent.id.type === 'Identifier') {
            var v = varModules[reqid][resolveProperty(node.parent.property)];
            vars[node.parent.parent.id.name] = v;
        }
        else if (isreqv && node.parent.type === 'MemberExpression'
        && node.parent.property.type === 'Identifier') {
            //vars[node.parent.parent.id.name] = varModules[reqid];
        }
        else if (isreqv && node.parent.type === 'CallExpression') {
            //
        }
        
        if (isreqm && node.parent.type === 'VariableDeclarator'
        && node.parent.id.type === 'Identifier') {
            varNames[node.parent.id.name] = reqid;
            var decs = node.parent.parent.declarations;
            var ix = decs.indexOf(node.parent);
            var dec;
            if (ix >= 0) {
                dec = decs[ix];
                decs.splice(ix, 1);
            }
            
            if (decs.length) {
                var src = unparse(node.parent.parent);
                updates.push({
                    start: node.parent.parent.start,
                    offset: node.parent.parent.end - node.parent.parent.start,
                    stream: st('var ')
                });
                decs.forEach(function (d, i) {
                    var key = (d.start + skipOffset)
                        + ',' + (d.end + skipOffset)
                    ;
                    skip[key] = true;
                    
                    var s = parse(modules, {
                        skip: skip,
                        skipOffset: skipOffset + (d.init ? d.init.start : 0),
                        vars: vars,
                        varNames: varNames
                    });
                    var up = {
                        start: node.parent.parent.end,
                        offset: 0,
                        stream: s
                    };
                    updates.push(up);
                    if (i < decs.length - 1) {
                        var comma;
                        if (i === ix - 1) {
                            comma = body.slice(d.end, dec.start);
                        }
                        else comma = body.slice(d.end, decs[i+1].start);
                        updates.push({
                            start: node.parent.parent.end,
                            offset: 0,
                            stream: st(comma)
                        });
                    }
                    else {
                        updates.push({
                            start: node.parent.parent.end,
                            offset: 0,
                            stream: st(';')
                        });
                    }
                    s.end(unparse(d));
                });
            }
            else {
                updates.push({
                    start: node.parent.parent.start,
                    offset: node.parent.parent.end - node.parent.parent.start,
                    stream: st()
                });
            }
        }
        else if (isreqm && node.parent.type === 'AssignmentExpression'
        && node.parent.left.type === 'Identifier') {
            varNames[node.parent.left.name] = reqid;
            var cur = node.parent.parent;
            if (cur.type === 'SequenceExpression') {
                var ex = cur.expressions;
                var ix = ex.indexOf(node.parent);
                if (ix >= 0) ex.splice(ix, 1);
                updates.push({
                    start: node.parent.parent.start,
                    offset: node.parent.parent.end - node.parent.parent.start,
                    stream: st(unparse(node.parent.parent))
                });
            }
            else {
                updates.push({
                    start: node.parent.parent.start,
                    offset: node.parent.parent.end - node.parent.parent.start,
                    stream: st()
                });
            }
        }
        else if (isreqm && node.parent.type === 'MemberExpression'
        && isStaticProperty(node.parent.property)
        && node.parent.parent.type === 'VariableDeclarator'
        && node.parent.parent.id.type === 'Identifier') {
            varNames[node.parent.parent.id.name] = [
                reqid, resolveProperty(node.parent.property)
            ];
            var decNode = node.parent.parent.parent;
            var decs = decNode.declarations;
            var ix = decs.indexOf(node.parent.parent);
            if (ix >= 0) decs.splice(ix, 1);
            
            updates.push({
                start: decNode.start,
                offset: decNode.end - decNode.start,
                stream: decs.length ? st(unparse(decNode)) : st()
            });
        }
        else if (isreqm && node.parent.type === 'MemberExpression'
        && isStaticProperty(node.parent.property)) {
            var name = resolveProperty(node.parent.property);
            var cur = copy(node.parent.parent);
            cur.callee = copy(node.parent.property);
            cur.callee.parent = cur;
            traverse(cur.callee, modules[reqid][name]);
        }
        else if (isreqm && node.parent.type === 'CallExpression') {
            var cur = copy(node.parent);
            var iname = Math.pow(16,8) * Math.random();
            cur.callee = {
                type: 'Identifier',
                name: '_' + Math.floor(iname).toString(16),
                parent: cur
            };
            traverse(cur.callee, modules[reqid]);
        }
        
        if (node.type === 'Identifier' && has(varNames, node.name)) {
            var vn = varNames[node.name];
            if (Array.isArray(vn)) {
                traverse(node, modules[vn[0]][vn[1]]);
            }
            else traverse(node, modules[vn]);
        }
    }
    
    function traverse (node, val) {
        for (var p = node; p; p = p.parent) {
            if (p.start === undefined || p.end === undefined) continue;
            var key = (p.start + skipOffset)
                + ',' + (p.end + skipOffset)
            ;
            if (skip[key]) {
                skip[key] = false;
                return;
            }
        }
        
        if (skip[key]) {
            skip[key] = false;
            return;
        }
        
        if (node.parent.type === 'CallExpression') {
            if (typeof val !== 'function') {
                return error(
                    'tried to statically call ' + inspect(val)
                    + ' as a function'
                );
            }

            var xvars = copy(vars);
            xvars[node.name] = val;

            var res = evaluate(node.parent, xvars);
            if (res !== undefined) {
                updates.push({
                    start: node.parent.start,
                    offset: node.parent.end - node.parent.start,
                    stream: isStream(res) ? wrapStream(res) : st(String(res))
                });
            }
        }
        else if (node.parent.type === 'MemberExpression') {
            if (!isStaticProperty(node.parent.property)) {
                return error(
                    'dynamic property in member expression: '
                    + node.parent.source()
                );
            }
            
            var cur = node.parent.parent;
            
            if (cur.type === 'MemberExpression') {
                cur = cur.parent;
                if (cur.type !== 'CallExpression'
                && cur.parent.type === 'CallExpression') {
                    cur = cur.parent;
                }
            }
            if (node.parent.type === 'MemberExpression'
            && (cur.type !== 'CallExpression'
            && cur.type !== 'MemberExpression')) {
                cur = node.parent;
            }
            
            var xvars = copy(vars);
            xvars[node.name] = val;
            
            var res = evaluate(cur, xvars);
            if (res !== undefined) {
                updates.push({
                    start: cur.start,
                    offset: cur.end - cur.start,
                    stream: isStream(res) ? wrapStream(res) : st(String(res))
                });
            }
        }
        else if (node.parent.type === 'UnaryExpression') {
            var xvars = copy(vars);
            xvars[node.name] = val;

            var res = evaluate(node.parent, xvars);
            if (res !== undefined) {
                updates.push({
                    start: node.parent.start,
                    offset: node.parent.end - node.parent.start,
                    stream: isStream(res) ? wrapStream(res) : st(String(res))
                });
            } else {
                output.emit('error', new Error(
                    'unsupported unary operator: ' + node.parent.operator
                ));
            }
        }
        else {
            output.emit('error', new Error(
                'unsupported type for static module: ' + node.parent.type
                + '\nat expression:\n\n  ' + unparse(node.parent) + '\n'
            ));
        }
    }
}

function isRequire (node) {
    var c = node.callee;
    return c
        && node.type === 'CallExpression'
        && c.type === 'Identifier'
        && c.name === 'require'
    ;
}

function isStream (s) {
    return s && typeof s === 'object' && typeof s.pipe === 'function';
}

function wrapStream (s) {
    if (typeof s.read === 'function') return s
    else return (new Readable).wrap(s)
}

function isStaticProperty(node) {
    return node.type === 'Identifier' || node.type === 'Literal';
}

function resolveProperty(node) {
    return node.type === 'Identifier' ? node.name : node.value;
}

function st (msg) {
    var r = new Readable;
    r._read = function () {};
    if (msg != null) r.push(msg);
    r.push(null);
    return r;
}
