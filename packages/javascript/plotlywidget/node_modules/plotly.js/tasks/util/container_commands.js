var constants = require('./constants');

var containerCommands = {
    cdHome: 'cd ' + constants.testContainerHome,
    cpIndex: 'cp -f test/image/index.html ../server_app/index.html',
    injectEnv: [
        'sed -i',
        's/process.env.PLOTLY_MAPBOX_DEFAULT_ACCESS_TOKEN/\\\'' + constants.mapboxAccessToken + '\\\'/',
        '../server_app/main.js'
    ].join(' '),
    restart: 'supervisorctl restart nw1'
};

containerCommands.ping = [
    'wget',
    '--server-response --spider --tries=20 --retry-connrefused',
    constants.testContainerUrl + 'ping'
].join(' ');

containerCommands.setup = [
    containerCommands.cpIndex,
    containerCommands.injectEnv,
    containerCommands.restart,
    containerCommands.ping,
    'sleep 5'
].join(' && ');

containerCommands.dockerRun = [
    'docker run -d',
    '--name', constants.testContainerName,
    '-v', constants.pathToRoot + ':' + constants.testContainerHome,
    '-p', constants.testContainerPort + ':' + constants.testContainerPort,
    constants.testContainerImage
].join(' ');

containerCommands.getRunCmd = function(isCI, commands) {
    var _commands = Array.isArray(commands) ? commands.slice() : [commands];
    var cmd;

    if(isCI) {
        _commands = [containerCommands.ping].concat(_commands);
        cmd = getRunCI(_commands);
    } else {
        _commands = [containerCommands.setup].concat(_commands);
        cmd = getRunLocal(_commands);
    }

    return cmd;
};

function getRunLocal(commands) {
    commands = [containerCommands.cdHome].concat(commands);
    return [
        'docker exec -i',
        constants.testContainerName,
        '/bin/bash -c',
        '"' + commands.join(' && ') + '"'
    ].join(' ');
}

function getRunCI(commands) {
    commands = [containerCommands.cdHome].concat(commands);
    return commands.join(' && ');
}

module.exports = containerCommands;
