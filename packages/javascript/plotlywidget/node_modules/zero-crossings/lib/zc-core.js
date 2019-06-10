module.exports = require('cwise-compiler')({
    args: ['array', {
        offset: [1],
        array: 0
    }, 'scalar', 'scalar', 'index'],
    pre: {
        "body": "{}",
        "args": [],
        "thisVars": [],
        "localVars": []
    },
    post: {
        "body": "{}",
        "args": [],
        "thisVars": [],
        "localVars": []
    },
    body: {
        "body": "{\n        var _inline_1_da = _inline_1_arg0_ - _inline_1_arg3_\n        var _inline_1_db = _inline_1_arg1_ - _inline_1_arg3_\n        if((_inline_1_da >= 0) !== (_inline_1_db >= 0)) {\n          _inline_1_arg2_.push(_inline_1_arg4_[0] + 0.5 + 0.5 * (_inline_1_da + _inline_1_db) / (_inline_1_da - _inline_1_db))\n        }\n      }",
        "args": [{
            "name": "_inline_1_arg0_",
            "lvalue": false,
            "rvalue": true,
            "count": 1
        }, {
            "name": "_inline_1_arg1_",
            "lvalue": false,
            "rvalue": true,
            "count": 1
        }, {
            "name": "_inline_1_arg2_",
            "lvalue": false,
            "rvalue": true,
            "count": 1
        }, {
            "name": "_inline_1_arg3_",
            "lvalue": false,
            "rvalue": true,
            "count": 2
        }, {
            "name": "_inline_1_arg4_",
            "lvalue": false,
            "rvalue": true,
            "count": 1
        }],
        "thisVars": [],
        "localVars": ["_inline_1_da", "_inline_1_db"]
    },
    funcName: 'zeroCrossings'
})
