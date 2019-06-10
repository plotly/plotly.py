cwise-compiler
==============
Just the compiler from cwise.  You can call this directly if you know what you are doing and want to skip calling cwise-parser and including esprima.  This is only recommended in extreme cases though.  Otherwise you should stick to the default interface in cwise and not mess around with this craziness.

[![build status](https://secure.travis-ci.org/scijs/cwise-compiler.png)](http://travis-ci.org/scijs/cwise-compiler)

# Install
Install using [npm](https://www.npmjs.com/):

    npm install cwise-compiler

# API
#### `require("cwise-compiler")(procedure)`
Compiles a cwise procedure for the given procedure.  The object procedure must have the following fields:

* `args` An array of argument types (as in cwise)
* `pre` A parsed pre function
* `body` A parsed body function
* `post` A parsed post function
* `funcName` Name of the function
* `blockSize` Block size to generate
* `debug` Debug mode flag

# License
(c) 2013 Mikola Lysenko. MIT License
