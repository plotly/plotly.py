
# Release guide

## Release process - full release of `plotly` package

This is the release process for releasing plotly.py version `X.Y.Z`, including changelogs, GitHub release and forum announcement.

### Prerequisites

Ensure you have the following installed:

* `uv>=0.12.15`
* A virtual environment: `uv venv`
* Membership of the `libraries_admin` GitHub team

### Prepare local environment

* `git switch main && git pull`
* `git status`: ensure your working tree is clean
* `uv pip install -e ".[dev_optional]"`
* `cd js && npm ci && cd ..`

### Finalize changelog

Review the contents of `CHANGELOG.md` under the **Unreleased** header. We try to follow
the [keepachangelog](https://keepachangelog.com/en/1.0.0/) guidelines.

**Note: You don't need to update the "Unreleased" header with the new version number,
as that will be done automatically as part of the next step.**

Use the `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security`
labels for all changes to plotly.py.  If the version of plotly.js has
been updated, include this as the first `Updated` entry. Call out any
notable changes as sub-bullets (new trace types in particular), and provide
a link to the plotly.js CHANGELOG.

### Update version numbers

**Create a release branch `git checkout -b release-X.Y.Z` _from the tip of `origin/main`_.**

- Ensure that you have `npm` and `uv` installed in your environment

- Run the command `python commands.py bumpversion X.Y.Z`, which will update the version to X.Y.Z in the following places
  - `pyproject.toml`
  - `uv.lock`
  - `js/package.json`
  - `js/package-lock.json`
  - `plotly/labextension/*`
  - `CHANGELOG.md` (Adds a new header for X.Y.Z above the unreleased items)
  - `CITATION.cff`

- Run `git diff` and ensure the above files were all updated correctly.
  - Note: The current date is used as the release date in `CHANGELOG.md` and `CITATION.cff`. If you want to use a different date, edit these files manually afterward.
  - If the bumpversion command failed for any reason, you can update the versions yourself by doing the following:
    - Manually update the version number (and release date, as needed) in `pyproject.toml`, `CHANGELOG.md` and `CITATION.cff`
    - Run `uv lock` to update `uv.lock`
    - From the `js/` dir, run `npm version X.Y.Z` to update `js/package.json` and `js/package-lock.json`
    - From the `js/` dir, run `npm run build:labextension` to regenerate the files in `plotly/labextension/`

- Commit and push the changed files to the release branch:
    ```sh
    $ git add -A
    $ git commit -m "version changes for vX.Y.Z"
    $ git push
    ```
- Create a GitHub pull request from `release-X.Y.Z` to `main`, wait for CI to be green and approval, and merge it
- Create and push the tag on the merge commit on `main`. The publish workflow rejects tags that are not reachable from `main`:
    ```sh
    $ git switch main && git pull
    $ git tag vX.Y.Z
    $ git push origin vX.Y.Z
    ```

### Start the publish workflow

1. Go to the [Publish to PyPI workflow](https://github.com/plotly/plotly.py/actions/workflows/publish-pypi.yml) and choose "Run workflow".
2. Leave the branch as `main` (the `pypi` environment only deploys from `main`) and enter the tag, for example `v7.1.0` or `v7.1.0rc0`.
3. The workflow validates the tag, builds the wheel and sdist from it once, and checks that the wheel and sdist (which are named after the version in `pyproject.toml`) carry the tag's version. It then waits for approval of the `pypi` environment.

The accepted tag shapes are `vX.Y.Z`, `vX.Y.ZaN`, `vX.Y.ZbN` and `vX.Y.ZrcN`. Anything else (`.dev`, `.post`, `-rc.1`) is rejected before anything is built.

### Manual QA in Jupyter

We don't currently have automated tests for Jupyter, so we do this QA step manually, while the workflow waits for approval.

When the `build` job finishes, open the workflow run and download the `dist` artifact. The filenames
will contain version numbers; make sure the version numbers are correct. These are the exact files
that will be uploaded to PyPI and attached to the GitHub release.

Set up an environment with Jupyter, AnyWidget, and Pandas installed (`pip install jupyter anywidget pandas`). Then:

- unzip the downloaded `dist` artifact
- `pip uninstall plotly`
- `pip install path/to/dist/plotly-X.Y.Z-py3-none-any.whl`

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

### If QA fails

Nothing is published until you approve the `pypi` deployment, so a problem found before that point can be fixed in place and the same version number reused.

1. If the run is waiting for approval, open it, choose "Review deployments", select `pypi`, and choose "Reject". The run fails, nothing is uploaded to PyPI and no GitHub release is created. (If a build or validation job already failed, there is nothing to reject.)
2. Fix the problem on `main` through the normal PR process.
3. Move the tag to the new tip of `main`:
    ```sh
    $ git switch main && git pull
    $ git tag -d vX.Y.Z
    $ git push origin :refs/tags/vX.Y.Z
    $ git tag vX.Y.Z
    $ git push origin vX.Y.Z
    ```
4. Run the publish workflow again with the same tag and redo QA on the new `dist` artifact.

Once PyPI has accepted the files, the version number is taken permanently. PyPI doesn't allow a file name to be uploaded again, even after the file is deleted. If a problem is found after the upload, fix it on `main` and release a new version number.

### Publish the GitHub release

**Only members of the `libraries_admin` team can approve publishing to PyPI.**

1. In the workflow run, choose "Review deployments", select `pypi`, and approve. To abandon the release, reject instead; nothing is uploaded and no GitHub release is created.
2. The workflow uploads the QA'd files to PyPI with trusted publishing (no API token needed).
3. Only after PyPI accepts the files, the workflow creates and publishes a GitHub release for the tag with the same files attached and the notes copied from the version's section of `CHANGELOG.md`. The pre-release flag is set from the version (`a`, `b` and `rc` versions are pre-releases), and the workflow fails if the flag and the version disagree.
4. Open the release and edit the notes if they need polish (for example the title and a link to the forum announcement, see "Notify Stakeholders").

If the upload step fails, no GitHub release is created. Fix the cause and re-run the workflow for the same tag; files already on PyPI are skipped. If the GitHub release step fails after PyPI succeeded, delete any partial release and re-run.

### Update documentation site

1. Search for the previous version string in the docs and replace it with the new version string, including but not necessarily limited to the following files:
    - `doc/apidoc/conf.py`
    - `doc/requirements.txt`
2. `doc-prod` should already have been merged on a regular basis into `main`, but
start by doing it first if not. Then merge `main` into `doc-prod` to deploy the doc related
to features in the release.
3. in a clone of the [`graphing-library-docs` repo](https://github.com/plotly/graphing-library-docs):
    1. bump the version of plotly.py in `_data/pyversion.json`
    2. bump the version of plotly.js with `cd _data && python get_plotschema.py <PLOTLY.JS VERSION>` fixing any errors that come up.

       **About `_data/orderings.json`:** `get_plotschema.py` downloads the raw `plot-schema.json` from the specified plotly.js release and uses `_data/orderings.json` (which lives in `graphing-library-docs`, not plotly.js) to determine the order in which traces, trace attributes, and layout attributes appear in the [reference documentation](https://plotly.com/python/reference/). The file has three sections:
       - `layout` — top-level layout attributes (e.g. `hovermode`, `clickmode`, `xaxis`)
       - `traces` — order of trace types (e.g. `scatter`, `bar`, `pie`)
       - `trace_attr_order` — order of attributes shared across traces

       If plotly.js adds new traces or trace/layout attributes that aren't listed in `orderings.json`, `get_plotschema.py` prints a warning like `missing key in attributes: <attribute-name>` and appends the missing entry to the end of its section. To resolve:

       - Add each missing attribute to the appropriate section of `/_data/orderings.json` in the position you want it to appear in the reference docs.
       - When in doubt about trace-attribute placement, match plotly.js's native order: open the regenerated `_data/plotschema.json` and find where plotly.js itself places the attribute (e.g. inspect a representative trace's `attributes` keys in order). Following the native order keeps related attributes grouped (for example, `texttemplate` → `texttemplatefallback`).
       - For new top-level layout attributes, group them with semantically related entries rather than appending to the end (for example, a new click-behavior attribute like `clickanywhere` belongs next to `clickmode`).
       - Re-run `python get_plotschema.py <PLOTLY.JS VERSION>` after editing `orderings.json` and confirm the warnings are gone.
    3. Rebuild the Algolia `schema` index with `ALGOLIA_API_KEY=<key> make update_ref_search`
    4. Rebuild the Algolia `python` index with `ALGOLIA_API_KEY=<key> make update_python_search`
    5. Commit and push the changes to `master` in that repo

### Notify Stakeholders

* Post an announcement to the [Plotly Python forum](https://community.plotly.com/c/plotly-python/5), with links to the README installation instructions and to the CHANGELOG.
* Update the previous announcement to point to this one
* Update the GitHub Release entry and CHANGELOG entry to have the nice title and a link to the announcement
* Follow up on issues resolved in this release or forum posts with better answers as of this release

## Release process - Release *Candidate* of `plotly` package

(rough notes for a rough/ad hoc process!)

It's the same process as above except that the version has an `a`, `b` or `rc` suffix, for example `python commands.py bumpversion 7.1.0rc0` and tag `v7.1.0rc0`. Alpha and beta versions work the same way. The `npm` form of the version uses a dash (`7.1.0-rc0`) and `npm version` normalizes it automatically during `bumpversion`. We also don't update the docs with RC information and we inform a limited number of stakeholders.

The publish workflow derives "pre-release" from the version, so no extra flags are needed. A pre-release is uploaded to PyPI as a pre-release and its GitHub release is flagged as a pre-release. A stable version is never flagged as a pre-release, and the other way round.

Pre-release versions are not installed by default;
users must explicitly request them (e.g., `pip install plotly==X.Y.ZrcN`).
