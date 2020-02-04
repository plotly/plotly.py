# Contributing

The bottom line. Follow your Nose, or our Nose. Write-run-love tests :fist:.

## Code of Conduct

Check out the [Code of Conduct](CODE_OF_CONDUCT.md). Don't tl:dr; it, but the general idea is to be nice.

## Have a Bug Report?

Open an issue! Go to https://github.com/plotly/plotly.py/issues. It's possible that your issue was already addressed. If it wasn't, open it. We also accept PRs; take a look at the steps below for instructions on how to do this.

## Have Questions about Plotly?

Check out our Support App: https://support.plot.ly/libraries/python or Community Forum: https://community.plot.ly/.

## Want to improve the plotly documentation?

Thank you! Instructions on how to contribute to the documentation are given [here](doc/contributing.md). Please also read the next section if you need to setup a development environment. 

## Setup a Development Environment

### Fork, Clone, Setup Your Version of the Plotly Python API

First, you'll need to *get* our project. This is the appropriate *clone* command (if you're unfamiliar with this process, https://help.github.com/articles/fork-a-repo):

**DO THIS (in the directory where you want the repo to live)**

```bash
git clone https://github.com/your_github_username/plotly.py.git
cd plotly.py
```

### Create a virtual environment for plotly development

You can use either [conda][conda-env] or [virtualenv][virtualenv] to create a virtual environment for plotly development, e.g.

```bash
conda create -n plotly-dev python
conda activate plotly-dev
```

[conda-env]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
[virtualenv]: http://docs.python-guide.org/en/latest/dev/virtualenvs/

### Install requirements

    $ pip install -r packages/python/plotly/requirements.txt
    $ pip install -r packages/python/plotly/optional-requirements.txt

### Editable install of plotly packages

    $ pip install -e packages/python/plotly/
    $ pip install -e packages/python/chart-studio/
    $ pip install -e packages/python/plotly-geo/

### ipywidgets development install

Run the following commands in your virtual environment to use the
development version of `FigureWidget`, 

    $ jupyter nbextension enable --py widgetsnbextension
    $ jupyter nbextension install --py --symlink --sys-prefix plotlywidget
    $ jupyter nbextension enable --py --sys-prefix plotlywidget

To make plotly plots show up in JupyterLab, you also need to [install the plotly jupyterlab extensions][plotly-jl].

[plotly-jl]: https://plot.ly/python/getting-started/#jupyterlab-support-python-35
    
### Configure black code formatting
This repo uses the [Black](https://black.readthedocs.io/en/stable/) code formatter,
and the [pre-commit](https://pre-commit.com/) library to manage a git commit hook to
run Black prior to each commit.  Both pre-commit and black are included in the
`packages/python/plotly/optional-requirements.txt` file, so you should have them
installed already if you've been following along.

To enable the Black formatting git hook, run the following from within your virtual
environment.

```bash
(plotly_dev) $ pre-commit install
``` 

Now, whenever you perform a commit, the Black formatter will run.  If the formatter
makes no changes, then the commit will proceed.  But if the formatter does make changes,
then the commit will abort.  To proceed, stage the files that the formatter
modified and commit again.

If you don't want to use `pre-commit`, then you can run black manually prior to making
a PR as follows.

```bash
(plotly_dev) $ black .
```

### Making a Development Branch

Third, *don't* work in the `master` branch. As soon as you get your master branch ready, run:

**DO THIS (but change the branch name)**
```bash
git checkout -b my-dev-branch
```

... where you should give your branch a more descriptive name than `my-dev-branch`

### Pull Request When Ready

Once you've made your changes (and hopefully written some tests...), make that pull request!


## Update to a new version of Plotly.js
First update the version of the `plotly.js` dependency in `js/package.json`.

Then run the `updateplotlyjs` command with:

```bash
$ python setup.py updateplotlyjs
```

This will download new versions of `plot-schema.json` and `plotly.min.js` from 
the `plotly/plotly.js` GitHub repository (and place them in 
`plotly/package_data`). It will then regenerate all of the `graph_objs`
classes based on the new schema.

## Testing

We take advantage of two tools to run tests:

* [`tox`](https://tox.readthedocs.io/en/latest/), which is both a virtualenv management and test tool.
* [`nose`](https://nose.readthedocs.org/en/latest/), which is is an extension of Python's unittest

### Running Tests with `nose`

Since our tests cover *all* the functionality, to prevent tons of errors from showing up and having to parse through a messy output, you'll need to install `optional-requirements.txt` as explained above.

After you've done that, go ahead and follow (y)our Nose!

```bash
nosetests -w  packages/python/plotly/plotly/tests/
```

Or for more *verbose* output:

```bash
nosetests -w  packages/python/plotly/plotly/tests/ -v
```

Either of those will run *every* test we've written for the Python API. You can get more granular by running something like:

```bash
nosetests -w  packages/python/plotly/plotly/tests/test_core/
```

... or even more granular by running something like:

```bash
nosetests plotly/tests/test_plotly/test_plot.py
```

### Running tests with `tox`

Running tests with tox is much more powerful, but requires a bit more setup.

You'll need to export an environment variable for *each* tox environment you wish to test with. For example, if you want to test with `Python 2.7` and
`Python 3.6`, but only care to check the `core` specs, you would need to ensure that the following variables are exported:

```
export PLOTLY_TOX_PYTHON_27=<python binary>
export PLOTLY_TOX_PYTHON_36=<python binary>
```

Where the `<python binary` is going to be specific to your development setup. As a more complete example, you might have this loaded in a `.bash_profile` (or equivalent shell loader):

```bash
############
# tox envs #
############

export PLOTLY_TOX_PYTHON_27=python2.7
export PLOTLY_TOX_PYTHON_34=python3.4
export TOXENV=py27-core,py34-core
```

Where `TOXENV` is the environment list you want to use when invoking `tox` from the command line. Note that the `PLOTLY_TOX_*` pattern is used to pass in variables for use in the `tox.ini` file. Though this is a little setup, intensive, you'll get the following benefits:

* `tox` will automatically manage a virtual env for each environment you want to test in.
* You only have to run `tox` and know that the module is working in both `Python 2` and `Python 3`.

Finally, `tox` allows you to pass in additional command line arguments that are formatted in (by us) in the `tox.ini` file, see `{posargs}`. This is setup to help with our `nose attr` configuration. To run only tests that are *not* tagged with `slow`, you could use the following command:

```bash
tox -- -a '!slow'
```

Note that anything after `--` is substituted in for `{posargs}` in the tox.ini. For completeness, because it's reasonably confusing, if you want to force a match for *multiple* `nose attr` tags, you comma-separate the tags like so:

```bash
tox -- -a '!slow','!matplotlib'
```

### Writing Tests

You're *strongly* encouraged to write tests that check your added functionality.

When you write a new test anywhere under the `tests` directory, if your PR gets accepted, that test will run in a virtual machine to ensure that future changes don't break your contributions!

Test accounts include: `PythonTest`, `PlotlyImageTest`, and  `PlotlyStageTest`. 

## Release process - plotly package

This is the release process for releasing `plotly.py` version `X.Y.Z` with
`plotlywidget` version `A.B.C`.

Note: The `plotlywidget` instructions must be followed if any change
has been made in the `packages/javascript` directory source code, OR if the version of
plotly.js has been updated.  If neither of these is the case, there's no need
to increment the `plotlywidget` version or to publish a new version to npm.

### Create a release branch
After all of the functionality for the release has been merged into master,
create a branch named `release_X.Y.Z`. This branch will become the
final version

### Finalize changelog
Review the contents of `packages/python/plotly/CHANGELOG.md`. We try to follow
the [keepachangelog](https://keepachangelog.com/en/1.0.0/) guidelines.
Make sure the changelog includes the version being published at the top, along
with the expected publication date.

Use the `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`
labels for all changes to plotly.py.  If the version of plotly.js has
been updated, include this as the first `Updated` entry. Call out any
noteable changes as sub-bullets (new trace types in particular), and provide
a link to the plotly.js CHANGELOG.

As the first entry in the changelog, include a `JupyterLab Versions` section.
Here, document the versions of `plotlywidget`, 
`@jupyter-widgets/jupyterlab-manager`, `jupyterlab`, and
`@jupyterlab/plotly-extension` that are known to be compatible with this
version of `plotly.py`.

Note: Use the official (not release candidate) versions in the CHANGELOG.

### Update README.md installation instructions

Update the installation instructions in the README to the new versions of all
of the dependencies. Use the release candidate versions, this way we can point
people to the README of the `release_X.Y.Z` as the instructions for trying out
the release candidate.

Note that the conda installation instructions must include
"-c plotly/lable/test" rather than "-c plotly" in order to install the
release candidate version.

Update the `doc/python/getting-started.md` file with the same version numbers.

Commit Changelog, README and getting-started updates.

### Bump to release candidate version
 1) Manually update the plotlywidget version to `A.B.C-rc.1` in the files
specified below.

 - `packages/python/plotly/plotly/_widget_version.py`:
   + Update `__frontend_version__` to `^A.B.C-rc.1` (Note the `^` prefix)
 - `packages/javascript/plotlywidget/package.json`
   + Update `"version"` to `A.B.C-rc.1`
   
 2) Commit the changes
 
 3) Tag this commit on the release branch as `vX.Y.Zrc1` and `widget-vA.B.C-rc.1`
   
In both cases `rc` is the semantic versioning code for Release Candidate.
   
The number 1 means that this is the first release candidate, this number can
be incremented if we need to publish multiple release candidates.
Note that the `npm` suffix is `-rc.1` and the PyPI suffix is `rc1`.
 
Publishing `plotly.py` and `plotlywidget` as release candidates
allows us to go through the publication process, and test that the
installed packages work properly before general users will get them by
default. It also gives us the opportunity to ask specific users to test
that their bug reports are in fact resolved before we pull the trigger
on the official release.

### Publish release candidate to PyPI
To upload to PyPI you'll also need to have `twine` installed:
```bash
(plotly_dev) $ pip install twine
```

And, you'll need the credentials file `~/.pypirc`. Request access from
@jonmmease and @chriddyp. Then, from inside the repository:

```bash
(plotly_dev) $ git checkout release_X.Y.Z
(plotly_dev) $ git stash
(plotly_dev) $ python setup.py sdist bdist_wheel
(plotly_dev) $ twine upload dist/plotly-X.Y.Zrc1*
```

### Publish release candidate of `plotlywidget` and `jupyterlab-plotly` to NPM
Now, publish the release candidate of the `plotlywidget` NPM package.

```bash
cd ./packages/javascript/plotlywidget
npm publish --access public --tag next
```

The `--tag next` part ensures that users won't install this version unless
they explicitly ask for the version or for the version wtih the `next` tag.

Do the same in the `jupyterlab-plotly` directory.

### Publish release candidate to plotly anaconda channel
To publish package to the plotly anaconda channel you'll need to have the
anaconda or miniconda distribution installed, and you'll need to have the
`anaconda-client` package installed.

```bash
(plotly_dev) $ conda build recipe/
```

Next run `anaconda login` and enter the credentials for the plotly anaconda
channel.
          
Then upload artifacts to the anaconda channel using the test label. Using the test
label will ensure that people will only download the release candidate version
if they explicitly request it.

```
$ anaconda upload --label test /path/to/anaconda3/conda-bld/noarch/plotly-*.tar.bz2 
```

Then logout with `anaconda logout` 

### Manually test the release candidate
Create a fresh virtual environment (or conda environment) and install
the release candidate by following the new `README.md` instructions
(the instructions updated above to include the release candidate versions)

Run through the example notebooks at
https://github.com/jonmmease/plotly_ipywidget_notebooks using the classic
notebook and JupyterLab. Make sure `FigureWidget` objects are displayed as
plotly figures, and make sure the in-place updates and callbacks work.

If appropriate, ask users who have submitted bug reports or feature 
requests that are resolved in this version to try out the release candidate.

If problems are found in the release candidate, fix them on the release
branch and then publish another release candidate with the candidate number
incremented.

### Finalize CHANGELOG and README
Update CHANGELOG with release date and update README with final versions.

In the conda installation instructions, be sure to change the
"-c plotly/label/test" argument to "-c plotly"
 
Commit updates.

### Finalize versions
When no problems are identified in the release candidate, remove the
release candidate suffix from the following version strings:

 - `plotly/_widget_version.py`:
   + Update `__frontend_version__` to `^A.B.C` (Note the `^` prefix)
 - `packages/javascript/plotlywidget/package.json`
   + Update `"version"` to `A.B.C`
 - `packages/javascript/jupyterlab-plotly/package.json`
   + Update `"version"` to `A.B.C`
   
Commit and push to the release branch.

### Merge release into master
Make sure the integration tests are passing on the release branch, then merge
it into master on GitHub.

Make sure tests also pass on master, then update your local master,
tag this merge commit as `vX.Y.Z` (e.g. `v3.1.1`) and `widget-vA.B.C` 

push the tag.

```bash
(plotly_dev) $ git checkout master
(plotly_dev) $ git stash
(plotly_dev) $ git pull origin master
(plotly_dev) $ git tag vX.Y.Z
(plotly_dev) $ git push origin vX.Y.Z
(plotly_dev) $ git tag widget-vA.B.C
(plotly_dev) $ git push origin widget-vA.B.C
```

### Publishing to PYPI

Publish the final version to PyPI

```bash
(plotly_dev) $ cd packages/python/plotly
(plotly_dev) $ python setup.py sdist bdist_wheel
(plotly_dev) $ twine upload dist/plotly-X.Y.Z*
```

After it has uploaded, move to another environment and double+triple check that you are able to upgrade ok:
```bash
$ pip install plotly --upgrade
```

And ask one of your friends to do it too. Our tests should catch any issues, but you never know.

<3 Team Plotly

### Publish widget library to npm
Finally, publish the final version of the widget library to npm with:

```bash
cd ./js
npm publish --access public
```

### Publishing to the plotly conda channel
Follow the anaconda upload instructions as described for the release candidate
above, except:

 - Do not include the `--label test` argument when uploading
 
```
$ anaconda upload /path/to/anaconda3/conda-bld/noarch/plotly-*.tar.bz2 
```

### Add GitHub Release entry
Go to https://github.com/plotly/plotly.py/releases and "Draft a new release"

Enter the vX.Y.Z tag

Make "Release title" the same string as the tag.

Copy changelog section for this version as the "Describe this release"

### Upgrade doc requirements and API doc

Files to be updated:
- `doc/apidoc/conf.py` with new version number
- `doc/requirements.txt`
- `binder/requirements.txt`

### Synchronize master and doc-prod branches

doc-prod should already have been merged on a regular basis into master, but
start doing it first. Then merge master into doc-prod to deploy the doc related
to features in the release.

### Post announcement
Post a simple announcement to the Plotly Python forum, with links to the
README installation instructions and to the CHANGELOG.

## Release process - plotly-geo package
The `plotly-geo` package contains the shape file resources used by plotly.py.
These files are relatively large and change infrequently so it is useful
to release them in a separate package.

### Update version
Update the version of the `plotly-geo` package in
`packages/python/plotly-geo/setup.py`.

This version is not intended to match the version of plotly.py.

### Update CHANGELOG
Add a new entry to the CHANGELOG at `packages/python/plotly-geo/CHANGELOG.md`
and commit the changes.

### Tag Release
Create a new tag for the release

```bash
(plotly_dev) $ git checkout master
(plotly_dev) $ git stash
(plotly_dev) $ git pull origin master
(plotly_dev) $ git tag plotly-geo-vX.Y.Z
(plotly_dev) $ git push origin plotly-geo-vX.Y.Z
```

### Publishing to PYPI
Publish the final version to PyPI

```bash
(plotly_dev) $ cd packages/python/plotly-geo
(plotly_dev) $ python setup.py sdist bdist_wheel
(plotly_dev) $ twine upload dist/plotly-geo-X.Y.Z.tar.gz
(plotly_dev) $ twine upload dist/plotly_geo-X.Y.Z-py3-none-any.whl
```

### Publish to plotly anaconda channel
From `packages/python/plotly-geo`, build the conda packge
```bash
(plotly_dev) $ conda build recipe/
```

Then upload to the plotly anaconda channel as described above

## Release process - chart-studio package
The `chart-studio` package contains the utilities for interacting with 
Chart Studio (both Cloud or On-Prem).

### Update version
Update the version of the `chart-studio` package in
`packages/python/chart-studio/setup.py`.

This version is not intended to match the version of plotly.py.

### Update CHANGELOG
Add a new entry to the CHANGELOG at `packages/python/chart-studio/CHANGELOG.md`
and commit the changes.

### Tag Release
Create a new tag for the release

```bash
(plotly_dev) $ git checkout master
(plotly_dev) $ git stash
(plotly_dev) $ git pull origin master
(plotly_dev) $ git tag chart-studio-vX.Y.Z
(plotly_dev) $ git push origin chart-studio-vX.Y.Z
```

### Publishing to PYPI
Publish the final version to PyPI

```bash
(plotly_dev) $ cd packages/python/chart-studio
(plotly_dev) $ python setup.py sdist bdist_wheel
(plotly_dev) $ twine upload dist/chart-studio-X.Y.Z.tar.gz
(plotly_dev) $ twine upload dist/chart_studio-X.Y.Z-py3-none-any.whl
```

### Publish to plotly anaconda channel
From `packages/python/plotly-geo`, build the conda packge
```bash
(plotly_dev) $ conda build recipe/
```

Then upload to the plotly anaconda channel as described above

## Contributing to the Figure Factories
If you are interested in contributing to the ever-growing Plotly figure factory library in Python, check out the [documentation][ff-home] to learn how.

[ff-home]: packages/python/plotly/plotly/figure_factory/README.md
