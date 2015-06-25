""" Plotly Offline
    A module to use Plotly's graphing library with Python
    without connecting to a public or private plotly enterprise
    server.
"""
import utils
import uuid
import json
import os
import requests


def download_plotlyjs(download_url, plotlyjs_dir='~/.plotly/plotlyjs'):
    plotlyjs_path = os.path.expanduser(
        os.path.join(*'~/.plotly/plotlyjs'.split('/')))

    if not os.path.exists(plotlyjs_path):
        os.makedirs(plotlyjs_path)

    res = requests.get(download_url + '/sourcefiles.json')
    res.raise_for_status()

    with open(os.path.join(plotlyjs_path, 'sourcefiles.json'), 'w') as f:
        f.write(res.content)

    download_queue = json.loads(res.content)['files']
    for fn in download_queue:
        file_url = download_url + '/' + fn
        print('Downloading {}'.format(file_url))
        res = requests.get(file_url)
        res.raise_for_status()

        file_path = os.path.join(plotlyjs_path, *fn.split('/'))
        file_dir = os.path.dirname(file_path)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        with open(file_path, 'w') as f:
            print('Copying into {}'.format(file_path))
            f.write(res.content)

    print('\n\n'
          'Success! Now start an IPython notebook, '
          'initialize offline mode with\n'
          'plotly.offline.init_notebook_mode()\n'
          'and make your first offline graph:\n'
          'plotly.offline.iplot([{"x": [1, 2, 3], "y": [3, 1, 6]}])\n')


def init_notebook_mode(plotlyjs_dir='~/.plotly/plotlyjs'):
    # TODO: check if ipython is available...?
    from IPython.display import HTML, display

    # Split and join the install path for cross-OS directories
    plotlyjs_dir = os.path.expanduser(os.path.join(*'~/.plotly/plotlyjs'.split('/')))
    sourcefiles_path = os.path.join(plotlyjs_dir, 'sourcefiles.json')
    if not os.path.exists(sourcefiles_path):
        raise Exception('Plotly Offline configuration file at {source_path} '
                        'is not found.\n'
                        'If you have a Plotly Offline license, then try '
                        'running plotly.offline.configure_offline(url) '
                        'with a licensed download url.\n'
                        "Don't have a Plotly Offline license?"
                        'Contact sales@plot.ly learn more about licensing.\n'
                        'Questions? support@plot.ly.'
                        .format(source_path=sourcefiles_path))

    sourcefiles = json.load(open(sourcefiles_path))['files']

    # Include all of the files in the dependencies folder
    scriptpaths = [os.path.join(plotlyjs_dir, *sourcefile.split('/'))
                   for sourcefile in sourcefiles]

    unrequirejs = ('<script type="text/javascript">'
                   'require=requirejs=define=undefined;</script>')

    display(HTML(
        unrequirejs +
        '\n'.join([
            '<script type="text/javascript">' + open(script).read() +
            '</script>' for script in scriptpaths
        ])
    ))


def iplot(figure_or_data, show_link=True, link_text='Export to plot.ly'):
    """
    """
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

    script = '\n'.join([
        'Plotly.plot("{id}", {data}, {layout}).then(function() {{',
        '    $(".{id}.loading").remove();',
        '    $(".link--embedview").text("{link_text}");'
    ]).format(id=plotdivid,
              data=jdata,
              layout=jlayout,
              link_text=link_text)

    if not show_link:
        script += '\n'.join([
            '    $("{} .link--embedview").remove();'.format(plotdivid),
            '\n});'])
    else:
        script += '\n});'

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

