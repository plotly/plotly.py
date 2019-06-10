var constants = require('./util/constants');
var common = require('./util/common');
var containerCommands = require('./util/container_commands');

var msg = [
    'Running image comparison tests using build/plotly.js from',
    common.getTimeLastModified(constants.pathToPlotlyBuild),
    '\n'
].join(' ');

var cmd = containerCommands.getRunCmd(
    process.env.CIRCLECI,
    'node test/image/compare_pixels_test.js ' + process.argv.slice(2).join(' ')
);

console.log(msg);
common.execCmd(cmd);
