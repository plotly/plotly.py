""" Plotly Offline
    A module to use Plotly's graphing library with Python
    without connecting to a public or private plotly enterprise
    server.
"""
from __future__ import absolute_import

import os
import uuid
import warnings
from pkg_resources import resource_string
import time
import webbrowser

from requests.compat import json as _json

import plotly
from plotly import optional_imports, tools, utils
from plotly.exceptions import PlotlyError

ipython = optional_imports.get_module('IPython')
ipython_display = optional_imports.get_module('IPython.display')
matplotlib = optional_imports.get_module('matplotlib')

__PLOTLY_OFFLINE_INITIALIZED = False

__IMAGE_FORMATS = ['jpeg', 'png', 'webp', 'svg']


def download_plotlyjs(download_url):
    warnings.warn('''
        `download_plotlyjs` is deprecated and will be removed in the
        next release. plotly.js is shipped with this module, it is no
        longer necessary to download this bundle separately.
    ''', DeprecationWarning)
    pass


def get_plotlyjs():
    path = os.path.join('package_data', 'plotly.min.js')
    plotlyjs = resource_string('plotly', path).decode('utf-8')
    return plotlyjs

def get_image_download_script(caller):
    """
    This function will return a script that will download an image of a Plotly
    plot.

    Keyword Arguments:
    caller ('plot', 'iplot') -- specifies which function made the call for the
        download script. If `iplot`, then an extra condition is added into the
        download script to ensure that download prompts aren't initiated on
        page reloads.
    """

    if caller == 'iplot':
        check_start = 'if(document.readyState == \'complete\') {{'
        check_end = '}}'
    elif caller == 'plot':
        check_start = ''
        check_end = ''
    else:
        raise ValueError('caller should only be one of `iplot` or `plot`')

    return(
        ('<script>'
         'function downloadimage(format, height, width,'
         ' filename) {{'
         'var p = document.getElementById(\'{plot_id}\');'
         'Plotly.downloadImage(p, {{format: format, height: height, '
         'width: width, filename: filename}});}};' +
         check_start +
         '{{downloadimage(\'{format}\', {height}, {width}, '
         '\'{filename}\');}}' +
         check_end +
         '</script>')
    )


def init_notebook_mode(connected=False):
    """
    Initialize plotly.js in the browser if it hasn't been loaded into the DOM
    yet. This is an idempotent method and can and should be called from any
    offline methods that require plotly.js to be loaded into the notebook dom.

    Keyword arguments:

    connected (default=False) -- If True, the plotly.js library will be loaded
    from an online CDN. If False, the plotly.js library will be loaded locally
    from the plotly python package

    Use `connected=True` if you want your notebooks to have smaller file sizes.
    In the case where `connected=False`, the entirety of the plotly.js library
    will be loaded into the notebook, which will result in a file-size increase
    of a couple megabytes. Additionally, because the library will be downloaded
    from the web, you and your viewers must be connected to the internet to be
    able to view charts within this notebook.

    Use `connected=False` if you want you and your collaborators to be able to
    create and view these charts regardless of the availability of an internet
    connection. This is the default option since it is the most predictable.
    Note that under this setting the library will be included inline inside
    your notebook, resulting in much larger notebook sizes compared to the case
    where `connected=True`.
    """
    if not ipython:
        raise ImportError('`iplot` can only run inside an IPython Notebook.')

    global __PLOTLY_OFFLINE_INITIALIZED

    if connected:
        # Inject plotly.js into the output cell
        script_inject = (
            ''
            '<script>'
            'requirejs.config({'
            'paths: { '
            # Note we omit the extension .js because require will include it.
            '\'plotly\': [\'https://cdn.plot.ly/plotly-latest.min\']},'
            '});'
            'if(!window.Plotly) {{'
            'require([\'plotly\'],'
            'function(plotly) {window.Plotly=plotly;});'
            '}}'
            '</script>'
        )
    else:
        # Inject plotly.js into the output cell
        script_inject = (
            ''
            '<script type=\'text/javascript\'>'
            'if(!window.Plotly){{'
            'define(\'plotly\', function(require, exports, module) {{'
            '{script}'
            '}});'
            'require([\'plotly\'], function(Plotly) {{'
            'window.Plotly = Plotly;'
            '}});'
            '}}'
            '</script>'
            '').format(script=get_plotlyjs())

    display_bundle = {
        'text/html': script_inject,
        'text/vnd.plotly.v1+html': script_inject
    }
    ipython_display.display(display_bundle, raw=True)
    __PLOTLY_OFFLINE_INITIALIZED = True


def _plot_html(figure_or_data, config, validate, default_width,
               default_height, global_requirejs):
    # force no validation if frames is in the call
    # TODO - add validation for frames in call - #605
    if 'frames' in figure_or_data:
        figure = tools.return_figure_from_figure_or_data(
            figure_or_data, False
        )
    else:
        figure = tools.return_figure_from_figure_or_data(
            figure_or_data, validate
        )

    width = figure.get('layout', {}).get('width', default_width)
    height = figure.get('layout', {}).get('height', default_height)

    try:
        float(width)
    except (ValueError, TypeError):
        pass
    else:
        width = str(width) + 'px'

    try:
        float(height)
    except (ValueError, TypeError):
        pass
    else:
        height = str(height) + 'px'

    plotdivid = uuid.uuid4()
    jdata = _json.dumps(figure.get('data', []), cls=utils.PlotlyJSONEncoder)
    jlayout = _json.dumps(figure.get('layout', {}),
                          cls=utils.PlotlyJSONEncoder)
    if 'frames' in figure_or_data:
        jframes = _json.dumps(figure.get('frames', {}),
                              cls=utils.PlotlyJSONEncoder)

    configkeys = (
        'editable',
        'autosizable',
        'fillFrame',
        'frameMargins',
        'scrollZoom',
        'doubleClick',
        'showTips',
        'showLink',
        'sendData',
        'linkText',
        'showSources',
        'displayModeBar',
        'modeBarButtonsToRemove',
        'modeBarButtonsToAdd',
        'modeBarButtons',
        'displaylogo',
        'plotGlPixelRatio',
        'setBackground',
        'topojsonURL'
    )

    config_clean = dict((k, config[k]) for k in configkeys if k in config)
    jconfig = _json.dumps(config_clean)

    # TODO: The get_config 'source of truth' should
    # really be somewhere other than plotly.plotly
    plotly_platform_url = plotly.plotly.get_config().get('plotly_domain',
                                                         'https://plot.ly')
    if (plotly_platform_url != 'https://plot.ly' and
            config['linkText'] == 'Export to plot.ly'):

        link_domain = plotly_platform_url\
            .replace('https://', '')\
            .replace('http://', '')
        link_text = config['linkText'].replace('plot.ly', link_domain)
        config['linkText'] = link_text
        jconfig = jconfig.replace('Export to plot.ly', link_text)

    if 'frames' in figure_or_data:
        script = '''
        Plotly.plot(
            '{id}',
            {data},
            {layout},
            {config}
        ).then(function () {add_frames}).then(function(){animate})
        '''.format(
            id=plotdivid,
            data=jdata,
            layout=jlayout,
            config=jconfig,
            add_frames="{" + "return Plotly.addFrames('{id}',{frames}".format(
                id=plotdivid, frames=jframes
            ) + ");}",
            animate="{" + "Plotly.animate('{id}');".format(id=plotdivid) + "}"
        )
    else:
        script = 'Plotly.newPlot("{id}", {data}, {layout}, {config})'.format(
            id=plotdivid,
            data=jdata,
            layout=jlayout,
            config=jconfig)

    optional_line1 = ('require(["plotly"], function(Plotly) {{ '
                      if global_requirejs else '')
    optional_line2 = ('}});' if global_requirejs else '')

    plotly_html_div = (
        ''
        '<div id="{id}" style="height: {height}; width: {width};" '
        'class="plotly-graph-div">'
        '</div>'
        '<script type="text/javascript">' +
        optional_line1 +
        'window.PLOTLYENV=window.PLOTLYENV || {{}};'
        'window.PLOTLYENV.BASE_URL="' + plotly_platform_url + '";'
        '{script}' +
        optional_line2 +
        '</script>'
        '').format(
        id=plotdivid, script=script,
        height=height, width=width)

    return plotly_html_div, plotdivid, width, height


def iplot(figure_or_data, show_link=True, link_text='Export to plot.ly',
          validate=True, image=None, filename='plot_image', image_width=800,
          image_height=600, config=None):
    """
    Draw plotly graphs inside an IPython or Jupyter notebook without
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
    validate (default=True) -- validate that all of the keys in the figure
                               are valid? omit if your version of plotly.js
                               has become outdated with your version of
                               graph_reference.json or if you need to include
                               extra, unnecessary keys in your figure.
    image (default=None |'png' |'jpeg' |'svg' |'webp') -- This parameter sets
        the format of the image to be downloaded, if we choose to download an
        image. This parameter has a default value of None indicating that no
        image should be downloaded. Please note: for higher resolution images
        and more export options, consider making requests to our image servers.
        Type: `help(py.image)` for more details.
    filename (default='plot') -- Sets the name of the file your image
        will be saved to. The extension should not be included.
    image_height (default=600) -- Specifies the height of the image in `px`.
    image_width (default=800) -- Specifies the width of the image in `px`.
    config (default=None) -- Plot view options dictionary. Keyword arguments
        `show_link` and `link_text` set the associated options in this
        dictionary if it doesn't contain them already.

    Example:
    ```
    from plotly.offline import init_notebook_mode, iplot
    init_notebook_mode()
    iplot([{'x': [1, 2, 3], 'y': [5, 2, 7]}])
    # We can also download an image of the plot by setting the image to the
    format you want. e.g. `image='png'`
    iplot([{'x': [1, 2, 3], 'y': [5, 2, 7]}], image='png')
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
    if not ipython:
        raise ImportError('`iplot` can only run inside an IPython Notebook.')

    config = dict(config) if config else {}
    config.setdefault('showLink', show_link)
    config.setdefault('linkText', link_text)

    plot_html, plotdivid, width, height = _plot_html(
        figure_or_data, config, validate, '100%', 525, True
    )

    figure = tools.return_figure_from_figure_or_data(figure_or_data, validate)

    # Though it can add quite a bit to the display-bundle size, we include
    # multiple representations of the plot so that the display environment can
    # choose which one to act on.
    data = _json.loads(_json.dumps(figure['data'],
                                   cls=plotly.utils.PlotlyJSONEncoder))
    layout = _json.loads(_json.dumps(figure.get('layout', {}),
                                     cls=plotly.utils.PlotlyJSONEncoder))
    frames = _json.loads(_json.dumps(figure.get('frames', None),
                                     cls=plotly.utils.PlotlyJSONEncoder))

    fig = {'data': data, 'layout': layout}
    if frames:
        fig['frames'] = frames

    display_bundle = {
        'application/vnd.plotly.v1+json': fig,
        'text/html': plot_html,
        'text/vnd.plotly.v1+html': plot_html
    }
    ipython_display.display(display_bundle, raw=True)

    if image:
        if image not in __IMAGE_FORMATS:
            raise ValueError('The image parameter must be one of the following'
                             ': {}'.format(__IMAGE_FORMATS)
                             )
        # if image is given, and is a valid format, we will download the image
        script = get_image_download_script('iplot').format(format=image,
                                                           width=image_width,
                                                           height=image_height,
                                                           filename=filename,
                                                           plot_id=plotdivid)
        # allow time for the plot to draw
        time.sleep(1)
        # inject code to download an image of the plot
        ipython_display.display(ipython_display.HTML(script))


def plot(figure_or_data, show_link=True, link_text='Export to plot.ly',
         validate=True, output_type='file', include_plotlyjs=True,
         filename='temp-plot.html', auto_open=True, image=None,
         image_filename='plot_image', image_width=800, image_height=600,
         config=None):
    """ Create a plotly graph locally as an HTML document or string.

    Example:
    ```
    from plotly.offline import plot
    import plotly.graph_objs as go

    plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='my-graph.html')
    # We can also download an image of the plot by setting the image parameter
    # to the image format we want
    plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='my-graph.html'
         image='jpeg')
    ```
    More examples below.

    figure_or_data -- a plotly.graph_objs.Figure or plotly.graph_objs.Data or
                      dict or list that describes a Plotly graph.
                      See https://plot.ly/python/ for examples of
                      graph descriptions.

    Keyword arguments:
    show_link (default=True) -- display a link in the bottom-right corner of
        of the chart that will export the chart to Plotly Cloud or
        Plotly Enterprise
    link_text (default='Export to plot.ly') -- the text of export link
    validate (default=True) -- validate that all of the keys in the figure
        are valid? omit if your version of plotly.js has become outdated
        with your version of graph_reference.json or if you need to include
        extra, unnecessary keys in your figure.
    output_type ('file' | 'div' - default 'file') -- if 'file', then
        the graph is saved as a standalone HTML file and `plot`
        returns None.
        If 'div', then `plot` returns a string that just contains the
        HTML <div> that contains the graph and the script to generate the
        graph.
        Use 'file' if you want to save and view a single graph at a time
        in a standalone HTML file.
        Use 'div' if you are embedding these graphs in an HTML file with
        other graphs or HTML markup, like a HTML report or an website.
    include_plotlyjs (default=True) -- If True, include the plotly.js
        source code in the output file or string.
        Set as False if your HTML file already contains a copy of the plotly.js
        library.
    filename (default='temp-plot.html') -- The local filename to save the
        outputted chart to. If the filename already exists, it will be
        overwritten. This argument only applies if `output_type` is 'file'.
    auto_open (default=True) -- If True, open the saved file in a
        web browser after saving.
        This argument only applies if `output_type` is 'file'.
    image (default=None |'png' |'jpeg' |'svg' |'webp') -- This parameter sets
        the format of the image to be downloaded, if we choose to download an
        image. This parameter has a default value of None indicating that no
        image should be downloaded. Please note: for higher resolution images
        and more export options, consider making requests to our image servers.
        Type: `help(py.image)` for more details.
    image_filename (default='plot_image') -- Sets the name of the file your
        image will be saved to. The extension should not be included.
    image_height (default=600) -- Specifies the height of the image in `px`.
    image_width (default=800) -- Specifies the width of the image in `px`.
    config (default=None) -- Plot view options dictionary. Keyword arguments
        `show_link` and `link_text` set the associated options in this
        dictionary if it doesn't contain them already.
    """
    if output_type not in ['div', 'file']:
        raise ValueError(
            "`output_type` argument must be 'div' or 'file'. "
            "You supplied `" + output_type + "``")
    if not filename.endswith('.html') and output_type == 'file':
        warnings.warn(
            "Your filename `" + filename + "` didn't end with .html. "
            "Adding .html to the end of your file.")
        filename += '.html'

    config = dict(config) if config else {}
    config.setdefault('showLink', show_link)
    config.setdefault('linkText', link_text)

    plot_html, plotdivid, width, height = _plot_html(
        figure_or_data, config, validate,
        '100%', '100%', global_requirejs=False)

    resize_script = ''
    if width == '100%' or height == '100%':
        resize_script = (
            ''
            '<script type="text/javascript">'
            'window.addEventListener("resize", function(){{'
            'Plotly.Plots.resize(document.getElementById("{id}"));}});'
            '</script>'
        ).format(id=plotdivid)

    if output_type == 'file':
        with open(filename, 'w') as f:
            if include_plotlyjs:
                plotly_js_script = ''.join([
                    '<script type="text/javascript">',
                    get_plotlyjs(),
                    '</script>',
                ])
            else:
                plotly_js_script = ''

            if image:
                if image not in __IMAGE_FORMATS:
                    raise ValueError('The image parameter must be one of the '
                                     'following: {}'.format(__IMAGE_FORMATS)
                                     )
                # if the check passes then download script is injected.
                # write the download script:
                script = get_image_download_script('plot')
                script = script.format(format=image,
                                       width=image_width,
                                       height=image_height,
                                       filename=image_filename,
                                       plot_id=plotdivid)
            else:
                script = ''

            f.write(''.join([
                '<html>',
                '<head><meta charset="utf-8" /></head>',
                '<body>',
                plotly_js_script,
                plot_html,
                resize_script,
                script,
                '</body>',
                '</html>']))

        url = 'file://' + os.path.abspath(filename)
        if auto_open:
            webbrowser.open(url)

        return url

    elif output_type == 'div':
        if include_plotlyjs:
            return ''.join([
                '<div>',
                '<script type="text/javascript">',
                get_plotlyjs(),
                '</script>',
                plot_html,
                resize_script,
                '</div>',
            ])
        else:
            return plot_html


def plot_mpl(mpl_fig, resize=False, strip_style=False,
             verbose=False, show_link=True, link_text='Export to plot.ly',
             validate=True, output_type='file', include_plotlyjs=True,
             filename='temp-plot.html', auto_open=True,
             image=None, image_filename='plot_image',
             image_height=600, image_width=800):
    """
    Convert a matplotlib figure to a Plotly graph stored locally as HTML.

    For more information on converting matplotlib visualizations to plotly
    graphs, call help(plotly.tools.mpl_to_plotly)

    For more information on creating plotly charts locally as an HTML document
    or string, call help(plotly.offline.plot)

    mpl_fig -- a matplotlib figure object to convert to a plotly graph

    Keyword arguments:
    resize (default=False) -- allow plotly to choose the figure size.
    strip_style (default=False) -- allow plotly to choose style options.
    verbose (default=False) -- print message.
    show_link (default=True) -- display a link in the bottom-right corner of
        of the chart that will export the chart to Plotly Cloud or
        Plotly Enterprise
    link_text (default='Export to plot.ly') -- the text of export link
    validate (default=True) -- validate that all of the keys in the figure
        are valid? omit if your version of plotly.js has become outdated
        with your version of graph_reference.json or if you need to include
        extra, unnecessary keys in your figure.
    output_type ('file' | 'div' - default 'file') -- if 'file', then
        the graph is saved as a standalone HTML file and `plot`
        returns None.
        If 'div', then `plot` returns a string that just contains the
        HTML <div> that contains the graph and the script to generate the
        graph.
        Use 'file' if you want to save and view a single graph at a time
        in a standalone HTML file.
        Use 'div' if you are embedding these graphs in an HTML file with
        other graphs or HTML markup, like a HTML report or an website.
    include_plotlyjs (default=True) -- If True, include the plotly.js
        source code in the output file or string.
        Set as False if your HTML file already contains a copy of the plotly.js
        library.
    filename (default='temp-plot.html') -- The local filename to save the
        outputted chart to. If the filename already exists, it will be
        overwritten. This argument only applies if `output_type` is 'file'.
    auto_open (default=True) -- If True, open the saved file in a
        web browser after saving.
        This argument only applies if `output_type` is 'file'.
    image (default=None |'png' |'jpeg' |'svg' |'webp') -- This parameter sets
        the format of the image to be downloaded, if we choose to download an
        image. This parameter has a default value of None indicating that no
        image should be downloaded.
    image_filename (default='plot_image') -- Sets the name of the file your
        image will be saved to. The extension should not be included.
    image_height (default=600) -- Specifies the height of the image in `px`.
    image_width (default=800) -- Specifies the width of the image in `px`.

    Example:
    ```
    from plotly.offline import init_notebook_mode, plot_mpl
    import matplotlib.pyplot as plt

    init_notebook_mode()

    fig = plt.figure()
    x = [10, 15, 20, 25, 30]
    y = [100, 250, 200, 150, 300]
    plt.plot(x, y, "o")

    plot_mpl(fig)
    # If you want to to download an image of the figure as well
    plot_mpl(fig, image='png')
    ```
    """
    plotly_plot = tools.mpl_to_plotly(mpl_fig, resize, strip_style, verbose)
    return plot(plotly_plot, show_link, link_text, validate, output_type,
                include_plotlyjs, filename, auto_open,
                image=image, image_filename=image_filename,
                image_height=image_height, image_width=image_width)


def iplot_mpl(mpl_fig, resize=False, strip_style=False,
              verbose=False, show_link=True,
              link_text='Export to plot.ly', validate=True,
              image=None, image_filename='plot_image',
              image_height=600, image_width=800):
    """
    Convert a matplotlib figure to a plotly graph and plot inside an IPython
    notebook without connecting to an external server.

    To save the chart to Plotly Cloud or Plotly Enterprise, use
    `plotly.plotly.plot_mpl`.

    For more information on converting matplotlib visualizations to plotly
    graphs call `help(plotly.tools.mpl_to_plotly)`

    For more information on plotting plotly charts offline in an Ipython
    notebook call `help(plotly.offline.iplot)`

    mpl_fig -- a matplotlib.figure to convert to a plotly graph

    Keyword arguments:
    resize (default=False) -- allow plotly to choose the figure size.
    strip_style (default=False) -- allow plotly to choose style options.
    verbose (default=False) -- print message.
    show_link (default=True) -- display a link in the bottom-right corner of
                                of the chart that will export the chart to
                                Plotly Cloud or Plotly Enterprise
    link_text (default='Export to plot.ly') -- the text of export link
    validate (default=True) -- validate that all of the keys in the figure
                               are valid? omit if your version of plotly.js
                               has become outdated with your version of
                               graph_reference.json or if you need to include
                               extra, unnecessary keys in your figure.
    image (default=None |'png' |'jpeg' |'svg' |'webp') -- This parameter sets
        the format of the image to be downloaded, if we choose to download an
        image. This parameter has a default value of None indicating that no
        image should be downloaded.
    image_filename (default='plot_image') -- Sets the name of the file your
        image will be saved to. The extension should not be included.
    image_height (default=600) -- Specifies the height of the image in `px`.
    image_width (default=800) -- Specifies the width of the image in `px`.

    Example:
    ```
    from plotly.offline import init_notebook_mode, iplot_mpl
    import matplotlib.pyplot as plt

    fig = plt.figure()
    x = [10, 15, 20, 25, 30]
    y = [100, 250, 200, 150, 300]
    plt.plot(x, y, "o")

    init_notebook_mode()
    iplot_mpl(fig)
    # and if you want to download an image of the figure as well
    iplot_mpl(fig, image='jpeg')
    ```
    """
    plotly_plot = tools.mpl_to_plotly(mpl_fig, resize, strip_style, verbose)
    return iplot(plotly_plot, show_link, link_text, validate,
                 image=image, filename=image_filename,
                 image_height=image_height, image_width=image_width)


def enable_mpl_offline(resize=False, strip_style=False,
                       verbose=False, show_link=True,
                       link_text='Export to plot.ly', validate=True):
    """
    Convert mpl plots to locally hosted HTML documents.

    This function should be used with the inline matplotlib backend
    that ships with IPython that can be enabled with `%pylab inline`
    or `%matplotlib inline`. This works by adding an HTML formatter
    for Figure objects; the existing SVG/PNG formatters will remain
    enabled.

    (idea taken from `mpld3._display.enable_notebook`)

    Example:
    ```
    from plotly.offline import enable_mpl_offline
    import matplotlib.pyplot as plt

    enable_mpl_offline()

    fig = plt.figure()
    x = [10, 15, 20, 25, 30]
    y = [100, 250, 200, 150, 300]
    plt.plot(x, y, "o")
    fig
    ```
    """
    init_notebook_mode()

    ip = ipython.core.getipython.get_ipython()
    formatter = ip.display_formatter.formatters['text/html']
    formatter.for_type(matplotlib.figure.Figure,
                       lambda fig: iplot_mpl(fig, resize, strip_style, verbose,
                                             show_link, link_text, validate))
