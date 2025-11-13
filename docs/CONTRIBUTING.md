# Contribute to Plotly's [Python Documentation](https://plotly.com/python/)

Plotly welcomes contributions to its [open-source Python graphing libraries documentation](https://plotly.com/python) from its community of users.

Our Python tutorials are written in Markdown files in the `doc/python/` directory of this repository. 

## Contribute Quickly to Plotly's Python Graphing Library Documentation
  
To quickly make a contribution to Plotly's Python graphing libraries documentation, simply submit a pull request with the change you would like to suggest. This can be done using the GitHub graphical user interface at https://github.com/plotly/plotly.py/. 

The easiest way to do this is to follow the `Edit this page on GitHub` link at the top right of the page you are interested in contributing to:

![Screen Shot 2020-01-07 at 12 45 39 PM](https://user-images.githubusercontent.com/1557650/71916356-bfe53800-314b-11ea-92b6-eb763037f6d5.png)

**You don't have to worry about breaking the site when you submit a pull request!** This is because your change will not be merged to production immediately. A Plotly team member will first perform a code review on your pull request in order to ensure that it definitely increases the health of Plotly's graphing libraries codebase.

## Mkdocs Setup

Before proceeding, make sure you are working in the `docs` directory. This is where all of the files needed
to build the site using Mkdocs are.

### Create a Virtual Environment

Create a *virtual environment* for the project so that packages you install won't affect other projects you are working on.
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

All dependencies are listed in `pyproject.toml` under `docs`. These include Mkdocs extensions used for features such as redirects as well as dependencies needed to properly run the examples in `doc/python/`.

If you are using `uv`, you can install the dependencies using this command:

```bash
uv sync --extra docs
```

If you are using `conda` or `virtualenv`,
or if `uv sync` does not work as you expect,
you can install all packages with:

```bash
pip install -e '.[docs]'
```

### File Structure

- `docs/build/` is where Mkdocs builds the local copy of the site. This is only updated if you run `make docs` or `mkdocs build`.
- `doc/python/` is where handwritten markdown files are contained. These files need to be run through the `bin/run_markdown.py` script to generate the output for each code block.
- `docs/pages/` is where Mkdocs looks for content to build the site and contains the generated output for the pages in `doc/python/`. It also includes the pages Mkdocs creates by parsing the docstrings of the modules in `plotly/` under `docs/pages/reference/`, the custom css files used for styling (`docs/pages/css/`), and HTML files that override Mkdocs templates to add custom functionality (`docs/pages/overrides/`). There is one special case in `static-image-export.md` that uses `img.show()`. To insert the images into the markdown file, `bin/run_markdown.py` saves the images into `docs/pages/imgs/`.
- `docs/mkdocs.yml` contains the configuration for the Mkdocs build such as extensions, site name and navigation.


### Building the Site

To modify the `plotly.graph_objects` API reference pages there are a couple of steps you may need to take:

1. If you update the docstrings for the functions, you need to regenerate the auto-generated files under `plotly/graph_objects/`. To do this, run `make generate`. Note: the docstrings need to be written in `numpy` style for `mkdocstrings` to parse it properly.
2. To update the pages in `docs/pages/graph_objects/`, run `make reference`.

Update the examples under `docs/pages/` by running `make examples` which rebuilds pages with changes, `make examples-force` to force all pages to be rebuilt or `uv run bin/run_markdown.py --outdir pages --htmldir pages/examples --inline --verbose 2 doc/python/page_name.md` if you only need to update one page. The `bin/run_markdown.py` script runs each of the codeblocks in python and inserts the generated output under it.

Then, run `make docs` to rebuild the local copy of the site in `build/` or `mkdocs serve` to run the site on localhost.

> Note: Running the site on localhost using `mkdocs serve` ensures all the Mkdocs features and redirects work properly. Some features such as search are not available if you view the HTML files under `docs/` using a regular HTML file viewer (ie. "View in Browser" command on VSCode)


### Macros

In `mkdocs.yml`, the `extra` section defines configuration values used across the documentation. For example, you can specify the Plotly.js version in `extra.js_version`. The `macros` plugin makes `js_version` accessible in scripts such as `bin/examples_pages.py` when CodePen examples are being embedded into the HTML snippets generated into `tmp/javascript`.


## Overriding Mkdocs material themes

To modify the HTML components of the Mkdocs site, copy the template from the [`mkdocs-material` repository](https://github.com/squidfunk/mkdocs-material/tree/master/material/templates). Then, make these changes in `pages/overrides`.

You can either modify the existing files in `pages/overrides` or add a new file, paste the template for the component you are modifying and make your changes. Make sure to use the same file structure as the `mkdocs-material` default theme.

For example, to change the footer, copy the `footer.html` template from the [`mkdocs-material` repository](https://github.com/squidfunk/mkdocs-material/blob/master/material/templates/partials/footer.html), then create a `footer.html` file under `pages/overrides/partials/`, paste and modify it.

See [the official documentation](https://squidfunk.github.io/mkdocs-material/customization/) for more details.


## Mkdocs Validation

In `mkdocs.yml`, there is a section `validation` that defines how Mkdocs presents any issues and resolves links. When you build the site, there are some `INFO` logs that can be ignored.

`Doc file <source_file_name>.md contains an unrecognized relative link '../<target_file_name>/', it was left as is` is an `INFO` log that happens because Mkdocs cannot resolve the link during build, but when the site is running, the redirects defined in `mkdocs.yml` will make sure these links redirect to the proper page. If a redirect does not exist for the page referenced in the link, then it is a regular missing page error and needs to be fixed.

Any internal references in the markdown files, are resolved by Mkdocs relative to `docs/`. So, absolute links will be correctly resolved when the site is running. This is configured `mkdocs.yml` with the line `absolute_links: relative_to_docs`.