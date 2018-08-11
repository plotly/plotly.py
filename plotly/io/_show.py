import plotly.plotly as ply
import plotly.offline as plo
import plotly.graph_objs as go
from IPython.display import display, Image
from plotly.basedatatypes import BaseFigure
from . import to_image

_show_config = {'default_backend': 'ipywidgets-notebook'}

def show(fig, backend=None, **kwargs):
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
    elif backend == 'image-ipython':
        img = to_image(fig)
        display(Image(img))
    elif backend == 'offline-qt':
        show_qt(fig, **kwargs)
    else:
        raise ValueError("Invalid backend '%s'" % backend)


def set_backend(backend):
    _show_config['default_backend'] = backend


def get_backend():
    return _show_config['default_backend']

# Hold references to views so they're not garbage collected
_qt_views = []

def show_qt(fig):
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    raw_html = '<html><head><meta charset="utf-8" />'
    raw_html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
    raw_html += '<body>'
    raw_html += plo.plot(fig, include_plotlyjs=False, output_type='div')
    raw_html += '</body></html>'

    if hasattr(fig, '_window') and fig._window is not None and fig._window.isVisible():
        # Reuse window
        fig_view = fig._window
    else:
        # Create a new window
        fig_view = QWebEngineView()

    # setHtml has a 2MB size limit, need to switch to setUrl on tmp file
    # for large figures.
    fig_view.setHtml(raw_html)
    fig_view.show()
    fig_view.raise_()
    if isinstance(fig, BaseFigure):
        fig._window = fig_view

    _qt_views.append(fig_view)
