import base64
import json
import webbrowser
import uuid
import inspect

import six
from plotly.io import to_json, to_image
from plotly import utils, optional_imports
from plotly.io._orca import ensure_server
from plotly.offline.offline import _get_jconfig, get_plotlyjs

ipython_display = optional_imports.get_module('IPython.display')

try:
    from http.server import BaseHTTPRequestHandler, HTTPServer
except ImportError:
    # Python 2.7
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class RendererRepr(object):
    """
    A mixin implementing a simple __repr__ for Renderer classes
    """
    def __repr__(self):
        try:
            init_sig = inspect.signature(self.__init__)
            init_args = list(init_sig.parameters.keys())
        except AttributeError:
            # Python 2.7
            argspec = inspect.getargspec(self.__init__)
            init_args = [a for a in argspec.args if a != 'self']

        return "{cls}({attrs})\n{doc}".format(
            cls=self.__class__.__name__,
            attrs=", ".join("{}={!r}".format(k, self.__dict__[k])
                           for k in init_args),
            doc=self.__doc__)


class MimetypeRenderer(RendererRepr):
    """
    Base class for all mime type renderers
    """
    def activate(self):
        pass

    def to_mimebundle(self, fig_dict):
        raise NotImplementedError()


class JsonRenderer(MimetypeRenderer):
    """
    Renderer to display figures as JSON hierarchies.  This renderer is
    compatible with JupyterLab and VSCode.

    mime type: 'application/json'
    """
    def to_mimebundle(self, fig_dict):
        value = json.loads(to_json(fig_dict))
        return {'application/json': value}


# Plotly mimetype
class PlotlyRenderer(MimetypeRenderer):
    """
    Renderer to display figures using the plotly mime type.  This renderer is
    compatible with JupyterLab (using the @jupyterlab/plotly-extension),
    VSCode, and nteract.

    mime type: 'application/vnd.plotly.v1+json'
    """
    def __init__(self, config=None):
        self.config = dict(config) if config else {}

    def to_mimebundle(self, fig_dict):
        config = _get_jconfig(self.config)
        if config:
            fig_dict['config'] = config
        return {'application/vnd.plotly.v1+json': fig_dict}


# Static Image
class ImageRenderer(MimetypeRenderer):
    """
    Base class for all static image renderers
    """
    def __init__(self,
                 mime_type,
                 b64_encode=False,
                 format=None,
                 width=None,
                 height=None,
                 scale=None):

        self.mime_type = mime_type
        self.b64_encode = b64_encode
        self.format = format
        self.width = width
        self.height = height
        self.scale = scale

    def activate(self):
        # Start up orca server to reduce the delay on first render
        ensure_server()

    def to_mimebundle(self, fig_dict):
        image_bytes = to_image(
            fig_dict,
            format=self.format,
            width=self.width,
            height=self.height,
            scale=self.scale)

        if self.b64_encode:
            image_str = base64.b64encode(image_bytes).decode('utf8')
        else:
            image_str = image_bytes.decode('utf8')

        return {self.mime_type: image_str}


class PngRenderer(ImageRenderer):
    """
    Renderer to display figures as static PNG images.  This renderer requires
    the orca command-line utility and is broadly compatible across IPython
    environments (classic Jupyter Notebook, JupyterLab, QtConsole, VSCode,
    PyCharm, etc) and nbconvert targets (HTML, PDF, etc.).

    mime type: 'image/png'
    """
    def __init__(self, width=None, height=None, scale=None):
        super(PngRenderer, self).__init__(
            mime_type='image/png',
            b64_encode=True,
            format='png',
            width=width,
            height=height,
            scale=scale)


class SvgRenderer(ImageRenderer):
    """
    Renderer to display figures as static SVG images.  This renderer requires
    the orca command-line utility and is broadly compatible across IPython
    environments (classic Jupyter Notebook, JupyterLab, QtConsole, VSCode,
    PyCharm, etc) and nbconvert targets (HTML, PDF, etc.).

    mime type: 'image/svg+xml'
    """
    def __init__(self, width=None, height=None, scale=None):
        super(SvgRenderer, self).__init__(
            mime_type='image/svg+xml',
            b64_encode=False,
            format='svg',
            width=width,
            height=height,
            scale=scale)


class JpegRenderer(ImageRenderer):
    """
    Renderer to display figures as static JPEG images.  This renderer requires
    the orca command-line utility and is broadly compatible across IPython
    environments (classic Jupyter Notebook, JupyterLab, QtConsole, VSCode,
    PyCharm, etc) and nbconvert targets (HTML, PDF, etc.).

    mime type: 'image/jpeg'
    """
    def __init__(self, width=None, height=None, scale=None):
        super(JpegRenderer, self).__init__(
            mime_type='image/jpeg',
            b64_encode=True,
            format='jpg',
            width=width,
            height=height,
            scale=scale)


class PdfRenderer(ImageRenderer):
    """
    Renderer to display figures as static PDF images.  This renderer requires
    the orca command-line utility and is compatible with JupyterLab and the
    LaTeX-based nbconvert export to PDF.

    mime type: 'application/pdf'
    """
    def __init__(self, width=None, height=None, scale=None):
        super(PdfRenderer, self).__init__(
            mime_type='application/pdf',
            b64_encode=True,
            format='pdf',
            width=width,
            height=height,
            scale=scale)


# HTML
# Build script to set global PlotlyConfig object. This must execute before
# plotly.js is loaded.
_window_plotly_config = """\
window.PlotlyConfig = {MathJaxConfig: 'local'};"""


class HtmlRenderer(MimetypeRenderer):
    """
    Base class for all HTML mime type renderers

    mime type: 'text/html'
    """
    def __init__(self,
                 connected=False,
                 fullhtml=False,
                 requirejs=True,
                 global_init=False,
                 config=None,
                 auto_play=False):

        self.config = dict(config) if config else {}
        self.auto_play = auto_play
        self.connected = connected
        self.global_init = global_init
        self.requirejs = requirejs
        self.fullhtml = fullhtml

    def activate(self):
        if self.global_init:
            if not ipython_display:
                raise ValueError(
                    'The {cls} class requires ipython but it is not installed'
                    .format(cls=self.__class__.__name__))

            if not self.requirejs:
                raise ValueError(
                    'global_init is only supported with requirejs=True')

            if self.connected:
                # Connected so we configure requirejs with the plotly CDN
                script = """\
        <script type="text/javascript">
        {win_config}
        if (typeof require !== 'undefined') {{
        require.undef("plotly");
        requirejs.config({{
            paths: {{
                'plotly': ['https://cdn.plot.ly/plotly-latest.min']
            }}
        }});
        require(['plotly'], function(Plotly) {{
            window._Plotly = Plotly;
        }});
        }}
        </script>
        """.format(win_config=_window_plotly_config)

            else:
                # If not connected then we embed a copy of the plotly.js
                # library in the notebook
                script = """\
        <script type="text/javascript">
        {win_config}
        if (typeof require !== 'undefined') {{
        require.undef("plotly");
        define('plotly', function(require, exports, module) {{
            {script}
        }});
        require(['plotly'], function(Plotly) {{
            window._Plotly = Plotly;
        }});
        }}
        </script>
        """.format(script=get_plotlyjs(), win_config=_window_plotly_config)

            ipython_display.display_html(script, raw=True)

    def to_mimebundle(self, fig_dict):
        plotdivid = uuid.uuid4()

        # Serialize figure
        jdata = json.dumps(
            fig_dict.get('data', []), cls=utils.PlotlyJSONEncoder)
        jlayout = json.dumps(
            fig_dict.get('layout', {}), cls=utils.PlotlyJSONEncoder)

        if fig_dict.get('frames', None):
            jframes = json.dumps(
                fig_dict.get('frames', []), cls=utils.PlotlyJSONEncoder)
        else:
            jframes = None

        # Serialize figure config
        config = _get_jconfig(self.config)
        jconfig = json.dumps(config)

        # Platform URL
        plotly_platform_url = config.get('plotly_domain', 'https://plot.ly')

        # Build script body
        if jframes:
            if self.auto_play:
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

        # Build div

        # Handle require
        if self.requirejs:
            require_start = 'require(["plotly"], function(Plotly) {'
            require_end = '});'
            load_plotlyjs = ''
        else:
            require_start = ''
            require_end = ''
            if self.connected:
                load_plotlyjs = """\
<script type="text/javascript">{win_config}</script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>""".format(
                    win_config=_window_plotly_config)
            else:
                load_plotlyjs = """\
<script type="text/javascript">{win_config}</script>
<script type="text/javascript">
{plotlyjs}
</script>""".format(win_config=_window_plotly_config, plotlyjs=get_plotlyjs())

        # Handle fullhtml
        if self.fullhtml:
            html_start = ''
            html_end = ''
        else:
            html_start = ''
            html_end = ''

        plotly_html_div = """
{html_start}
    {load_plotlyjs}
    <div id="{id}" class="plotly-graph-div"></div>
    <script type="text/javascript">
        {require_start}
            window.PLOTLYENV=window.PLOTLYENV || {{}};
            window.PLOTLYENV.BASE_URL='{plotly_platform_url}'
            {script}
        {require_end}
    </script>
{html_end}""".format(
            html_start=html_start,
            load_plotlyjs=load_plotlyjs,
            id=plotdivid,
            plotly_platform_url=plotly_platform_url,
            require_start=require_start,
            script=script,
            require_end=require_end,
            html_end=html_end)

        return {'text/html': plotly_html_div}


class NotebookRenderer(HtmlRenderer):
    """
    Renderer to display interactive figures in the classic Jupyter Notebook.
    This renderer is also useful for notebooks that will be converted to
    HTML using nbconvert/nbviewer as it will produce standalone HTML files
    that include interactive figures.

    This renderer automatically performs global notebook initialization when
    activated.

    mime type: 'text/html'
    """
    def __init__(self, connected=False, config=None, auto_play=False):
        super(NotebookRenderer, self).__init__(
            connected=connected,
            fullhtml=False,
            requirejs=True,
            global_init=True,
            config=config,
            auto_play=auto_play)


class KaggleRenderer(HtmlRenderer):
    """
    Renderer to display interactive figures in Kaggle Notebooks.

    Same as NotebookRenderer but with connected=True so that the plotly.js
    bundle is loaded from a CDN rather than being embedded in the notebook.

    This renderer is enabled by default when running in a Kaggle notebook.

    mime type: 'text/html'
    """
    def __init__(self, config=None, auto_play=False):
        super(KaggleRenderer, self).__init__(
            connected=True,
            fullhtml=False,
            requirejs=True,
            global_init=True,
            config=config,
            auto_play=auto_play)


class ColabRenderer(HtmlRenderer):
    """
    Renderer to display interactive figures in Google Colab Notebooks.

    This renderer is enabled by default when running in a Colab notebook.

    mime type: 'text/html'
    """
    def __init__(self, config=None, auto_play=False):
        super(ColabRenderer, self).__init__(
            connected=True,
            fullhtml=True,
            requirejs=False,
            global_init=False,
            config=config,
            auto_play=auto_play)


class SideEffectRenderer(RendererRepr):
    """
    Base class for side-effect renderers.  SideEffectRenderer subclasses
    do not display figures inline in a notebook environment, but render
    figures by some external means (e.g. a separate browser tab).

    Unlike MimetypeRenderer subclasses, SideEffectRenderer subclasses are not
    invoked when a figure is asked to display itself in the notebook.
    Instead, they are invoked when the plotly.io.show function is called
    on a figure.
    """
    def activate(self):
        pass

    def render(self, fig):
        raise NotImplementedError()


def open_html_in_browser(html, using=None, new=0, autoraise=True):
    """
    Display html in a web browser without creating a temp file.

    Instantiates a trivial http server and uses the webbrowser modeul to
    open a URL to retrieve html from that server.

    Parameters
    ----------
    html: str
        HTML string to display
    using, new, autoraise:
        See docstrings in webbrowser.get and webbrowser.open
    """
    if isinstance(html, six.string_types):
        html = html.encode('utf8')

    class OneShotRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            bufferSize = 1024*1024
            for i in range(0, len(html), bufferSize):
                self.wfile.write(html[i:i+bufferSize])

        def log_message(self, format, *args):
            # Silence stderr logging
            pass

    server = HTTPServer(('127.0.0.1', 0), OneShotRequestHandler)
    webbrowser.get(using).open(
        'http://127.0.0.1:%s' % server.server_port,
        new=new,
        autoraise=autoraise)

    server.handle_request()


class BrowserRenderer(SideEffectRenderer):
    """
    Renderer to display interactive figures in an external web browser.
    This renderer will open a new browser window or tab when the
    plotly.io.show function is called on a figure.

    This renderer has no ipython/jupyter dependencies and is a good choice
    for use in environments that do not support the inline display of
    interactive figures.

    mime type: 'text/html'
    """
    def __init__(self,
                 config=None,
                 auto_play=False,
                 using=None,
                 new=0,
                 autoraise=True):

        # TODO: add browser name and open num here
        # define
        self.config = config
        self.auto_play = auto_play
        self.using = using
        self.new = new
        self.autoraise = autoraise

    def render(self, fig_dict):
        renderer = HtmlRenderer(
            connected=False,
            fullhtml=True,
            requirejs=False,
            global_init=False,
            config=self.config,
            auto_play=self.auto_play)

        bundle = renderer.to_mimebundle(fig_dict)
        html = bundle['text/html']
        open_html_in_browser(html, self.using, self.new, self.autoraise)
