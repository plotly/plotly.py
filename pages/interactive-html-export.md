---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.6
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
    version: 3.10.11
  plotly:
    description: Plotly allows you to save interactive HTML versions of your figures
      to your local disk.
    display_as: file_settings
    language: python
    layout: base
    name: Interactive HTML Export
    order: 31
    page_type: u-guide
    permalink: python/interactive-html-export/
    thumbnail: thumbnail/static-image-export.png
---

### Interactive vs Static Export

Plotly figures are interactive when viewed in a web browser: you can hover over data points, pan and zoom axes, and show and hide traces by clicking or double-clicking on the legend. You can export figures either to [static image file formats like PNG, JPEG, SVG or PDF](static-image-export.md) or you can export them to HTML files which can be opened in a browser. This page explains how to do the latter.

<!-- #region -->
### Saving to an HTML file

Any figure can be saved as an HTML file using the `write_html` method. These HTML files can be opened in any web browser to access the fully interactive figure.

```python
import plotly.express as px

fig = px.scatter(x=range(10), y=range(10))
fig.write_html("path/to/file.html")
```
<!-- #endregion -->

### Controlling the size of the HTML file

By default, the resulting HTML file is a fully self-contained HTML file which can be uploaded to a web server or shared via email or other file-sharing mechanisms. The downside to this approach is that the file is very large (5Mb+) because it contains an inlined copy of the Plotly.js library required to make the figure interactive. This can be controlled via the `include_plotlyjs` argument (see below).

### Inserting Plotly Output into HTML using a Jinja2 Template

You can insert Plotly output and text related to your data into HTML templates using Jinja2. Use `.to_html` to send the HTML to a Python string variable rather than using `write_html` to send the HTML to a disk file.  Use the `full_html=False` option to output just the code necessary to add a figure to a template. We don't want to output a full HTML page, as the template will define the rest of the page's structure — for example, the page's `HTML` and `BODY` tags.  First create an HTML template file containing a Jinja `{{ variable }}`.  In this example, we customize the HTML in the template file by replacing the Jinja variable `{{ fig }}` with our graphic `fig`.

<!-- #region -->

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;meta charset="utf-8" /&gt;   &lt;!--It is necessary to use the UTF-8 encoding with plotly graphics to get e.g. negative signs to render correctly --&gt;
&lt;meta name="viewport" content="width=device-width, initial-scale=1.0" /&gt;
&lt;/head&gt;

&lt;body&gt;
&lt;h1&gt;Here's a Plotly graph!&lt;/h1&gt;
{{ fig }}
&lt;p&gt;And here's some text after the graph.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
```


Then use the following Python to replace `{{ fig }}` in the template with HTML that will display the Plotly figure "fig":

```python
import plotly.express as px
from jinja2 import Template

data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')

output_html_path=r"/path/to/output.html"
input_template_path = r"/path/to/template.html"

plotly_jinja_data = {"fig":fig.to_html(full_html=False)}
#consider also defining the include_plotlyjs parameter to point to an external Plotly.js as described above

with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_template_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))
```
<!-- #endregion -->

### HTML export in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python {hide_code=true}
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'interactive-html-export', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Full Parameter Documentation

```python
import plotly.graph_objects as go

help(go.Figure.write_html)
```

**Output:**
```
Help on function write_html in module plotly.basedatatypes:

write_html(self, *args, **kwargs)
    Write a figure to an HTML file representation

    Parameters
    ----------
    file : str or writeable
        A string representing a local file path or a writeable object
        (e.g. a pathlib.Path object or an open file descriptor)
    config : dict or None (default None)
        Plotly.js figure config options
    auto_play : bool (default=True)
        Whether to automatically start the animation sequence on page load
        if the figure contains frames. Has no effect if the figure does not
        contain frames.
    include_plotlyjs : bool or string (default True)
        Specifies how the plotly.js library is included/loaded in the output
        div string.

        If True, a script tag containing the plotly.js source code (~3MB)
        is included in the output.  HTML files generated with this option are
        fully self-contained and can be used offline.

        If 'cdn', a script tag that references the plotly.js CDN is included
        in the output. HTML files generated with this option are about 3MB
        smaller than those generated with include_plotlyjs=True, but they
        require an active internet connection in order to load the plotly.js
        library.

        If 'directory', a script tag is included that references an external
        plotly.min.js bundle that is assumed to reside in the same
        directory as the HTML file. If `file` is a string to a local file
        path and `full_html` is True, then the plotly.min.js bundle is copied
        into the directory of the resulting HTML file. If a file named
        plotly.min.js already exists in the output directory then this file
        is left unmodified and no copy is performed. HTML files generated
        with this option can be used offline, but they require a copy of
        the plotly.min.js bundle in the same directory. This option is
        useful when many figures will be saved as HTML files in the same
        directory because the plotly.js source code will be included only
        once per output directory, rather than once per output file.

        If a string that ends in '.js', a script tag is included that
        references the specified path. This approach can be used to point
        the resulting HTML file to an alternative CDN or local bundle.

        If False, no script tag referencing plotly.js is included. This is
        useful when the resulting div string will be placed inside an HTML
        document that already loads plotly.js.  This option is not advised
        when full_html=True as it will result in a non-functional html file.

    include_mathjax : bool or string (default False)
        Specifies how the MathJax.js library is included in the output html
        div string.  MathJax is required in order to display labels
        with LaTeX typesetting.

        If False, no script tag referencing MathJax.js will be included in the
        output.

        If 'cdn', a script tag that references a MathJax CDN location will be
        included in the output.  HTML div strings generated with this option
        will be able to display LaTeX typesetting as long as internet access
        is available.

        If a string that ends in '.js', a script tag is included that
        references the specified path. This approach can be used to point the
        resulting HTML div string to an alternative CDN.
    post_script : str or list or None (default None)
        JavaScript snippet(s) to be included in the resulting div just after
        plot creation.  The string(s) may include '{plot_id}' placeholders
        that will then be replaced by the `id` of the div element that the
        plotly.js figure is associated with.  One application for this script
        is to install custom plotly.js event handlers.
    full_html : bool (default True)
        If True, produce a string containing a complete HTML document
        starting with an <html> tag.  If False, produce a string containing
        a single <div> element.
    animation_opts : dict or None (default None)
        dict of custom animation parameters to be passed to the function
        Plotly.animate in Plotly.js. See
        https://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js
        for available options. Has no effect if the figure does not contain
        frames, or auto_play is False.
    default_width, default_height : number or str (default '100%')
        The default figure width/height to use if the provided figure does not
        specify its own layout.width/layout.height property.  May be
        specified in pixels as an integer (e.g. 500), or as a css width style
        string (e.g. '500px', '100%').
    validate : bool (default True)
        True if the figure should be validated before being converted to
        JSON, False otherwise.
    auto_open : bool (default True)
        If True, open the saved file in a web browser after saving.
        This argument only applies if `full_html` is True.
    div_id : str (default None)
        If provided, this is the value of the id attribute of the div tag. If None, the
        id attribute is a UUID.

    Returns
    -------
    None
```
