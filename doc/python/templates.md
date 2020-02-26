---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.2
  kernelspec:
    display_name: Python 3
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
    version: 3.7.3
  plotly:
    description: Theming and templates with plotly with Python
    display_as: file_settings
    language: python
    layout: base
    name: Theming and templates
    order: 7
    page_type: u-guide
    permalink: python/templates/
    thumbnail: thumbnail/theming-and-templates.png
---

### Theming and templates

The Plotly Python library comes pre-loaded with several themes that you can get started using right away, and it also provides support for creating and registering your own themes.

> Note on terminology: Theming generally refers to the process of defining default styles for visual elements. Themes in plotly are implemented using objects called templates. Templates are slightly more general than traditional themes because in addition to defining default styles, templates can pre-populate a figure with visual elements like annotations, shapes, images, and more. In the documentation we will refer to the overall process of defining default styles as theming, and when in comes to the plotly API we will talk about how themes are implemented using templates.

### Using built-in themes

#### View available themes

To see information about the available themes and the current default theme, display the `plotly.io.templates` configuration object like this.

```python
import plotly.io as pio
pio.templates
```

From this, we can see that the default theme is `"plotly"`, and we can see the names of several additional themes that we can choose from.

#### Specifying themes in Plotly Express

All Plotly Express functions accept a `template` argument that can be set to the name of a registered theme (or to a `Template` object as discussed later in this section). Here is an example of using Plotly Express to build and display the same scatter plot with six different themes.

```python
import plotly.express as px

df = px.data.gapminder()
df_2007 = df.query("year==2007")

for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig = px.scatter(df_2007,
                     x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     log_x=True, size_max=60,
                     template=template, title="Gapminder 2007: '%s' theme" % template)
    fig.show()
```

#### Specifying themes in graph object figures

The theme for a particular graph object figure can be specified by setting the `template` property of the figure's `layout` to the name of a registered theme (or to a `Template` object as discussed later in this section). Here is an example of constructing a surface plot and then displaying it with each of six themes.

```python
import plotly.graph_objects as go
import pandas as pd

z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")

fig = go.Figure(
    data=go.Surface(z=z_data.values),
    layout=go.Layout(
        title="Mt Bruno Elevation",
        width=500,
        height=500,
    ))

for template in ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]:
    fig.update_layout(template=template, title="Mt Bruno Elevation: '%s' theme" % template)
    fig.show()
```

#### Specifying a default themes

If a theme is not provided to a Plotly Express function or to a graph object figure, then the default theme is used. The default theme starts out as `"plotly"`, but it can be changed by setting the `plotly.io.templates.default` property to the name of a registered theme.

Here is an example of changing to default theme to `"plotly_white"` and then constructing a scatter plot with Plotly Express without providing a template.

> Note: Default themes persist for the duration of a single session, but they do not persist across sessions. If you are working in an IPython kernel, this means that default themes will persist for the life of the kernel, but they will not persist across kernel restarts.

```python
import plotly.io as pio
import plotly.express as px

pio.templates.default = "plotly_white"

df = px.data.gapminder()
df_2007 = df.query("year==2007")

fig = px.scatter(df_2007,
                 x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 log_x=True, size_max=60,
                 title="Gapminder 2007: current default theme")
fig.show()
```

#### Disable default theming

If you do not wish to use any of the new themes by default, or you want your figures to look exactly the way they did prior to plotly.py version 4, you can disable default theming by setting the default theme to `"none"`.

```python
import plotly.io as pio
pio.templates.default = "none"
```

### Creating themes

#### Representing themes with Template objects

Themes in plotly.py are represented by instances of the `Template` class from the `plotly.graph_objects.layout` module. A `Template` is a graph object that contains two top-level properties: `layout` and `data`. These template properties are described in their own sections below.

#### The template layout property

The `layout` property of a template is a graph object with the exact same structure as the `layout` property of a figure. When you provide values for properties of the template's `layout`, these values will be used as the defaults in any figure that this template is applied to.

Here is an example that creates a template that sets the default title font to size 24 Rockwell, and then constructs a graph object figure with this template.

```python
import plotly.graph_objects as go

large_rockwell_template = dict(
    layout=go.Layout(title_font=dict(family="Rockwell", size=24))
)

fig = go.Figure()
fig.update_layout(title="Figure Title",
                  template=large_rockwell_template)
fig.show()
```

> Note: this example uses magic underscore notation to write `go.Layout(title=dict(font=dict(...)))` as `go.Layout(title_font=dict(...))`

#### The template data property

The `data` property of a template is used to customize the default values of the properties of traces that are added to a figure that the template is applied to. This `data` property holds a graph object, with type `go.layout.template.Data`, that has a property named after each supported trace type. These trace type properties are then assigned lists or tuples of graph object traces of the corresponding type.

Here is an example that creates a template that sets the default scatter trace markers to be size 20 diamonds, and then constructs a graph object figure with this template.

```python
import plotly.graph_objects as go

diamond_template = go.layout.Template()
diamond_template.data.scatter = [go.Scatter(marker=dict(symbol="diamond", size=20))]

fig = go.Figure()
fig.update_layout(template=diamond_template)
fig.add_scatter(y=[2, 1, 3], mode="markers")
fig.show()
```

If a trace type property is set to a list of more than one trace, then the default properties are cycled as more traces are added to the figure. Here is an example that creates a template that cycles the default marker symbol for scatter traces, and then constructs a figure that uses this template.

```python
import plotly.graph_objects as go

symbol_template = go.layout.Template()
symbol_template.data.scatter = [
    go.Scatter(marker=dict(symbol="diamond", size=10)),
    go.Scatter(marker=dict(symbol="square", size=10)),
    go.Scatter(marker=dict(symbol="circle", size=10)),
]

fig = go.Figure()
fig.update_layout(template=symbol_template)
fig.add_scatter(y=[1, 2, 3], mode="markers", name="first")
fig.add_scatter(y=[2, 3, 4], mode="markers", name="second")
fig.add_scatter(y=[3, 4, 5], mode="markers", name="third")
fig.add_scatter(y=[4, 5, 6], mode="markers", name="forth")
fig.show()
```

Note that because we built the template with a list of 3 scatter trace graph objects (one each for the diamond, square, and circle symbols), the forth scatter trace in the figure cycles around and takes on the defaults specified in the first template trace (The diamond symbol).

#### Theming object tuple properties

Some properties in the figure hierarchy are specified as tuples of objects. For example, the text annotations for a graph object figure can be stored as a tuple of `go.layout.Annotation` objects in the `annotations` property of the figure's layout.

To use a template to configure the default properties of all of the elements in an object tuple property (e.g. `layout.annotations`), use the `*defaults` property in the template that corresponds to the tuple property (e.g. `layout.template.layout.annotationdefaults`). The `*defaults` template property should be set to a single graph object that matches the type of the elements of the corresponding tuple. The properties of this `*defaults` object in the template will be applied to all elements of the object tuple in the figure that the template is applied to.

Here is an example that creates a template that specifies the default annotation text color, and then constructs a figure that uses this template.

```python
import plotly.graph_objects as go

annotation_template = go.layout.Template()
annotation_template.layout.annotationdefaults = dict(font=dict(color="crimson"))

fig = go.Figure()
fig.update_layout(
     template=annotation_template,
     annotations=[
         dict(text="Look Here", x=1, y=1),
         dict(text="Look There", x=2, y=2)
     ]
 )
fig.show()
```

#### Including tuple elements in a theme

The previous section described how to use a template to customize the default properties of tuple elements that are added to a figure that the template is applied to. This is useful for styling, for example, any annotations, shapes, or images that will eventually be added to the figure.

It is also possible for a template to define tuple elements that should be included, as is, in any figure that the template is applied to. This is done by specifying a list of one or more tuple element graph objects (e.g. `go.layout.Annotation` objects) as the value of the corresponding tuple property in the template (e.g. at `template.layout.annotations`). Note that the `name` property of these tuple element graph objects must be set to a unique non-empty string.

Here is an example that creates a template that adds a large semi-transparent "DRAFT" watermark to the middle of the figure, and constructs a figure using this template.

```python
import plotly.graph_objects as go

draft_template = go.layout.Template()
draft_template.layout.annotations = [
    dict(
        name="draft watermark",
        text="DRAFT",
        textangle=-30,
        opacity=0.1,
        font=dict(color="black", size=100),
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
    )
]

fig=go.Figure()
fig.update_layout(template=draft_template)
fig.show()
```

#### Customizing theme tuple elements in a figure

The previous section described how a template can be used to add default tuple element graph objects (e.g. annotations, shapes, or images) to a figure. The properties of these default tuple elements can be customized from within the figure by adding an tuple element with a `templateitemname` property that matches the `name` property of the template object.

Here is an example, using the same `draft_template` defined above, that customizes the watermark from within the figure to read "CONFIDENTIAL" rather than "DRAFT".

```python
import plotly.graph_objects as go

draft_template = go.layout.Template()
draft_template.layout.annotations = [
    dict(
        name="draft watermark",
        text="DRAFT",
        textangle=-30,
        opacity=0.1,
        font=dict(color="black", size=100),
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
    )
]

fig = go.Figure()
fig.update_layout(
    template=draft_template,
    annotations=[
        dict(
            templateitemname="draft watermark",
            text="CONFIDENTIAL",
        )
    ]
)
fig.show()
```

#### Registering themes as named templates

The examples above construct and configure a `Template` object and then pass that object as the template specification to graph object figures (as the `layout.template` property) or Plotly Express functions (as the `template` keyword argument). It is also possible to register custom templates by name so that the name itself can be used to refer to the template. To register a template, use dictionary-style assignment to associate the template object with a name in the `plotly.io.templates` configuration object.

Here is an example of registering the draft watermark template from the previous sections as a template named `"draft"`. Then a graph object figure is created with the draft template specified by name.

```python
import plotly.graph_objects as go
import plotly.io as pio

pio.templates["draft"] = go.layout.Template(
    layout_annotations=[
        dict(
            name="draft watermark",
            text="DRAFT",
            textangle=-30,
            opacity=0.1,
            font=dict(color="black", size=100),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
    ]
)

fig = go.Figure()
fig.update_layout(template="draft")
fig.show()
```

> Note: this example uses magic underscore notation to write `go.layout.Template(layout=dict(annotations=[...]))` as ``go.layout.Template(layout_annotations=[...])`

It is also possible to set your own custom template as the default so that you do not need to pass it by name when constructing graph object figures or calling Plotly Express functions.

```python
import plotly.graph_objects as go
import plotly.io as pio

pio.templates["draft"] = go.layout.Template(
    layout_annotations=[
        dict(
            name="draft watermark",
            text="DRAFT",
            textangle=-30,
            opacity=0.1,
            font=dict(color="black", size=100),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
    ]
)
pio.templates.default = "draft"

fig = go.Figure()
fig.show()
```

#### Combining themes

You may have noticed that figures displayed with the custom templates defined above do not have the gray background and white gridlines that are part of the default styling of figures created with plotly.py. The reason for this is that the default styling is specified in a template named `"plotly"`, and specifying a custom template overrides the default `"plotly"` template.

If you want the styling of a custom template to be applied on top of the default styling of the `"plotly"` template, then you will need to combine the custom template with the `"plotly"` template. Multiple registered templates (whether built-in or user-defined) can be combined by specifying a template string that contains multiple template names joined on `"+"` characters.

Here is an example of setting the default template to be a combination of the built-in `"plotly"` template and the custom `"draft"` template from the previous example.

```python
import plotly.graph_objects as go
import plotly.io as pio

pio.templates["draft"] = go.layout.Template(
    layout_annotations=[
        dict(
            name="draft watermark",
            text="DRAFT",
            textangle=-30,
            opacity=0.1,
            font=dict(color="black", size=100),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
    ]
)
pio.templates.default = "plotly+draft"

fig = go.Figure()
fig.show()
```

Combining themes is also supported by Plotly Express

```python
import plotly.io as pio
import plotly.express as px

pio.templates["draft"] = go.layout.Template(
    layout_annotations=[
        dict(
            name="draft watermark",
            text="DRAFT",
            textangle=-30,
            opacity=0.1,
            font=dict(color="black", size=100),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
    ]
)
pio.templates.default = "plotly+draft"

df = px.data.gapminder()
df_2007 = df.query("year==2007")

fig = px.scatter(df_2007,
                 x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 log_x=True, size_max=60,
                 title="Gapminder 2007: current default theme")
fig.show()
```

<!-- #region -->

#### Saving and distributing custom themes

The easiest way to save and distribute a custom template is to make a `*.py` file that creates and registers the template when it is imported. Here is an example of the contents of a file called `my_themes.py` that creates and registers the `"draft"` template when it is imported

**my_themes.py**

---

```python
import plotly.graph_objects as go
import plotly.io as pio

pio.templates["draft"] = go.layout.Template(
    layout_annotations=[
        dict(
            name="draft watermark",
            text="DRAFT",
            textangle=-30,
            opacity=0.1,
            font=dict(color="black", size=100),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
    ]
)
```

---

To get access to the `"draft"` template, import the `my_themes` module.

```python
import my_themes
import plotly.io as pio
pio.templates.default = "draft"
...
```

> Note: In order for the import to succeed, the `my_themes.py` file must be on Python's module search path. See https://docs.python.org/3/tutorial/modules.html#the-module-search-path for more information.

<!-- #endregion -->

#### Examining built-in themes

It may be useful to examine the contents and structure of the built-in templates when creating your own custom templates. The `Template` graph object for a registered template can be loaded using dictionary-style key access on the `plotly.io.templates` configuration object. Here is an example of loading the `Template` graph object for the `"plotly"` template, and then displaying the value of the template's `layout` property.

```python
import plotly.io as pio
plotly_template = pio.templates["plotly"]
plotly_template.layout
```
