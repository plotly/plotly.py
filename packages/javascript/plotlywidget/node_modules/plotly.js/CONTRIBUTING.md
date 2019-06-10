# Contributing to plotly.js

## Opening issues

Please read the [issue guidelines](./.github/ISSUE_TEMPLATE.md).

## Making pull requests

Please read the [pull request guidelines](./.github/PULL_REQUEST_TEMPLATE.md).

## GitHub labels

We use the following [labels](https://github.com/plotly/plotly.js/labels) to track issues and PRs:

| Label | Purpose |
|--------|---------|
| `type: bug` | bug report confirmed by a plotly team member |
| `type: regression` | bug that introduced a change in behavior from one version to the next |
| `type: feature` | planned feature additions |
| `type: translation` | localization-related tasks |
| `type: performance` | performance related tasks |
| `type: maintenance` | source code cleanup resulting in no enhancement for users |
| `type: documentation` | API doc or attribute description improvements |
| `type: community` | issue left open for community input and pull requests |
| `type: duplicate` | *self-explanatory* |
| `type: wontfix` | *self-explanatory* |
| `status: discussion needed` | Issue or PR that required discussion among maintainers before moving forward |
| `status: in progress` | PRs that required some initial feedback but not ready to merge |
| `status: reviewable` | PRs that are completed from the author's perspective |
| `status: on hold` | PRs that are put on hold |

## Development

#### Prerequisites

- git
- [node.js](https://nodejs.org/en/). We recommend using node.js v10.x, but all
  versions starting from v6 should work.  Upgrading and managing node versions
  can be easily done using [`nvm`](https://github.com/creationix/nvm) or its
  Windows alternatives.
- [`npm`](https://www.npmjs.com/) v6.x and up (which ships by default with
  node.js v10.x) to ensure that the
  [`package-lock.json`](https://docs.npmjs.com/files/package-lock.json) file is
  used and updated correctly.

#### Step 1: Clone the plotly.js repo and install its dependencies

```bash
git clone https://github.com/plotly/plotly.js.git
cd plotly.js
npm install
```

#### Step 2: Setup test environment

```bash
npm run pretest
```

#### Step 3: Start the test dashboard

```bash
npm start
```

This command bundles up the source files with source maps using
[browserify](https://github.com/substack/node-browserify), starts a
[watchify](https://github.com/substack/watchify) file watcher (making the your
dev plotly.js bundle update every time a source file is saved) and opens up a
tab in your browser.

#### Step 4: Open up the console and start developing

A typical workflow is to make some modifications to the source, update the
test dashboard, inspect and debug the changes, then repeat. The test dashboard
comes bundled with some useful tools while developing - all bundled under the
`Tabs` object:


| Method/Property        | Description |
|------------------------|-------------|
| `Tabs.fresh([id])` | Creates a fresh graph div and returns it (default id of `graph`). |
| `Tabs.getGraph([id])` | Returns the default or specified graph div. |
| `Tabs.plotMock(mock, [id])` | Plots the specified mock (`.json` extension is not required). |
| `Tabs.snapshot([id])` | Creates a png snapshot of the plot and places it below. |
| `Tabs.reload()` | Reloads the plotly.js script and will execute `Tabs.onReload` once completed. |
| `Tabs.onReload()` | By default, set to `noop` but you may set `Tabs.onReload` to any function you wish. This is useful for replotting a mock or test every time you reload the plotly.js script. |
| `Tabs.purge()` | Destroys all plots. |

View [the source](https://github.com/plotly/plotly.js/blob/master/devtools/test_dashboard/devtools.js) for more info.

Three additional helpers exist that are refreshed every second:

* `gd` - this is the default plot div
* `fullData` - shortcut to `gd._fullData`
* `fullLayout` - shortcut to `gd._fullLayout`

There is also a search bar in the top right of the dashboard. This fuzzy-searches
image mocks based on their file name and trace type.

#### Other npm scripts

- `npm run preprocess`: pre-processes the css and svg source file in js. This
  script must be run manually when updating the css and svg source files.
- `npm run watch`: starts a watchify file watcher just like the test dashboard but
  without booting up a server.

## Testing

Both jasmine and image tests are run on
[CircleCI](https://circleci.com/gh/plotly/plotly.js) on every push to this
repo.

### Jasmine tests

Jasmine tests are run in a browser using
[karma](https://github.com/karma-runner/karma). To run them locally:

```
npm run test-jasmine
```

To run a specific suite, use:

```
npm run test-jasmine -- <suite>
```

where the `<suite>` corresponds to the suite's file name as found in
[`test/jasmine/tests/`](https://github.com/plotly/plotly.js/tree/master/test/jasmine/tests).

You can also test multiple suites at a time, for example:

```
npm run test-jasmine -- bar axes scatter
```

which will run tests in the `bar_test.js`, `axes_test.js` and `scatter_test.js`
suites.

To turn off the `autoWatch` / auto-bundle / multiple run mode:

```
npm run test-jasmine -- <suite> --nowatch
```

In certain situations, you may find that the default reporting is not verbose
enough to pin down the source of the failing test. In this situation, you may
wish to use
[karma-verbose-reporter](https://www.npmjs.com/package/karma-verbose-reporter):

```
npm run test-jasmine -- <suite> --verbose
```

For more info on the karma / jasmine CLI:

```
npm run test-jasmine -- --help
npm run test-jasmine -- --info
```

### Image pixel comparison tests

Image pixel comparison tests are run in a docker container. For more
information on how to run them locally, please refer to [image test
README](https://github.com/plotly/plotly.js/blob/master/test/image/README.md).

Running the test locally outputs the generated png images in `build/test_images/` and the png diffs in `build/test_images_diff/` (two git-ignored directories).

To view the image pixel comparison test results, run

```
npm run start-image_viewer
```
which shows the baseline image, the generated image, the diff and the json mocks of test cases that failed.

To view the results of a run on CircleCI, download the `build/test_images/` and `build/test_images_diff/` artifacts into your local repo and then run `npm run start-image_viewer`.

### Writing interaction tests
Keep in mind that the interaction coordinates are relative to the top-left corner of the plot, including the margins. To produce a reliable interaction test, 
it may be necessary to fix the width, height, margins, X axis range and Y axis range of the plot. For example:

```
Plotly.newPlot(gd, [{
    x: [1, 1, 1, 2, 2, 2, 3, 3, 3],
    y: [1, 2, 3, 1, 2, 3, 1, 2, 3],
    mode: 'markers'
}], {
    width: 400, height: 400,
    margin: {l: 100, r: 100, t: 100, b: 100},
    xaxis: {range: [0, 4]},
    yaxis: {range: [0, 4]}
});
```

This will produce the following plot, and say you want to simulate a selection path of (175, 175) to (225, 225):

<img src="https://user-images.githubusercontent.com/31989842/38890553-0bc6190c-4282-11e8-8efc-077bf05ca565.png">


## Repo organization

- Distributed files are in `dist/`
- CommonJS require-able modules are in `lib/`
- Sources files are in `src/`, including the index
- Build and repo management scripts are in `tasks/`
- All tasks can be run using [`npm run-script`](https://docs.npmjs.com/cli/run-script)
- Tests are `test/`, they are partitioned into `image` and `jasmine` tests
- Test dashboard and image viewer code is in `devtools/`
- Built files are in `build/` (most files in here are git-ignored, the css and font built files are exceptions)


## Coding style

Check if ok, with `npm run lint`

- See [eslintrc](https://github.com/plotly/plotly.js/blob/master/.eslintrc) and
  the eslint [list of rules](http://eslint.org/docs/rules/) for more details.
- Rules listed in the eslintrc file with the ignore flag `0` are the recommended
  rules for new code added.
