# -*- coding: utf-8 -*-

from __future__ import absolute_import

from collections import OrderedDict

from plotly import exceptions, optional_imports
from plotly.graph_objs import graph_objs

# Optional imports, may be None for users that only use our core functionality.
np = optional_imports.get_module('numpy')
scp = optional_imports.get_module('scipy')
sch = optional_imports.get_module('scipy.cluster.hierarchy')
scs = optional_imports.get_module('scipy.spatial')


def create_dendrogram(X, orientation="bottom", labels=None,
                      colorscale=None, distfun=None,
                      linkagefun=lambda x: sch.linkage(x, 'complete')):
    """
    BETA function that returns a dendrogram Plotly figure object.

    :param (ndarray) X: Matrix of observations as array of arrays
    :param (str) orientation: 'top', 'right', 'bottom', or 'left'
    :param (list) labels: List of axis category labels(observation labels)
    :param (list) colorscale: Optional colorscale for dendrogram tree
    :param (function) distfun: Function to compute the pairwise distance from
                               the observations
    :param (function) linkagefun: Function to compute the linkage matrix from
                                  the pairwise distances

        clusters

    Example 1: Simple bottom oriented dendrogram
    ```
    import plotly.plotly as py
    from plotly.figure_factory import create_dendrogram

    import numpy as np

    X = np.random.rand(10,10)
    dendro = create_dendrogram(X)
    plot_url = py.plot(dendro, filename='simple-dendrogram')

    ```

    Example 2: Dendrogram to put on the left of the heatmap
    ```
    import plotly.plotly as py
    from plotly.figure_factory import create_dendrogram

    import numpy as np

    X = np.random.rand(5,5)
    names = ['Jack', 'Oxana', 'John', 'Chelsea', 'Mark']
    dendro = create_dendrogram(X, orientation='right', labels=names)
    dendro['layout'].update({'width':700, 'height':500})

    py.iplot(dendro, filename='vertical-dendrogram')
    ```

    Example 3: Dendrogram with Pandas
    ```
    import plotly.plotly as py
    from plotly.figure_factory import create_dendrogram

    import numpy as np
    import pandas as pd

    Index= ['A','B','C','D','E','F','G','H','I','J']
    df = pd.DataFrame(abs(np.random.randn(10, 10)), index=Index)
    fig = create_dendrogram(df, labels=Index)
    url = py.plot(fig, filename='pandas-dendrogram')
    ```
    """
    if not scp or not scs or not sch:
        raise ImportError("FigureFactory.create_dendrogram requires scipy, \
                            scipy.spatial and scipy.hierarchy")

    s = X.shape
    if len(s) != 2:
        exceptions.PlotlyError("X should be 2-dimensional array.")

    if distfun is None:
        distfun = scs.distance.pdist

    dendrogram = _Dendrogram(X, orientation, labels, colorscale,
                             distfun=distfun, linkagefun=linkagefun)

    return {'layout': dendrogram.layout,
            'data': dendrogram.data}


class _Dendrogram(object):
    """Refer to FigureFactory.create_dendrogram() for docstring."""

    def __init__(self, X, orientation='bottom', labels=None, colorscale=None,
                 width="100%", height="100%", xaxis='xaxis', yaxis='yaxis',
                 distfun=None,
                 linkagefun=lambda x: sch.linkage(x, 'complete')):
        self.orientation = orientation
        self.labels = labels
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.data = []
        self.leaves = []
        self.sign = {self.xaxis: 1, self.yaxis: 1}
        self.layout = {self.xaxis: {}, self.yaxis: {}}

        if self.orientation in ['left', 'bottom']:
            self.sign[self.xaxis] = 1
        else:
            self.sign[self.xaxis] = -1

        if self.orientation in ['right', 'bottom']:
            self.sign[self.yaxis] = 1
        else:
            self.sign[self.yaxis] = -1

        if distfun is None:
            distfun = scs.distance.pdist

        (dd_traces, xvals, yvals,
            ordered_labels, leaves) = self.get_dendrogram_traces(X, colorscale,
                                                                 distfun,
                                                                 linkagefun)

        self.labels = ordered_labels
        self.leaves = leaves
        yvals_flat = yvals.flatten()
        xvals_flat = xvals.flatten()

        self.zero_vals = []

        for i in range(len(yvals_flat)):
            if yvals_flat[i] == 0.0 and xvals_flat[i] not in self.zero_vals:
                self.zero_vals.append(xvals_flat[i])

        self.zero_vals.sort()

        self.layout = self.set_figure_layout(width, height)
        self.data = graph_objs.Data(dd_traces)

    def get_color_dict(self, colorscale):
        """
        Returns colorscale used for dendrogram tree clusters.

        :param (list) colorscale: Colors to use for the plot in rgb format.
        :rtype (dict): A dict of default colors mapped to the user colorscale.

        """

        # These are the color codes returned for dendrograms
        # We're replacing them with nicer colors
        d = {'r': 'red',
             'g': 'green',
             'b': 'blue',
             'c': 'cyan',
             'm': 'magenta',
             'y': 'yellow',
             'k': 'black',
             'w': 'white'}
        default_colors = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

        if colorscale is None:
            colorscale = [
                'rgb(0,116,217)',  # blue
                'rgb(35,205,205)',  # cyan
                'rgb(61,153,112)',  # green
                'rgb(40,35,35)',  # black
                'rgb(133,20,75)',  # magenta
                'rgb(255,65,54)',  # red
                'rgb(255,255,255)',  # white
                'rgb(255,220,0)']  # yellow

        for i in range(len(default_colors.keys())):
            k = list(default_colors.keys())[i]  # PY3 won't index keys
            if i < len(colorscale):
                default_colors[k] = colorscale[i]

        return default_colors

    def set_axis_layout(self, axis_key):
        """
        Sets and returns default axis object for dendrogram figure.

        :param (str) axis_key: E.g., 'xaxis', 'xaxis1', 'yaxis', yaxis1', etc.
        :rtype (dict): An axis_key dictionary with set parameters.

        """
        axis_defaults = {
                'type': 'linear',
                'ticks': 'outside',
                'mirror': 'allticks',
                'rangemode': 'tozero',
                'showticklabels': True,
                'zeroline': False,
                'showgrid': False,
                'showline': True,
            }

        if len(self.labels) != 0:
            axis_key_labels = self.xaxis
            if self.orientation in ['left', 'right']:
                axis_key_labels = self.yaxis
            if axis_key_labels not in self.layout:
                self.layout[axis_key_labels] = {}
            self.layout[axis_key_labels]['tickvals'] = \
                [zv*self.sign[axis_key] for zv in self.zero_vals]
            self.layout[axis_key_labels]['ticktext'] = self.labels
            self.layout[axis_key_labels]['tickmode'] = 'array'

        self.layout[axis_key].update(axis_defaults)

        return self.layout[axis_key]

    def set_figure_layout(self, width, height):
        """
        Sets and returns default layout object for dendrogram figure.

        """
        self.layout.update({
            'showlegend': False,
            'autosize': False,
            'hovermode': 'closest',
            'width': width,
            'height': height
        })

        self.set_axis_layout(self.xaxis)
        self.set_axis_layout(self.yaxis)

        return self.layout

    def get_dendrogram_traces(self, X, colorscale, distfun, linkagefun):
        """
        Calculates all the elements needed for plotting a dendrogram.

        :param (ndarray) X: Matrix of observations as array of arrays
        :param (list) colorscale: Color scale for dendrogram tree clusters
        :param (function) distfun: Function to compute the pairwise distance
                                   from the observations
        :param (function) linkagefun: Function to compute the linkage matrix
                                      from the pairwise distances
        :rtype (tuple): Contains all the traces in the following order:
            (a) trace_list: List of Plotly trace objects for dendrogram tree
            (b) icoord: All X points of the dendrogram tree as array of arrays
                with length 4
            (c) dcoord: All Y points of the dendrogram tree as array of arrays
                with length 4
            (d) ordered_labels: leaf labels in the order they are going to
                appear on the plot
            (e) P['leaves']: left-to-right traversal of the leaves

        """
        d = distfun(X)
        Z = linkagefun(d)
        P = sch.dendrogram(Z, orientation=self.orientation,
                           labels=self.labels, no_plot=True)

        icoord = scp.array(P['icoord'])
        dcoord = scp.array(P['dcoord'])
        ordered_labels = scp.array(P['ivl'])
        color_list = scp.array(P['color_list'])
        colors = self.get_color_dict(colorscale)

        trace_list = []

        for i in range(len(icoord)):
            # xs and ys are arrays of 4 points that make up the '∩' shapes
            # of the dendrogram tree
            if self.orientation in ['top', 'bottom']:
                xs = icoord[i]
            else:
                xs = dcoord[i]

            if self.orientation in ['top', 'bottom']:
                ys = dcoord[i]
            else:
                ys = icoord[i]
            color_key = color_list[i]
            trace = graph_objs.Scatter(
                x=np.multiply(self.sign[self.xaxis], xs),
                y=np.multiply(self.sign[self.yaxis], ys),
                mode='lines',
                marker=graph_objs.Marker(color=colors[color_key])
            )

            try:
                x_index = int(self.xaxis[-1])
            except ValueError:
                x_index = ''

            try:
                y_index = int(self.yaxis[-1])
            except ValueError:
                y_index = ''

            trace['xaxis'] = 'x' + x_index
            trace['yaxis'] = 'y' + y_index

            trace_list.append(trace)

        return trace_list, icoord, dcoord, ordered_labels, P['leaves']
