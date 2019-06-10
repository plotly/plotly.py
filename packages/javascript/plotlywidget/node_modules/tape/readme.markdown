# tape

tap-producing test harness for node and browsers

[![browser support](https://ci.testling.com/substack/tape.png)](http://ci.testling.com/substack/tape)

[![build status](https://secure.travis-ci.org/substack/tape.svg?branch=master)](http://travis-ci.org/substack/tape)

![tape](https://web.archive.org/web/20170612184731if_/http://substack.net/images/tape_drive.png)

# example

``` js
var test = require('tape');

test('timing test', function (t) {
    t.plan(2);

    t.equal(typeof Date.now, 'function');
    var start = Date.now();

    setTimeout(function () {
        t.equal(Date.now() - start, 100);
    }, 100);
});
```

```
$ node example/timing.js
TAP version 13
# timing test
ok 1 should be equal
not ok 2 should be equal
  ---
    operator: equal
    expected: 100
    actual:   107
  ...

1..2
# tests 2
# pass  1
# fail  1
```

# usage

You always need to `require('tape')` in test files. You can run the tests by
usual node means (`require('test-file.js')` or `node test-file.js`). You can
also run tests using the `tape` binary to utilize globbing, on Windows for
example:

```sh
$ tape tests/**/*.js
```

`tape`'s arguments are passed to the
[`glob`](https://www.npmjs.com/package/glob) module. If you want `glob` to
perform the expansion on a system where the shell performs such expansion, quote
the arguments as necessary:

```sh
$ tape 'tests/**/*.js'
$ tape "tests/**/*.js"
```

## Preloading modules

Additionally, it is possible to make `tape` load one or more modules before running any tests, by using the `-r` or `--require` flag. Here's an example that loads [babel-register](http://babeljs.io/docs/usage/require/) before running any tests, to allow for JIT compilation:

```sh
$ tape -r babel-register tests/**/*.js
```

Depending on the module you're loading, you may be able to parameterize it using environment variables or auxiliary files. Babel, for instance, will load options from [`.babelrc`](http://babeljs.io/docs/usage/babelrc/) at runtime.

The `-r` flag behaves exactly like node's `require`, and uses the same module resolution algorithm. This means that if you need to load local modules, you have to prepend their path with `./` or `../` accordingly.

For example:

```sh
$ tape -r ./my/local/module tests/**/*.js
```

Please note that all modules loaded using the `-r` flag will run *before* any tests, regardless of when they are specified. For example, `tape -r a b -r c` will actually load `a` and `c` *before* loading `b`, since they are flagged as required modules.

# things that go well with tape

`tape` maintains a fairly minimal core. Additional features are usually added by using another module alongside `tape`.

## pretty reporters

The default TAP output is good for machines and humans that are robots.

If you want a more colorful / pretty output there are lots of modules on npm
that will output something pretty if you pipe TAP into them:

- [tap-spec](https://github.com/scottcorgan/tap-spec)
- [tap-dot](https://github.com/scottcorgan/tap-dot)
- [faucet](https://github.com/substack/faucet)
- [tap-bail](https://github.com/juliangruber/tap-bail)
- [tap-browser-color](https://github.com/kirbysayshi/tap-browser-color)
- [tap-json](https://github.com/gummesson/tap-json)
- [tap-min](https://github.com/derhuerst/tap-min)
- [tap-nyan](https://github.com/calvinmetcalf/tap-nyan)
- [tap-pessimist](https://www.npmjs.org/package/tap-pessimist)
- [tap-prettify](https://github.com/toolness/tap-prettify)
- [colortape](https://github.com/shuhei/colortape)
- [tap-xunit](https://github.com/aghassemi/tap-xunit)
- [tap-difflet](https://github.com/namuol/tap-difflet)
- [tape-dom](https://github.com/gritzko/tape-dom)
- [tap-diff](https://github.com/axross/tap-diff)
- [tap-notify](https://github.com/axross/tap-notify)
- [tap-summary](https://github.com/zoubin/tap-summary)
- [tap-markdown](https://github.com/Hypercubed/tap-markdown)
- [tap-html](https://github.com/gabrielcsapo/tap-html)
- [tap-react-browser](https://github.com/mcnuttandrew/tap-react-browser)
- [tap-junit](https://github.com/dhershman1/tap-junit)

To use them, try `node test/index.js | tap-spec` or pipe it into one
of the modules of your choice!

## uncaught exceptions

By default, uncaught exceptions in your tests will not be intercepted, and will cause `tape` to crash. If you find this behavior undesirable, use [`tape-catch`](https://github.com/michaelrhodes/tape-catch) to report any exceptions as TAP errors.

## other

- CoffeeScript support with https://www.npmjs.com/package/coffeetape
- Promise support with https://www.npmjs.com/package/blue-tape or https://www.npmjs.com/package/tape-promise
- ES6 support with https://www.npmjs.com/package/babel-tape-runner or https://www.npmjs.com/package/buble-tape-runner
- Different test syntax with https://github.com/pguth/flip-tape (warning: mutates String.prototype)
- Electron test runner with https://github.com/tundrax/electron-tap
- Concurrency support with https://github.com/imsnif/mixed-tape

# methods

The assertion methods in `tape` are heavily influenced or copied from the methods
in [node-tap](https://github.com/isaacs/node-tap).

```js
var test = require('tape')
```

## test([name], [opts], cb)

Create a new test with an optional `name` string and optional `opts` object.
`cb(t)` fires with the new test object `t` once all preceding tests have
finished. Tests execute serially.

Available `opts` options are:
- opts.skip = true/false. See test.skip.
- opts.timeout = 500. Set a timeout for the test, after which it will fail. See test.timeoutAfter.
- opts.objectPrintDepth = 5. Configure max depth of expected / actual object printing. Environmental variable `NODE_TAPE_OBJECT_PRINT_DEPTH` can set the desired default depth for all tests; locally-set values will take precedence.
- opts.todo = true/false. Test will be allowed to fail.

If you forget to `t.plan()` out how many assertions you are going to run and you
don't call `t.end()` explicitly, your test will hang.

## test.skip([name], [opts], cb)

Generate a new test that will be skipped over.

## test.onFinish(fn)

The onFinish hook will get invoked when ALL `tape` tests have finished
right before `tape` is about to print the test summary.

## test.onFailure(fn)

The onFailure hook will get invoked whenever any `tape` tests has failed.

## t.plan(n)

Declare that `n` assertions should be run. `t.end()` will be called
automatically after the `n`th assertion. If there are any more assertions after
the `n`th, or after `t.end()` is called, they will generate errors.

## t.end(err)

Declare the end of a test explicitly. If `err` is passed in `t.end` will assert
that it is falsey.

## t.fail(msg)

Generate a failing assertion with a message `msg`.

## t.pass(msg)

Generate a passing assertion with a message `msg`.

## t.timeoutAfter(ms)

Automatically timeout the test after X ms.

## t.skip(msg)

Generate an assertion that will be skipped over.

## t.ok(value, msg)

Assert that `value` is truthy with an optional description of the assertion `msg`.

Aliases: `t.true()`, `t.assert()`

## t.notOk(value, msg)

Assert that `value` is falsy with an optional description of the assertion `msg`.

Aliases: `t.false()`, `t.notok()`

## t.error(err, msg)

Assert that `err` is falsy. If `err` is non-falsy, use its `err.message` as the
description message.

Aliases: `t.ifError()`, `t.ifErr()`, `t.iferror()`

## t.equal(actual, expected, msg)

Assert that `actual === expected` with an optional description of the assertion `msg`.

Aliases: `t.equals()`, `t.isEqual()`, `t.is()`, `t.strictEqual()`,
`t.strictEquals()`

## t.notEqual(actual, expected, msg)

Assert that `actual !== expected` with an optional description of the assertion `msg`.

Aliases: `t.notEquals()`, `t.notStrictEqual()`, `t.notStrictEquals()`,
`t.isNotEqual()`, `t.isNot()`, `t.not()`, `t.doesNotEqual()`, `t.isInequal()`

## t.deepEqual(actual, expected, msg)

Assert that `actual` and `expected` have the same structure and nested values using
[node's deepEqual() algorithm](https://github.com/substack/node-deep-equal)
with strict comparisons (`===`) on leaf nodes and an optional description of the assertion `msg`.

Aliases: `t.deepEquals()`, `t.isEquivalent()`, `t.same()`

## t.notDeepEqual(actual, expected, msg)

Assert that `actual` and `expected` do not have the same structure and nested values using
[node's deepEqual() algorithm](https://github.com/substack/node-deep-equal)
with strict comparisons (`===`) on leaf nodes and an optional description of the assertion `msg`.

Aliases: `t.notDeepEquals`, `t.notEquivalent()`, `t.notDeeply()`, `t.notSame()`,
`t.isNotDeepEqual()`, `t.isNotDeeply()`, `t.isNotEquivalent()`,
`t.isInequivalent()`

## t.deepLooseEqual(actual, expected, msg)

Assert that `actual` and `expected` have the same structure and nested values using
[node's deepEqual() algorithm](https://github.com/substack/node-deep-equal)
with loose comparisons (`==`) on leaf nodes and an optional description of the assertion `msg`.

Aliases: `t.looseEqual()`, `t.looseEquals()`

## t.notDeepLooseEqual(actual, expected, msg)

Assert that `actual` and `expected` do not have the same structure and nested values using
[node's deepEqual() algorithm](https://github.com/substack/node-deep-equal)
with loose comparisons (`==`) on leaf nodes and an optional description of the assertion `msg`.

Aliases: `t.notLooseEqual()`, `t.notLooseEquals()`

## t.throws(fn, expected, msg)

Assert that the function call `fn()` throws an exception. `expected`, if present, must be a `RegExp` or `Function`. The `RegExp` matches the string representation of the exception, as generated by `err.toString()`. The `Function` is the exception thrown (e.g. `Error`). `msg` is an optional description of the assertion.

## t.doesNotThrow(fn, expected, msg)

Assert that the function call `fn()` does not throw an exception. `expected`, if present, limits what should not be thrown. For example, set `expected` to `/user/` to fail the test only if the string representation of the exception contains the word `user`. Any other exception would pass the test. If `expected` is omitted, any exception will fail the test. `msg` is an optional description of the assertion.

## t.test(name, [opts], cb)

Create a subtest with a new test handle `st` from `cb(st)` inside the current
test `t`. `cb(st)` will only fire when `t` finishes. Additional tests queued up
after `t` will not be run until all subtests finish.

You may pass the same options that [`test()`](#testname-opts-cb) accepts.

## t.comment(message)

Print a message without breaking the tap output. (Useful when using e.g. `tap-colorize` where output is buffered & `console.log` will print in incorrect order vis-a-vis tap output.)

## var htest = test.createHarness()

Create a new test harness instance, which is a function like `test()`, but with
a new pending stack and test state.

By default the TAP output goes to `console.log()`. You can pipe the output to
someplace else if you `htest.createStream().pipe()` to a destination stream on
the first tick.

## test.only([name], [opts], cb)

Like `test([name], [opts], cb)` except if you use `.only` this is the only test case
that will run for the entire process, all other test cases using `tape` will
be ignored.

## var stream = test.createStream(opts)

Create a stream of output, bypassing the default output stream that writes
messages to `console.log()`. By default `stream` will be a text stream of TAP
output, but you can get an object stream instead by setting `opts.objectMode` to
`true`.

### tap stream reporter

You can create your own custom test reporter using this `createStream()` api:

``` js
var test = require('tape');
var path = require('path');

test.createStream().pipe(process.stdout);

process.argv.slice(2).forEach(function (file) {
    require(path.resolve(file));
});
```

You could substitute `process.stdout` for whatever other output stream you want,
like a network connection or a file.

Pass in test files to run as arguments:

```sh
$ node tap.js test/x.js test/y.js
TAP version 13
# (anonymous)
not ok 1 should be equal
  ---
    operator: equal
    expected: "boop"
    actual:   "beep"
  ...
# (anonymous)
ok 2 should be equal
ok 3 (unnamed assert)
# wheee
ok 4 (unnamed assert)

1..4
# tests 4
# pass  3
# fail  1
```

### object stream reporter

Here's how you can render an object stream instead of TAP:

``` js
var test = require('tape');
var path = require('path');

test.createStream({ objectMode: true }).on('data', function (row) {
    console.log(JSON.stringify(row))
});

process.argv.slice(2).forEach(function (file) {
    require(path.resolve(file));
});
```

The output for this runner is:

```sh
$ node object.js test/x.js test/y.js
{"type":"test","name":"(anonymous)","id":0}
{"id":0,"ok":false,"name":"should be equal","operator":"equal","actual":"beep","expected":"boop","error":{},"test":0,"type":"assert"}
{"type":"end","test":0}
{"type":"test","name":"(anonymous)","id":1}
{"id":0,"ok":true,"name":"should be equal","operator":"equal","actual":2,"expected":2,"test":1,"type":"assert"}
{"id":1,"ok":true,"name":"(unnamed assert)","operator":"ok","actual":true,"expected":true,"test":1,"type":"assert"}
{"type":"end","test":1}
{"type":"test","name":"wheee","id":2}
{"id":0,"ok":true,"name":"(unnamed assert)","operator":"ok","actual":true,"expected":true,"test":2,"type":"assert"}
{"type":"end","test":2}
```

# install

With [npm](https://npmjs.org) do:

```sh
npm install tape --save-dev
```

# license

MIT
