import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import product
import os

visualize = os.environ.get("VISUALIZE", 0)

line_positions = [
    "top left",
    "top right",
    "top",
    "bottom left",
    "bottom right",
    "bottom",
    "left",
    "right",
]
rect_positions = [
    "inside top left",
    "inside top right",
    "inside top",
    "inside bottom left",
    "inside bottom right",
    "inside bottom",
    "inside left",
    "inside right",
    "inside",
    "outside top left",
    "outside top right",
    "outside top",
    "outside bottom left",
    "outside bottom right",
    "outside bottom",
    "outside left",
    "outside right",
]
fig = make_subplots(
    2, 2, column_widths=[3, 1], row_heights=[1, 3], vertical_spacing=0.07
)
for rc, pos, ax, sh in zip(
    product(range(2), range(2)),
    [line_positions, line_positions, rect_positions, rect_positions],
    ["x", "y", "x", "y"],
    ["vline", "hline", "vrect", "hrect"],
):
    r, c = rc
    r += 1
    c = ((c + 1) % 2 if r == 1 else c) + 1
    fig.update_xaxes(row=r, col=c, range=[0, len(pos) if sh[0] == "v" else 1])
    fig.update_yaxes(row=r, col=c, range=[0, len(pos) if sh[0] == "h" else 1])
    fig.add_trace(go.Scatter(x=[], y=[]), row=r, col=c)
    for n, p in enumerate(pos):
        f = eval("fig.add_%s" % (sh,))
        args = (
            {ax: n + 0.5}
            if sh.endswith("line")
            else {ax + "0": n + 0.1, ax + "1": n + 0.9}
        )
        args["annotation_text"] = p
        args["annotation_position"] = p
        args["annotation_font_size"] = 8
        args["annotation_font_color"] = "white"
        args["row"] = r
        args["col"] = c
        args["annotation_bgcolor"] = "grey"
        if sh[0] == "v":
            args["annotation_textangle"] = 90
        f(**args)
fig.update_layout(title="Annotated hline, vline, hrect, vrect")

if visualize:
    fig.show()
