/**
* Copyright 2012-2019, Plotly, Inc.
* All rights reserved.
*
* This source code is licensed under the MIT license found in the
* LICENSE file in the root directory of this source tree.
*/

'use strict';

// Modified from https://github.com/ArthurClemens/Javascript-Undo-Manager
// Copyright (c) 2010-2013 Arthur Clemens, arthur@visiblearea.com
module.exports = function UndoManager() {
    var undoCommands = [];
    var index = -1;
    var isExecuting = false;
    var callback;

    function execute(command, action) {
        if(!command) return this;

        isExecuting = true;
        command[action]();
        isExecuting = false;

        return this;
    }

    return {
        add: function(command) {
            if(isExecuting) return this;
            undoCommands.splice(index + 1, undoCommands.length - index);
            undoCommands.push(command);
            index = undoCommands.length - 1;
            return this;
        },
        setCallback: function(callbackFunc) { callback = callbackFunc; },
        undo: function() {
            var command = undoCommands[index];
            if(!command) return this;
            execute(command, 'undo');
            index -= 1;
            if(callback) callback(command.undo);
            return this;
        },
        redo: function() {
            var command = undoCommands[index + 1];
            if(!command) return this;
            execute(command, 'redo');
            index += 1;
            if(callback) callback(command.redo);
            return this;
        },
        clear: function() {
            undoCommands = [];
            index = -1;
        },
        hasUndo: function() { return index !== -1; },
        hasRedo: function() { return index < (undoCommands.length - 1); },
        getCommands: function() { return undoCommands; },
        getPreviousCommand: function() { return undoCommands[index - 1]; },
        getIndex: function() { return index; }
    };
};
