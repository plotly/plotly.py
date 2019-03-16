from __future__ import absolute_import, division

import base64
import json
import textwrap
import uuid
import six
import os
import webbrowser

from IPython.display import display_html, display

from plotly import utils
from plotly.io import to_json, to_image
from plotly.io._orca import ensure_server
from plotly.offline.offline import _get_jconfig, get_plotlyjs
from plotly.io._utils import validate_coerce_fig_to_dict


# Renderer configuration class
# -----------------------------
class RenderersConfig(object):
    """
    Singleton object containing the current renderer configurations
    """
    def __init__(self):
        self._renderers = {}
        self._default_name = None
        self._default_renderers = []

    # ### Magic methods ###
    # Make this act as a dict of renderers
    def __len__(self):
        return len(self._renderers)

    def __contains__(self, item):
        return item in self._renderers

    def __iter__(self):
        return iter(self._renderers)

    def __getitem__(self, item):
        renderer = self._renderers[item]
        return renderer

    def __setitem__(self, key, value):
        if not isinstance(value, (MimetypeRenderer, SideEffectRenderer)):
            raise ValueError("""\
Renderer must be a subclass of MimetypeRenderer or SideEffectRenderer.
    Received value with type: {typ}""".format(typ=type(value)))

        self._renderers[key] = value

    def __delitem__(self, key):
        # Remove template
        del self._renderers[key]

        # Check if we need to remove it as the default
        if self._default == key:
            self._default = None

    def keys(self):
        return self._renderers.keys()

    def items(self):
        return self._renderers.items()

    def update(self, d={}, **kwargs):
        """
        Update one or more renderers from a dict or from input keyword
        arguments.

        Parameters
        ----------
        d: dict
            Dictionary from renderer names to new renderer objects.

        kwargs
            Named argument value pairs where the name is a renderer name
            and the value is a new renderer object
        """
        for k, v in dict(d, **kwargs).items():
            self[k] = v

    # ### Properties ###
    @property
    def default(self):
        """
        The default renderer, or None if no there is no default

        If not None, the default renderer is automatically used to render
        figures when they are displayed in a jupyter notebook or when using
        the plotly.io.show function

        The names of available templates may be retrieved with:

        >>> import plotly.io as pio
        >>> list(pio.renderers)

        Returns
        -------
        str
        """
        return self._default_name

    @default.setter
    def default(self, value):
        # Handle None
        if value is None:
            self._default_name = None
            self._default_renderers = []
            return

        # Store defaults name and list of renderer(s)
        renderer_names = self._validate_coerce_renderers(value)
        self._default_name = value
        self._default_renderers = [self[name] for name in renderer_names]

        # Activate default renderer(s)
        for renderer in self._default_renderers:
            renderer.activate()

    def _validate_coerce_renderers(self, renderers_string):
        # Validate value
        if not isinstance(renderers_string, six.string_types):
            raise ValueError('Renderer must be specified as a string')

        renderer_names = renderers_string.split('+')
        invalid = [name for name in renderer_names if name not in self]
        if invalid:
            raise ValueError("""
Invalid named renderer(s) received: {}""".format(str(invalid)))

        return renderer_names

    def __repr__(self):
        return """\
Renderers configuration
-----------------------
    Default renderer: {default}
    Available renderers:
{available}
""".format(default=repr(self.default),
           available=self._available_templates_str())

    def _available_templates_str(self):
        """
        Return nicely wrapped string representation of all
        available template names
        """
        available = '\n'.join(textwrap.wrap(
            repr(list(self)),
            width=79 - 8,
            initial_indent=' ' * 8,
            subsequent_indent=' ' * 9
        ))
        return available

    def _build_mime_bundle(self, fig_dict, renderers_string=None):
        if renderers_string:
            renderer_names = self._validate_coerce_renderers(renderers_string)
            renderers_list = [self[name] for name in renderer_names]
            for renderer in renderers_list:
                if isinstance(renderer, MimetypeRenderer):
                    renderer.activate()
        else:
            renderers_list = self._default_renderers

        bundle = {}
        for renderer in renderers_list:
            if isinstance(renderer, MimetypeRenderer):
                bundle.update(renderer.to_mimebundle(fig_dict))

        return bundle

    def _perform_side_effect_rendering(self, fig_dict, renderers_string=None):
        if renderers_string:
            renderer_names = self._validate_coerce_renderers(renderers_string)
            renderers_list = [self[name] for name in renderer_names]
            for renderer in renderers_list:
                if isinstance(renderer, SideEffectRenderer):
                    renderer.activate()
        else:
            renderers_list = self._default_renderers

        for renderer in renderers_list:
            if isinstance(renderer, SideEffectRenderer):
                renderer.render(fig_dict)


# Make config a singleton object
# ------------------------------
renderers = RenderersConfig()
del RenderersConfig


class MimetypeRenderer(object):
    def activate(self):
        pass

    def to_mimebundle(self, fig_dict):
        raise NotImplementedError()


# JSON
class JsonRenderer(MimetypeRenderer):
    def to_mimebundle(self, fig_dict):
        value = json.loads(to_json(fig_dict))
        return {'application/json': value}


# Plotly mimetype
class PlotlyRenderer(MimetypeRenderer):
    def __init__(self, config=None):
        self.config = dict(config) if config else {}

    def to_mimebundle(self, fig_dict):
        config = _get_jconfig(self.config)
        if config:
            fig_dict['config'] = config
        return {'application/vnd.plotly.v1+json': fig_dict}


# Static Image
class ImageRenderer(MimetypeRenderer):
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
    def __init__(self, width=None, height=None, scale=None):
        super(PngRenderer, self).__init__(
            mime_type='image/png',
            b64_encode=True,
            format='png',
            width=width,
            height=height,
            scale=scale)


class SvgRenderer(ImageRenderer):
    def __init__(self, width=None, height=None, scale=None):
        super(SvgRenderer, self).__init__(
            mime_type='image/svg+xml',
            b64_encode=False,
            format='svg',
            width=width,
            height=height,
            scale=scale)


class PdfRenderer(ImageRenderer):
    def __init__(self, width=None, height=None, scale=None):
        super(PdfRenderer, self).__init__(
            mime_type='application/pdf',
            b64_encode=True,
            format='pdf',
            width=width,
            height=height,
            scale=scale)


class JpegRenderer(ImageRenderer):
    def __init__(self, width=None, height=None, scale=None):
        super(JpegRenderer, self).__init__(
            mime_type='image/jpeg',
            b64_encode=True,
            format='jpg',
            width=width,
            height=height,
            scale=scale)


# HTML
# Build script to set global PlotlyConfig object. This must execute before
# plotly.js is loaded.
_window_plotly_config = """\
window.PlotlyConfig = {MathJaxConfig: 'local'};"""


class HtmlRenderer(MimetypeRenderer):

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

            display_html(script, raw=True)

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
    Same as NotebookRenderer but with connected True
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
    Google Colab compatible HTML renderer
    """
    def __init__(self, config=None, auto_play=False):
        super(ColabRenderer, self).__init__(
            connected=True,
            fullhtml=True,
            requirejs=False,
            global_init=False,
            config=config,
            auto_play=auto_play)


class SideEffectRenderer(object):

    def activate(self):
        pass

    def render(self, fig):
        raise NotImplementedError()


def open_html_in_browser(html):
    """Display html in the default web browser without creating a temp file.

    Instantiates a trivial http server and calls webbrowser.open with a URL
    to retrieve html from that server.
    """
    from http.server import BaseHTTPRequestHandler, HTTPServer

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
    webbrowser.open('http://127.0.0.1:%s' % server.server_port)
    server.handle_request()


class BrowserRenderer(SideEffectRenderer):
    def __init__(self, config=None, auto_play=False):
        self.config = config
        self.auto_play = auto_play

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
        open_html_in_browser(html)


# Show
def show(fig, renderer=None, validate=True):
    fig_dict = validate_coerce_fig_to_dict(fig, validate)

    # Mimetype renderers
    bundle = renderers._build_mime_bundle(
        fig_dict, renderers_string=renderer)
    if bundle:
        display(bundle, raw=True)

    # Side effect renderers
    renderers._perform_side_effect_rendering(
        fig_dict, renderers_string=renderer)


# Register renderers

# Plotly mime type
plotly_renderer = PlotlyRenderer()
renderers['plotly_mimetype'] = plotly_renderer
renderers['jupyterlab'] = plotly_renderer
renderers['nteract'] = plotly_renderer
renderers['vscode'] = plotly_renderer

# HTML-based
config = {'responsive': True}
renderers['notebook'] = NotebookRenderer(config=config)
renderers['notebook_connected'] = NotebookRenderer(
    config=config, connected=True)
renderers['kaggle'] = KaggleRenderer(config=config)
renderers['colab'] = ColabRenderer(config=config)

# JSON
renderers['json'] = JsonRenderer()

# Static Image
img_kwargs = dict(height=450, width=700)
renderers['png'] = PngRenderer(**img_kwargs)
jpeg_renderer = JpegRenderer(**img_kwargs)
renderers['jpeg'] = jpeg_renderer
renderers['jpg'] = jpeg_renderer

renderers['svg'] = SvgRenderer(**img_kwargs)
renderers['pdf'] = PdfRenderer(**img_kwargs)

# Side effects
renderers['browser'] = BrowserRenderer(config=config)

# Set default renderer
default_renderer = 'plotly_mimetype'

# Check Colab
try:
    import google.colab
    default_renderer = 'colab'
except ImportError:
    pass

# Check Kaggle
if os.path.exists('/kaggle/input'):
    default_renderer = 'kaggle'

# Set default renderer
renderers.default = default_renderer
