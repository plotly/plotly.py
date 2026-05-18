# Documentation of plotly.py

## Introduction: structure and required packages

The `doc` directory contains the source files of the documentation of plotly.py.
It is composed of two parts:

- inside the [`python/` directory](python), tutorials corresponding to https://plotly.com/python/
- inside the [`apidoc/` directory](apidoc), configuration files for generating
  the API reference documentation (hosted on https://plotly.com/python-api-reference/)

Python packages required to build the docs are listed in
[`requirements.txt`](requirements.txt) in the `doc` directory.

## Local environment setup

Before building the documentation locally, you need to set up a dedicated
environment with the doc-specific dependencies.

```bash
cd doc
uv venv --python 3.9
source .venv/bin/activate
uv pip install -r requirements.txt
```

If you are documenting a feature that has not yet been released, you also need
an editable install of plotly so your local changes are reflected:

```bash
uv pip uninstall plotly       # remove the PyPI version installed by requirements.txt
uv pip install -e ..          # install from your local checkout
```

### Mapbox token

Several geographic examples require a free Mapbox public token. Without it,
those specific pages will fail to build.

1. Create an account at https://account.mapbox.com/auth/signup
2. Navigate to https://account.mapbox.com/ and copy your "Default public token"
3. Save it to the file `doc/python/.mapbox_token`

The Makefile symlinks this token into the build directory automatically.

## Tutorials (`python` directory)

Each tutorial is a markdown (`.md`) file, which can be opened in Jupyter
Notebook or in JupyterLab by installing [jupytext](https://jupytext.readthedocs.io/en/latest/install.html).

For small edits (e.g., correcting typos) to an existing tutorial, you can simply click on the "edit this
page on GitHub" link at the top right of the page (e.g. clicking on this link
on https://plotly.com/python/bar-charts/ will take you to
https://github.com/plotly/plotly.py/edit/doc-prod/doc/python/bar-charts.md,
where you can edit the page on GitHub).

For more important edits where you need to run the notebook to check the output,
clone the repository and setup an environment as described in the [main
contributing notes](../CONTRIBUTING.md). If you're writing documentation at the
same time as you are developing a feature, make sure to install with editable
install (`pip install -e`, as described in [main
contributing notes](../CONTRIBUTING.md)), so that you only need to restart
the Jupyter kernel when you have changed the source code of the feature.

### Branches

Two different cases exist, whether you are documenting a feature already
released, or which has just been included but not yet released.

- Case of an already released feature: your changes can be deployed to the
  documentation website as soon as they have been merged, and you should start
  your branch off the `doc-prod` branch and open your pull request against this
  `doc-prod` branch.
- Case of a new (not released yet) feature: start your branch / pull request
  against the `main` branch. `main` and `doc-prod` will be synchronized at
  release time, so that the documentation of the feature is only deployed when
  it is available in a released version of `plotly.py`.

#### Keeping `main` and `doc-prod` in sync

Changes to `doc-prod` are **not** automatically merged back into `main`. To
prevent the branches from diverging, `doc-prod` should be merged into `main` on
a regular basis via a pull request (e.g., a branch named
`merge-doc-prod-to-main-branch` merged into `main`).

At release time the synchronization is bidirectional (see also
[`RELEASE.md`](../RELEASE.md)):

1. **`doc-prod` → `main`** — merge any outstanding doc-only fixes into `main`
   (if not already done recently).
2. **`main` → `doc-prod`** — merge `main` into `doc-prod` so that documentation
   for newly released features is deployed to the live site.
3. **Publish the site** — update the
   [`graphing-library-docs`](https://github.com/plotly/graphing-library-docs)
   repo to bump the plotly.py and plotly.js versions and rebuild the Algolia
   search indexes. See the
   [Update documentation site](../RELEASE.md#update-documentation-site)
   section of `RELEASE.md` for the full procedure.

> **Release prep:** When synchronizing `main` into `doc-prod` for a new
> release, update the `plotly==` version pin in `requirements.txt` to match
> the newly released version. The `doc-prod` build uses this pinned version
> (not an editable install), so examples that rely on new features will fail
> if the pin is stale.

### Tutorial file format

Tutorial files are Markdown files with a YAML frontmatter block that contains
Jupyter notebook metadata (used by jupytext) and plotly-specific metadata (used
by the documentation site for navigation, SEO, and categorization).

Here is an annotated example of the frontmatter:

```yaml
---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.9.0
  plotly:
    description: Short description for SEO and page previews.
    display_as: basic          # Category: basic, statistical, scientific, maps, 3d, etc.
    language: python
    layout: base
    name: Page Title           # Displayed in the navigation sidebar
    order: 3                   # Position within the display_as category
    page_type: example_index
    permalink: python/my-page/ # URL path on the documentation site
    thumbnail: thumbnail/my-page.jpg
---
```

The `plotly` metadata fields are the most important to get right:

| Field | Description |
|-------|-------------|
| `name` | Page title shown in the sidebar and browser tab |
| `permalink` | URL slug — must match the filename (e.g., `bar-charts.md` → `python/bar-charts/`) |
| `description` | Short description used by search engines |
| `display_as` | Category grouping (e.g., `basic`, `statistical`, `scientific`, `maps`, `3d_charts`, `file_settings`) |
| `order` | Numeric sort order within the category |
| `page_type` | Typically `example_index` for tutorial pages |
| `thumbnail` | Path to the thumbnail image |

Code cells are written as fenced code blocks with the `python` language tag.
Each code cell is separated by a blank line and starts with ` ```python `.
Markdown cells are written as regular Markdown text between code blocks.

### Creating a new tutorial page

1. **Copy an existing tutorial** from `doc/python/` as a starting point to get
   the frontmatter structure right.
2. **Update the frontmatter** — at minimum, change `name`, `permalink`,
   `description`, `display_as`, and `order`. Make sure `permalink` matches the
   filename (e.g., `my-feature.md` → `python/my-feature/`).
3. **Write examples** using fenced `python` code blocks. Each block becomes a
   separate Jupyter cell when the file is converted.
4. **Test in Jupyter** — open the file directly in JupyterLab (with jupytext
   installed) and run all cells to verify the examples work:
   ```bash
   jupyter lab doc/python/my-feature.md
   ```
5. **Build the single page** (optional) — you can build just your page instead
   of the entire doc set:
   ```bash
   cd doc
   make build/html/2019-07-03-my-feature.html
   ```
6. **Check that CI passes** — push your branch and open a pull request. The CI
   will build all pages and run validation on frontmatter and page ordering.

### Guidelines

We try to write short, standalone and (almost) self-explaining examples. Most
examples should focus on a single feature.

Checklist

- Each example should have a clear title (titles are used for the navigation
  bar and indexed by search engines)
- Package imports should be called in the same cell as the example, so that it
  is possible to copy-paste a single cell to reproduce the example.
- Variable names should be consistent with other examples, for example use
  `fig` for a `Figure` object, `df` for a pandas dataframe, etc.
- Examples should not be too long to execute (typically < 10s), since the doc is
  built as part of the continuous integration (CI) process. Examples taking
  longer to execute should be discussed in a new issue to decide whether they
  can be accepted.

### Build process

#### Building all tutorials

From the `doc` directory, with the virtual environment activated:

```bash
cd doc
source .venv/bin/activate
make
```

This runs through every `.md` file in `python/` and:

1. Appends the "What About Dash?" footer from `what_about_dash.md`
2. Converts each Markdown file to a Jupyter notebook using **jupytext**
3. Executes the notebook and converts it to HTML using **nbconvert** (with a
   10-minute timeout per notebook)
4. Outputs HTML files to `build/html/` with a `2019-07-03-` date prefix
5. Generates redirect pages for v3 backward compatibility and "next version"
   previews

To build in parallel (as CI does):

```bash
make -kj8
```

The `-k` flag continues past failures and `-j8` runs 8 jobs in parallel.

#### Building a single tutorial

To build only one page (useful during development):

```bash
make build/html/2019-07-03-bar-charts.html
```

The filename follows the pattern `2019-07-03-<markdown-filename-without-extension>.html`.

> **Why the `2019-07-03-` prefix?** The downstream `graphing-library-docs`
> site uses Jekyll, whose `_posts/` collection only processes files matching
> the pattern `YYYY-MM-DD-title.ext` and silently ignores anything else.
> The specific date is an arbitrary placeholder — its value is never
> displayed; it just satisfies Jekyll's filename parser.

#### Build output

| Directory | Contents |
|-----------|----------|
| `build/ipynb/` | Intermediate Jupyter notebook files |
| `build/html/` | Final HTML tutorial pages |
| `build/html/redir/` | Redirect pages (v3 and next-version) |
| `build/failures/` | Stderr logs for pages that failed to build |

If a build fails, check `build/failures/<page-name>` for the error output.

## API reference documentation (`apidoc` directory)

We use [sphinx](http://www.sphinx-doc.org/en/master/) and its [`autodoc`
extension](http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
in order to generate the documentation of the API. Sphinx uses the [reST markup
language](https://www.sphinx-doc.org/en/2.0/usage/restructuredtext/basics.html).

### Building the API docs

The API docs require an editable install of plotly because the build process
temporarily modifies source files (renaming `graph_objects` references to the
internal `graph_objs` name for Sphinx, then reverting afterward).

```bash
cd doc
source .venv/bin/activate
uv pip uninstall plotly
uv pip install -e ..
cd apidoc
make html
```

The output is written to `apidoc/_build/html/`.

### How the API doc build works

The `apidoc/Makefile` performs several steps:

1. Temporarily rewrites `:class:` cross-references in `plotly/graph_objs/` to
   use the internal `graph_objs` name so Sphinx can resolve them.
2. Copies color module files into `plotly/colors/` and `plotly/express/colors/`
   so their docstrings are picked up.
3. Runs `sphinx-apidoc` to auto-generate `.rst` stubs from the Python source,
   excluding `validators/`, `tests/`, `matplotlylib/`, `offline/`, and `api/`.
4. Runs `sphinx-build` to produce HTML from the `.rst` files.
5. Reverts the `graph_objs` source changes with `git checkout`.
6. Cleans up the temporarily copied color files.
7. Renames all `graph_objs` references back to `graph_objects` in the generated
   HTML and related files.

### Adding new API objects

Lists of objects to be documented are found in `.rst` files corresponding to
submodules:

| File | Module |
|------|--------|
| `plotly.express.rst` | `plotly.express` (high-level API) |
| `plotly.graph_objects.rst` | `plotly.graph_objects` (traces, layout) |
| `plotly.io.rst` | `plotly.io` (display, read, write) |
| `plotly.subplots.rst` | `plotly.subplots` (subplot helpers) |
| `plotly.figure_factory.rst` | `plotly.figure_factory` |
| `basefigure.rst` | `BaseFigure` class |

When a new object is added to the exposed API, it needs to be added to the
corresponding `.rst` file to appear in the API doc.

### Other files

- `css` files are found in `_static`
- Template files are found in `_templates`. `.rst` templates describe how the
  autodoc of the different objects should look like.
- `conf.py` contains the Sphinx configuration (theme, extensions, etc.)

## CI/CD pipeline

Documentation is built and deployed automatically by the GitHub Actions workflow
defined in `.github/workflows/build-doc.yml`.

### What triggers a build

| Event | What happens |
|-------|-------------|
| Pull request (any branch) | Tutorials are built and validated. The build artifact is uploaded but not deployed. |
| Push to `doc-prod` | Full build: tutorials are built, validated, and deployed. API docs are also built and deployed. |

### Build steps

1. **Environment setup** — Python 3.9, `uv`, and system dependencies (`rename`
   utility) are installed.
2. **Install doc dependencies** — `uv pip install -r requirements.txt` inside
   `doc/`.
3. **Install editable plotly** (non-`doc-prod` branches only) — Replaces the
   PyPI plotly with the local checkout so that in-development features are
   available.
4. **Build HTML tutorials** — Runs `make -kj8` (twice, to retry transient
   failures). Then downloads and runs validation scripts from
   `plotly/graphing-library-docs`:
   - `front-matter-ci.py` validates the YAML frontmatter of all built pages.
   - `check-or-enforce-order.py` verifies page ordering within categories.
5. **Upload build artifact** — The built HTML is uploaded as a GitHub Actions
   artifact named `doc-html` for inspection.

### Deployment (doc-prod only)

When changes are pushed to `doc-prod`, the workflow deploys to three branches
of the [`plotly/plotly.py-docs`](https://github.com/plotly/plotly.py-docs)
repository:

| Target branch | Contents |
|---------------|----------|
| `built` | Final HTML tutorial pages |
| `built_ipynb` | Intermediate Jupyter notebook files |
| `gh-pages` | API reference HTML (built by Sphinx) |

After deploying, the workflow triggers a downstream build in
[`plotly/graphing-library-docs`](https://github.com/plotly/graphing-library-docs)
by pushing an empty commit. That repository generates the final
https://plotly.com/python site.

### Summary of the full deployment path

```
doc/python/*.md  (source)
    ↓  make (jupytext + nbconvert)
doc/build/html/*.html  (built tutorials)
    ↓  CI deploys to plotly/plotly.py-docs@built
plotly/graphing-library-docs  (triggered rebuild)
    ↓  Jekyll site generation
https://plotly.com/python/  (live site)
```

## Troubleshooting

### A single page fails to build

Check `build/failures/<page-name>` for the full error output. Common causes:

- **Missing import or dataset** — make sure all imports and remote data URLs
  are correct.
- **Timeout** — the default is 600 seconds (10 minutes). If your example
  legitimately needs more time, discuss in an issue before increasing the
  timeout.
- **Missing Mapbox token** — geographic examples will fail if
  `doc/python/.mapbox_token` does not exist.

### `make` fails immediately

- Confirm you are running from the `doc/` directory with the virtual
  environment activated.
- Check that `jupytext` and `nbconvert` are installed: `jupytext --version`
  and `jupyter nbconvert --version`.

### API doc build fails on `graph_objs` references

The API doc build temporarily modifies files under `plotly/graph_objs/`. If a
previous build was interrupted, those files may be in a dirty state. Reset them
with:

```bash
git checkout -- plotly/graph_objs
```

### CI frontmatter validation fails

The CI runs `front-matter-ci.py` and `check-or-enforce-order.py` against the
built HTML. Ensure your tutorial's YAML frontmatter includes all required
fields (`name`, `permalink`, `description`, `display_as`, `order`, `layout`,
`language`) and that the `order` value does not conflict with existing pages in
the same `display_as` category.
