# Contributing

Thank you for your interest in contributing to plotly.py!
We are actively looking for diverse contributors with diverse background and skills.

This guide starts with a general description of the different ways to contribute to plotly.py,
then explains the technical aspects of preparing your contribution.

## Code of Conduct

Please note that all contributos are required to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Different Ways to Contribute

There are many ways to contribute to plotly.py.
To do any effectively,
it is important to understand the structure of the code and the repository.

-   The [`plotly.graph_objects`](https://plotly.com/python/graph-objects/) module (usually imported as `go`)
    is [generated from the plotly.js schema](https://plotly.com/python/figure-structure/),
    so changes to be made in this package need to be contributed to [plotly.js](https://github.com/plotly/plotly.js)
    or to the code generation system in `./codegen/`.
    Code generation creates traces and layout classes that have a direct correspondence to their JavaScript counterparts,
    while higher-level methods that work on figures regardless of the current schema (e.g., `BaseFigure.for_each_trace`)
    are defined in `plotly/basedatatypes.py`.
    Additional helper methods such as `update_layout` `add_trace` are also defined there for the `Figure` object.

-   The [`plotly.express`](https://plotly.com/python/plotly-express/) module (usually imported as `px`)
    is a high-level API that uses `graph_objects` under the hood.
    Its code is in `plotly/express/`.
    Plotly Express functions generally concern themselves with formatting data and creating figures out of `plotly.graph_objects` instances;
    they are designed to be consistent with each other and to do as little computation in Python as possible.

-   Other pure-Python submodules include `plotly.io` (a low-level interface for displaying, reading and writing figures)
    and `plotly.subplots` (helper function for layout of multi-plot figures)

-   Tests are found in `tests`.
    These are organized in subdirectories according to what they test:
    see the "Setup" section below for more details.

-   Documentation is found in `doc/`, and its structure is described in [its README file](doc/README.md).
    The documentation is a great place to start contributing,
    since you can add or modify examples without setting up a full environment.

Code and documentation are not the only way to contribute:
you can also help by:

-   Reporting bugs at <https://github.com/plotly/plotly.py/issues>.
    Please take a moment to see if your problem has already been reported, and if so, add a comment to the existing issue;
    we will try to prioritize those that affect the most people.

-   Submitting feature requests (also at <https://github.com/plotly/plotly.py/issues>).
    Again, please add a comment to an existing issue if the feature you want has already been requested.

-   Helping other users on the community forum at <https://community.plot.ly/>.

If you'd like to know more,
we recommend reading [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/).

## Setup

This section explains how to set up a development environment so that you can contribute code and/or tests.
Note that if you are modifying a single documentation page,
you can do it directly on GitHub by clicking on the "Edit this page on GitHub" link without cloning the repository.

### Get a Local Copy of the Project

We use Git and GitHub to manage our project;
if you are not familiar with them,
there are great resources like <http://try.github.io/> to get you started.

The first step is to [fork the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) on GitHub
so that you have your own copy to work with.
Once you have done that,
you can run the following command to get a local copy of your repository
(replacing `your_github_id` with your GitHub ID):

```bash
git clone https://github.com/your_github_id/plotly.py.git
```

You can then go into that newly-forked repository using:

```bash
cd plotly.py
```

### Create a Virtual Environment

Next,
you should create a *virtual environment* for the project
so that packages you install won't affect other projects you are working on.
We recommend using [`uv`](https://docs.astral.sh/uv/) for this:

```bash
uv venv --python 3.12
source .venv/bin/activate
```

Alternatively,
you can use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)
or [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
to create and manage your virtual environment;
see those tools' documentation for more information.

### Install Packages

If you are using `uv`,
you can install all of the packages needed for developing and testing plotly.py with this command:

```bash
uv sync --extra dev
```

If you are using `conda` or `virtualenv`,
or if `uv sync` does not work as you expect,
you can install all packages with:

```bash
pip install -e '.[dev]'
```

If you're testing local changes in Jupyter Lab or Jupyter Notebook, you'll want to run these commands when you're setting up your development environment:
```bash
pip install jupyter
jupyter labextension develop .
```
If you don't run that command, your figure will not render in the Jupyter Lab/ Jupyter Notebook editors. 

If you're changing any of the code under the `js/` directory, you'll also want to run these commands:
```
cd js/
npm ci
npm run build
```

These commands also create an *editable install* of plotly.py
so that you can test your changes iteratively without having to rebuild the plotly.py package explicitly;
for more information please see
[the `pip` documentation on editable installs](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs)
Please note that the single quotes are needed to escape the `[]` characters.

### Formatting

This repo uses [ruff](https://astral.sh/ruff) to format Python code consistently.
(Ruff is included in `pyproject.toml`,
so you should have installed it already if you've been following along.)
You can run ruff prior to making a PR with:

```bash
ruff check .
```

### Making Your Change

Do *not* work in the `main` branch directly.
Instead,
create a new branch for your work with the following command
(replacing `your-branch` with a meaningful name):

```bash
git checkout -b your-branch
```

Once you have made your changes and tested them,
push your changes to your fork of the plotly.py repository on GitHub
and create your pull request.

> **Managing `uv.lock`**
>
> Please do _not_ commit changes to `uv.lock`
> unless you have added, removed, or changed dependencies in `pyproject.toml`.

### Testing

We use [pytest](https://docs.pytest.org/) for managing and running tests.
You are strongly encouraged to write or modify tests whenever you add or change functionality;
we are more likely to review and merge PRs with tests than ones without.

If you have installed all the dependencies as explained above,
you can run all the tests with:

```bash
python -m pytest tests
```

During development,
you can speed things up by running only the tests in a particular file:

```bash
python -m pytest tests/test_plotly/test_plot.py
```

See [pytest's documentation](https://docs.pytest.org/) for more details.

## Advanced

### Generating the JavaScript Bundles for Jupyter

If you make changes to any files in the `js/` directory,
you must run `npm install && npm run build` in the `js/` directory to rebuild the FigureWidget and JupyterLab extension.
You must then commit the build artifacts produced in `plotly/labextension`.
A CI job will verify that this step has been done correctly.

### Jupyter

The `js/` directory contains Javascript code which helps use Plotly in Jupyter notebooks.
Two kinds of Jupyter support are included:

1.  **Mime Renderer JupyterLab extension**:
    This is the default renderer for Plotly `Figure()` objects in Jupyter notebooks.
    The Plotly mime renderer JupyterLab extension is used automatically by JupyterLab (and Jupyter Notebook)
    when it sees the MIME type `application/vnd.plotly.v1+json` in the notebook output.
    The MIME renderer loads `plotly.js` a single time and references it each time a Plotly figure is used in the notebook,
    which allows us to avoid embedding `plotly.js` in the notebook output.
    The JupyterLab extension source code is located at `js/src/mimeExtension.ts`
    and the compiled extension code is located at `plotly/labextension` in the built Python package.
    The command `jupyter labextension build` (which is one of the steps called by `npm run build`) compiles the extension
    and places the build artifacts in `plotly/labextension`. 

2.  **FigureWidget**:
    This is a more interactive method for rendering Plotly charts in notebooks.
    FigureWidget is used by creating a `FigureWidget` object inside the notebook code in place of a `Figure`.
    It supports communication between the Javascript frontend and Python backend,
    but requires the installation of an additional Python package called `anywidget`.
    The FigureWidget source code is located at `js/src/widget.ts`,
    and is included in the built Python package at `plotly/package_data/widgetbundle.js`. 

### Updating to a New Version of plotly.js

First, update the version of the `plotly.js` dependency in `js/package.json`.
Once you have done that,
run the `updateplotlyjs` command:

```bash
python commands.py updateplotlyjs
```

This downloads new versions of `plot-schema.json` and `plotly.min.js` from the `plotly/plotly.js` GitHub repository
and places them in `plotly/package_data`.
It then regenerates all of the `graph_objs` classes based on the new schema.

### Using a Development Branch of Plotly.js

If your development branch is in [the plotly.js repository](https://github.com/plotly/plotly.js)
you can update to development versions of `plotly.js` with this command:

```bash
python commands.py updateplotlyjsdev --devrepo reponame --devbranch branchname
```

This fetches the `plotly.js` in the CircleCI artifact of the branch `branchname` of the repo `reponame`.
If `--devrepo` or `--devbranch` are omitted,
`updateplotlyjsdev` defaults to `plotly/plotly.js` and `master` respectively.

### Local Repository

If you have a local repository of `plotly.js` you'd like to try,
you can prepare the package by running the following commands
*in your local plotly.js repository*:

```bash
npm run build
npm pack
mv plotly.js-*.tgz plotly.js.tgz
```

You can then run the following command
*in your local plotly.py repository*:

```bash
python commands.py updateplotlyjsdev --local /path/to/your/plotly.js/
```
