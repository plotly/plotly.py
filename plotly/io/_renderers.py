from __future__ import absolute_import, division

import textwrap
import six
import os

from IPython.display import display

from plotly.io._base_renderers import (
    MimetypeRenderer, SideEffectRenderer, PlotlyRenderer, NotebookRenderer,
    KaggleRenderer, ColabRenderer, JsonRenderer, PngRenderer, JpegRenderer,
    SvgRenderer, PdfRenderer, BrowserRenderer)
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
renderers['firefox'] = BrowserRenderer(config=config, using='firefox')
renderers['chrome'] = BrowserRenderer(config=config, using='chrome')

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
