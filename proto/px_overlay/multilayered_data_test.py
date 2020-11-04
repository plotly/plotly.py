import test_data
import numpy as np
import plotly.express as px
from px_combine import px_combine_secondary_y, px_simple_combine

df = test_data.multilayered_data(d_divs=[2, 3, 4, 2], rwalk=0.1)
print(df)
last_cat = df.columns[3]
figs = []
for px_call, last_cat_0 in zip([px.line, px.bar], list(set(df[last_cat]))):
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

figs[0].add_hline(y=1, row=1, col="all")
figs[1].add_vline(x=10, row="all", col=2)
figs[0].add_annotation(
    x=0.25, y=0.5, xref="x domain", yref="y domain", row=2, col=3, text="yo"
)
figs[1].add_annotation(
    x=0.5, y=0.35, xref="x domain", yref="y domain", row=1, col=2, text="budday"
)
figs[0].layout.barmode = "group"
figs[1].layout.barmode = "relative"
final_fig = px_simple_combine(*figs)
for fig in figs:
    fig.show()
final_fig.show()
