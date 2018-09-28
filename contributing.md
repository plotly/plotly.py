# Contributing

The bottom line. Follow your Nose, or our Nose. Write-run-love tests :fist:.

## Code of Conduct

Check out the [Code of Conduct](CODE_OF_CONDUCT.md). Don't tl:dr; it, but the general idea is to be nice.

## Have a Bug Report?

Open an issue! Go to https://github.com/plotly/plotly.py/issues. It's possible that your issue was already addressed. If it wasn't, open it. We also accept PRs; take a look at the steps below for instructions on how to do this.

## Have Questions about Plotly?

Check out our Support App: https://support.plot.ly/libraries/python or Community Forum: https://community.plot.ly/.

## Setup

### Fork, Clone, Setup Your Version of the Plotly Python API

First, you'll need to *get* our project. This is the appropriate *clone* command (if you're unfamiliar with this process, https://help.github.com/articles/fork-a-repo):

**DO THIS (in the directory where you want the repo to live)**

```bash
git clone https://github.com/your_github_username/plotly.py.git
```

### Submodules

Second, this project uses git submodules! They're both helpful and, at times, difficult to work with. The good news is you probably don't need to think about them! Just run the following shell command to make sure that your local repo is wired properly:

**DO THIS (run this command in your new `plotly.py` directory)**

```bash
make setup_subs
```

That's going to initialize the submodules we use in this project, update them so that they're synced to the proper commit, and copy files to the appropriate locations in your local repo.

Here's what you need to know: changes to any files inside the following directories **will get overwritten**. These are synced with the submodules, if you need to change functionality there, you will need to make a pull request in the appropriate sub project repository.
- chunked_requests
- graph_reference
- mplexporter

Additionally, there are some project shortcuts that live in the `makefile` file. You can read all about this in the `make_instructions.txt` file. OR, just run:

```bash
make readme
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

## Suggestions

### Local Python
Setting up Python versions that *don't* require you to use `sudo` is a good idea. In addition, the core Python on your machine may not be the Python that we've developed in! Here are some nice guides for Mac, Windows, and Linux:
- http://docs.python-guide.org/en/latest/starting/install/osx/
- http://docs.python-guide.org/en/latest/starting/install/win/
- http://docs.python-guide.org/en/latest/starting/install/linux/

### Virtualenv
Virtualenv is a way to create Python environments on your machine that know nothing about one another. This is really helpful for ironing out dependency-problems arising from different versions of packages. Here's a nice guide on how to do this: http://docs.python-guide.org/en/latest/dev/virtualenvs/

### Alter Your PYTHONPATH
The PYTHONPATH variable in your shell tells Python where to look for modules. Since you'll be developing, it'll be a pain to need to *install* Python every time you need to test some functionality (or at least ensure you're running code from the right directory...). You can easily make this change from a shell:

```bash
export PYTHONPATH="/path/to/local/repo:$PYTHONPATH"
```

Note, that's non-permanent. When you close the shell, that variable definition disappears. Also, `path/to/local/repo` is *your* specific repository path (e.g., `/Users/andrew/projects/python-api`).

### Why?

Now you can run the following code and be guaranteed to have a working development version that you can make changes to on-the-fly, test, and be confident will not break on other's machines!

```bash
pip install -r requirements.txt
pip install -r optional-requirements.txt
export PYTHONPATH="/path/to/local/repo:$PYTHONPATH"
```

## Dependencies

There's a short list of core dependencies you'll need installed in your Python environment to have any sort of fun with Plotly's Python API (see `requirements.txt`). Additionally, you're likely to have even more fun if you install some other requirements (see `optional-requirements.txt`).

### Dependencies and Virtualenv

If you decided to follow the suggestion about the Virtualenv *and* you've run `source bin/activate` within your new virtualenv directory to activate it--you can run the following to install the core dependencies:

```bash
pip install -r requirements.txt
```

To install the optional dependencies:

```bash
pip install -r optional-requirements.txt
```

## ipywidget development install
    $ jupyter nbextension enable --py widgetsnbextension
    $ jupyter nbextension install --py --symlink --sys-prefix plotlywidget
    $ jupyter nbextension enable --py --sys-prefix plotlywidget

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
nosetests -w plotly/tests
```

Or for more *verbose* output:

```bash
nosetests -w plotly/tests -v
```

Either of those will run *every* test we've written for the Python API. You can get more granular by running something like:

```bash
nosetests -w plotly/tests/test_plotly
```

... or even more granular by running something like:

```bash
nosetests plotly/tests/test_plotly/test_plot.py
```

### Running tests with `tox`

Running tests with tox is much more powerful, but requires a bit more setup.

You'll need to export an environment variable for *each* tox environment you wish to test with. For example, if you want to test with `Python 2.7` and
`Python 3.4`, but only care to check the `core` specs, you would need to ensure that the following variables are exported:

```
export PLOTLY_TOX_PYTHON_27=<python binary>
export PLOTLY_TOX_PYTHON_34=<python binary>
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

### Release process

This is the release process for releasing `plotly.py` version `X.Y.Z` with
`plotlywidget` version `A.B.C`.

Note: The `plotlywidget` instructions must be followed if any change
has been made in the `js/` directory source code, OR if the version of
plotly.js has been updated.  If neither of these is the case, there's no need
to increment the `plotlywidget` version or to publish a new version to npm.

#### Create a release branch
After all of the functionality for the release has been merged into master,
create a branch named `release_X.Y.Z`. This branch will become the
final version

#### Bump to release candidate version
Next increment the version of `plotly.py` to `X.Y.Zrc1`, and the version of
`plotlywidget` to `A.B.C-rc.1`. In both cases `rc` is the semantic versioning
code for Release Candidate. The number 1 means that this is the first release
candidate, this number can be incremented if we need to publish multiple
release candidates. Note that the `npm` suffix is `-rc.1` and the PyPI
suffix is `rc1`.

 - `plotly/version.py`:
   + Update `__version__` to `X.Y.Zrc1`
   + Update `__frontend_version__` to `^A.B.C-rc.1` (Note the `^` prefix)
 - `js/package.json`
   + Update `"version"` to `A.B.C-rc.1`
 
Publishing `plotly.py` and `plotlywidget` as release candidates
allows us to go through the publication process, and test that the
installed packages work properly before general users will get them by
default. It also gives us the opportunity to ask specific users to test
that their bug reports are in fact resolved before we pull the trigger
on the official release.

#### Finalize changelog
Review the contents of `CHANGELOG.md`. We try to follow the
[keepachangelog](https://keepachangelog.com/en/1.0.0/) guidelines.  Make sure
the changelog includes the version being published at the top, along with the
expected publication date.

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

#### Update README.md installation instructions

Update the installation instructions in the README to the new versions of all
of the dependencies. Use the release candidate versions, this way we can point
people to the README of the `release_X.Y.Z` as the instructions for trying out
the release candidate.

#### Publish release candidate to PyPI
To upload to PyPI you'll also need to have `twine` installed:
```bash
(plotly.py) $ pip install twine
```

And, you'll need the credentials file `~/.pypirc`. Request access from
@theengineear and @chriddyp. Then, from inside the repository:

```bash
(plotly.py) $ git checkout release_X.Y.Z
(plotly.py) $ git stash
(plotly.py) $ python setup.py sdist bdist_wheel
(plotly.py) $ twine upload dist/plotly-X.Y.Zrc1*
```

#### Publish release candidate of `plotlywidget` to NPM
Now, publish the release candidate of the `plotlywidget` NPM package.

```bash
cd ./js
npm publish --access public --tag next
```

The `--tag next` part ensures that users won't install this version unless
they explicitly ask for the version or for the version wtih the `next` tag.

#### Publish release candidate to plotly anaconda channel
Conda packages are built automatically on circleci for each push where all
tests pass on `master` and `release_` branches.

Conda packages for Python X.Y are included as "artifacts" of the circleci
job named `python-X-Y-conda`.

First download the artifacts for each Python version: 
 - Click the "Details" button next to check named " ci/circleci: python-X-Y-conda". This will take you to the circleci dashboard for that job.
 - Click on the "Artifacts" tab, and expend the directory tree to root/project/artifacts/conda_packages_X.Y.zip.
 - Click to download this zip file.

Then unzip all of the artifact zip files into the same directory. You should
end up with a directory structure like
 - /path/to/packages
   - conda_packages_2_7
     - win-64
       - plotly-X.Y.Z-py27_0.tar.bz2
     - win-32
       - plotly-X.Y.Z-py27_0.tar.bz2
     - linux-64
       - plotly-X.Y.Z-py27_0.tar.bz2
     - ...
   - conda_packages_3_5
     - win-64
       - plotly-X.Y.Z-py35_0.tar.bz2
     - ...
   - conda_packages_3_6
     - ...
   - conda_packages_3_7
     - ...

Next run `anaconda login` and enter the credentials for the plotly anaconda
channel.
          
Then upload artifacts to the anaconda channel using the test label. Using the test
label will ensure that people will only download the release candidate version
if they explicitly request it.

```
$ anaconda upload --label test /path/to/packages/conda_packages_*/*/plotly-*.tar.bz2 
```

Then logout with `anaconda logout` 

#### Manually test the release candidate
Create a fresh virtual environment (or conda environment) and install
the release candidate by following the new `README.md` instructions,
replacing `X.Y.Z` with `X.Y.Zrc1` and `A.B.C` with `A.B.C-rc.1`.

In particular 
 - `pip install plotly==X.Y.Z` -> `pip install plotly==X.Y.Zrc1`
 - `jupyter labextension install plotlywidget@A.B.C` ->
    `jupyter labextension install plotlywidget@A.B.C-rc.1`

Run through the example notebooks at
https://github.com/jonmmease/plotly_ipywidget_notebooks using the classic
notebook and JupyterLab. Make sure `FigureWidget` objects are displayed as
plotly figures, and make sure the in-place updates and callbacks work.

If appropriate, ask users who have submitted bug reports or feature 
requests that are resolved in this version to try out the release candidate.

If problems are found in the release candidate, fix them on the release
branch and then publish another release candidate with the candidate number
incremented.

#### Finalize versions
When no problems are identified in the release candidate, remove the
release candidate suffix from the following version strings:
 
 - `plotly/version.py`:
   + Update `__version__` to `X.Y.Z`
   + Update `__frontend_version__` to `^A.B.C` (Note the `^` prefix)
 - `js/package.json`
   + Update `"version"` to `A.B.C`

#### Merge release into master
Make sure the integration tests are passing on the release branch, then merge
it into master on GitHub.

Make sure tests also pass on master, then update your local master,
tag this merge commit as `vX.Y.Z` (e.g. `v3.1.1`), and push the tag.

```bash
(plotly.py) $ git checkout master
(plotly.py) $ git stash
(plotly.py) $ git pull origin master
(plotly.py) $ git tag vX.Y.Z
(plotly.py) $ git push origin vX.Y.Z
```

#### Publishing to Pip

Publish the final version to PyPI

```bash
(plotly.py) $ python setup.py sdist bdist_wheel
(plotly.py) $ twine upload dist/plotly-X.Y.Z*
```

After it has uploaded, move to another environment and double+triple check that you are able to upgrade ok:
```bash
$ pip install plotly --upgrade
```

And ask one of your friends to do it too. Our tests should catch any issues, but you never know.

<3 Team Plotly

#### Publish widget library to npm
Finally, publish the final version of the widget library to npm with:

```bash
cd ./js
npm publish --access public
```

#### Publishing to the plotly conda channel
Follow the anaconda upload instructions as described for the release candidate
above, except:

 - Download the package artifacts from the circleci jobs that ran against
   master.
 - Do not include the `--label test` argument when uploading
 
```
$ anaconda upload /path/to/packages/conda_packages_*/*/plotly-*.tar.bz2 
```

#### Add GitHub Release entry
Go to https://github.com/plotly/plotly.py/releases and "Draft a new release"

Enter the vX.Y.Z tag

Make "Release title" the same string as the tag.

Copy changelog section for this version as the "Describe this release"

#### Post announcement
Post a simple announcement to the Plotly Python forum, with links to the
README installation instructions and to the CHANGELOG.

# Contributing to the Figure Factories
If you are interested in contributing to the ever-growing Plotly figure factory library in Python, check out the [documentation](https://github.com/plotly/plotly.py/blob/master/plotly/figure_factory/README.md) to learn how.
