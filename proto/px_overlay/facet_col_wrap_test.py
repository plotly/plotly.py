import plotly.express as px
import test_data
from px_combine import px_simple_combine

df = test_data.multilayered_data(d_divs=[6, 3, 2], rwalk=0.1)
last_cat = df.columns[2]
last_cat_types = list(set(df[last_cat]))
fig0 = px.line(
    df.loc[df[last_cat] == last_cat_types[0]],
    x="x",
    y="y",
    facet_col=df.columns[0],
    facet_col_wrap=3,
    color=df.columns[1],
).update_layout(title="%s=%s" % (last_cat, last_cat_types[0]))
fig1 = px.line(
    df.loc[df[last_cat] == last_cat_types[1]],
    x="x",
    y="y",
    facet_col=df.columns[0],
    facet_col_wrap=3,
    color=df.columns[1],
).update_layout(title="%s=%s" % (last_cat, last_cat_types[1]))
fig = px_simple_combine(fig0, fig1, fig1_secondary_y=True)
fig0.show()
fig1.show()
fig.show()
