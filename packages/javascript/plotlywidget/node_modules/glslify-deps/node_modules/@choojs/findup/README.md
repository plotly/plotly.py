[![build status](https://secure.travis-ci.org/choojs/findup.png)](http://travis-ci.org/choojs/findup)
@choojs/findup
=======

> This is a fork of [Filirom1/findup](https://github.com/Filirom1/findup), pending [#16](https://github.com/Filirom1/findup/pull/16).

### Install

```sh
npm install -g @choojs/findup
```

### Usage

Find up a file in ancestor's dir


    .
    ├── config.json
    └── f
        └── e
            └── d
                └── c
                    ├── b
                    │   └── a
                    └── config.json

### Options

- `maxdepth`: (Number, default -1) How far to traverse before giving up. If maxdepth is `-1`, then there is no limit.

#### Async

findup(dir, fileName, options, callback)
findup(dir, iterator, options, callback) with `iterator(dir, cb)` where cb only accept `true` or `false`

```js
var findup = require('@choojs/findup');


findup(__dirname + '/f/e/d/c/b/a', 'config.json', function(err, dir){
  // if(e) e === new Error('not found')
  // dir === '/f/e/d/c'
});
```

or

```js
findup(__dirname + '/f/e/d/c/b/a', function(dir, cb){
  require('path').exists(dir + '/config.json', cb);
}, function(err, dir){
  // if(e) e === new Error('not found')
  // dir === '/f/e/d/c'
});
```

#### EventEmitter

findup(dir, fileName, options)

```js
var findup = require('@choojs/findup');
var fup = findup(__dirname + '/f/e/d/c/b/a', 'config.json');
```

findup(dir, iterator, options) with `iterator(dir, cb)` where cb only accept `true` or `false`

```js
var findup = require('@choojs/findup');
var fup = findup(__dirname + '/f/e/d/c/b/a', function(dir, cb){
  require('path').exists(dir + '/config.json', cb);
});
```

findup return an EventEmitter. 3 events are emitted: `found`, `error`, `end`

`found` event is emitted each time a file is found.

You can stop the traversing by calling `stop` manually.

```js
fup.on('found', function(dir){
  // dir === '/f/e/d/c'
  fup.stop();
});
```

`error` event is emitted when error happens

```js
fup.on('error', function(e){
  // if(e) e === new Error('not found')
});
```

`end` event is emitted at the end of the traversing or after `stop()` is
called.

```js
fup.on('end', function(){
  // happy end
});
```

#### Sync

findup(dir, fileName)
findup(dir, iteratorSync) with `iteratorSync` return `true` or `false`
```js
var findup = require('@choojs/findup');

try{
  var dir = findup.sync(__dirname + '/f/e/d/c/b/a', 'config.json'); // dir === '/f/e/d/c'
}catch(e){
  // if(e) e === new Error('not found')
}
```

#### CLI
```js
npm install -g @choojs/findup

$ cd test/fixture/f/e/d/c/b/a/
$ findup package.json
/root/findup/package.json
```

Usage

```
$ findup -h

Usage: findup [FILE]

    --name, -n       The name of the file to found
    --dir, -d        The directoy where we will start walking up    $PWD
    --help, -h       show usage                                     false
    --verbose, -v    print log                                      false
```

### LICENSE MIT

### Read the tests :)
