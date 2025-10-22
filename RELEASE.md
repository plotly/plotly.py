
# Release guide

## Release process - full release of `plotly` package

This is the release process for releasing plotly.py version `X.Y.Z`, including changelogs, GitHub release and forum announcement.

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

### Update version numbers

**Create a release branch `git checkout -b release-X.Y.Z` _from the tip of `origin/main`_.**

- Manually update the versions to `X.Y.Z` in the files specified below:
  - `pyproject.toml`
    - update version
  - `CHANGELOG.md`
    - update version and release date
    - finalize changelog entries according to instructions above
  - `CITATION.cff`
    - update version and release date
- Run `uv lock` to update the version number in the `uv.lock` file (do not update manually)
- Commit and push your changes to the release branch:
    ```sh
    $ git add -u
    $ git commit -m "version changes for vX.Y.Z"
    $ git push
    ```
- Create a GitHub pull request from `release-X.Y.Z` to `main` and wait for CI to be green
- On the release branch, create and push a tag for the release:
    ```sh
    $ git tag vX.Y.Z
    $ git push origin vX.Y.Z
    ```

### Manual QA in Jupyter

We don't currently have automated tests for Jupyter, so we do this QA step manually.

The `full_build` job in the `release_build` workflow in CircleCI produces a tarball of artifacts `output.tgz` 
which you should download and decompress, which will give you a directory called `output`. The filenames within 
will contain version numbers; make sure the version numbers are correct.

Set up an environment with Jupyter, AnyWidget, and Pandas installed (`pip install jupyter anywidget pandas`). Then:

- unzip downloaded `output.tgz`
- `pip uninstall plotly`
- `pip install path/to/output/dist/plotly-X.Y.Z-py3-none-any.whl`

You'll want to check, in both JupyterLab (launch with `jupyter lab`) and Jupyter Notebook (launch with `jupyter notebook`), 
that `go.Figure()` and `go.FigureWidget()` work as expected. 

Notes:
- **Start by creating a brand new notebook each time** so that there is no caching of previous results
- **Do not run the Jupyter commands from the root `plotly.py/` directory on your machine** because Jupyter may be confused 
by metadata from previous plotly.py builds

Code for testing `go.Figure()`:
```python
import plotly
import plotly.graph_objects as go

print(plotly.__version__)  # Make sure version is correct
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4], y=[1, 3, 2, 4]))
fig.show()  # Figure should render in notebook
```

Code for testing `go.FigureWidget()`:
```python
import plotly
import plotly.graph_objects as go

print(plotly.__version__)  # Make sure version is correct
fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4], y=[1, 3, 2, 4]))
figure_widget = go.FigureWidget(fig)
figure_widget  # Figure should render in notebook
```

Once these are verified working, you can move on to publishing the release.

### Merge the release PR and make a GitHub release

- Merge the pull request you created above into `main`
- Go to https://github.com/plotly/plotly.py/releases and "Draft a new release"
- Enter the `vX.Y.Z` tag you created already above and make "Release title" the same string as the tag.
- Copy the changelog section for this version into "Describe this release"
- Upload the build artifacts downloaded in the previous step (`.tar` and `.whl`)

### Publishing to PyPI

The final step is to publish the release to PyPI. **You will need special permissions from Plotly leadership to do this.**.

You must install first install [Twine](https://pypi.org/project/twine/) (`pip install twine`) if not already installed.

Publishing to PyPI:
```bash
(plotly_dev) $ cd path/to/output
(plotly_dev) $ twine upload plotly-X.Y.Z*
```

You will be prompted to enter an API token; this can be generated in your PyPI account settings. 
Your account must have permissions to publish to the `plotly` project on PyPI.

### Update documentation site

1. Search for the previous version string in the docs and replace it with the new version string, including but not necessarily limited to the following files:
    - `doc/apidoc/conf.py`
    - `doc/requirements.txt`
2. `doc-prod` should already have been merged on a regular basis into `main`, but
start by doing it first if not. Then merge `main` into `doc-prod` to deploy the doc related
to features in the release.
3. in a clone of the [`graphing-library-docs` repo](https://github.com/plotly/graphing-library-docs):
    1. bump the version of plotly.py in  `_data/pyversion.json`
    2. bump the version of plotly.js with `cd _data && python get_plotschema.py <PLOTLY.JS VERSION>` fixing any errors that come up.
      - If plotly.js contains any new traces or trace or layout attributes, you'll get a warning `“missing key in attributes: <attribute-name>`. To resolve, add the attribute to the relevant section in `/_data/orderings.json` in the position you want it to appear in the reference docs.
    3. rebuild the Algolia `schema` index with `ALGOLIA_API_KEY=<key> make update_ref_search`
    4. Rebuild the Algolia `python` index with `ALGOLIA_API_KEY=<key> make update_python_search`
    5. Commit and push the changes to `master` in that repo

### Notify Stakeholders

* Post an announcement to the [Plotly Python forum](https://community.plotly.com/c/plotly-python/5), with links to the README installation instructions and to the CHANGELOG.
* Update the previous announcement to point to this one
* Update the GitHub Release entry and CHANGELOG entry to have the nice title and a link to the announcement
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
