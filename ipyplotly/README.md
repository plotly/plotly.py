ipyplotly
=========

Experiments towards a Pythonic [Plotly](https://plot.ly/) API 
and [ipywidget](http://ipywidgets.readthedocs.io/en/latest/index.html) for use in the Jupyter Notebook.

Features
--------
 - Plots may be displayed in the notebook, and then updated in-place using property assignment syntax.
 - The entire plotting API is now discoverable using tab completion and documented with descriptive docstrings.
 - Property validation is performed in the Python library and informative error messages are raised on validation 
 failures.
 - Arbitrary Python callbacks may be executed upon zoom, pan, click, hover, and data selection events.
 - Multiple views of the same plot may be displayed across different notebook output cells.
 - Static PNG and SVG images may be exported programmatically with no external dependencies or network connection 
 required.
 - Plot transitions may be animated with custom duration and easing properties.
 - Numpy arrays are transferred between the Python and JavaScript libraries using the binary serialization protocol 
 introduced in ipywidgets 7.0.
 - Plots may be combined with built-in 
 [ipywidgets](http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html) 
 to create rich dashboard layouts in the notebook


Development Installation
------------------------

For a development installation (requires npm),

    $ git clone https://github.com/jmmease/ipyplotly.git
    $ cd ipyplotly
    $ pip install -e .
    $ pip install yapf
    $ python setup.py codegen
    $ jupyter nbextension enable --py widgetsnbextension
    $ jupyter nbextension install --py --symlink --sys-prefix ipyplotly
    $ jupyter nbextension enable --py --sys-prefix ipyplotly

Python Version Requirements
---------------------------
 - Usage requires Python >= 3.5
 - Code generation requires Python >= 3.6

Future
------
This project was a successful experiment to test the feasibility of creating a 
Plotly ipywidget library.  This approach has been embraced by the official
[plotly.py](https://github.com/plotly/plotly.py) project and will be integrated into
a new major version of plotly.py in the not-too-distant future.

See [plotly/plotly.py#942](https://github.com/plotly/plotly.py/pull/942) for current status.
