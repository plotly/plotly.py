# gamma

[gamma function](http://en.wikipedia.org/wiki/Gamma_function)
in javascript using the
[lanczos approximation](http://en.wikipedia.org/wiki/Lanczos_approximation)
for small values and the 
[spouge approximation](https://en.wikipedia.org/wiki/Spouge's_approximation) for
larger values

[![browser support](http://ci.testling.com/substack/gamma.js.png)](http://ci.testling.com/substack/gamma.js)

[![build status](https://secure.travis-ci.org/substack/gamma.js.png)](http://travis-ci.org/substack/gamma.js)

# example

```
> var gamma = require('gamma')
> gamma(5)
23.999999999999996
> gamma(1.6)
0.8935153492876909
```

# methods

var gamma = require('gamma')

## gamma(z)

Return the gamma function over `z`. Complex numbers aren't supported, only reals.

## gamma.log(z)

Return the natural log of the gamma function for `z`.

This function is used internally by the spouge approximation to compute large
values.

# install

With [npm](http://npmjs.org) do:

```
npm install gamma
```

# kudos

Implementation transliterated from the python script on the wikipedia entry for
the
[lanczos approximation](http://en.wikipedia.org/wiki/Lanczos_approximation).

Spouge approximation from [Niggler](https://github.com/Niggler).

# license

MIT
