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
    description: Supported Colors and Fonts
    display_as: file_settings
    language: python
    layout: base
    name: Supported Colors and Fonts
    order: 40
    page_type: example_index
    permalink: python/colors-fonts/
    thumbnail: null
---

# Supported Colors and Fonts



```python hide_code=true
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
```

```python hide_code=true
from IPython.display import HTML, display

def show_color(color_name):
    display(HTML(f'<div style="background-color:{color_name}; width:100px; height:50px; border:1px solid black"></div>'))

# Example usage
for color in supported_colors:
    print(color)
    show_color(color)
```

```python

```
