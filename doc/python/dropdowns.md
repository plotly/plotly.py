---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.8.0
  plotly:
    description: How to add dropdowns to update Plotly chart attributes in Python.
    display_as: controls
    language: python
    layout: base
    name: Dropdown Menus
    order: 2
    page_type: example_index
    permalink: python/dropdowns/
    thumbnail: thumbnail/dropdown.jpg
---

#### Methods
The [updatemenu method](https://plotly.com/python/reference/layout/updatemenus/#layout-updatemenus-buttons-method) determines which [plotly.js function](https://plotly.com/javascript/plotlyjs-function-reference/) will be used to modify the chart. There are 4 possible methods:
- `"restyle"`: modify data or data attributes
- `"relayout"`: modify layout attributes
- `"update"`: modify data **and** layout attributes
- `"animate"`: start or pause an [animation](https://plotly.com/python/#animations)


## Restyle Dropdown
The `"restyle"` method should be used when modifying the data and data attributes of the graph.

### Update One Data Attribute

This example demonstrates how to update a single data attribute: chart `type` with the `"restyle"` method.

```python
import plotly.graph_objects as go

import pandas as pd

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv")

# create figure
fig = go.Figure()

# Add surface trace
fig.add_trace(go.Surface(z=df.values.tolist(), colorscale="Viridis"))

# Update plot sizing
fig.update_layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    template="plotly_white",
)

# Update 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# Add dropdown
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["type", "surface"],
                    label="3D Surface",
                    method="restyle"
                ),
                dict(
                    args=["type", "heatmap"],
                    label="Heatmap",
                    method="restyle"
                )
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

# Add annotation
fig.update_layout(
    annotations=[
        dict(text="Trace type:", showarrow=False,
        x=0, y=1.085, yref="paper", align="left")
    ]
)

fig.show()
```

### Update Several Data Attributes

This example demonstrates how to update several data attributes: colorscale, colorscale direction, and line display with the "restyle" method.

```python
import plotly.graph_objects as go

import pandas as pd

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv")

# Create figure
fig = go.Figure()

# Add surface trace
fig.add_trace(go.Heatmap(z=df.values.tolist(), colorscale="Viridis"))

# Update plot sizing
fig.update_layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=100, b=0, l=0, r=0),
)

# Update 3D scene options
fig.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# Add dropdowns
button_layer_1_height = 1.08
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["colorscale", "Viridis"],
                    label="Viridis",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Cividis"],
                    label="Cividis",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Blues"],
                    label="Blues",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Greens"],
                    label="Greens",
                    method="restyle"
                ),
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
        dict(
            buttons=list([
                dict(
                    args=["reversescale", False],
                    label="False",
                    method="restyle"
                ),
                dict(
                    args=["reversescale", True],
                    label="True",
                    method="restyle"
                )
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.37,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
        dict(
            buttons=list([
                dict(
                    args=[{"contours.showlines": False, "type": "contour"}],
                    label="Hide lines",
                    method="restyle"
                ),
                dict(
                    args=[{"contours.showlines": True, "type": "contour"}],
                    label="Show lines",
                    method="restyle"
                ),
            ]),
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.58,
            xanchor="left",
            y=button_layer_1_height,
            yanchor="top"
        ),
    ]
)

fig.update_layout(
    annotations=[
        dict(text="colorscale", x=0, xref="paper", y=1.06, yref="paper",
                             align="left", showarrow=False),
        dict(text="Reverse<br>Colorscale", x=0.25, xref="paper", y=1.07,
                             yref="paper", showarrow=False),
        dict(text="Lines", x=0.54, xref="paper", y=1.06, yref="paper",
                             showarrow=False)
    ])

fig.show()
```

## Relayout Dropdown
The `"relayout"` method should be used when modifying the layout attributes of the graph.<br>

### Update One Layout Attribute

This example demonstrates how to update a layout attribute: chart `type` with the `"relayout"` method.

```python
import plotly.graph_objects as go

# Generate dataset
import numpy as np
np.random.seed(1)

x0 = np.random.normal(2, 0.4, 400)
y0 = np.random.normal(2, 0.4, 400)
x1 = np.random.normal(3, 0.6, 600)
y1 = np.random.normal(6, 0.4, 400)
x2 = np.random.normal(4, 0.2, 200)
y2 = np.random.normal(4, 0.4, 200)

# Create figure
fig = go.Figure()

# Add traces
fig.add_trace(
    go.Scatter(
        x=x0,
        y=y0,
        mode="markers",
        marker=dict(color="DarkOrange")
    )
)

fig.add_trace(
    go.Scatter(
        x=x1,
        y=y1,
        mode="markers",
        marker=dict(color="Crimson")
    )
)

fig.add_trace(
    go.Scatter(
        x=x2,
        y=y2,
        mode="markers",
        marker=dict(color="RebeccaPurple")
    )
)

# Add buttons that add shapes
cluster0 = [dict(type="circle",
                            xref="x", yref="y",
                            x0=min(x0), y0=min(y0),
                            x1=max(x0), y1=max(y0),
                            line=dict(color="DarkOrange"))]
cluster1 = [dict(type="circle",
                            xref="x", yref="y",
                            x0=min(x1), y0=min(y1),
                            x1=max(x1), y1=max(y1),
                            line=dict(color="Crimson"))]
cluster2 = [dict(type="circle",
                            xref="x", yref="y",
                            x0=min(x2), y0=min(y2),
                            x1=max(x2), y1=max(y2),
                            line=dict(color="RebeccaPurple"))]

fig.update_layout(
    updatemenus=[
        dict(buttons=list([
            dict(label="None",
                 method="relayout",
                 args=["shapes", []]),
            dict(label="Cluster 0",
                 method="relayout",
                 args=["shapes", cluster0]),
            dict(label="Cluster 1",
                 method="relayout",
                 args=["shapes", cluster1]),
            dict(label="Cluster 2",
                 method="relayout",
                 args=["shapes", cluster2]),
            dict(label="All",
                 method="relayout",
                 args=["shapes", cluster0 + cluster1 + cluster2])
        ]),
        )
    ]
)

# Update remaining layout properties
fig.update_layout(
    title_text="Highlight Clusters",
    showlegend=False,
)

fig.show()
```

### Update Dropdown

The `"update"` method should be used when modifying the data and layout sections of the graph.<br>
This example demonstrates how to update which traces are displayed while simultaneously updating layout attributes such as the chart title and annotations.

```python
import plotly.graph_objects as go

import pandas as pd

# Load dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
df.columns = [col.replace("AAPL.", "") for col in df.columns]

# Initialize figure
fig = go.Figure()

# Add Traces

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=list(df.High),
               name="High",
               line=dict(color="#33CFA5")))

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=[df.High.mean()] * len(df.index),
               name="High Average",
               visible=False,
               line=dict(color="#33CFA5", dash="dash")))

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=list(df.Low),
               name="Low",
               line=dict(color="#F06A6A")))

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=[df.Low.mean()] * len(df.index),
               name="Low Average",
               visible=False,
               line=dict(color="#F06A6A", dash="dash")))

# Add Annotations and Buttons
high_annotations = [dict(x="2016-03-01",
                         y=df.High.mean(),
                         xref="x", yref="y",
                         text="High Average:<br> %.3f" % df.High.mean(),
                         ax=0, ay=-40),
                    dict(x=df.Date[df.High.idxmax()],
                         y=df.High.max(),
                         xref="x", yref="y",
                         text="High Max:<br> %.3f" % df.High.max(),
                         ax=-40, ay=-40)]
low_annotations = [dict(x="2015-05-01",
                        y=df.Low.mean(),
                        xref="x", yref="y",
                        text="Low Average:<br> %.3f" % df.Low.mean(),
                        ax=0, ay=40),
                   dict(x=df.Date[df.High.idxmin()],
                        y=df.Low.min(),
                        xref="x", yref="y",
                        text="Low Min:<br> %.3f" % df.Low.min(),
                        ax=0, ay=40)]

fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="None",
                     method="update",
                     args=[{"visible": [True, False, True, False]},
                           {"title": "Yahoo",
                            "annotations": []}]),
                dict(label="High",
                     method="update",
                     args=[{"visible": [True, True, False, False]},
                           {"title": "Yahoo High",
                            "annotations": high_annotations}]),
                dict(label="Low",
                     method="update",
                     args=[{"visible": [False, False, True, True]},
                           {"title": "Yahoo Low",
                            "annotations": low_annotations}]),
                dict(label="Both",
                     method="update",
                     args=[{"visible": [True, True, True, True]},
                           {"title": "Yahoo",
                            "annotations": high_annotations + low_annotations}]),
            ]),
        )
    ])

# Set title
fig.update_layout(title_text="Yahoo")

fig.show()
```

### Graph Selection Dropdowns in Jinja

It is straight forward to create each potential view as a separate graph and then use Jinja to insert each potential view into a div on a JavaScript enabled webpage with a dropdown that chooses which div to display. This approach produces code that requires little customization or updating as you e.g. add, drop, or reorder views or traces, so it is particularly compelling for prototyping and rapid iteration. It produces web pages that are larger than the webpages produced through the built in method which is a consideration for very large figures with hundreds or thousands of data points in traces that appear in multiple selections. This approach requires both a Python program and a Jinja template file.  The documentation on [using Jinja templates with Plotly](https://plotly.com/python/interactive-html-export/#inserting-plotly-output-into-html-using-a-jinja2-template) is relevant background.  

<!-- #region -->

#### Python Code File

```python
import plotly.express as px
from jinja2 import Template
import collections
# Load the gapminder dataset
df = px.data.gapminder()

# Create a dictionary with Plotly figures as values
fig_dict = {}

# we need to fill that dictionary with figures.  this example assumes that each figure has a title and that
# we want to use the titles as descriptions in the drop down
# This example happens to fill the dictionary by creating a scatter plot for each continent using the 2007 Gapminder data
for continent in df['continent'].unique():
    # Filter data for the current continent 
    continent_data = df[(df['continent'] == continent) & (df['year'] == 2007)]
    
    fig_dict[continent] = px.scatter(continent_data, x='gdpPercap', y='lifeExp', 
                     title=f'GDP vs Life Expectancy for {continent}',
                     labels={'gdpPercap': 'GDP per Capita (USD)', 'lifeExp': 'Life Expectancy (Years)'},
                     hover_name='country',size="pop", size_max=55 
                     )
    #Standardizing the axes makes the graphs easier to compare
    fig_dict[continent].update_xaxes(range=[0,50000])
    fig_dict[continent].update_yaxes(range=[25,90])

    
# Create a dictionary, data_for_jinja with two entries:
# the value for the "dropdown_entries" key is a string containing a series of <option> tags, one tag for each item in the drop down
# the value for the "divs" key is a string with a series of <div> tags, each containing the content that appears only when the user selects the corresponding item from the dropdown
# in this example, the content of each div is a figure and descriptive text.  
data_for_jinja= collections.defaultdict(str)
text_dict = {}
for n, figname in enumerate(fig_dict.keys()):
    text_dict[figname]=f"Here is some custom text about the {figname} figure"  #This is a succinct way to populate text_dict; in practice you'd probably populate it manually elsewhere
    data_for_jinja["dropdown_entries"]+=f"<option value='{figname}'>{fig_dict[figname].layout.title.text}</option>"
    #YOU MAY NEED TO UPDATE THE LINK TO THE LATEST PLOTLY.JS
    fig_html = fig_dict[figname].to_html(full_html=False, config=dict(responsive=False, scrollZoom=False, doubleClick=False), include_plotlyjs = "cdn")
    initially_hide_divs_other_than_the_first = "style=""display:none;"""*(n>0)   
    data_for_jinja["divs"]+=f'<div id="{figname}" class="content-div" {initially_hide_divs_other_than_the_first}>{fig_html}{text_dict[figname]}</div>'

# Insert data into the template and write the file to disk
# You'll need to add the path to your template and to your preferred output location
input_template_path=r"<path-to-Jinja-template.html>"
output_html_path=r"<path-to-output-file.html>"

with open(output_html_path, "w", encoding='utf-8') as output_file:
    with open(input_template_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(data_for_jinja))
```

#### Jinja HTML Template


```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;

&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container"&gt;
        &lt;h1&gt;Select an analysis&lt;/h1&gt;
        &lt;select id="dropdown" class="form-control"&gt;
    {{ dropdown_entries }}
        &lt;/select&gt;


        {{ divs }}

    &lt;/div&gt;

    &lt;script&gt;
        document.getElementById('dropdown').addEventListener('change', function() {
            const divs = document.querySelectorAll('.content-div');
            divs.forEach(div =&gt; div.style.display = 'none');

            const selectedDiv = document.getElementById(this.value);
            if (selectedDiv) {
                selectedDiv.style.display = 'block';
            }
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

<!-- #endregion -->

#### Reference
See https://plotly.com/python/reference/layout/updatemenus/ for more information about `updatemenu` dropdowns.
