""" Plotly Offline
    A module to use Plotly's graphing library with Python
    without connecting to a public or private plotly enterprise
    server.
"""
from __future__ import absolute_import

import json
import os
import uuid

import requests

from plotly import session, tools, utils
from plotly.exceptions import PlotlyError

PLOTLY_OFFLINE_DIRECTORY = plotlyjs_path = os.path.expanduser(
    os.path.join(*'~/.plotly/plotlyjs'.split('/')))
PLOTLY_OFFLINE_BUNDLE = os.path.join(PLOTLY_OFFLINE_DIRECTORY,
                                     'plotly-ipython-offline-bundle.js')


__PLOTLY_OFFLINE_INITIALIZED = False


def download_plotlyjs(download_url):
    if not os.path.exists(PLOTLY_OFFLINE_DIRECTORY):
        os.makedirs(PLOTLY_OFFLINE_DIRECTORY)

    res = requests.get(download_url)
    res.raise_for_status()

    with open(PLOTLY_OFFLINE_BUNDLE, 'wb') as f:
        f.write(res.content)

    print('\n'.join([
        'Success! Now start an IPython notebook and run the following ' +
        'code to make your first offline graph:',
        '',
        'import plotly',
        'plotly.offline.init_notebook_mode() '
        '# run at the start of every ipython notebook',
        'plotly.offline.iplot([{"x": [1, 2, 3], "y": [3, 1, 6]}])'
    ]))


def init_notebook_mode():
    """
    Initialize Plotly Offline mode in an IPython Notebook.
    Run this function at the start of an IPython notebook
    to load the necessary javascript files for creating
    Plotly graphs with plotly.offline.iplot.
    """
    if not tools._ipython_imported:
        raise ImportError('`iplot` can only run inside an IPython Notebook.')
    from IPython.display import HTML, display

    if not os.path.exists(PLOTLY_OFFLINE_BUNDLE):
        raise PlotlyError('Plotly Offline source file at {source_path} '
                          'is not found.\n'
                          'If you have a Plotly Offline license, then try '
                          'running plotly.offline.download_plotlyjs(url) '
                          'with a licensed download url.\n'
                          "Don't have a Plotly Offline license? "
                          'Contact sales@plot.ly learn more about licensing.\n'
                          'Questions? support@plot.ly.'
                          .format(source_path=PLOTLY_OFFLINE_BUNDLE))

    global __PLOTLY_OFFLINE_INITIALIZED
    __PLOTLY_OFFLINE_INITIALIZED = True
    display(HTML('<script type="text/javascript">' +
                 open(PLOTLY_OFFLINE_BUNDLE).read() + '</script>'))


def iplot(figure_or_data, show_link=True, link_text='Export to plot.ly'):
    """
    Draw plotly graphs inside an IPython notebook without
    connecting to an external server.
    To save the chart to Plotly Cloud or Plotly Enterprise, use
    `plotly.plotly.iplot`.
    To embed an image of the chart, use `plotly.image.ishow`.

    figure_or_data -- a plotly.graph_objs.Figure or plotly.graph_objs.Data or
                      dict or list that describes a Plotly graph.
                      See https://plot.ly/python/ for examples of
                      graph descriptions.

    Keyword arguments:
    show_link (default=True) -- display a link in the bottom-right corner of
                                of the chart that will export the chart to
                                Plotly Cloud or Plotly Enterprise
    link_text (default='Export to plot.ly') -- the text of export link

    Example:
    ```
    from plotly.offline import init_notebook_mode, iplot
    init_notebook_mode()

    iplot([{'x': [1, 2, 3], 'y': [5, 2, 7]}])
    ```
    """
    if not __PLOTLY_OFFLINE_INITIALIZED:
        raise PlotlyError('\n'.join([
            'Plotly Offline mode has not been initialized in this notebook. '
            'Run: ',
            '',
            'import plotly',
            'plotly.offline.init_notebook_mode() '
            '# run at the start of every ipython notebook',
        ]))
    if not tools._ipython_imported:
        raise ImportError('`iplot` can only run inside an IPython Notebook.')

    from IPython.display import HTML, display
    if isinstance(figure_or_data, dict):
        data = figure_or_data['data']
        layout = figure_or_data.get('layout', {})
    else:
        data = figure_or_data
        layout = {}

    width = layout.get('width', '100%')
    height = layout.get('height', 525)
    try:
        float(width)
    except (ValueError, TypeError):
        pass
    else:
        width = str(width) + 'px'

    try:
        float(width)
    except (ValueError, TypeError):
        pass
    else:
        width = str(width) + 'px'

    plotdivid = uuid.uuid4()
    jdata = json.dumps(data, cls=utils.PlotlyJSONEncoder)
    jlayout = json.dumps(layout, cls=utils.PlotlyJSONEncoder)

    if show_link is False:
        link_text = ''

    plotly_platform_url = session.get_session_config().get('plotly_domain',
                                                           'https://plot.ly')
    if (plotly_platform_url != 'https://plot.ly' and
            link_text == 'Export to plot.ly'):

        link_domain = plotly_platform_url\
            .replace('https://', '')\
            .replace('http://', '')
        link_text = link_text.replace('plot.ly', link_domain)

    display(HTML(
        '<script type="text/javascript">'
        'window.PLOTLYENV=window.PLOTLYENV || {};'
        'window.PLOTLYENV.BASE_URL="' + plotly_platform_url + '";'
        'Plotly.LINKTEXT = "' + link_text + '";'
        '</script>'
    ))

    script = '\n'.join([
        'Plotly.plot("{id}", {data}, {layout}).then(function() {{',
        '    $(".{id}.loading").remove();',
        '}})'
    ]).format(id=plotdivid,
              data=jdata,
              layout=jlayout,
              link_text=link_text)

    display(HTML(''
                 '<div class="{id} loading" style="color: rgb(50,50,50);">'
                 'Drawing...</div>'
                 '<div id="{id}" style="height: {height}; width: {width};" '
                 'class="plotly-graph-div">'
                 '</div>'
                 '<script type="text/javascript">'
                 '{script}'
                 '</script>'
                 ''.format(id=plotdivid, script=script,
                           height=height, width=width)))


def plot():
    """ Configured to work with localhost Plotly graph viewer
    """
    raise NotImplementedError

