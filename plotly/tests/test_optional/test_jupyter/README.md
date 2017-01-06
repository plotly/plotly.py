# plotly.py Jupyter Notebook JS test suite

To make sure that plotly.py works properly inside Jupyter Notebooks in both
`plotly.plotly` and `plotly.offline`, we here run JavaScript tests in a browser.

See PR [#545](https://github.com/plotly/plotly.py/pull/545) for example of what
can go wrong in Jupyter Notebooks.


## Running the tests

Install JavaScript dependencies:

```bash
(plotly.py/plotly/tests/test_optional/test_jupyter) $ npm install
```

Run the tests:

```bash
(plotly.py/plotly/tests/test_optional/test_jupyter) $ nosetests

# or from the repo root
(plotly.py) $ nosetests plotly/tests/test_optional/test_jupyter
```

## Add a test case

- Open up `jupyter notebook`.

- Add a few code cells testing what you wish to test. No need to execute them!

- Save the resulting `.ipynb` file in `fixtures/` (e.g. `my_test.ipynb`)

- Add a JavaScript test file in `js_tests/` by first requiring the in-house
  [`tape`](https://github.com/substack/tape) test wrapper found in `lib/tape-wrapper.js`.

For example,

```js
var test = require('../lib/tape-wrapper');

test('should have one plotly.js graph', function(t) {
    t.plan(1);

    var nodes = document.querySelectorAll('.js-plotly-plot');
    t.equal(nodes.length, 1);
});
```

asserts that one plotly graph is present in the notebook.

At the moment, it is highly recommended that the `js` test file has the same name
(minus the extension) as the `.ipynb` fixture (i.e. `my_test.js` in this
example).

- Add a test case in `test_jupyter.py`. If both the fixture and `js` test file
have the same name, simply add:

```py
class MyTest(Common):
    __test__ = True
    name = 'my_test'
```

to `test_jupyter.py` and you're done :beers:


## How does this work?

The `Common` test class in `test_jupyter.py`:

- Loads up a given `.ipynb` fixture

- Executes all code cells and converts them to HTML using the
[`nbconvert`](https://nbconvert.readthedocs.io/en/latest/) and
[`ipykernel`](http://ipython.readthedocs.io/en/stable/install/kernel_install.html)
modules.

- Saves the resulting HTML file is saved in `fixtures/` but is git-ignored.

Then, `Common` runs an `npm` command in the shell:

```bash
npm test -- <path-to-html-fixture> <path-to-js-test-file>
```

which runs a minimal server using `lib/server.js`.

In details, `lib/server.js`:

-  bundles up the `js` test code into a single bundle using
[`browserify`](https://github.com/substack/node-browserify)

- stubs in a `<script>` tag to include the `js` test bundle in the fixture HTML

- starts a simple http server

- launches Chrome at the HTML fixture URL

- once the page is loaded, the `js` tests are run and results are logged in the
terminal


See PR [#549](https://github.com/plotly/plotly.py/pull/549) for the details on
how this suite was first implemented.
