# Building plotly.js

The easiest way to bundle plotly.js into your application is to use one of the distributed plotly.js packages on npm. These distributed packages should just work with **any** build framework. That said, if you're looking to save a few bytes, read the section below corresponding to your building framework.

## Webpack

For plotly.js to build with Webpack you will need to install [ify-loader@v1.1.0+](https://github.com/hughsk/ify-loader) and add it to your `webpack.config.json`. This adds Browserify transform compatibility to Webpack which is necessary for some plotly.js dependencies.

A repo that demonstrates how to build plotly.js with Webpack can be found [here](https://github.com/plotly/plotly-webpack). In short add `ify-loader` to the `module` section in your `webpack.config.js`:

```js
...
    module: {
        rules: [
            {
                test: /\.js$/,
                loader: 'ify-loader'
            }
        ]
    },
...
```

## Browserify

Given source file:

```js
// file: index.js

var Plotly = require('plotly.js');

// ....
```

then simply run,


```
browserify index.js > bundle.js
```

## Angular CLI

Currently Angular CLI uses Webpack under the hood to bundle and build your Angular application.
Sadly it doesn't allow you to override its Webpack config in order to add the plugin mentioned in the [Webpack](#webpack) section.
Without this plugin your build will fail when it tries to build glslify for WebGL plots.

Currently 2 solutions exists to circumvent this issue:

1) If you need to use WebGL plots, you can create a Webpack config from your Angular CLI project with [ng eject](https://github.com/angular/angular-cli/wiki/eject). This will allow you to follow the instructions regarding Webpack.
2) If you don't need to use WebGL plots, you can make a custom build containing only the required modules for your plots. The clean way to do it with Angular CLI is not the method described in the [Modules](https://github.com/plotly/plotly.js/blob/master/README.md#modules) section of the README but the following:

```typescript
// in the Component you want to create a graph
import * as Plotly from 'plotly.js';
```

```json
// in src/tsconfig.app.json
// List here the modules you want to import
// this example is for scatter plots
{
    "compilerOptions": {
        "paths": {
            "plotly.js": [
                "../node_modules/plotly.js/lib/core.js",
                "../node_modules/plotly.js/lib/scatter.js"
            ]
        }
    }
}
```
