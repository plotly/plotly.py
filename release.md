
# How to release plotly packages

## Release process - plotly package

This is the release process for releasing `plotly.py` version `X.Y.Z` with
`plotlywidget`/`jupyterlab-plotly` with matching versions.

Note: it's easier to lock all three versions together, even if it means we occasionally
push no-change versions to NPM/PyPI/Conda.

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
 1) Manually update the plotlywidget version to `X.Y.Z-rc.1` in the files
specified below.

 - `packages/python/plotly/plotly/_widget_version.py`:
   + Update `__frontend_version__` to `^X.Y.Z-rc.1` (Note the `^` prefix)
 - `packages/javascript/plotlywidget/package.json`
   + Update `"version"` to `X.Y.Z-rc.1`
   + Ensure you're using `node` version 8 and `npm` version 6 to minimize diffs to `package-lock.json`
   + Run `rm -rf node_modules && npm install && npm run build`
 - `packages/javascript/jupyterlab-plotly/package.json`
   + Update `"version"` to `X.Y.Z-rc.1`
   + Ensure you're using `node` version 8 and `npm` version 6 to minimize diffs to `package-lock.json`
   + Run `rm -rf node_modules && npm install && npm run build`

 2) Commit the changes

 3) Tag this commit on the release branch as `vX.Y.Zrc1`

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
(plotly_dev) $ cd packages/python/plotly
(plotly_dev) $ git checkout release_X.Y.Z
(plotly_dev) $ git stash
(plotly_dev) $ rm -rf dist
(plotly_dev) $ python setup.py sdist bdist_wheel
(plotly_dev) $ rm dist/*dirty*
(plotly_dev) $ twine upload dist/plotly-X.Y.Zrc1*
```

Note: this will intentionally fail if your current git tree is dirty, because we want the tag
to reflect what is being released, and the version number comes from the tag and the dirty-state.


### Publish release candidate of `plotlywidget` and `jupyterlab-plotly` to NPM
Now, publish the release candidate of the `plotlywidget` NPM package.

```bash
cd ./packages/javascript/plotlywidget
npm run build && npm publish --access public --tag next
```

The `--tag next` part ensures that users won't install this version unless
they explicitly ask for the version or for the version wtih the `next` tag.

Do the same in the `jupyterlab-plotly` directory.

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

### Finalize CHANGELOG and README
Update CHANGELOG with release date and update README with final versions.

In the conda installation instructions, be sure to change the
"-c plotly/label/test" argument to "-c plotly"

Update the doc/python/getting-started.md file with the same version numbers.

Commit Changelog, README and getting-started updates.

### Finalize versions
When no problems are identified in the release candidate, remove the
release candidate suffix from the following version strings:

 - `plotly/_widget_version.py`:
   + Update `__frontend_version__` to `^X.Y.Z` (Note the `^` prefix)
 - `packages/javascript/plotlywidget/package.json`
   + Update `"version"` to `X.Y.Z`
   + Ensure you're using `node` version 8 and `npm` version 6 to minimize diffs to `package-lock.json`
   + Run `rm -rf node_modules && npm install && npm run build`
 - `packages/javascript/jupyterlab-plotly/package.json`
   + Update `"version"` to `X.Y.Z`
   + Ensure you're using `node` version 8 and `npm` version 6 to minimize diffs to `package-lock.json`
   + Run `rm -rf node_modules && npm install && npm run build`
 - Run `git diff` and ensure that only the files you modified and the build artifacts have changed
 - Ensure that the diff in `package-lock.json` seems sane
 - Commit and push to the release branch.

### Merge release into master
Make sure the integration tests are passing on the release branch, then merge
it into master on GitHub.

Make sure tests also pass on master, then update your local master,
tag this merge commit as `vX.Y.Z` (e.g. `v3.1.1`)

push the tag.

```bash
(plotly_dev) $ git checkout master
(plotly_dev) $ git stash
(plotly_dev) $ git pull origin master
(plotly_dev) $ git tag vX.Y.Z
(plotly_dev) $ git push origin vX.Y.Z
```

### Publishing to PYPI

Publish the final version to PyPI

```bash
(plotly_dev) $ cd packages/python/plotly
(plotly_dev) $ rm -rf dist
(plotly_dev) $ python setup.py sdist bdist_wheel
(plotly_dev) $ rm dist/*dirty*
(plotly_dev) $ twine upload dist/plotly-X.Y.Z*
```

Note: this will intentionally fail if your current git tree is dirty, because we want the tag
to reflect what is being released, and the version number comes from the tag and the dirty-state.

After it has uploaded, move to another environment and double+triple check that you are able to upgrade ok:
```bash
$ pip install plotly --upgrade
```

And ask one of your friends to do it too. Our tests should catch any issues, but you never know.

<3 Team Plotly

### Publish widget library to npm
Finally, publish the final version of the widget library to npm with:

```bash
cd packages/javascript/jupyterlab-plotly
npm run build && npm publish --access public
cd packages/javascript/plotlywidget
npm run build && npm publish --access public
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

Then upload to the plotly anaconda channel as described above.
