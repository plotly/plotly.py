---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.0
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
    version: 3.13.2
  plotly:
    description: A list of supported named CSS Colors
    display_as: file_settings
    language: python
    layout: base
    name: Supported CSS Colors
    order: 40
    page_type: example_index
    permalink: python/css-colors/
    thumbnail: thumbnail/shape.jpg
---

# Supported CSS Colors

Many properties in Plotly.py for configuring colors support named CSS colors. For example, marker colors:

```python
import plotly.graph_objects as go

fig = go.Figure([
    go.Bar(
        x=['Jan', 'Feb', 'Mar', 'Apr'],
        y=[20, 14, 25, 16],
        name='Primary Product',
        # Named CSS color
        marker_color='royalblue'
    )
])
    
fig.show()
```

These colors are supported in Plotly.py when a property accepts a [named CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color).

```python hide_code=true
import plotly.graph_objects as go
import pandas as pd

supported_colors = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
            "beige", "bisque", "black", "blanchedalmond", "blue",
            "blueviolet", "brown", "burlywood", "cadetblue",
            "chartreuse", "chocolate", "coral", "cornflowerblue",
            "cornsilk", "crimson", "cyan", "darkblue", "darkcyan",
            "darkgoldenrod", "darkgray", "darkgrey", "darkgreen",
            "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
            "darkorchid", "darkred", "darksalmon", "darkseagreen",
            "darkslateblue", "darkslategray", "darkslategrey",
            "darkturquoise", "darkviolet", "deeppink", "deepskyblue",
            "dimgray", "dimgrey", "dodgerblue", "firebrick",
            "floralwhite", "forestgreen", "fuchsia", "gainsboro",
            "ghostwhite", "gold", "goldenrod", "gray", "grey", "green",
            "greenyellow", "honeydew", "hotpink", "indianred", "indigo",
            "ivory", "khaki", "lavender", "lavenderblush", "lawngreen",
            "lemonchiffon", "lightblue", "lightcoral", "lightcyan",
            "lightgoldenrodyellow", "lightgray", "lightgrey",
            "lightgreen", "lightpink", "lightsalmon", "lightseagreen",
            "lightskyblue", "lightslategray", "lightslategrey",
            "lightsteelblue", "lightyellow", "lime", "limegreen",
            "linen", "magenta", "maroon", "mediumaquamarine",
            "mediumblue", "mediumorchid", "mediumpurple",
            "mediumseagreen", "mediumslateblue", "mediumspringgreen",
            "mediumturquoise", "mediumvioletred", "midnightblue",
            "mintcream", "mistyrose", "moccasin", "navajowhite", "navy",
            "oldlace", "olive", "olivedrab", "orange", "orangered",
            "orchid", "palegoldenrod", "palegreen", "paleturquoise",
            "palevioletred", "papayawhip", "peachpuff", "peru", "pink",
            "plum", "powderblue", "purple", "red", "rosybrown",
            "royalblue", "rebeccapurple", "saddlebrown", "salmon",
            "sandybrown", "seagreen", "seashell", "sienna", "silver",
            "skyblue", "slateblue", "slategray", "slategrey", "snow",
            "springgreen", "steelblue", "tan", "teal", "thistle", "tomato",
            "turquoise", "violet", "wheat", "white", "whitesmoke",
            "yellow", "yellowgreen"]

fig = go.Figure(layout=dict(title="Supported Named CSS Colors"))

for i, color in enumerate(supported_colors):
    row, col = i // 5, i % 5
    x0, y0 = col * 1.2, -row * 1.2
    
    fig.add_shape(
        type="rect",
        x0=x0, y0=y0,
        x1=x0+1, y1=y0+1,
        fillcolor=color,
        line=dict(color="black", width=0.2),
    )
    
    fig.add_annotation(
        x=x0+0.5, y=y0-0.1,
        text=color,
        showarrow=False,
        font=dict(size=10)
    )

fig.update_layout(
    height=((len(supported_colors) // 5) + (1 if len(supported_colors) % 5 else 0)) * 120,
    width=800,
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=50, r=50, t=50, b=50),
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        range=[-0.5, 6]
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        scaleanchor="x",
        scaleratio=1,
        range=[-((len(supported_colors) // 5) + 1) * 1.2, 1.5]
    )
)

fig.show()
```
