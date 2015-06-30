""" Plotly Offline
    A module to use Plotly's graphing library with Python
    without connecting to a public or private plotly enterprise
    server.
"""
from __future__ import absolute_import

import uuid
import json
import os
import requests

import plotly.plotly as py
from plotly import utils
from plotly import exceptions

PLOTLY_OFFLINE_DIRECTORY = plotlyjs_path = os.path.expanduser(
    os.path.join(*'~/.plotly/plotlyjs'.split('/')))
PLOTLY_OFFLINE_BUNDLE = os.path.join(PLOTLY_OFFLINE_DIRECTORY,
                                     'plotly-ipython-offline-bundle.js')

__PLOTLY_OFFLINE_INITIALIZED = False


def download_plotlyjs(download_url):
    if not os.path.exists(plotlyjs_path):
        os.makedirs(plotlyjs_path)

    res = requests.get(download_url)
    res.raise_for_status()

    with open(PLOTLY_OFFLINE_BUNDLE, 'w') as f:
        f.write(res.content)

    print('\n'.join([
        'Success! Now start an IPython notebook and run the following ' +
        'code to make your first offline graph:',
        '',
        'import plotly',
        'plotly.offline.init_notebook_mode() # initialize offline mode',
        'plotly.offline.iplot([{"x": [1, 2, 3], "y": [3, 1, 6]}])'
    ]))


def init_notebook_mode():
    # TODO: check if ipython is available...?
    from IPython.display import HTML, display

    if not os.path.exists(PLOTLY_OFFLINE_BUNDLE):
        raise Exception('Plotly Offline source file at {source_path} '
                        'is not found.\n'
                        'If you have a Plotly Offline license, then try '
                        'running plotly.offline.configure_offline(url) '
                        'with a licensed download url.\n'
                        "Don't have a Plotly Offline license?"
                        'Contact sales@plot.ly learn more about licensing.\n'
                        'Questions? support@plot.ly.'
                        .format(source_path=PLOTLY_OFFLINE_BUNDLE))

    global __PLOTLY_OFFLINE_INITIALIZED
    __PLOTLY_OFFLINE_INITIALIZED = True
    display(HTML('<script type="text/javascript">' +
                 open(PLOTLY_OFFLINE_BUNDLE).read() + '</script>'))


def iplot(figure_or_data, show_link=True, link_text='Export to plot.ly'):
    """
    """
    if not __PLOTLY_OFFLINE_INITIALIZED:
        raise exceptions.PlotlyError('\n'.join([
            'Plotly Offline mode has not been initialized in this notebook. '
            'Run: ',
            '',
            'import plotly',
            'plotly.offline.init_notebook_mode() '
            '# run at the start of every ipython notebook',
        ]))
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
        width = str(width) + 'px'
    except:
        pass
    try:
        float(height)
        height = str(height) + 'px'
    except:
        pass

    plotdivid = uuid.uuid4()
    jdata = json.dumps(data, cls=utils.PlotlyJSONEncoder)
    jlayout = json.dumps(layout, cls=utils.PlotlyJSONEncoder)

    if show_link is False:
        link_text = ''

    plotly_platform_url = py.get_config().get('plotly_domain',
                                              'https://plot.ly')
    if (plotly_platform_url != 'https://plot.ly' and
            link_text == 'Export to plot.ly'):

        link_domain = plotly_platform_url\
            .replace('https://', '')\
            .replace('http://', '')
        link_text = link_text.replace('plot.ly', link_domain)

    display(HTML(
        '<script type="text/javascript">'
        'window.PLOTLYENV={"BASE_URL": "' + plotly_platform_url + '"};'
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
