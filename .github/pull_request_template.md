<!--
Please uncomment this block and fill in this checklist if your PR makes substantial changes to documentation in the `doc` directory.
Not all boxes must be checked for every PR:
check those that apply to your PR and leave the rest unchecked to discuss with your reviewer.

If your PR modifies code of the `plotly` package, we have a different checklist below.

## Documentation PR

- [ ] I have seen the [`doc/README.md`](https://github.com/plotly/plotly.py/blob/main/doc/README.md) file.
- [ ] This change runs in the current version of Plotly on PyPI and targets the `doc-prod` branch OR it targets the `main` branch.
- [ ] If this PR modifies the first example in a page or adds a new one, it is a `px` example if at all possible.
- [ ] Every new/modified example has a descriptive title and motivating sentence or paragraph.
- [ ] Every new/modified example is independently runnable.
- [ ] Every new/modified example is optimized for short line count and focuses on the Plotly/visualization-related aspects of the example rather than the computation required to produce the data being visualized.
- [ ] Meaningful/relatable datasets are used for all new examples instead of randomly-generated data where possible.
- [ ] The random seed is set if using randomly-generated data.
- [ ] New/modified remote datasets are loaded from https://plotly.github.io/datasets and added to https://github.com/plotly/datasets.
- [ ] Large computations are avoided in the new/modified examples in favour of loading remote datasets that represent the output of such computations.
- [ ] Imports are `plotly.graph_objects as go`, `plotly.express as px`, and/or `plotly.io as pio`.
- [ ] Data frames are always called `df`.
- [ ] `fig = <something>` is called high up in each new/modified example (either `px.<something>` or `make_subplots` or `go.Figure`).
- [ ] Liberal use is made of `fig.add_*` and `fig.update_*` rather than `go.Figure(data=..., layout=...)`.
- [ ] Specific adders and updaters like `fig.add_shape` and `fig.update_xaxes` are used instead of big `fig.update_layout` calls.
- [ ] `fig.show()` is at the end of each example.
- [ ] `plotly.plot()` and `plotly.iplot()` are not used in any example.
- [ ] Named colors are used instead of hex codes wherever possible.
- [ ] Code blocks are marked with `&#96;&#96;&#96;python`.

## Code PR

- [ ] I have read through the [contributing notes](https://github.com/plotly/plotly.py/blob/main/CONTRIBUTING.md) and understand the structure of the package. In particular, if my PR modifies code of `plotly.graph_objects`, my modifications concern the code generator and *not* the generated files.
- [ ] I have added tests or modified existing tests.
- [ ] For a new feature, I have added documentation examples (please see the doc checklist as well).
- [ ] I have added a CHANGELOG entry if changing anything substantial.
- [ ] For a new feature or a change in behavior, I have updated the relevant docstrings in the code.

-->
