JupyterLab Services
===================

Javascript client for the Jupyter services REST APIs

[API Docs](http://jupyterlab.github.io/jupyterlab/)

[REST API Docs](http://petstore.swagger.io/?url=https://raw.githubusercontent.com/jupyter/notebook/master/notebook/services/api/api.yaml)

Note: All functions and classes using the REST API allow a `serverSettings` 
parameter to configure requests.
Requests are made using the `fetch` API, which is available in modern browsers
or via `npm install fetch` for node users.  The `whatwg-fetch` npm package
can be used to polyfill browsers that do not support the `fetch` API.


Package Install
---------------

**Prerequisites**
- [node](http://nodejs.org/)
- [python](https://www.anaconda.com/download)

```bash
npm install --save @jupyterlab/services
conda install notebook  # notebook 4.3+ required
```


Source Build
------------

**Prerequisites**
- [git](http://git-scm.com/)
- [node 0.12+](http://nodejs.org/)
- [python](https://www.anaconda.com/download)

```bash
git clone https://github.com/jupyterlab/jupyterlab.git
cd packages/services
npm install
npm run build
conda install notebook  # notebook 4.3+ required
```

**Rebuild**
```bash
npm run clean
npm run build
```


Run Tests
---------

Follow the source build instructions first.

```bash
npm test
```


Build Docs
----------

Follow the source build instructions first.

```bash
npm run docs
```

Navigate to `docs/index.html`.


Supported Runtimes
------------------

The runtime versions which are currently *known to work* are listed below.
Earlier versions may also work, but come with no guarantees.

- Node 0.12.7+
- IE 11+
- Firefox 32+
- Chrome 38+

Note: "requirejs" may need be included in a global context for `Comm` targets
using the a `target_module` (in the classic Notebook).
This can be as a `<script>` tag in the browser or by using the `requirejs`
package in node (`npm install requirejs` and setting 
`global.requirejs = require('requirejs');`).


Starting the Notebook Server
----------------------------

Follow the package install instructions first.

The library requires a running Jupyter Notebook server, launched as:

```bash
jupyter notebook
```


Bundling for the Browser
------------------------

Follow the package install instructions first.

See `examples/browser` for an example of using Webpack to bundle the library.

Note: Some browsers (such as IE11), require a polyfill for Promises.
The example demonstrates the use of the polyfill.  See also notes about
the `fetch` API polyfill above.


Usage from Node.js
------------------

Follow the package install instructions first.

See `examples/node` for an example of using an ES5 node script.


Usage Examples
--------------

**Note:** This module is fully compatible with Node/Babel/ES6/ES5. The
examples below are written in TypeScript using ES6 syntax.  Simply
omit the type declarations when using a language other than TypeScript.
A translator such as Babel can be used to convert from ES6 -> ES5.

**Kernel**

```typescript
import {
  KernelMessage, Kernel
} from '@jupyterlab/services';


// Get a list of available kernels and connect to one.
Kernel.listRunning().then(kernelModels => {
  Kernel.connectTo(kernelModels[0]).then((kernel) => {
    console.log(kernel.name);
  });
});


// Get info about the available kernels and start a new one.
Kernel.getSpecs().then(kernelSpecs => {
  console.log('Default spec:', kernelSpecs.default);
  console.log('Available specs', Object.keys(kernelSpecs.kernelspecs));
  // use the default name
  let options: Kernel.IOptions = {
    name: kernelSpecs.default
  };
  Kernel.startNew(options).then(kernel => {
    // Execute and handle replies.
    let future = kernel.requestExecute({ code: 'a = 1' } );
    future.done.then(() => {
      console.log('Future is fulfilled');
    });
    future.onIOPub = (msg) => {
      console.log(msg.content);  // Print rich output data.
    };

    // Restart the kernel and then send an inspect message.
    kernel.restart().then(() => {
      let request: KernelMessage.IInspectRequest = {
        code: 'hello', cursor_pos: 4, detail_level: 0
      };
      kernel.requestInspect(request).then(reply => {
        console.log(reply.content.data);
      });
    });

    // Interrupt the kernel and then send a complete message.
    kernel.interrupt().then(() => {
      kernel.requestComplete({ code: 'impor', cursor_pos: 4 } ).then((reply) => {
        console.log(reply.content.matches);
      });
    });

    // Register a callback for when the kernel changes state.
    kernel.statusChanged.connect((status) => {
      console.log('status', status);
    });

    // Kill the kernel.
    kernel.shutdown().then(() => {
      console.log('Kernel shut down');
    });
  });
});

```

**Session**

```typescript
import {
  Session
} from '@jupyterlab/services';


// Get a list of available sessions and connect to one.
Session.listRunning().then(sessionModels => {
  Session.connectTo(sessionModels[0]).then((session) => {
    console.log(session.kernel.name);
  });
});

// Start a new session.
let options = {
  kernelName: 'python',
  path: '/tmp/foo.ipynb'
};

Session.startNew(options).then(session => {
  // Execute and handle replies on the kernel.
  let future = session.kernel.requestExecute({ code: 'a = 1' });
  future.done.then(() => {
    console.log('Future is fulfilled');
  });

  // Rename the session.
  session.setPath('/local/bar.ipynb').then(() => {
    console.log('Session renamed to', session.path);
  });

  // Register a callback for when the session dies.
  session.terminated.connect(() => {
    console.log('session died');
  });

  // Kill the session.
  session.shutdown().then(() => {
    console.log('session closed');
  });

});

```

**Comm**

```typescript

import {
  Kernel
} from '@jupyterlab/services';

// Create a comm from the server side.
//
// Get info about the available kernels and connect to one.
Kernel.getSpecs().then(kernelSpecs => {
  return Kernel.startNew({
    name: kernelSpecs.default,
  });
}).then(kernel => {
  let comm = kernel.connectToComm('test');
  comm.open('initial state');
  comm.send('test');
  comm.close('bye');
});

// Create a comm from the client side.
Kernel.getSpecs().then(kernelSpecs => {
  return Kernel.startNew({
    name: kernelSpecs.default,
  });
}).then(kernel => {
  kernel.registerCommTarget('test2', (comm, commMsg) => {
    if (commMsg.content.target_name !== 'test2') {
       return;
    }
    comm.onMsg = (msg) => {
      console.log(msg);  // 'hello'
    };
    comm.onClose = (msg) => {
      console.log(msg);  // 'bye'
    };
  });

  let code = [
    'from ipykernel.comm import Comm',
    'comm = Comm(target_name="test2")',
    'comm.send(data="hello")',
    'comm.close(data="bye")'
  ].join('\n');
  kernel.requestExecute({ code: code });
});
```

**Contents**

```typescript
import {
  ContentsManager
} from '@jupyterlab/services';

let contents = new ContentsManager();

// Create a new python file.
contents.newUntitled({ path: '/foo', type: 'file', ext: 'py' }).then(
  (model) => {
    console.log('new file:', model.path);
  }
);

// Get the contents of a directory.
contents.get('/foo/bar').then(
  (model) => {
    console.log('files:', model.content);
  }
);

// Rename a file.
contents.rename('/foo/bar.txt', '/foo/baz.txt');

// Save a file.
contents.save('/foo/test.ipynb');

// Delete a file.
contents.delete('/foo/bar.txt');

// Copy a file.
contents.copy('/foo/bar.txt', '/baz').then((model) => {
    console.log('new path', model.path);
});

// Create a checkpoint.
contents.createCheckpoint('/foo/bar.ipynb').then((model) => {
  let checkpoint = model;

  // Restore a checkpoint.
  contents.restoreCheckpoint('/foo/bar.ipynb', checkpoint.id);

  // Delete a checkpoint.
  contents.deleteCheckpoint('/foo/bar.ipynb', checkpoint.id);
});

// List checkpoints for a file.
contents.listCheckpoints('/foo/bar.txt').then((models) => {
    console.log(models[0].id);
});
```

**Configuration**

```typescript
import {
  ConfigWithDefaults, ConfigSection
} from '@jupyterlab/services';

// The base url of the Jupyter server.

ConfigSection.create({ name: 'notebook' }).then(section => {
  let config = new ConfigWithDefaults({
    section,
    defaults: { default_cell_type: 'code' },
    className: 'Notebook'
  });
  console.log(config.get('default_cell_type'));   // 'code'
  config.set('foo', 'bar').then(data => {
     console.log(data); // "{ 'foo': 'bar' }"
  });
});
```

**Terminals**

```typescript
import {
  TerminalSession
} from '@jupyterlab/services';


// Create a named terminal session and send some data.
TerminalSession.startNew().then(session => {
  session.send({ type: 'stdin', content: ['foo'] });
});
```
