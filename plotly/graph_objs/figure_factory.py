# coding=utf-8
"""
Helper methods for creating non-standardized Plotly traces/figures.

"""
import math
from collections import OrderedDict

from plotly import exceptions
from plotly.graph_objs import graph_objs
from plotly.tools import (_numpy_imported, _scipy_imported,
                          _scipy__spatial_imported,
                          _scipy__cluster__hierarchy_imported)

if _scipy_imported:
    import scipy
    import scipy as scp
if _numpy_imported:
    import numpy as np
if _scipy__spatial_imported:
    import scipy.spatial as scs
if _scipy__cluster__hierarchy_imported:
    import scipy.cluster.hierarchy as sch


# Default colours for finance charts
_DEFAULT_INCREASING_COLOR = '#3D9970'  # http://clrs.cc
_DEFAULT_DECREASING_COLOR = '#FF4136'


class FigureFactory(object):
    """
    BETA functions to create specific chart types.

    This is beta as in: subject to change in a backwards incompatible way
    without notice.

    Supported chart types include candlestick, open high low close, quiver,
    and streamline. See FigureFactory.create_candlestick,
    FigureFactory.create_ohlc, FigureFactory.create_quiver, or
    FigureFactory.create_streamline for for more infomation and examples of a
    specific chart type.
    """

    @staticmethod
    def _validate_equal_length(*args):
        """
        Validates that data lists or ndarrays are the same length.

        :raises: (PlotlyError) If any data lists are not the same length.
        """
        length = len(args[0])
        if any(len(lst) != length for lst in args):
            raise exceptions.PlotlyError("Oops! Your data lists or ndarrays "
                                         "should be the same length.")

    @staticmethod
    def _validate_ohlc(open, high, low, close, direction, **kwargs):
        """
        ohlc and candlestick specific validations

        Specifically, this checks that the high value is the greatest value and
        the low value is the lowest value in each unit.

        See FigureFactory.create_ohlc() or FigureFactory.create_candlestick()
        for params

        :raises: (PlotlyError) If the high value is not the greatest value in
            each unit.
        :raises: (PlotlyError) If the low value is not the lowest value in each
            unit.
        :raises: (PlotlyError) If direction is not 'increasing' or 'decreasing'
        """
        for lst in [open, low, close]:
            for index in range(len(high)):
                if high[index] < lst[index]:
                    raise exceptions.PlotlyError("Oops! Looks like some of "
                                                 "your high values are less "
                                                 "the corresponding open, "
                                                 "low, or close values. "
                                                 "Double check that your data "
                                                 "is entered in O-H-L-C order")

        for lst in [open, high, close]:
            for index in range(len(low)):
                if low[index] > lst[index]:
                    raise exceptions.PlotlyError("Oops! Looks like some of "
                                                 "your low values are greater "
                                                 "than the corresponding high"
                                                 ", open, or close values. "
                                                 "Double check that your data "
                                                 "is entered in O-H-L-C order")

        direction_opts = ('increasing', 'decreasing', 'both')
        if direction not in direction_opts:
            raise exceptions.PlotlyError("direction must be defined as "
                                         "'increasing', 'decreasing', or "
                                         "'both'")

    @staticmethod
    def _validate_distplot(hist_data, curve_type):
        """
        distplot specific validations

        :raises: (PlotlyError) If hist_data is not a list of lists
        :raises: (PlotlyError) If curve_type is not valid (i.e. not 'kde' or
            'normal').
        """
        try:
            import pandas as pd
            _pandas_imported = True
        except ImportError:
            _pandas_imported = False

        hist_data_types = (list,)
        if _numpy_imported:
            hist_data_types += (np.ndarray,)
        if _pandas_imported:
            hist_data_types += (pd.core.series.Series,)

        if not isinstance(hist_data[0], hist_data_types):
                raise exceptions.PlotlyError("Oops, this function was written "
                                             "to handle multiple datasets, if "
                                             "you want to plot just one, make "
                                             "sure your hist_data variable is "
                                             "still a list of lists, i.e. x = "
                                             "[1, 2, 3] -> x = [[1, 2, 3]]")

        curve_opts = ('kde', 'normal')
        if curve_type not in curve_opts:
            raise exceptions.PlotlyError("curve_type must be defined as "
                                         "'kde' or 'normal'")

        if _scipy_imported is False:
            raise ImportError("FigureFactory.create_distplot requires scipy")

    @staticmethod
    def _validate_positive_scalars(**kwargs):
        """
        Validates that all values given in key/val pairs are positive.

        Accepts kwargs to improve Exception messages.

        :raises: (PlotlyError) If any value is < 0 or raises.
        """
        for key, val in kwargs.items():
            try:
                if val <= 0:
                    raise ValueError('{} must be > 0, got {}'.format(key, val))
            except TypeError:
                raise exceptions.PlotlyError('{} must be a number, got {}'
                                             .format(key, val))

    @staticmethod
    def _validate_streamline(x, y):
        """
        streamline specific validations

        Specifically, this checks that x and y are both evenly spaced,
        and that the package numpy is available.

        See FigureFactory.create_streamline() for params

        :raises: (ImportError) If numpy is not available.
        :raises: (PlotlyError) If x is not evenly spaced.
        :raises: (PlotlyError) If y is not evenly spaced.
        """
        if _numpy_imported is False:
            raise ImportError("FigureFactory.create_streamline requires numpy")
        for index in range(len(x) - 1):
            if ((x[index + 1] - x[index]) - (x[1] - x[0])) > .0001:
                raise exceptions.PlotlyError("x must be a 1 dimensional, "
                                             "evenly spaced array")
        for index in range(len(y) - 1):
            if ((y[index + 1] - y[index]) -
               (y[1] - y[0])) > .0001:
                raise exceptions.PlotlyError("y must be a 1 dimensional, "
                                             "evenly spaced array")

    @staticmethod
    def _flatten(array):
        """
        Uses list comprehension to flatten array

        :param (array): An iterable to flatten
        :raises (PlotlyError): If iterable is not nested.
        :rtype (list): The flattened list.
        """
        try:
            return [item for sublist in array for item in sublist]
        except TypeError:
            raise exceptions.PlotlyError("Your data array could not be "
                                         "flattened! Make sure your data is "
                                         "entered as lists or ndarrays!")

    @staticmethod
    def create_quiver(x, y, u, v, scale=.1, arrow_scale=.3,
                      angle=math.pi / 9, **kwargs):
        """
        Returns data for a quiver plot.

        :param (list|ndarray) x: x coordinates of the arrow locations
        :param (list|ndarray) y: y coordinates of the arrow locations
        :param (list|ndarray) u: x components of the arrow vectors
        :param (list|ndarray) v: y components of the arrow vectors
        :param (float in [0,1]) scale: scales size of the arrows(ideally to
            avoid overlap). Default = .1
        :param (float in [0,1]) arrow_scale: value multiplied to length of barb
            to get length of arrowhead. Default = .3
        :param (angle in radians) angle: angle of arrowhead. Default = pi/9
        :param kwargs: kwargs passed through plotly.graph_objs.Scatter
            for more information on valid kwargs call
            help(plotly.graph_objs.Scatter)

        :rtype (dict): returns a representation of quiver figure.

        Example 1: Trivial Quiver
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF

        import math

        # 1 Arrow from (0,0) to (1,1)
        fig = FF.create_quiver(x=[0], y=[0],
                               u=[1], v=[1],
                               scale=1)

        py.plot(fig, filename='quiver')
        ```

        Example 2: Quiver plot using meshgrid
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF

        import numpy as np
        import math

        # Add data
        x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
        u = np.cos(x)*y
        v = np.sin(x)*y

        #Create quiver
        fig = FF.create_quiver(x, y, u, v)

        # Plot
        py.plot(fig, filename='quiver')
        ```

        Example 3: Styling the quiver plot
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF
        import numpy as np
        import math

        # Add data
        x, y = np.meshgrid(np.arange(-np.pi, math.pi, .5),
                           np.arange(-math.pi, math.pi, .5))
        u = np.cos(x)*y
        v = np.sin(x)*y

        # Create quiver
        fig = FF.create_quiver(x, y, u, v, scale=.2,
                               arrow_scale=.3,
                               angle=math.pi/6,
                               name='Wind Velocity',
                               line=Line(width=1))

        # Add title to layout
        fig['layout'].update(title='Quiver Plot')

        # Plot
        py.plot(fig, filename='quiver')
        ```
        """
        FigureFactory._validate_equal_length(x, y, u, v)
        FigureFactory._validate_positive_scalars(arrow_scale=arrow_scale,
                                                 scale=scale)

        barb_x, barb_y = _Quiver(x, y, u, v, scale,
                                 arrow_scale, angle).get_barbs()
        arrow_x, arrow_y = _Quiver(x, y, u, v, scale,
                                   arrow_scale, angle).get_quiver_arrows()
        quiver = graph_objs.Scatter(x=barb_x + arrow_x,
                                    y=barb_y + arrow_y,
                                    mode='lines', **kwargs)

        data = [quiver]
        layout = graph_objs.Layout(hovermode='closest')

        return graph_objs.Figure(data=data, layout=layout)

    @staticmethod
    def create_streamline(x, y, u, v,
                          density=1, angle=math.pi / 9,
                          arrow_scale=.09, **kwargs):
        """
        Returns data for a streamline plot.

        :param (list|ndarray) x: 1 dimensional, evenly spaced list or array
        :param (list|ndarray) y: 1 dimensional, evenly spaced list or array
        :param (ndarray) u: 2 dimensional array
        :param (ndarray) v: 2 dimensional array
        :param (float|int) density: controls the density of streamlines in
            plot. This is multiplied by 30 to scale similiarly to other
            available streamline functions such as matplotlib.
            Default = 1
        :param (angle in radians) angle: angle of arrowhead. Default = pi/9
        :param (float in [0,1]) arrow_scale: value to scale length of arrowhead
            Default = .09
        :param kwargs: kwargs passed through plotly.graph_objs.Scatter
            for more information on valid kwargs call
            help(plotly.graph_objs.Scatter)

        :rtype (dict): returns a representation of streamline figure.

        Example 1: Plot simple streamline and increase arrow size
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF

        import numpy as np
        import math

        # Add data
        x = np.linspace(-3, 3, 100)
        y = np.linspace(-3, 3, 100)
        Y, X = np.meshgrid(x, y)
        u = -1 - X**2 + Y
        v = 1 + X - Y**2
        u = u.T  # Transpose
        v = v.T  # Transpose

        # Create streamline
        fig = FF.create_streamline(x, y, u, v,
                                   arrow_scale=.1)

        # Plot
        py.plot(fig, filename='streamline')
        ```

        Example 2: from nbviewer.ipython.org/github/barbagroup/AeroPython
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF

        import numpy as np
        import math

        # Add data
        N = 50
        x_start, x_end = -2.0, 2.0
        y_start, y_end = -1.0, 1.0
        x = np.linspace(x_start, x_end, N)
        y = np.linspace(y_start, y_end, N)
        X, Y = np.meshgrid(x, y)
        ss = 5.0
        x_s, y_s = -1.0, 0.0

        # Compute the velocity field on the mesh grid
        u_s = ss/(2*np.pi) * (X-x_s)/((X-x_s)**2 + (Y-y_s)**2)
        v_s = ss/(2*np.pi) * (Y-y_s)/((X-x_s)**2 + (Y-y_s)**2)

        # Create streamline
        fig = FF.create_streamline(x, y, u_s, v_s,
                                   density=2, name='streamline')

        # Add source point
        point = Scatter(x=[x_s], y=[y_s], mode='markers',
                        marker=Marker(size=14), name='source point')

        # Plot
        fig['data'].append(point)
        py.plot(fig, filename='streamline')
        ```
        """
        FigureFactory._validate_equal_length(x, y)
        FigureFactory._validate_equal_length(u, v)
        FigureFactory._validate_streamline(x, y)
        FigureFactory._validate_positive_scalars(density=density,
                                                arrow_scale=arrow_scale)

        streamline_x, streamline_y = _Streamline(x, y, u, v,
                                                 density, angle,
                                                 arrow_scale).sum_streamlines()
        arrow_x, arrow_y = _Streamline(x, y, u, v,
                                       density, angle,
                                       arrow_scale).get_streamline_arrows()

        streamline = graph_objs.Scatter(x=streamline_x + arrow_x,
                                        y=streamline_y + arrow_y,
                                        mode='lines', **kwargs)

        data = [streamline]
        layout = graph_objs.Layout(hovermode='closest')

        return graph_objs.Figure(data=data, layout=layout)

    @staticmethod
    def _make_increasing_ohlc(open, high, low, close, dates, **kwargs):
        """
        Makes increasing ohlc sticks

        _make_increasing_ohlc() and _make_decreasing_ohlc separate the
        increasing trace from the decreasing trace so kwargs (such as
        color) can be passed separately to increasing or decreasing traces
        when direction is set to 'increasing' or 'decreasing' in
        FigureFactory.create_candlestick()

        :param (list) open: opening values
        :param (list) high: high values
        :param (list) low: low values
        :param (list) close: closing values
        :param (list) dates: list of datetime objects. Default: None
        :param kwargs: kwargs to be passed to increasing trace via
            plotly.graph_objs.Scatter.

        :rtype (trace) ohlc_incr_data: Scatter trace of all increasing ohlc
            sticks.
        """
        (flat_increase_x,
         flat_increase_y,
         text_increase) = _OHLC(open, high, low, close, dates).get_increase()

        if 'name' in kwargs:
            showlegend = True
        else:
            kwargs.setdefault('name', 'Increasing')
            showlegend = False

        kwargs.setdefault('line', dict(color=_DEFAULT_INCREASING_COLOR,
                                       width=1))
        kwargs.setdefault('text', text_increase)

        ohlc_incr = dict(type='scatter',
                         x=flat_increase_x,
                         y=flat_increase_y,
                         mode='lines',
                         showlegend=showlegend,
                         **kwargs)
        return ohlc_incr

    @staticmethod
    def _make_decreasing_ohlc(open, high, low, close, dates, **kwargs):
        """
        Makes decreasing ohlc sticks

        :param (list) open: opening values
        :param (list) high: high values
        :param (list) low: low values
        :param (list) close: closing values
        :param (list) dates: list of datetime objects. Default: None
        :param kwargs: kwargs to be passed to increasing trace via
            plotly.graph_objs.Scatter.

        :rtype (trace) ohlc_decr_data: Scatter trace of all decreasing ohlc
            sticks.
        """
        (flat_decrease_x,
         flat_decrease_y,
         text_decrease) = _OHLC(open, high, low, close, dates).get_decrease()

        kwargs.setdefault('line', dict(color=_DEFAULT_DECREASING_COLOR,
                                       width=1))
        kwargs.setdefault('text', text_decrease)
        kwargs.setdefault('showlegend', False)
        kwargs.setdefault('name', 'Decreasing')

        ohlc_decr = dict(type='scatter',
                         x=flat_decrease_x,
                         y=flat_decrease_y,
                         mode='lines',
                         **kwargs)
        return ohlc_decr

    @staticmethod
    def create_ohlc(open, high, low, close,
                    dates=None, direction='both',
                    **kwargs):
        """
        BETA function that creates an ohlc chart

        :param (list) open: opening values
        :param (list) high: high values
        :param (list) low: low values
        :param (list) close: closing
        :param (list) dates: list of datetime objects. Default: None
        :param (string) direction: direction can be 'increasing', 'decreasing',
            or 'both'. When the direction is 'increasing', the returned figure
            consists of all units where the close value is greater than the
            corresponding open value, and when the direction is 'decreasing',
            the returned figure consists of all units where the close value is
            less than or equal to the corresponding open value. When the
            direction is 'both', both increasing and decreasing units are
            returned. Default: 'both'
        :param kwargs: kwargs passed through plotly.graph_objs.Scatter.
            These kwargs describe other attributes about the ohlc Scatter trace
            such as the color or the legend name. For more information on valid
            kwargs call help(plotly.graph_objs.Scatter)

        :rtype (dict): returns a representation of an ohlc chart figure.

        Example 1: Simple OHLC chart from a Pandas DataFrame
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF
        from datetime import datetime

        import pandas.io.data as web

        df = web.DataReader("aapl", 'yahoo', datetime(2008, 8, 15),
                            datetime(2008, 10, 15))
        fig = FF.create_ohlc(df.Open, df.High, df.Low, df.Close,
                             dates=df.index)

        py.plot(fig, filename='finance/aapl-ohlc')
        ```

        Example 2: Add text and annotations to the OHLC chart
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF
        from datetime import datetime

        import pandas.io.data as web

        df = web.DataReader("aapl", 'yahoo', datetime(2008, 8, 15),
                            datetime(2008, 10, 15))
        fig = FF.create_ohlc(df.Open, df.High, df.Low, df.Close,
                             dates=df.index)

        # Update the fig - See https://plot.ly/python/reference/#Layout
        fig['layout'].update({
            'title': 'The Great Recession',
            'yaxis': {'title': 'AAPL Stock'},
            'shapes': [{
                'x0': '2008-09-15', 'x1': '2008-09-15', 'type': 'line',
                'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
                'line': {'color': 'rgb(40,40,40)', 'width': 0.5}
            }],
            'annotations': [{
                'text': "the fall of Lehman Brothers",
                'x': '2008-09-15', 'y': 1.02,
                'xref': 'x', 'yref': 'paper',
                'showarrow': False, 'xanchor': 'left'
            }]
        })

        py.plot(fig, filename='finance/aapl-recession-ohlc', validate=False)
        ```

        Example 3: Customize the OHLC colors
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF
        from plotly.graph_objs import Line, Marker
        from datetime import datetime

        import pandas.io.data as web

        df = web.DataReader("aapl", 'yahoo', datetime(2008, 1, 1),
                            datetime(2009, 4, 1))

        # Make increasing ohlc sticks and customize their color and name
        fig_increasing = FF.create_ohlc(df.Open, df.High, df.Low, df.Close,
                                        dates=df.index,
            direction='increasing', name='AAPL',
            line=Line(color='rgb(150, 200, 250)'))

        # Make decreasing ohlc sticks and customize their color and name
        fig_decreasing = FF.create_ohlc(df.Open, df.High, df.Low, df.Close,
                                        dates=df.index,
                                        direction='decreasing',
                                        line=Line(color='rgb(128, 128, 128)'))

        # Initialize the figure
        fig = fig_increasing

        # Add decreasing data with .extend()
        fig['data'].extend(fig_decreasing['data'])

        py.iplot(fig, filename='finance/aapl-ohlc-colors', validate=False)
        ```

        Example 4: OHLC chart with datetime objects
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF

        from datetime import datetime

        # Add data
        open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
        high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
        low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
        close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
        dates = [datetime(year=2013, month=10, day=10),
                 datetime(year=2013, month=11, day=10),
                 datetime(year=2013, month=12, day=10),
                 datetime(year=2014, month=1, day=10),
                 datetime(year=2014, month=2, day=10)]

        # Create ohlc
        fig = FF.create_ohlc(open_data, high_data,
            low_data, close_data, dates=dates)

        py.iplot(fig, filename='finance/simple-ohlc', validate=False)
        ```
        """
        if dates is not None:
            FigureFactory._validate_equal_length(open, high, low, close, dates)
        else:
            FigureFactory._validate_equal_length(open, high, low, close)
        FigureFactory._validate_ohlc(open, high, low, close, direction,
                                     **kwargs)

        if direction is 'increasing':
            ohlc_incr = FigureFactory._make_increasing_ohlc(open, high,
                                                            low, close,
                                                            dates, **kwargs)
            data = [ohlc_incr]
        elif direction is 'decreasing':
            ohlc_decr = FigureFactory._make_decreasing_ohlc(open, high,
                                                            low, close,
                                                            dates, **kwargs)
            data = [ohlc_decr]
        else:
            ohlc_incr = FigureFactory._make_increasing_ohlc(open, high,
                                                            low, close,
                                                            dates, **kwargs)
            ohlc_decr = FigureFactory._make_decreasing_ohlc(open, high,
                                                            low, close,
                                                            dates, **kwargs)
            data = [ohlc_incr, ohlc_decr]

        layout = graph_objs.Layout(xaxis=dict(zeroline=False),
                                   hovermode='closest')

        return graph_objs.Figure(data=data, layout=layout)

    @staticmethod
    def _make_increasing_candle(open, high, low, close, dates, **kwargs):
        """
        Makes boxplot trace for increasing candlesticks

        _make_increasing_candle() and _make_decreasing_candle separate the
        increasing traces from the decreasing traces so kwargs (such as
        color) can be passed separately to increasing or decreasing traces
        when direction is set to 'increasing' or 'decreasing' in
        FigureFactory.create_candlestick()

        :param (list) open: opening values
        :param (list) high: high values
        :param (list) low: low values
        :param (list) close: closing values
        :param (list) dates: list of datetime objects. Default: None
        :param kwargs: kwargs to be passed to increasing trace via
            plotly.graph_objs.Scatter.

        :rtype (list) candle_incr_data: list of the box trace for
            increasing candlesticks.
        """
        increase_x, increase_y = _Candlestick(
            open, high, low, close, dates, **kwargs).get_candle_increase()

        if 'line' in kwargs:
            kwargs.setdefault('fillcolor', kwargs['line']['color'])
        else:
            kwargs.setdefault('fillcolor', _DEFAULT_INCREASING_COLOR)
        if 'name' in kwargs:
            kwargs.setdefault('showlegend', True)
        else:
            kwargs.setdefault('showlegend', False)
        kwargs.setdefault('name', 'Increasing')
        kwargs.setdefault('line', dict(color=_DEFAULT_INCREASING_COLOR))

        candle_incr_data = dict(type='box',
                                x=increase_x,
                                y=increase_y,
                                whiskerwidth=0,
                                boxpoints=False,
                                **kwargs)

        return [candle_incr_data]

    @staticmethod
    def _make_decreasing_candle(open, high, low, close, dates, **kwargs):
        """
        Makes boxplot trace for decreasing candlesticks

        :param (list) open: opening values
        :param (list) high: high values
        :param (list) low: low values
        :param (list) close: closing values
        :param (list) dates: list of datetime objects. Default: None
        :param kwargs: kwargs to be passed to decreasing trace via
            plotly.graph_objs.Scatter.

        :rtype (list) candle_decr_data: list of the box trace for
            decreasing candlesticks.
        """

        decrease_x, decrease_y = _Candlestick(
            open, high, low, close, dates, **kwargs).get_candle_decrease()

        if 'line' in kwargs:
            kwargs.setdefault('fillcolor', kwargs['line']['color'])
        else:
            kwargs.setdefault('fillcolor', _DEFAULT_DECREASING_COLOR)
        kwargs.setdefault('showlegend', False)
        kwargs.setdefault('line', dict(color=_DEFAULT_DECREASING_COLOR))
        kwargs.setdefault('name', 'Decreasing')

        candle_decr_data = dict(type='box',
                                x=decrease_x,
                                y=decrease_y,
                                whiskerwidth=0,
                                boxpoints=False,
                                **kwargs)

        return [candle_decr_data]

    @staticmethod
    def create_candlestick(open, high, low, close,
                           dates=None, direction='both', **kwargs):
        """
        BETA function that creates a candlestick chart

        :param (list) open: opening values
        :param (list) high: high values
        :param (list) low: low values
        :param (list) close: closing values
        :param (list) dates: list of datetime objects. Default: None
        :param (string) direction: direction can be 'increasing', 'decreasing',
            or 'both'. When the direction is 'increasing', the returned figure
            consists of all candlesticks where the close value is greater than
            the corresponding open value, and when the direction is
            'decreasing', the returned figure consists of all candlesticks
            where the close value is less than or equal to the corresponding
            open value. When the direction is 'both', both increasing and
            decreasing candlesticks are returned. Default: 'both'
        :param kwargs: kwargs passed through plotly.graph_objs.Scatter.
            These kwargs describe other attributes about the ohlc Scatter trace
            such as the color or the legend name. For more information on valid
            kwargs call help(plotly.graph_objs.Scatter)

        :rtype (dict): returns a representation of candlestick chart figure.

        Example 1: Simple candlestick chart from a Pandas DataFrame
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF
        from datetime import datetime

        import pandas.io.data as web

        df = web.DataReader("aapl", 'yahoo', datetime(2007, 10, 1),
                            datetime(2009, 4, 1))
        fig = FF.create_candlestick(df.Open, df.High, df.Low, df.Close,
                                    dates=df.index)
        py.plot(fig, filename='finance/aapl-candlestick', validate=False)
        ```

        Example 2: Add text and annotations to the candlestick chart
        ```
        fig = FF.create_candlestick(df.Open, df.High, df.Low, df.Close,
                                    dates=df.index)
        # Update the fig - See https://plot.ly/python/reference/#Layout
        fig['layout'].update({
            'title': 'The Great Recession',
            'yaxis': {'title': 'AAPL Stock'},
            'shapes': [{
                'x0': '2007-12-01', 'x1': '2007-12-01',
                'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
                'line': {'color': 'rgb(30,30,30)', 'width': 1}
            }],
            'annotations': [{
                'x': '2007-12-01', 'y': 0.05, 'xref': 'x', 'yref': 'paper',
                'showarrow': False, 'xanchor': 'left',
                'text': 'Official start of the recession'
            }]
        })
        py.plot(fig, filename='finance/aapl-recession-candlestick',
                validate=False)
        ```

        Example 3: Customize the candlestick colors
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF
        from plotly.graph_objs import Line, Marker
        from datetime import datetime

        import pandas.io.data as web

        df = web.DataReader("aapl", 'yahoo', datetime(2008, 1, 1),
                            datetime(2009, 4, 1))

        # Make increasing candlesticks and customize their color and name
        fig_increasing = FF.create_candlestick(
            df.Open, df.High, df.Low, df.Close, dates=df.index,
            direction='increasing', name='AAPL',
            marker=Marker(color='rgb(150, 200, 250)'),
            line=Line(color='rgb(150, 200, 250)')
        )

        # Make decreasing candlesticks and customize their color and name
        fig_decreasing = FF.create_candlestick(
            df.Open, df.High, df.Low, df.Close, dates=df.index,
            direction='decreasing', marker=Marker(color='rgb(128, 128, 128)'),
            line=Line(color='rgb(128, 128, 128)')
        )

        # Initialize the figure
        fig = fig_increasing

        # Add decreasing data with .extend()
        fig['data'].extend(fig_decreasing['data'])

        py.iplot(fig, filename='finance/aapl-candlestick-custom',
                 validate=False)
        ```

        Example 4: Candlestick chart with datetime objects
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF

        from datetime import datetime

        # Add data
        open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
        high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
        low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
        close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
        dates = [datetime(year=2013, month=10, day=10),
                 datetime(year=2013, month=11, day=10),
                 datetime(year=2013, month=12, day=10),
                 datetime(year=2014, month=1, day=10),
                 datetime(year=2014, month=2, day=10)]

        # Create ohlc
        fig = FF.create_candlestick(open_data, high_data,
            low_data, close_data, dates=dates)

        py.iplot(fig, filename='finance/simple-candlestick', validate=False)
        ```
        """
        if dates is not None:
            FigureFactory._validate_equal_length(open, high, low, close, dates)
        else:
            FigureFactory._validate_equal_length(open, high, low, close)
        FigureFactory._validate_ohlc(open, high, low, close, direction,
                                     **kwargs)

        if direction is 'increasing':
            candle_incr_data = FigureFactory._make_increasing_candle(
                open, high, low, close, dates, **kwargs)
            data = candle_incr_data
        elif direction is 'decreasing':
            candle_decr_data = FigureFactory._make_decreasing_candle(
                open, high, low, close, dates, **kwargs)
            data = candle_decr_data
        else:
            candle_incr_data = FigureFactory._make_increasing_candle(
                open, high, low, close, dates, **kwargs)
            candle_decr_data = FigureFactory._make_decreasing_candle(
                open, high, low, close, dates, **kwargs)
            data = candle_incr_data + candle_decr_data

        layout = graph_objs.Layout()
        return graph_objs.Figure(data=data, layout=layout)

    @staticmethod
    def create_distplot(hist_data, group_labels,
                        bin_size=1., curve_type='kde',
                        colors=None, rug_text=None,
                        show_hist=True, show_curve=True,
                        show_rug=True):
        """
        BETA function that creates a distplot similar to seaborn.distplot

        The distplot can be composed of all or any combination of the following
        3 components: (1) histogram, (2) curve: (a) kernal density estimation
        or (b) normal curve, and (3) rug plot. Additionally, multiple distplots
        (from multiple datasets) can be created in the same plot.

        :param (list[list]) hist_data: Use list of lists to plot multiple data
            sets on the same plot.
        :param (list[str]) group_labels: Names for each data set.
        :param (float) bin_size: Size of histogram bins. Default = 1.
        :param (str) curve_type: 'kde' or 'normal'. Default = 'kde'
        :param (bool) show_hist: Add histogram to distplot? Default = True
        :param (bool) show_curve: Add curve to distplot? Default = True
        :param (bool) show_rug: Add rug to distplot? Default = True
        :param (list[str]) colors: Colors for traces.
        :param (list[list]) rug_text: Hovertext values for rug_plot,
        :return (dict): Representation of a distplot figure.

        Example 1: Simple distplot of 1 data set
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF

        hist_data = [[1.1, 1.1, 2.5, 3.0, 3.5,
                      3.5, 4.1, 4.4, 4.5, 4.5,
                      5.0, 5.0, 5.2, 5.5, 5.5,
                      5.5, 5.5, 5.5, 6.1, 7.0]]

        group_labels = ['distplot example']

        fig = FF.create_distplot(hist_data, group_labels)

        url = py.plot(fig, filename='Simple distplot', validate=False)
        ```

        Example 2: Two data sets and added rug text
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF

        # Add histogram data
        hist1_x = [0.8, 1.2, 0.2, 0.6, 1.6,
                   -0.9, -0.07, 1.95, 0.9, -0.2,
                   -0.5, 0.3, 0.4, -0.37, 0.6]
        hist2_x = [0.8, 1.5, 1.5, 0.6, 0.59,
                   1.0, 0.8, 1.7, 0.5, 0.8,
                   -0.3, 1.2, 0.56, 0.3, 2.2]

        # Group data together
        hist_data = [hist1_x, hist2_x]

        group_labels = ['2012', '2013']

        # Add text
        rug_text_1 = ['a1', 'b1', 'c1', 'd1', 'e1',
              'f1', 'g1', 'h1', 'i1', 'j1',
              'k1', 'l1', 'm1', 'n1', 'o1']

        rug_text_2 = ['a2', 'b2', 'c2', 'd2', 'e2',
              'f2', 'g2', 'h2', 'i2', 'j2',
              'k2', 'l2', 'm2', 'n2', 'o2']

        # Group text together
        rug_text_all = [rug_text_1, rug_text_2]

        # Create distplot
        fig = FF.create_distplot(
            hist_data, group_labels, rug_text=rug_text_all, bin_size=.2)

        # Add title
        fig['layout'].update(title='Dist Plot')

        # Plot!
        url = py.plot(fig, filename='Distplot with rug text', validate=False)
        ```

        Example 3: Plot with normal curve and hide rug plot
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF
        import numpy as np

        x1 = np.random.randn(190)
        x2 = np.random.randn(200)+1
        x3 = np.random.randn(200)-1
        x4 = np.random.randn(210)+2

        hist_data = [x1, x2, x3, x4]
        group_labels = ['2012', '2013', '2014', '2015']

        fig = FF.create_distplot(
            hist_data, group_labels, curve_type='normal',
            show_rug=False, bin_size=.4)

        url = py.plot(fig, filename='hist and normal curve', validate=False)

        Example 4: Distplot with Pandas
        ```
        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF
        import numpy as np
        import pandas as pd

        df = pd.DataFrame({'2012': np.random.randn(200),
                           '2013': np.random.randn(200)+1})
        py.iplot(FF.create_distplot([df[c] for c in df.columns], df.columns),
                                    filename='examples/distplot with pandas',
                                    validate=False)
        ```
        """
        colors = colors if colors is not None else []
        rug_text = rug_text if rug_text is not None else []
        FigureFactory._validate_distplot(hist_data, curve_type)
        FigureFactory._validate_equal_length(hist_data, group_labels)

        hist = _Distplot(
            hist_data, group_labels, bin_size,
            curve_type, colors, rug_text,
            show_hist, show_curve).make_hist()

        if curve_type == 'normal':
            curve = _Distplot(
                hist_data, group_labels, bin_size,
                curve_type, colors, rug_text,
                show_hist, show_curve).make_normal()
        else:
            curve = _Distplot(
                hist_data, group_labels, bin_size,
                curve_type, colors, rug_text,
                show_hist, show_curve).make_kde()

        rug = _Distplot(
            hist_data, group_labels, bin_size,
            curve_type, colors, rug_text,
            show_hist, show_curve).make_rug()

        data = []
        if show_hist:
            data.append(hist)
        if show_curve:
            data.append(curve)
        if show_rug:
            data.append(rug)
            layout = graph_objs.Layout(
                barmode='overlay',
                hovermode='closest',
                legend=dict(traceorder='reversed'),
                xaxis1=dict(domain=[0.0, 1.0],
                            anchor='y2',
                            zeroline=False),
                yaxis1=dict(domain=[0.35, 1],
                            anchor='free',
                            position=0.0),
                yaxis2=dict(domain=[0, 0.25],
                            anchor='x1',
                            dtick=1,
                            showticklabels=False))
        else:
            layout = graph_objs.Layout(
                barmode='overlay',
                hovermode='closest',
                legend=dict(traceorder='reversed'),
                xaxis1=dict(domain=[0.0, 1.0],
                            anchor='y2',
                            zeroline=False),
                yaxis1=dict(domain=[0., 1],
                            anchor='free',
                            position=0.0))

        data = sum(data, [])
        return graph_objs.Figure(data=data, layout=layout)

    @staticmethod
    def create_dendrogram(X, orientation="bottom", labels=None,
                          colorscale=None):
        """
        BETA function that returns a dendrogram Plotly figure object.

        :param (ndarray) X: Matrix of observations as array of arrays
        :param (str) orientation: 'top', 'right', 'bottom', or 'left'
        :param (list) labels: List of axis category labels(observation labels)
        :param (list) colorscale: Optional colorscale for dendrogram tree
            clusters

        Example 1: Simple bottom oriented dendrogram
        ```
        import numpy as np

        import plotly.plotly as py
        from plotly.tools import FigureFactory as FF

        X = np.random.rand(5,5)
        dendro = FF.create_dendrogram(X)
        py.iplot(dendro, validate=False, height=300, width=1000)

        ```

        Example 2: Dendrogram to put on the left of the heatmap
        ```
        X = np.random.rand(5,5)
        names = ['Jack', 'Oxana', 'John', 'Chelsea', 'Mark']
        dendro = FF.create_dendrogram(X, orientation='right', labels=names)

        py.iplot(dendro, validate=False, height=1000, width=300)
        ```

        """
        dependencies = (_scipy_imported and _scipy__spatial_imported and
                        _scipy__cluster__hierarchy_imported)

        if dependencies is False:
            raise ImportError("FigureFactory.create_dendrogram requires "
                              "scipy, scipy.spatial and scipy.hierarchy")

        s = X.shape
        if len(s) != 2:
            exceptions.PlotlyError("X should be 2-dimensional array.")

        dendrogram = _Dendrogram(X, orientation, labels, colorscale)

        return {'layout': dendrogram.layout,
                'data': dendrogram.data}


class _Quiver(FigureFactory):
    """
    Refer to FigureFactory.create_quiver() for docstring
    """
    def __init__(self, x, y, u, v,
                 scale, arrow_scale, angle, **kwargs):
        try:
            x = FigureFactory._flatten(x)
        except exceptions.PlotlyError:
            pass

        try:
            y = FigureFactory._flatten(y)
        except exceptions.PlotlyError:
            pass

        try:
            u = FigureFactory._flatten(u)
        except exceptions.PlotlyError:
            pass

        try:
            v = FigureFactory._flatten(v)
        except exceptions.PlotlyError:
            pass

        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.scale = scale
        self.arrow_scale = arrow_scale
        self.angle = angle
        self.end_x = []
        self.end_y = []
        self.scale_uv()
        self.get_barbs()
        self.get_quiver_arrows()

    def scale_uv(self):
        """
        Scales u and v to avoid overlap of the arrows.

        u and v are added to x and y to get the
        endpoints of the arrows so a smaller scale value will
        result in less overlap of arrows.
        """
        self.u = [i * self.scale for i in self.u]
        self.v = [i * self.scale for i in self.v]

    def get_barbs(self):
        """
        Creates x and y startpoint and endpoint pairs

        After finding the endpoint of each barb this zips startpoint and
        endpoint pairs to create 2 lists: x_values for barbs and y values
        for barbs

        :rtype: (list, list) barb_x, barb_y: list of startpoint and endpoint
            x_value pairs separated by a None to create the barb of the arrow,
            and list of startpoint and endpoint y_value pairs separated by a
            None to create the barb of the arrow.
        """
        self.end_x = [i + j for i, j in zip(self.x, self.u)]
        self.end_y = [i + j for i, j in zip(self.y, self.v)]
        empty = [None] * len(self.x)
        barb_x = FigureFactory._flatten(zip(self.x, self.end_x, empty))
        barb_y = FigureFactory._flatten(zip(self.y, self.end_y, empty))
        return barb_x, barb_y

    def get_quiver_arrows(self):
        """
        Creates lists of x and y values to plot the arrows

        Gets length of each barb then calculates the length of each side of
        the arrow. Gets angle of barb and applies angle to each side of the
        arrowhead. Next uses arrow_scale to scale the length of arrowhead and
        creates x and y values for arrowhead point1 and point2. Finally x and y
        values for point1, endpoint and point2s for each arrowhead are
        separated by a None and zipped to create lists of x and y values for
        the arrows.

        :rtype: (list, list) arrow_x, arrow_y: list of point1, endpoint, point2
            x_values separated by a None to create the arrowhead and list of
            point1, endpoint, point2 y_values separated by a None to create
            the barb of the arrow.
        """
        dif_x = [i - j for i, j in zip(self.end_x, self.x)]
        dif_y = [i - j for i, j in zip(self.end_y, self.y)]

        # Get barb lengths(default arrow length = 30% barb length)
        barb_len = [None] * len(self.x)
        for index in range(len(barb_len)):
            barb_len[index] = math.hypot(dif_x[index], dif_y[index])

        # Make arrow lengths
        arrow_len = [None] * len(self.x)
        arrow_len = [i * self.arrow_scale for i in barb_len]

        # Get barb angles
        barb_ang = [None] * len(self.x)
        for index in range(len(barb_ang)):
            barb_ang[index] = math.atan2(dif_y[index], dif_x[index])

        # Set angles to create arrow
        ang1 = [i + self.angle for i in barb_ang]
        ang2 = [i - self.angle for i in barb_ang]

        cos_ang1 = [None] * len(ang1)
        for index in range(len(ang1)):
            cos_ang1[index] = math.cos(ang1[index])
        seg1_x = [i * j for i, j in zip(arrow_len, cos_ang1)]

        sin_ang1 = [None] * len(ang1)
        for index in range(len(ang1)):
            sin_ang1[index] = math.sin(ang1[index])
        seg1_y = [i * j for i, j in zip(arrow_len, sin_ang1)]

        cos_ang2 = [None] * len(ang2)
        for index in range(len(ang2)):
            cos_ang2[index] = math.cos(ang2[index])
        seg2_x = [i * j for i, j in zip(arrow_len, cos_ang2)]

        sin_ang2 = [None] * len(ang2)
        for index in range(len(ang2)):
            sin_ang2[index] = math.sin(ang2[index])
        seg2_y = [i * j for i, j in zip(arrow_len, sin_ang2)]

        # Set coordinates to create arrow
        for index in range(len(self.end_x)):
            point1_x = [i - j for i, j in zip(self.end_x, seg1_x)]
            point1_y = [i - j for i, j in zip(self.end_y, seg1_y)]
            point2_x = [i - j for i, j in zip(self.end_x, seg2_x)]
            point2_y = [i - j for i, j in zip(self.end_y, seg2_y)]

        # Combine lists to create arrow
        empty = [None] * len(self.end_x)
        arrow_x = FigureFactory._flatten(zip(point1_x, self.end_x,
                                             point2_x, empty))
        arrow_y = FigureFactory._flatten(zip(point1_y, self.end_y,
                                             point2_y, empty))
        return arrow_x, arrow_y


class _Streamline(FigureFactory):
    """
    Refer to FigureFactory.create_streamline() for docstring
    """
    def __init__(self, x, y, u, v,
                 density, angle,
                 arrow_scale, **kwargs):
        self.x = np.array(x)
        self.y = np.array(y)
        self.u = np.array(u)
        self.v = np.array(v)
        self.angle = angle
        self.arrow_scale = arrow_scale
        self.density = int(30 * density)  # Scale similarly to other functions
        self.delta_x = self.x[1] - self.x[0]
        self.delta_y = self.y[1] - self.y[0]
        self.val_x = self.x
        self.val_y = self.y

        # Set up spacing
        self.blank = np.zeros((self.density, self.density))
        self.spacing_x = len(self.x) / float(self.density - 1)
        self.spacing_y = len(self.y) / float(self.density - 1)
        self.trajectories = []

        # Rescale speed onto axes-coordinates
        self.u = self.u / (self.x[-1] - self.x[0])
        self.v = self.v / (self.y[-1] - self.y[0])
        self.speed = np.sqrt(self.u ** 2 + self.v ** 2)

        # Rescale u and v for integrations.
        self.u *= len(self.x)
        self.v *= len(self.y)
        self.st_x = []
        self.st_y = []
        self.get_streamlines()
        self.sum_streamlines()
        self.get_streamline_arrows()

    def blank_pos(self, xi, yi):
        """
        Set up positions for trajectories to be used with rk4 function.
        """
        return (int((xi / self.spacing_x) + 0.5),
                int((yi / self.spacing_y) + 0.5))

    def value_at(self, a, xi, yi):
        """
        Set up for RK4 function, based on Bokeh's streamline code
        """
        if isinstance(xi, np.ndarray):
            self.x = xi.astype(np.int)
            self.y = yi.astype(np.int)
        else:
            self.val_x = np.int(xi)
            self.val_y = np.int(yi)
        a00 = a[self.val_y, self.val_x]
        a01 = a[self.val_y, self.val_x + 1]
        a10 = a[self.val_y + 1, self.val_x]
        a11 = a[self.val_y + 1, self.val_x + 1]
        xt = xi - self.val_x
        yt = yi - self.val_y
        a0 = a00 * (1 - xt) + a01 * xt
        a1 = a10 * (1 - xt) + a11 * xt
        return a0 * (1 - yt) + a1 * yt

    def rk4_integrate(self, x0, y0):
        """
        RK4 forward and back trajectories from the initial conditions.

        Adapted from Bokeh's streamline -uses Runge-Kutta method to fill
        x and y trajectories then checks length of traj (s in units of axes)
        """
        def f(xi, yi):
            dt_ds = 1. / self.value_at(self.speed, xi, yi)
            ui = self.value_at(self.u, xi, yi)
            vi = self.value_at(self.v, xi, yi)
            return ui * dt_ds, vi * dt_ds

        def g(xi, yi):
            dt_ds = 1. / self.value_at(self.speed, xi, yi)
            ui = self.value_at(self.u, xi, yi)
            vi = self.value_at(self.v, xi, yi)
            return -ui * dt_ds, -vi * dt_ds

        def check(xi, yi):
            return 0 <= xi < len(self.x) - 1 and 0 <= yi < len(self.y) - 1

        xb_changes = []
        yb_changes = []

        def rk4(x0, y0, f):
            ds = 0.01
            stotal = 0
            xi = x0
            yi = y0
            xb, yb = self.blank_pos(xi, yi)
            xf_traj = []
            yf_traj = []
            while check(xi, yi):
                xf_traj.append(xi)
                yf_traj.append(yi)
                try:
                    k1x, k1y = f(xi, yi)
                    k2x, k2y = f(xi + .5 * ds * k1x, yi + .5 * ds * k1y)
                    k3x, k3y = f(xi + .5 * ds * k2x, yi + .5 * ds * k2y)
                    k4x, k4y = f(xi + ds * k3x, yi + ds * k3y)
                except IndexError:
                    break
                xi += ds * (k1x + 2 * k2x + 2 * k3x + k4x) / 6.
                yi += ds * (k1y + 2 * k2y + 2 * k3y + k4y) / 6.
                if not check(xi, yi):
                    break
                stotal += ds
                new_xb, new_yb = self.blank_pos(xi, yi)
                if new_xb != xb or new_yb != yb:
                    if self.blank[new_yb, new_xb] == 0:
                        self.blank[new_yb, new_xb] = 1
                        xb_changes.append(new_xb)
                        yb_changes.append(new_yb)
                        xb = new_xb
                        yb = new_yb
                    else:
                        break
                if stotal > 2:
                    break
            return stotal, xf_traj, yf_traj

        sf, xf_traj, yf_traj = rk4(x0, y0, f)
        sb, xb_traj, yb_traj = rk4(x0, y0, g)
        stotal = sf + sb
        x_traj = xb_traj[::-1] + xf_traj[1:]
        y_traj = yb_traj[::-1] + yf_traj[1:]

        if len(x_traj) < 1:
            return None
        if stotal > .2:
            initxb, inityb = self.blank_pos(x0, y0)
            self.blank[inityb, initxb] = 1
            return x_traj, y_traj
        else:
            for xb, yb in zip(xb_changes, yb_changes):
                self.blank[yb, xb] = 0
            return None

    def traj(self, xb, yb):
        """
        Integrate trajectories

        :param (int) xb: results of passing xi through self.blank_pos
        :param (int) yb: results of passing yi through self.blank_pos

        Calculate each trajectory based on rk4 integrate method.
        """

        if xb < 0 or xb >= self.density or yb < 0 or yb >= self.density:
            return
        if self.blank[yb, xb] == 0:
            t = self.rk4_integrate(xb * self.spacing_x, yb * self.spacing_y)
            if t is not None:
                self.trajectories.append(t)

    def get_streamlines(self):
        """
        Get streamlines by building trajectory set.
        """
        for indent in range(self.density // 2):
            for xi in range(self.density - 2 * indent):
                self.traj(xi + indent, indent)
                self.traj(xi + indent, self.density - 1 - indent)
                self.traj(indent, xi + indent)
                self.traj(self.density - 1 - indent, xi + indent)

        self.st_x = [np.array(t[0]) * self.delta_x + self.x[0] for t in
                     self.trajectories]
        self.st_y = [np.array(t[1]) * self.delta_y + self.y[0] for t in
                     self.trajectories]

        for index in range(len(self.st_x)):
            self.st_x[index] = self.st_x[index].tolist()
            self.st_x[index].append(np.nan)

        for index in range(len(self.st_y)):
            self.st_y[index] = self.st_y[index].tolist()
            self.st_y[index].append(np.nan)

    def get_streamline_arrows(self):
        """
        Makes an arrow for each streamline.

        Gets angle of streamline at 1/3 mark and creates arrow coordinates
        based off of user defined angle and arrow_scale.

        :rtype (list, list) arrows_x: x-values to create arrowhead and
            arrows_y: y-values to create arrowhead
        """
        arrow_end_x = np.empty((len(self.st_x)))
        arrow_end_y = np.empty((len(self.st_y)))
        arrow_start_x = np.empty((len(self.st_x)))
        arrow_start_y = np.empty((len(self.st_y)))
        for index in range(len(self.st_x)):
            arrow_end_x[index] = (self.st_x[index]
                                  [int(len(self.st_x[index]) / 3)])
            arrow_start_x[index] = (self.st_x[index]
                                    [(int(len(self.st_x[index]) / 3)) - 1])
            arrow_end_y[index] = (self.st_y[index]
                                  [int(len(self.st_y[index]) / 3)])
            arrow_start_y[index] = (self.st_y[index]
                                    [(int(len(self.st_y[index]) / 3)) - 1])

        dif_x = arrow_end_x - arrow_start_x
        dif_y = arrow_end_y - arrow_start_y

        streamline_ang = np.arctan(dif_y / dif_x)

        ang1 = streamline_ang + self.angle
        ang2 = streamline_ang - self.angle

        seg1_x = np.cos(ang1) * self.arrow_scale
        seg1_y = np.sin(ang1) * self.arrow_scale
        seg2_x = np.cos(ang2) * self.arrow_scale
        seg2_y = np.sin(ang2) * self.arrow_scale

        point1_x = np.empty((len(dif_x)))
        point1_y = np.empty((len(dif_y)))
        point2_x = np.empty((len(dif_x)))
        point2_y = np.empty((len(dif_y)))

        for index in range(len(dif_x)):
            if dif_x[index] >= 0:
                point1_x[index] = arrow_end_x[index] - seg1_x[index]
                point1_y[index] = arrow_end_y[index] - seg1_y[index]
                point2_x[index] = arrow_end_x[index] - seg2_x[index]
                point2_y[index] = arrow_end_y[index] - seg2_y[index]
            else:
                point1_x[index] = arrow_end_x[index] + seg1_x[index]
                point1_y[index] = arrow_end_y[index] + seg1_y[index]
                point2_x[index] = arrow_end_x[index] + seg2_x[index]
                point2_y[index] = arrow_end_y[index] + seg2_y[index]

        space = np.empty((len(point1_x)))
        space[:] = np.nan

        # Combine arrays into matrix
        arrows_x = np.matrix([point1_x, arrow_end_x, point2_x, space])
        arrows_x = np.array(arrows_x)
        arrows_x = arrows_x.flatten('F')
        arrows_x = arrows_x.tolist()

        # Combine arrays into matrix
        arrows_y = np.matrix([point1_y, arrow_end_y, point2_y, space])
        arrows_y = np.array(arrows_y)
        arrows_y = arrows_y.flatten('F')
        arrows_y = arrows_y.tolist()

        return arrows_x, arrows_y

    def sum_streamlines(self):
        """
        Makes all streamlines readable as a single trace.

        :rtype (list, list): streamline_x: all x values for each streamline
            combined into single list and streamline_y: all y values for each
            streamline combined into single list
        """
        streamline_x = sum(self.st_x, [])
        streamline_y = sum(self.st_y, [])
        return streamline_x, streamline_y


class _OHLC(FigureFactory):
    """
    Refer to FigureFactory.create_ohlc_increase() for docstring.
    """
    def __init__(self, open, high, low, close, dates, **kwargs):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.empty = [None] * len(open)
        self.dates = dates

        self.all_x = []
        self.all_y = []
        self.increase_x = []
        self.increase_y = []
        self.decrease_x = []
        self.decrease_y = []
        self.get_all_xy()
        self.separate_increase_decrease()

    def get_all_xy(self):
        """
        Zip data to create OHLC shape

        OHLC shape: low to high vertical bar with
        horizontal branches for open and close values.
        If dates were added, the smallest date difference is calculated and
        multiplied by .2 to get the length of the open and close branches.
        If no date data was provided, the x-axis is a list of integers and the
        length of the open and close branches is .2.
        """
        self.all_y = list(zip(self.open, self.open, self.high,
                              self.low, self.close, self.close, self.empty))
        if self.dates is not None:
            date_dif = []
            for i in range(len(self.dates) - 1):
                date_dif.append(self.dates[i + 1] - self.dates[i])
            date_dif_min = (min(date_dif)) / 5
            self.all_x = [[x - date_dif_min, x, x, x, x, x +
                           date_dif_min, None] for x in self.dates]
        else:
            self.all_x = [[x - .2, x, x, x, x, x + .2, None]
                          for x in range(len(self.open))]

    def separate_increase_decrease(self):
        """
        Separate data into two groups: increase and decrease

        (1) Increase, where close > open and
        (2) Decrease, where close <= open
        """
        for index in range(len(self.open)):
            if self.close[index] is None:
                pass
            elif self.close[index] > self.open[index]:
                self.increase_x.append(self.all_x[index])
                self.increase_y.append(self.all_y[index])
            else:
                self.decrease_x.append(self.all_x[index])
                self.decrease_y.append(self.all_y[index])

    def get_increase(self):
        """
        Flatten increase data and get increase text

        :rtype (list, list, list): flat_increase_x: x-values for the increasing
            trace, flat_increase_y: y=values for the increasing trace and
            text_increase: hovertext for the increasing trace
        """
        flat_increase_x = FigureFactory._flatten(self.increase_x)
        flat_increase_y = FigureFactory._flatten(self.increase_y)
        text_increase = (("Open", "Open", "High",
                          "Low", "Close", "Close", '') *
                         (len(self.increase_x)))

        return flat_increase_x, flat_increase_y, text_increase

    def get_decrease(self):
        """
        Flatten decrease data and get decrease text

        :rtype (list, list, list): flat_decrease_x: x-values for the decreasing
            trace, flat_decrease_y: y=values for the decreasing trace and
            text_decrease: hovertext for the decreasing trace
        """
        flat_decrease_x = FigureFactory._flatten(self.decrease_x)
        flat_decrease_y = FigureFactory._flatten(self.decrease_y)
        text_decrease = (("Open", "Open", "High",
                          "Low", "Close", "Close", '') *
                         (len(self.decrease_x)))

        return flat_decrease_x, flat_decrease_y, text_decrease


class _Candlestick(FigureFactory):
    """
    Refer to FigureFactory.create_candlestick() for docstring.
    """
    def __init__(self, open, high, low, close, dates, **kwargs):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        if dates is not None:
            self.x = dates
        else:
            self.x = [x for x in range(len(self.open))]
        self.get_candle_increase()

    def get_candle_increase(self):
        """
        Separate increasing data from decreasing data.

        The data is increasing when close value > open value
        and decreasing when the close value <= open value.
        """
        increase_y = []
        increase_x = []
        for index in range(len(self.open)):
            if self.close[index] > self.open[index]:
                increase_y.append(self.low[index])
                increase_y.append(self.open[index])
                increase_y.append(self.close[index])
                increase_y.append(self.close[index])
                increase_y.append(self.close[index])
                increase_y.append(self.high[index])
                increase_x.append(self.x[index])

        increase_x = [[x, x, x, x, x, x] for x in increase_x]
        increase_x = FigureFactory._flatten(increase_x)

        return increase_x, increase_y

    def get_candle_decrease(self):
        """
        Separate increasing data from decreasing data.

        The data is increasing when close value > open value
        and decreasing when the close value <= open value.
        """
        decrease_y = []
        decrease_x = []
        for index in range(len(self.open)):
            if self.close[index] <= self.open[index]:
                decrease_y.append(self.low[index])
                decrease_y.append(self.open[index])
                decrease_y.append(self.close[index])
                decrease_y.append(self.close[index])
                decrease_y.append(self.close[index])
                decrease_y.append(self.high[index])
                decrease_x.append(self.x[index])

        decrease_x = [[x, x, x, x, x, x] for x in decrease_x]
        decrease_x = FigureFactory._flatten(decrease_x)

        return decrease_x, decrease_y


class _Distplot(FigureFactory):
    """
    Refer to TraceFactory.create_distplot() for docstring
    """
    def __init__(self, hist_data, group_labels,
                 bin_size, curve_type, colors,
                 rug_text, show_hist, show_curve):
        self.hist_data = hist_data
        self.group_labels = group_labels
        self.bin_size = bin_size
        self.show_hist = show_hist
        self.show_curve = show_curve
        self.trace_number = len(hist_data)
        if rug_text:
            self.rug_text = rug_text
        else:
            self.rug_text = [None] * self.trace_number

        self.start = []
        self.end = []
        if colors:
            self.colors = colors
        else:
            self.colors = [
                "rgb(31, 119, 180)", "rgb(255, 127, 14)",
                "rgb(44, 160, 44)", "rgb(214, 39, 40)",
                "rgb(148, 103, 189)", "rgb(140, 86, 75)",
                "rgb(227, 119, 194)", "rgb(127, 127, 127)",
                "rgb(188, 189, 34)", "rgb(23, 190, 207)"]
        self.curve_x = [None] * self.trace_number
        self.curve_y = [None] * self.trace_number

        for trace in self.hist_data:
            self.start.append(min(trace) * 1.)
            self.end.append(max(trace) * 1.)

    def make_hist(self):
        """
        Makes the histogram(s) for FigureFactory.create_distplot().

        :rtype (list) hist: list of histogram representations
        """
        hist = [None] * self.trace_number

        for index in range(self.trace_number):
            hist[index] = dict(type='histogram',
                               x=self.hist_data[index],
                               xaxis='x1',
                               yaxis='y1',
                               histnorm='probability',
                               name=self.group_labels[index],
                               legendgroup=self.group_labels[index],
                               marker=dict(color=self.colors[index]),
                               autobinx=False,
                               xbins=dict(start=self.start[index],
                                          end=self.end[index],
                                          size=self.bin_size),
                               opacity=.7)
        return hist

    def make_kde(self):
        """
        Makes the kernal density estimation(s) for create_distplot().

        This is called when curve_type = 'kde' in create_distplot().

        :rtype (list) curve: list of kde representations
        """
        curve = [None] * self.trace_number
        for index in range(self.trace_number):
            self.curve_x[index] = [self.start[index] +
                                   x * (self.end[index] - self.start[index]) /
                                   500 for x in range(500)]
            self.curve_y[index] = (scipy.stats.gaussian_kde
                                   (self.hist_data[index])
                                   (self.curve_x[index]))
            self.curve_y[index] *= self.bin_size

        for index in range(self.trace_number):
            curve[index] = dict(type='scatter',
                                x=self.curve_x[index],
                                y=self.curve_y[index],
                                xaxis='x1',
                                yaxis='y1',
                                mode='lines',
                                name=self.group_labels[index],
                                legendgroup=self.group_labels[index],
                                showlegend=False if self.show_hist else True,
                                marker=dict(color=self.colors[index]))
        return curve

    def make_normal(self):
        """
        Makes the normal curve(s) for create_distplot().

        This is called when curve_type = 'normal' in create_distplot().

        :rtype (list) curve: list of normal curve representations
        """
        curve = [None] * self.trace_number
        mean = [None] * self.trace_number
        sd = [None] * self.trace_number

        for index in range(self.trace_number):
            mean[index], sd[index] = (scipy.stats.norm.fit
                                      (self.hist_data[index]))
            self.curve_x[index] = [self.start[index] +
                                   x * (self.end[index] - self.start[index]) /
                                   500 for x in range(500)]
            self.curve_y[index] = scipy.stats.norm.pdf(
                self.curve_x[index], loc=mean[index], scale=sd[index])
            self.curve_y[index] *= self.bin_size

        for index in range(self.trace_number):
            curve[index] = dict(type='scatter',
                                x=self.curve_x[index],
                                y=self.curve_y[index],
                                xaxis='x1',
                                yaxis='y1',
                                mode='lines',
                                name=self.group_labels[index],
                                legendgroup=self.group_labels[index],
                                showlegend=False if self.show_hist else True,
                                marker=dict(color=self.colors[index]))
        return curve

    def make_rug(self):
        """
        Makes the rug plot(s) for create_distplot().

        :rtype (list) rug: list of rug plot representations
        """
        rug = [None] * self.trace_number
        for index in range(self.trace_number):

            rug[index] = dict(type='scatter',
                              x=self.hist_data[index],
                              y=([self.group_labels[index]] *
                                 len(self.hist_data[index])),
                              xaxis='x1',
                              yaxis='y2',
                              mode='markers',
                              name=self.group_labels[index],
                              legendgroup=self.group_labels[index],
                              showlegend=(False if self.show_hist or
                                          self.show_curve else True),
                              text=self.rug_text[index],
                              marker=dict(color=self.colors[index],
                                          symbol='line-ns-open'))
        return rug


class _Dendrogram(FigureFactory):
    """Refer to FigureFactory.create_dendrogram() for docstring."""

    def __init__(self, X, orientation='bottom', labels=None, colorscale=None,
                 width="100%", height="100%", xaxis='xaxis', yaxis='yaxis'):
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

        (dd_traces, xvals, yvals,
            ordered_labels, leaves) = self.get_dendrogram_traces(X, colorscale)

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

    def get_dendrogram_traces(self, X, colorscale):
        """
        Calculates all the elements needed for plotting a dendrogram.

        :param (ndarray) X: Matrix of observations as array of arrays
        :param (list) colorscale: Color scale for dendrogram tree clusters
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
        d = scs.distance.pdist(X)
        Z = sch.linkage(d, method='complete')
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
