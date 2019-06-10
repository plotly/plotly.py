// rollup.config.js
import commonjs from 'rollup-plugin-commonjs'
import babel from 'rollup-plugin-babel'
import tr from 'rollup-plugin-browserify-transform'
import glslify from 'glslify'
import resolve from 'rollup-plugin-node-resolve'

export default {
  input: 'index.js',
  output: {
    file: 'bundle.js',
    format: 'cjs'
  },
  plugins: [
    tr(glslify),
    resolve(),
    commonjs({
      sourceMap: false,
      include: ['index.js', 'scatter.js'],
      ignore: [
        'object-assign',
        'color-normalize',
        'array-bounds',
        'color-id',
        'point-cluster',
        'object-assign',
        'glslify',
        'pick-by-alias',
        'update-diff',
        'flatten-vertex-data',
        'is-iexplorer',
        'to-float32',
        'parse-rect'
      ]
    }),
    babel({
      'presets': ['@babel/preset-env']
    })
  ]
};
