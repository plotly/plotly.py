import plotly.plotly as ply
import plotly.offline as plo
import plotly.graph_objs as go
from IPython.display import display, Image
from . import to_image

_show_config = {'default_backend': 'ipywidgets-notebook'}

def show(fig, backend=None):
    if backend is None:
        backend = _show_config.get('default_backend', 'ipywidgets-notebook')

    if backend == 'offline-notebook':
        plo.iplot(fig)
    elif backend == 'offline-browser':
        plo.plot(fig, auto_open=True)
    elif backend == 'online-notebook':
        display(ply.iplot(fig))
    elif backend == 'online-browser':
        ply.plot(fig, auto_open=True)
    elif backend == 'ipywidgets-notebook':
        if not isinstance(fig, go.FigureWidget):
            fig = go.FigureWidget(fig)
        display(fig)
    elif backend == 'image-notebook':
        img = to_image(fig)
        display(Image(img))
    else:
        raise ValueError("Invalid backend '%s'" % backend)


def set_backend(backend):
    _show_config['default_backend'] = backend