import test_data
import numpy as np
import plotly.express as px
from px_overlay import px_simple_overlay

# Demonstrates px_overlay prototype.

# Make some data that can be faceted by row, col and color, and split into 2
# sets, which will go to the first and second figure respectively.
df = test_data.multilayered_data(d_divs=[2, 3, 4, 2], rwalk=0.1)

# The titles of the figures use the last dimension in the data. The title is
# formatted "column_name=column_value", so here we extract the column name.
last_cat = df.columns[3]
figs = []
for px_call, last_cat_0 in zip([px.line, px.bar], list(set(df[last_cat]))):
    # px_call is the chart type to make and last_cat_0 is the column_value for
    # that figure which is used in forming the title.
    df_slice = df.loc[df[last_cat] == last_cat_0]
    fig = px_call(
        df_slice,
        x="x",
        y="y",
        facet_row=df.columns[0],
        facet_col=df.columns[1],
        color=df.columns[2],
    )

    fig.update_layout(title="%s=%s" % (last_cat, last_cat_0,))
    figs.append(fig)

# Add some annotations to make sure they are copied to the final figure properly
figs[0].add_hline(y=1, row=1, col="all")
figs[0].add_annotation(
    x=0.25, y=0.5, xref="x domain", yref="y domain", row=2, col=3, text="yo"
)
# Note that these annotations should be mapped to a secondary y axis (observe this
# in the final figure by dragging their corresponding secondary y axes).
figs[1].add_vline(x=10, row="all", col=2)
figs[1].add_annotation(
    x=0.5, y=0.35, xref="x domain", yref="y", row=1, col=2, text="budday"
)
# Set the bar modes for both to see that the first figure that the barmode for
# the final figure will be taken from the figure that has bars.
figs[0].layout.barmode = "group"
figs[1].layout.barmode = "relative"

# overlay the figures
final_fig = px_simple_overlay(*figs, fig1_secondary_y=True)

# Show the initial figures
for fig in figs:
    fig.show()

# Show the final figure
final_fig.show()
