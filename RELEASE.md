
# Release guide

## Release process - full release of `plotly` package

This is the release process for releasing `plotly.py` version `X.Y.Z`, including changelogs, Github release and forum announcement.

### Finalize changelog

Review the contents of `CHANGELOG.md`. We try to follow
the [keepachangelog](https://keepachangelog.com/en/1.0.0/) guidelines.
Make sure the changelog includes the version being published at the top, along
with the expected publication date.

Use the `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`
labels for all changes to plotly.py.  If the version of plotly.js has
been updated, include this as the first `Updated` entry. Call out any
notable changes as sub-bullets (new trace types in particular), and provide
a link to the plotly.js CHANGELOG.

### Finalize versions

**Create a branch `git checkout -b release-X.Y.Z` *from the tip of `origin/master`*.**

Manually update the versions to `X.Y.Z` in the files specified below.

 - `pyproject.toml`
   + update version
 - `CHANGELOG.md`
   + update the release date
 - Commit your changes on the branch:
   + `git commit -a -m "version changes for vX.Y.Z"`
 - Create a tag for Github release
   + `git tag vX.Y.Z`
   + `git push --atomic origin release-X.Y.Z vX.Y.Z`
 - Create a Github pull request from `release-X.Y.Z` to `main` and wait for CI to be green

### Download and QA CI Artifacts

The `full_build` job in the `release_build` workflow in CircleCI produces a tarball of artifacts `output.tgz` which you should download and decompress, which will give you a directory called `output`. The filenames contained within will contain version numbers.

To locally install the PyPI dist, make sure you have an environment with JupyterLab installed (maybe one created with `conda create -n condatest python=3.10 jupyter anywidget pandas`):

- `tar xzf output.tgz`
- `pip uninstall plotly`
- `conda uninstall plotly` (just in case!)
- `pip install path/to/output/dist/plotly-X.Y.X-py3-none-any.whl`

You'll want to check, in both Lab and Notebook, **in a brand new notebook in each** so that there is no caching of previous results, that `go.Figure()` and `go.FigureWidget()` work without error.

### Publishing

Once you're satisfied that things render in Lab and Notebook in Widget and regular mode,
you can publish the artifacts. **You will need special credentials from Plotly leadership to do this.**.


Publishing to PyPI:
```bash
(plotly_dev) $ cd path/to/output
(plotly_dev) $ twine upload plotly-X.Y.Z*
```

### Merge the PR and make a Release

1. Merge the pull request you created above into `main`
2. Go to https://github.com/plotly/plotly.py/releases and "Draft a new release"
3. Enter the `vX.Y.Z` tag you created already above and make "Release title" the same string as the tag.
4. Copy the changelog section for this version as the "Describe this release"

### Update documentation site

1. Search for the previous version string in the docs and replace it with the new version string, including but not necessarily limited to the following files:
    - `doc/apidoc/conf.py`
    - `doc/requirements.txt`
2. `doc-prod` should already have been merged on a regular basis into `main`, but
start by doing it first if not. Then merge `main` into `doc-prod` to deploy the doc related
to features in the release.
3. in a clone of the [`graphing-library-docs` repo](https://github.com/plotly/graphing-library-docs):
    1. bump the version of Plotly.py in  `_data/pyversion.json`
    2. bump the version of Plotly.js with `cd _data && python get_plotschema.py <PLOTLY.JS VERSION>` fixing any errors that come up.
      - If Plotly.js contains any new traces or trace or layout attributes, you'll get a warning `“missing key in attributes: <attribute-name>`. To resolve, add the attribute to the relevant section in `/_data/orderings.json` in the position you want it to appear in the reference docs.
    3. rebuild the Algolia `schema` index with `ALGOLIA_API_KEY=<key> make update_ref_search`
    4. Rebuild the Algolia `python` index with `ALGOLIA_API_KEY=<key> make update_python_search`
    5. Commit and push the changes to `master` in that repo

### Notify Stakeholders

* Post an announcement to the Plotly Python forum, with links to the README installation instructions and to the CHANGELOG.
* Update the previous announcement to point to this one
* Update the Github Release entry and CHANGELOG entry to have the nice title and a link to the announcement
* Follow up on issues resolved in this release or forum posts with better answers as of this release

## Release process - Release *Candidate* of `plotly` package

(rough notes for a rough/ad hoc process!)

It's the same process as above except that the `X.Y.Z` version has a suffix and there are special instructions below for publishing an RC: note that the `npm` suffix is `-rc.1` and the PyPI suffix is `rc1`. We also don't update the docs with RC information and we inform a limited number of stakeholders.

PyPI RC (no special flags, just the `rc1` suffix):

```bash
(plotly_dev) $ twine upload dist/plotly-X.Y.Zrc1*
```

The `--tag next` part ensures that users won't install this version unless
they explicitly ask for the version or for the version with the `next` tag.
