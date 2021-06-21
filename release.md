
# How to release plotly packages

There are 3 Python packages (`plotly`, `plotly-geo` and `chart-studio`) which need to be
published to PyPI and conda, and 1 JS packages (`jupyterlab-plotly`)
which need to be published to NPM. In addition, there are various changelogs, github
releases and forum announcements to do :)

## Release process - `plotly` package and extensions

This is the release process for releasing `plotly.py` version `X.Y.Z` with
`jupyterlab-plotly` with matching versions.

> Note: it's easier to lock the JS extension and Python versions together, even if it means we occasionally
> push no-change versions to NPM/PyPI/Conda.

### Finalize changelog

Review the contents of `packages/python/plotly/CHANGELOG.md`. We try to follow
the [keepachangelog](https://keepachangelog.com/en/1.0.0/) guidelines.
Make sure the changelog includes the version being published at the top, along
with the expected publication date.

Use the `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`
labels for all changes to plotly.py.  If the version of plotly.js has
been updated, include this as the first `Updated` entry. Call out any
notable changes as sub-bullets (new trace types in particular), and provide
a link to the plotly.js CHANGELOG.

### Finalize versions

Manually update the versions to `X.Y.Z` in the files
specified below.

 - `CHANGELOG.md`
   + update the release date
 - `packages/python/plotly/README.md`
   + this must be done at this point because the README gets baked into PyPI
 - `plotly/_widget_version.py`:
   + Update `__frontend_version__` to `^X.Y.Z` (Note the `^` prefix)
 - `packages/javascript/jupyterlab-plotly/package.json`
   + Update `"version"` to `X.Y.Z`
   + Ensure you're using `node` version 12 and `npm` version 6 to minimize diffs to `package-lock.json`
   + Ensure you're in a Python virtual environment with JupyterLab 3 installed
   + Run `rm -rf node_modules && npm install && npm run build:prod`
 - This the last good time to install the extensions locally and check that everything works in dev mode
 - Run `git diff` and ensure that only the files you modified and the build artifacts have changed
 - Ensure that the diff in `package-lock.json` seems sane
 - Commit and tag but *don't push* until after everything is available on NPM/PyPI/Conda (see below):
   + `git commit -a -m "release vX.Y.Z"`
   + `git tag vX.Y.Z`

### Publish JS Extensions to NPM

Build and publish the final version of the extensions to NPM. We do this first because
once we push to PyPI the README will refer to these versions.

```bash
cd packages/javascript/jupyterlab-plotly
npm run build && npm publish --access public
```

Final checks could be done here if desired.

### Publishing to PyPI

Build and publish the final version to PyPI.

```bash
(plotly_dev) $ git status # make sure it's not dirty!
(plotly_dev) $ cd packages/python/plotly
(plotly_dev) $ rm -rf dist
(plotly_dev) $ python setup.py sdist bdist_wheel
(plotly_dev) $ rm -f dist/*dirty*
(plotly_dev) $ twine upload dist/plotly-X.Y.Z*
```

Note: this will intentionally fail if your current git tree is dirty, because we want the tag
to reflect what is being released, and the version number comes from the tag and the dirty-state.

After it has uploaded, move to another environment and double+triple check that you are able to upgrade ok:
```bash
$ pip install plotly --upgrade
```

And ask one of your friends to do it too. Our tests should catch any issues, but you never know.

### Publishing to the plotly conda channel

To publish package to the plotly anaconda channel you'll need to have the
anaconda or miniconda distribution installed, and you'll need to have the
`anaconda-client` package installed.

```bash
(plotly_dev) $ conda config --set anaconda_upload no
(plotly_dev) $ conda build recipe/
```

Then upload artifacts to the anaconda channel by running the upload command that `conda`
provides, which looks something like this:

```
$ anaconda upload /path/to/anaconda3/conda-bld/noarch/plotly-*.tar.bz2
```

### Push the commit and add GitHub Release entry

```bash
(plotly_dev) $ git push origin master
(plotly_dev) $ git push origin vX.Y.Z
```

1. Go to https://github.com/plotly/plotly.py/releases and "Draft a new release"
2. Enter the `vX.Y.Z` tag you created already above and make "Release title" the same string as the tag.
3. Copy the changelog section for this version as the "Describe this release"

### Update documentation site

1. Search for the previous version string in the docs and replace it with the new version string, including but not necessarily limited to the following files:
    - `doc/python/getting-started.md`
    - `doc/apidoc/conf.py`
    - `doc/requirements.txt`
    - `binder/requirements.txt`
2. `doc-prod` should already have been merged on a regular basis into `master`, but
start by doing it first if not. Then merge `master` into `doc-prod` to deploy the doc related
to features in the release.
3. in a clone of the [`graphing-library-docs` repo](https://github.com/plotly/graphing-library-docs):
    1. bump the version of Plotly.js with `cd _data && python get_plotschema.py <PLOTLY.JS VERSION>` fixing any errors that come up
    2. rebuild the Algolia `schema` index with `ALGOLIA_API_KEY=<key> make update_ref_search`
    3. Rebuild the Algolia `python` index with `ALGOLIA_API_KEY=<key> make update_python_search`
    4. Commit and push the changes to `master` in that repo

### Notify Stakeholders

* Post an announcement to the Plotly Python forum, with links to the README installation instructions and to the CHANGELOG.
* Update the previous announcement to point to this one
* Update the Github Release entry and CHANGELOG entry to have the nice title and a link to the announcement
* Follow up on issues resolved in this release or forum posts with better answers as of this release

## Release *Candidate* process - `plotly` package


### Bump to release candidate version

 1) Manually update the versions to `X.Y.Z-rc.1` in the files
specified below.

 - `packages/python/plotly/plotly/_widget_version.py`:
   + Update `__frontend_version__` to `^X.Y.Z-rc.1` (Note the `^` prefix)
 - `packages/javascript/jupyterlab-plotly/package.json`
   + Update `"version"` to `X.Y.Z-rc.1`
   + Ensure you're using `node` version 12 and `npm` version 6 to minimize diffs to `package-lock.json`
   + Ensure you're in a Python virtual environment with JupyterLab 3 installed
   + Run `rm -rf node_modules && npm install && npm run build:prod`

 2) Commit the changes

 3) Tag this commit on the release branch as `vX.Y.Zrc1`

In both cases `rc` is the semantic versioning code for Release Candidate.

The number 1 means that this is the first release candidate, this number can
be incremented if we need to publish multiple release candidates.
Note that the `npm` suffix is `-rc.1` and the PyPI suffix is `rc1`.

Publishing `plotly.py` and `jupyterlab-plotly` as release candidates
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

And, you'll need to be a maintainer on PyPI. Then, from inside the repository:

```bash
(plotly_dev) $ cd packages/python/plotly
(plotly_dev) $ git checkout release_X.Y.Z
(plotly_dev) $ git stash
(plotly_dev) $ rm -rf dist
(plotly_dev) $ python setup.py sdist bdist_wheel
(plotly_dev) $ rm -f dist/*dirty*
(plotly_dev) $ twine upload dist/plotly-X.Y.Zrc1*
```

Note: this will intentionally fail if your current git tree is dirty, because we want the tag
to reflect what is being released, and the version number comes from the tag and the dirty-state.


### Publish release candidate of JS Extensions to NPM

Now, publish the release candidate of the extensions to NPM.

```bash
cd ./packages/javascript/jupyterlab-plotly
npm run build && npm publish --access public --tag next
```

The `--tag next` part ensures that users won't install this version unless
they explicitly ask for the version or for the version with the `next` tag.

### Publish release candidate to plotly anaconda channel

To publish package to the plotly anaconda channel you'll need to have the
anaconda or miniconda distribution installed, and you'll need to have the
`anaconda-client` package installed.

```bash
(plotly_dev) $ conda config --set anaconda_upload no
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

## Release process - `plotly-geo` package

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

From `packages/python/plotly-geo`, build the conda package
```bash
(plotly_dev) $ conda build recipe/
```

Then upload to the plotly anaconda channel as described above

## Release process - `chart-studio` package

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

From `packages/python/plotly-geo`, build the conda package
```bash
(plotly_dev) $ conda build recipe/
```

Then upload to the plotly anaconda channel as described above.
