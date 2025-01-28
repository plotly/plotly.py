# `px.overlay` prototype

This demonstrates one possible way of combining two figures into a single
figure.

To see an example, run (from the root of the `plotly.py` repo):

```bash
PYTHONPATH=proto/px_overlay python proto/px_overlay/multilayered_data_test.py
```

To see the code that does the overlaying, start with the `px_simple_overlay`
function in `proto/px_overlay/px_overlay.py`. In this function there are a few
comments marked with `TODO` that indicate places for improvement in the
functionality.
