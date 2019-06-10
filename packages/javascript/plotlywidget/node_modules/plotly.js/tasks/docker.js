var constants = require('./util/constants');
var common = require('./util/common');
var containerCommands = require('./util/container_commands');

var isCI = process.env.CIRCLECI;
var arg = process.argv[2];

var msg, cmd, cb, errorCb;

switch(arg) {
    case 'pull':
        msg = 'Pulling latest docker image';
        cmd = 'docker pull ' + constants.testContainerImage;
        break;

    case 'run':
        msg = 'Booting up ' + constants.testContainerName + ' docker container';
        cmd = containerCommands.dockerRun;

        // if docker-run fails, try docker-start.
        errorCb = function(err) {
            if(err) common.execCmd('docker start ' + constants.testContainerName);
        };

        break;

    case 'setup':
        msg = 'Setting up ' + constants.testContainerName + ' docker container for testing';
        cmd = containerCommands.getRunCmd(isCI, containerCommands.setup);
        break;

    case 'stop':
        msg = 'Stopping ' + constants.testContainerName + ' docker container';
        cmd = 'docker stop ' + constants.testContainerName;
        break;

    case 'remove':
        msg = 'Removing ' + constants.testContainerName + ' docker container';
        cmd = 'docker rm ' + constants.testContainerName;
        break;

    default:
        console.log('Usage: pull, run, setup, stop, remove');
        process.exit(0);
        break;
}

console.log(msg);
common.execCmd(cmd, cb, errorCb);
