# ify-loader

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

[Webpack](https://github.com/webpack/webpack) loader to handle [browserify transforms](https://github.com/substack/browserify-handbook#browserifytransform-field) as intended.

## Usage

Install the loader using [npm](https://npmjs.com/):

``` glsl
npm install --save ify-loader
```

You can then update your `webpack.config.js` in a similar fashion to the following to add browserify transform support to your project's dependencies:

``` javascript
module.exports = {
  module: {
    loaders: [
      // This applies the loader to all of your dependencies,
      // and not any of the source files in your project:
      {
        test: /node_modules/,
        loader: 'ify-loader'
      }
    ]
  }
}
```

### Using transforms in your project

Note that you're also free to apply this loader to files in your own project. Include the following in your project's `webpack.config.js`:

``` javascript
module.exports = {
  module: {
    loaders: [
      // support local package.json browserify config
      {
        test: /\.js$/,
        loader: 'ify-loader',
        enforce: 'post'
      }
    ]
  }
}
```

Any browserify transforms you include in `package.json` will get picked up and applied this way:

``` json
{
  "name": "my-project",
  "dependencies": {
    "glslify": "5.0.0",
    "brfs": "1.4.2"
  },
  "browserify": {
    "transform": [
      "glslify",
      "brfs"
    ]
  }
}
```

## Why?

When given the choice, I lean more in favour of [browserify](http://browserify.org) for its simplicity and compatability with node.js — however from time to time I need to work on projects that use webpack. The thing I run into issues with most often when switching between the two is the difference in how webpack handles source transforms compared to browserify.

Webpack provides you with a "global" configuration where you specify how your project and its dependencies are transformed in a single place. Browserify, however, scopes transforms to the current package to avoid conflicts between different dependencies' sources using the  [`browserify.transform` property](https://github.com/substack/node-browserify#browserifytransform) in `package.json`.

There are pros and cons to both approaches — Webpack gives you more control, at the expense of having to configure each transform used in your dependency tree. Unlike [transform-loader](https://github.com/webpack/transform-loader), *ify-loader* will automatically determine which browserify transforms to apply to your dependencies for you the same way that browserify itself does, making the process a lot more bearable in complex projects!

## See Also

* [browserify](https://github.com/substack/node-browserify)
* [webpack](https://github.com/webpack/webpack)
* [transform-loader](https://github.com/webpack/transform-loader)

## License

MIT, see [LICENSE.md](http://github.com/hughsk/ify-loader/blob/master/LICENSE.md) for details.
