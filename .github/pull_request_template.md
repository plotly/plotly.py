<!--
Please uncomment this block and take a look at this checklist if your PR is making substantial changes to **documentation**/impacts files in the `doc` directory. Check all that apply to your PR, and leave the rest unchecked to discuss with your reviewer! Not all boxes must be checked for every PR :)

If your PR modifies code of the `plotly` package, we have a different checklist
below :-).

### Documentation PR

- [ ] I've [seen the `doc/README.md` file](https://github.com/plotly/plotly.py/blob/master/doc/README.md)
- [ ] This change runs in the current version of Plotly on PyPI and targets the `doc-prod` branch OR it targets the `master` branch
- [ ] If this PR modifies the first example in a page or adds a new one, it is a `px` example if at all possible
- [ ] Every new/modified example has a descriptive title and motivating sentence or paragraph
- [ ] Every new/modified example is independently runnable
- [ ] Every new/modified example is optimized for short line count	and focuses on the Plotly/visualization-related aspects of the example rather than the computation required to produce the data being visualized
- [ ] Meaningful/relatable datasets are used for all new examples instead of randomly-generated data where possible
- [ ] The random seed is set if using randomly-generated data in new/modified examples
- [ ] New/modified remote datasets are loaded from https://plotly.github.io/datasets and added to https://github.com/plotly/datasets
- [ ] Large computations are avoided in the new/modified examples in favour of loading remote datasets that represent the output of such computations
- [ ] Imports are `plotly.graph_objects as go` / `plotly.express as px` / `plotly.io as pio`
- [ ] Data frames are always called `df`
- [ ] `fig = <something>` call is high up in each new/modified example (either `px.<something>` or `make_subplots` or `go.Figure`)
- [ ] Liberal use is made of `fig.add_*` and `fig.update_*` rather than `go.Figure(data=..., layout=...)` in every new/modified example
- [ ] Specific adders and updaters like `fig.add_shape` and `fig.update_xaxes` are used instead of big `fig.update_layout` calls in every new/modified example
- [ ] `fig.show()` is at the end of each new/modified example
- [ ] `plotly.plot()` and `plotly.iplot()` are not used in any new/modified example
- [ ] Hex codes for colors are not used in any new/modified example in favour of [these nice ones](https://github.com/plotly/plotly.py/issues/2192)

## Code PR

- [ ] I have read through the [contributing notes](https://github.com/plotly/plotly.py/blob/master/contributing.md) and understand the structure of the package. In particular, if my PR modifies code of `plotly.graph_objects`, my modifications concern the `codegen` files and not generated files.
- [ ] I have added tests (if submitting a new feature or correcting a bug) or
  modified existing tests.
- [ ] For a new feature, I have added documentation examples in an existing or
  new tutorial notebook (please see the doc checklist as well).
- [ ] I have added a CHANGELOG entry if fixing/changing/adding anything substantial.
- [ ] For a new feature or a change in behaviour, I have updated the relevant docstrings in the code to describe the feature or behaviour (please see the doc checklist as well).

-->
