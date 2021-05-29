const path = require("path");
const version = require("./package.json").version;

// Custom webpack rules
const rules = [
  { test: /\.ts$/, loader: "ts-loader" },
  { test: /\.css$/, use: ["style-loader", "css-loader"] },
];

// Packages that shouldn't be bundled but loaded at runtime
const externals = ["@jupyter-widgets/base"];

const resolve = {
  extensions: [".webpack.js", ".web.js", ".ts", ".js"],
};

module.exports = [
  /**
   * Notebook extension
   *
   * This bundle only contains the part of the JavaScript that is run on load of
   * the notebook.
   */
  {
    entry: "./src/extension.ts",
    output: {
      filename: "index.js",
      path: path.resolve(
        __dirname,
        "..",
        "..",
        "python",
        "plotly",
        "jupyterlab_plotly",
        "nbextension"
      ),
      libraryTarget: "amd",
      publicPath: "",
    },
    module: {
      rules: rules,
    },
    externals,
    resolve,
  },

  /**
   * Embeddable jupyterlab-plotly bundle
   *
   * This bundle is almost identical to the notebook extension bundle. The only
   * difference is in the configuration of the webpack public path for the
   * static assets.
   *
   * The target bundle is always `dist/index.js`, which is the path required by
   * the custom widget embedder.
   */
  {
    entry: "./src/index.ts",
    output: {
      filename: "index.js",
      path: path.resolve(__dirname, "dist"),
      libraryTarget: "amd",
      library: "jupyterlab-plotly",
      publicPath: "https://unpkg.com/jupyterlab-plotly@" + version + "/dist/",
    },
    module: {
      rules: rules,
    },
    externals,
    resolve,
  },
];
