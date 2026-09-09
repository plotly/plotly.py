module.exports = {
  // Note: This config has no effect on the lab extension functionality,
  // but it helps ensure that webpack uses the same module and chunk IDs
  // across platforms, which makes it easier to compare build artifacts.
  optimization: {
    moduleIds: 'natural',
    chunkIds: 'natural',
    realContentHash: true
  },
};
