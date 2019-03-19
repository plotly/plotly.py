import uuid
import json
import os
import webbrowser

import six

from plotly.io._utils import validate_coerce_fig_to_dict
from plotly.offline.offline import _get_jconfig, get_plotlyjs
from plotly import utils


# Build script to set global PlotlyConfig object. This must execute before
# plotly.js is loaded.
_window_plotly_config = """\
window.PlotlyConfig = {MathJaxConfig: 'local'};"""


def to_div(fig,
           config=None,
           auto_play=True,
           include_plotlyjs=True,
           include_mathjax=False,
           validate=True):
    """
    Convert a figure to an HTML div representation

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure
    config: dict or None (default None)
        Plotly.js figure config options
    auto_play: bool (default=True)
        Whether to automatically start the animation sequence on page load
        if the figure contains frames. Has no effect if the figure does not
        contain frames.
    include_plotlyjs: bool or string (default True)
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
        directory as the HTML file.

        If 'require', Plotly.js is loaded using require.js.  This option
        assumes that require.js is globally available and that it has been
        globally configured to know how to find Plotly.js as 'plotly'.

        If a string that ends in '.js', a script tag is included that
        references the specified path. This approach can be used to point
        the resulting HTML file to an alternative CDN or local bundle.

        If False, no script tag referencing plotly.js is included. This is
        useful when the resulting div string will be placed inside an HTML
        document that already loads plotly.js.
    include_mathjax: bool or string (default False)
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
   validate: bool (default True)
        True if the figure should be validated before being converted to
        JSON, False otherwise.
    Returns
    -------
    str
        Representation of figure as an HTML div string
    """
    # ## Validate figure ##
    fig_dict = validate_coerce_fig_to_dict(fig, validate)

    # ## Generate div id ##
    plotdivid = uuid.uuid4()

    # ## Serialize figure ##
    jdata = json.dumps(
        fig_dict.get('data', []), cls=utils.PlotlyJSONEncoder)
    jlayout = json.dumps(
        fig_dict.get('layout', {}), cls=utils.PlotlyJSONEncoder)

    if fig_dict.get('frames', None):
        jframes = json.dumps(
            fig_dict.get('frames', []), cls=utils.PlotlyJSONEncoder)
    else:
        jframes = None

    # ## Serialize figure config ##
    config = _get_jconfig(config)
    jconfig = json.dumps(config)

    # ## Get platform URL ##
    plotly_platform_url = config.get('plotly_domain', 'https://plot.ly')

    # ## Build script body ##
    # This is the part that actually calls Plotly.js
    if jframes:
        if auto_play:
            animate = """.then(function(){{
                        Plotly.animate('{id}');
                    }}""".format(id=plotdivid)

        else:
            animate = ''

        script = '''
                if (document.getElementById("{id}")) {{
                    Plotly.plot(
                        '{id}',
                        {data},
                        {layout},
                        {config}
                    ).then(function () {add_frames}){animate}
                }}
                    '''.format(
            id=plotdivid,
            data=jdata,
            layout=jlayout,
            config=jconfig,
            add_frames="{" + "return Plotly.addFrames('{id}',{frames}".format(
                id=plotdivid, frames=jframes
            ) + ");}",
            animate=animate
        )
    else:
        script = """
            if (document.getElementById("{id}")) {{
                Plotly.newPlot("{id}", {data}, {layout}, {config}); 
            }}
            """.format(
            id=plotdivid,
            data=jdata,
            layout=jlayout,
            config=jconfig)

    # ## Handle loading/initializing plotly.js ##
    include_plotlyjs_orig = include_plotlyjs
    if isinstance(include_plotlyjs, six.string_types):
        include_plotlyjs = include_plotlyjs.lower()

    # Start/end of requirejs block (if any)
    require_start = ''
    require_end = ''

    # Init and load
    load_plotlyjs = ''

    # Init plotlyjs. This block needs to run before plotly.js is loaded in
    # order for MathJax configuration to work properly
    init_plotlyjs = """"<script type = "text/javascript">\
window.PlotlyConfig = {MathJaxConfig: 'local'};</script>"""

    if include_plotlyjs == 'require':
        require_start = 'require(["plotly"], function(Plotly) {'
        require_end = '});'

    elif include_plotlyjs == 'cdn':
        load_plotlyjs = """\
    {init_plotlyjs}
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>\
""".format(init_plotlyjs=init_plotlyjs)

    elif include_plotlyjs == 'directory':
        load_plotlyjs = """\
    {init_plotlyjs}
    <script src="plotly.min.js"></script>\
""".format(init_plotlyjs=init_plotlyjs)

    elif (isinstance(include_plotlyjs, six.string_types) and
          include_plotlyjs.endswith('.js')):
        load_plotlyjs = """\
    {init_plotlyjs}
    <script src="{url}"></script>\
""".format(init_plotlyjs=init_plotlyjs,
           url=include_plotlyjs_orig)

    elif include_plotlyjs:
        load_plotlyjs = """\
    {init_plotlyjs}
    <script type="text/javascript">{plotlyjs}</script>\
""".format(init_plotlyjs=init_plotlyjs,
           plotlyjs=get_plotlyjs())

    # ## Handle loading/initializing MathJax ##
    include_mathjax_orig = include_mathjax
    if isinstance(include_mathjax, six.string_types):
        include_mathjax = include_mathjax.lower()

    mathjax_template = """\
<script src="{url}?config=TeX-AMS-MML_SVG"></script>"""

    if include_mathjax == 'cdn':
        mathjax_script = mathjax_template.format(
            url=('https://cdnjs.cloudflare.com' 
                 '/ajax/libs/mathjax/2.7.5/MathJax.js'))

    elif (isinstance(include_mathjax, six.string_types) and
          include_mathjax.endswith('.js')):

        mathjax_script = mathjax_template.format(
            url=include_mathjax_orig)
    elif not include_mathjax:
        mathjax_script = ''
    else:
        raise ValueError("""\
Invalid value of type {typ} received as the include_mathjax argument
    Received value: {val}

include_mathjax may be specified as False, 'cdn', or a string ending with '.js' 
""".format(typ=type(include_mathjax), val=repr(include_mathjax)))

    plotly_html_div = """\
<div>
    {mathjax_script}
    {load_plotlyjs}
        <div id="{id}" class="plotly-graph-div"></div>
        <script type="text/javascript">
            {require_start}
                window.PLOTLYENV=window.PLOTLYENV || {{}};
                window.PLOTLYENV.BASE_URL='{plotly_platform_url}'
                {script}
            {require_end}
        </script>
    </div>""".format(
        mathjax_script=mathjax_script,
        load_plotlyjs=load_plotlyjs,
        id=plotdivid,
        plotly_platform_url=plotly_platform_url,
        require_start=require_start,
        script=script,
        require_end=require_end)

    return plotly_html_div


def to_html(fig,
            config=None,
            auto_play=True,
            include_plotlyjs=True,
            include_mathjax=False,
            validate=True):

    div = to_div(fig,
                 config=config,
                 auto_play=auto_play,
                 include_plotlyjs=include_plotlyjs,
                 include_mathjax=include_mathjax,
                 validate=validate)
    return """\
<html>
<head><meta charset="utf-8" /></head>
<body>
    {div}
</body>
</html>""".format(div=div)


def write_html(fig,
               file,
               config=None,
               auto_play=True,
               include_plotlyjs=True,
               include_mathjax=False,
               validate=True,
               auto_open=False):

    # Build HTML string
    html_str = to_html(
        fig,
        config=config,
        auto_play=auto_play,
        include_plotlyjs=include_plotlyjs,
        include_mathjax=include_mathjax,
        validate=validate)

    # Check if file is a string
    file_is_str = isinstance(file, six.string_types)

    # Write HTML string
    if file_is_str:
        with open(file, 'w') as f:
            f.write(html_str)
    else:
        file.write(html_str)

    # Check if we should copy plotly.min.js to output directory
    if file_is_str and include_plotlyjs == 'directory':
        bundle_path = os.path.join(
            os.path.dirname(file), 'plotly.min.js')

        if not os.path.exists(bundle_path):
            with open(bundle_path, 'w') as f:
                f.write(get_plotlyjs())

    # Handle auto_open
    if file_is_str and auto_open:
        url = 'file://' + os.path.abspath(file)
        webbrowser.open(url)
