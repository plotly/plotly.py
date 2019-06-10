import cleanup from 'rollup-plugin-cleanup';

export default {
    entry: 'src/mapbox-build.js',
    dest: 'dist/gl-matrix.js',
    format: 'umd',
    moduleName: 'glMatrix',
    plugins: [cleanup()]
};
