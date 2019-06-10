# glsl-resolve [![Flattr this!](https://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=hughskennedy&url=http://github.com/hughsk/glsl-resolve&title=glsl-resolve&description=hughsk/glsl-resolve%20on%20GitHub&language=en_GB&tags=flattr,github,javascript&category=software)[![experimental](http://hughsk.github.io/stability-badges/dist/experimental.svg)](http://github.com/hughsk/stability-badges) #

A wrapper for the [resolve](https://github.com/substack/node-resolve) module
that targets GLSL shaders instead of JavaScript.

## Usage ##

[![glsl-resolve](https://nodei.co/npm/glsl-resolve.png?mini=true)](https://nodei.co/npm/glsl-resolve)

The API is equivalent to *resolve* for both `resolve.async` and `resolve.sync`,
with the following exceptions:

* Node's core modules are excluded.

* The "main" file for a module is looked for first in a package.json's `glslify`
  property, then if `main` isn't a JavaScript file it'll look there too.
  Otherwise, it will default to trying `index.glsl`.

* Listed in order of priority, the following extensions are resolved instead of
  `.js` and `.json`:

  * `.glsl`
  * `.vert`
  * `.frag`
  * `.geom`
  * `.vs`
  * `.fs`
  * `.gs`
  * `.vsh`
  * `.fsh`
  * `.gsh`
  * `.vshader`
  * `.fshader`
  * `.gshader`

## License ##

MIT. See [LICENSE.md](http://github.com/hughsk/glsl-resolve/blob/master/LICENSE.md) for details.
