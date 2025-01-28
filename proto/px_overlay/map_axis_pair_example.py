import plotly.graph_objects as go
from plotly.subplots import make_subplots
import px_overlay
import pytest

fig0 = px_overlay.make_subplots_all_secondary_y(3, 4)
fig1 = px_overlay.make_subplots_all_secondary_y(4, 5)

for dims, f in zip([(3, 4), (4, 5)], [fig0, fig1]):
    for r, c in px_overlay.multi_index(*dims):
        for sy in [False, True]:
            f.add_trace(go.Scatter(x=[], y=[]), row=r + 1, col=c + 1, secondary_y=sy)

fig0.add_annotation(row=2, col=3, text="hi", x=0.25, xref="x domain", y=3)
fig0.add_annotation(
    row=3, col=4, text="hi", x=0.25, xref="x domain", y=2, secondary_y=True
)

for an in fig0.layout.annotations:
    oldaxpair = tuple([an[ref] for ref in ["xref", "yref"]])
    newaxpair = px_overlay.map_axis_pair(fig0, fig1, oldaxpair)
    newan = go.layout.Annotation(an)
    print(oldaxpair)
    print(newaxpair)
    newan["xref"], newan["yref"] = newaxpair
    fig1.add_annotation(newan)

fig0.show()
fig1.show()
