# shuffle-seed [![npm][npm-img]][npm-url] [![travis][travis-img]][travis-url] ![filesize][file-size-img]

[npm-img]: https://img.shields.io/npm/v/shuffle-seed.svg?style=flat-square
[npm-url]: https://npmjs.org/package/shuffle-seed
[travis-img]: https://img.shields.io/travis/webcaetano/shuffle-seed.svg?style=flat-square
[travis-url]: https://travis-ci.org/webcaetano/shuffle-seed
[file-size-img]: https://badge-size.herokuapp.com/webcaetano/shuffle-seed/master/shuffle-seed.min.js.svg?style=flat-square


Nodejs module to Shuffle an Array with seed :seedling:


Array Shuffle Seed based on module [davidbau/seedrandom](https://github.com/davidbau/seedrandom)

## Installation 

```
npm install shuffle-seed
```

## Usage :

```javascript
var shuffleSeed = require('shuffle-seed');
var a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
var resp = shuffleSeed.shuffle(a,"Kappa");
// result always will be [f','y','p','i','r','v','a','x','q','e','c','b','n','j','t','z','o','l','w','m','k','g','h','u','d','s']

shuffleSeed.unshuffle(resp,"Kappa");
// result ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
```


[![npm](https://nodei.co/npm/shuffle-seed.png?downloads=true&downloadRank=true&stars=true)](https://www.npmjs.com/package/shuffle-seed)

-------------------

The MIT [License](https://raw.githubusercontent.com/webcaetano/shuffle-seed/master/LICENSE)
