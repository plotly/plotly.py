### Horizontal and Vertical Lines and Boxes (Autoshapes) in Plotly.py

Horizontal and vertical lines and rectangles (autoshapes) that span an entire
plot can be added via the `add_hline`, `add_vline`, `add_hrect`, and `add_vrect`
methods of `plotly.graph_objects.Figure`. These shapes are fixed to the
endpoints of one axis, regardless of the range of the plot, and fixed to data
coordinates on the other axis. For example


```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width")

# Add a vertical line that spans the entire y axis
# intersecting the x axis at x=5
fig.add_vline(x=5, line_color="red")
# Add a horizontal line that spans the entire x axis
# intersecting the y axis at y=3
fig.add_hline(y=3, line_color="blue")
# Add a vertical rectangle that spans the entire y axis
# intersecting the x axis at 5.5 and 6.5
fig.add_vrect(x0=5.5, x1=6.5, line_color="purple")
# Add a horizontal rectangle that spans the entire x axis
# intersecting the y axis at 2.5 and 4
fig.add_hrect(y0=2.5, y1=4, line_color="orange")
# (try dragging the plot around)
fig.show()
```

#### Adding Autoshapes to Multiple Facets / Subplots

The same line or box can be added to mulitple facets by using the `'all'`
keyword in the `row` and `col` arguments like with `Figure.add_shape`. For
example
```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", facet_row="smoker", facet_col="sex")
# Adds a vertical line to all facets
fig.add_vline(x=30, row="all", col="all", line_color="purple")
# Adds a horizontal line to all the rows of the second column
fig.add_hline(y=6, row="all", col=2, line_color="yellow")
# Adds a vertical rectangle to all the columns of the first row
fig.add_vrect(x0=20, x1=40, row=1, col="all", line_color="green")
fig.show()
```

#### Adding Text Annotations to Autoshapes




