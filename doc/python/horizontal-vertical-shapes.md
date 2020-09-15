### Horizontal and Vertical Lines and Boxes in Plotly.py

Horizontal and vertical lines and rectangles that span an entire plot can be
added via the `add_hline`, `add_vline`, `add_hrect`, and `add_vrect` methods of
`plotly.graph_objects.Figure`. For example


```python
import plotly.express as px
df=px.data.iris()
fig=px.scatter(df,x='sepal_length',y='sepal_width')
fig.add_vline(x=5,line_color='red')
fig.add_hline(y=3,line_color='blue')
fig.add_vrect(x0=5.5,x1=6.5,line_color='Purple')
fig.add_hrect(y0=2.5,y1=4,line_color='Orange')
fig.show()
```
