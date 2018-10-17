from unittest import TestCase
from plotly import optional_imports
from plotly.graph_objs import graph_objs as go
from plotly.exceptions import PlotlyError

import plotly.figure_factory as ff
from plotly.tests.test_optional.optional_utils import NumpyTestUtilsMixin

import numpy as np
from scipy.spatial import Delaunay
import pandas as pd

shapely = optional_imports.get_module('shapely')
shapefile = optional_imports.get_module('shapefile')
gp = optional_imports.get_module('geopandas')


class TestDistplot(NumpyTestUtilsMixin, TestCase):

    def test_wrong_curve_type(self):

        # check: PlotlyError (and specific message) is raised if curve_type is
        # not 'kde' or 'normal'

        kwargs = {'hist_data': [[1, 2, 3]], 'group_labels': ['group'],
                  'curve_type': 'curve'}
        self.assertRaisesRegexp(PlotlyError, "curve_type must be defined as "
                                             "'kde' or 'normal'",
                                ff.create_distplot, **kwargs)

    def test_wrong_histdata_format(self):

        # check: PlotlyError if hist_data is not a list of lists or list of
        # np.ndarrays (if hist_data is entered as just a list the function
        # will fail)

        kwargs = {'hist_data': [1, 2, 3], 'group_labels': ['group']}
        self.assertRaises(PlotlyError, ff.create_distplot, **kwargs)

    def test_unequal_data_label_length(self):
        kwargs = {'hist_data': [[1, 2]], 'group_labels': ['group', 'group2']}
        self.assertRaises(PlotlyError, ff.create_distplot, **kwargs)

        kwargs = {'hist_data': [[1, 2], [1, 2, 3]], 'group_labels': ['group']}
        self.assertRaises(PlotlyError, ff.create_distplot, **kwargs)

    def test_simple_distplot_prob_density(self):

        # we should be able to create a single distplot with a simple dataset
        # and default kwargs

        dp = ff.create_distplot(hist_data=[[1, 2, 2, 3]],
                                group_labels=['distplot'],
                                histnorm='probability density')
        expected_dp_layout = {'barmode': 'overlay',
                              'hovermode': 'closest',
                              'legend': {'traceorder': 'reversed'},
                              'xaxis': {'anchor': 'y2', 'domain': [0.0, 1.0], 'zeroline': False},
                              'yaxis': {'anchor': 'free', 'domain': [0.35, 1], 'position': 0.0},
                              'yaxis2': {'anchor': 'x', 'domain': [0, 0.25], 'dtick': 1, 'showticklabels': False}}
        self.assert_fig_equal(dp['layout'], expected_dp_layout)

        expected_dp_data_hist = {'autobinx': False,
                                 'histnorm': 'probability density',
                                 'legendgroup': 'distplot',
                                 'marker': {'color': 'rgb(31, 119, 180)'},
                                 'name': 'distplot',
                                 'opacity': 0.7,
                                 'type': 'histogram',
                                 'x': [1, 2, 2, 3],
                                 'xaxis': 'x',
                                 'xbins': {'end': 3.0, 'size': 1.0, 'start': 1.0},
                                 'yaxis': 'y'}
        self.assert_fig_equal(dp['data'][0], expected_dp_data_hist)

        expected_dp_data_rug = {'legendgroup': 'distplot',
                                'marker': {'color': 'rgb(31, 119, 180)',
                                           'symbol': 'line-ns-open'},
                                'mode': 'markers',
                                'name': 'distplot',
                                'showlegend': False,
                                'type': 'scatter',
                                'x': [1, 2, 2, 3],
                                'xaxis': 'x',
                                'y': ['distplot', 'distplot',
                                      'distplot', 'distplot'],
                                'yaxis': 'y2'}
        self.assert_fig_equal(dp['data'][2], expected_dp_data_rug)

    def test_simple_distplot_prob(self):

        # we should be able to create a single distplot with a simple dataset
        # and default kwargs

        dp = ff.create_distplot(hist_data=[[1, 2, 2, 3]],
                                group_labels=['distplot'], histnorm='probability')
        expected_dp_layout = {'barmode': 'overlay',
                              'hovermode': 'closest',
                              'legend': {'traceorder': 'reversed'},
                              'xaxis': {'anchor': 'y2',
                                        'domain': [0.0, 1.0],
                                        'zeroline': False},
                              'yaxis': {'anchor': 'free',
                                        'domain': [0.35, 1],
                                        'position': 0.0},
                              'yaxis2': {'anchor': 'x',
                                         'domain': [0, 0.25],
                                         'dtick': 1,
                                         'showticklabels': False}}
        self.assert_fig_equal(dp['layout'], expected_dp_layout)

        expected_dp_data_hist = {'autobinx': False,
                                 'histnorm': 'probability',
                                 'legendgroup': 'distplot',
                                 'marker': {'color': 'rgb(31, 119, 180)'},
                                 'name': 'distplot',
                                 'opacity': 0.7,
                                 'type': 'histogram',
                                 'x': [1, 2, 2, 3],
                                 'xaxis': 'x',
                                 'xbins': {'end': 3.0, 'size': 1.0, 'start': 1.0},
                                 'yaxis': 'y'}
        self.assert_fig_equal(dp['data'][0], expected_dp_data_hist)

        expected_dp_data_rug = {'legendgroup': 'distplot',
                                'marker': {'color': 'rgb(31, 119, 180)',
                                           'symbol': 'line-ns-open'},
                                'mode': 'markers',
                                'name': 'distplot',
                                'showlegend': False,
                                'type': 'scatter',
                                'x': [1, 2, 2, 3],
                                'xaxis': 'x',
                                'y': ['distplot', 'distplot',
                                      'distplot', 'distplot'],
                                'yaxis': 'y2'}
        self.assert_fig_equal(dp['data'][2], expected_dp_data_rug)

    def test_distplot_more_args_prob_dens(self):

        # we should be able to create a distplot with 2 datasets no
        # rugplot, defined bin_size, and added title

        hist1_x = [0.8, 1.2, 0.2, 0.6, 1.6,
                   -0.9, -0.07, 1.95, 0.9, -0.2,
                   -0.5, 0.3, 0.4, -0.37, 0.6]
        hist2_x = [0.8, 1.5, 1.5, 0.6, 0.59,
                   1.0, 0.8, 1.7, 0.5, 0.8,
                   -0.3, 1.2, 0.56, 0.3, 2.2]

        hist_data = [hist1_x] + [hist2_x]
        group_labels = ['2012', '2013']

        dp = ff.create_distplot(hist_data, group_labels,
                                histnorm='probability density',
                                show_rug=False, bin_size=.2)
        dp['layout'].update(title='Dist Plot')

        expected_dp_layout = {'barmode': 'overlay',
                              'hovermode': 'closest',
                              'legend': {'traceorder': 'reversed'},
                              'xaxis': {'anchor': 'y2',
                                        'domain': [0.0, 1.0],
                                        'zeroline': False},
                              'yaxis': {'anchor': 'free',
                                        'domain': [0.0, 1],
                                        'position': 0.0},
                              'title': 'Dist Plot'}
        self.assert_fig_equal(dp['layout'], expected_dp_layout)

        expected_dp_data_hist_1 = {'autobinx': False,
                                   'histnorm': 'probability density',
                                   'legendgroup': '2012',
                                   'marker': {'color': 'rgb(31, 119, 180)'},
                                   'name': '2012',
                                   'opacity': 0.7,
                                   'type': 'histogram',
                                   'x': [0.8, 1.2, 0.2, 0.6, 1.6, -0.9, -0.07,
                                         1.95, 0.9, -0.2, -0.5, 0.3, 0.4,
                                         -0.37, 0.6],
                                   'xaxis': 'x',
                                   'xbins': {'end': 1.95, 'size': 0.2,
                                             'start': -0.9},
                                   'yaxis': 'y'}
        self.assert_fig_equal(dp['data'][0], expected_dp_data_hist_1)

        expected_dp_data_hist_2 = {'autobinx': False,
                                   'histnorm': 'probability density',
                                   'legendgroup': '2013',
                                   'marker': {'color': 'rgb(255, 127, 14)'},
                                   'name': '2013',
                                   'opacity': 0.7,
                                   'type': 'histogram',
                                   'x': [0.8, 1.5, 1.5, 0.6, 0.59, 1.0, 0.8,
                                         1.7, 0.5, 0.8, -0.3, 1.2, 0.56, 0.3,
                                         2.2],
                                   'xaxis': 'x',
                                   'xbins': {'end': 2.2, 'size': 0.2,
                                             'start': -0.3},
                                   'yaxis': 'y'}
        self.assert_fig_equal(dp['data'][1], expected_dp_data_hist_2)

    def test_distplot_more_args_prob(self):

        # we should be able to create a distplot with 2 datasets no
        # rugplot, defined bin_size, and added title

        hist1_x = [0.8, 1.2, 0.2, 0.6, 1.6,
                   -0.9, -0.07, 1.95, 0.9, -0.2,
                   -0.5, 0.3, 0.4, -0.37, 0.6]
        hist2_x = [0.8, 1.5, 1.5, 0.6, 0.59,
                   1.0, 0.8, 1.7, 0.5, 0.8,
                   -0.3, 1.2, 0.56, 0.3, 2.2]

        hist_data = [hist1_x] + [hist2_x]
        group_labels = ['2012', '2013']

        dp = ff.create_distplot(hist_data, group_labels,
                                histnorm='probability',
                                show_rug=False, bin_size=.2)
        dp['layout'].update(title='Dist Plot')

        expected_dp_layout = {'barmode': 'overlay',
                              'hovermode': 'closest',
                              'legend': {'traceorder': 'reversed'},
                              'title': 'Dist Plot',
                              'xaxis': {'anchor': 'y2',
                                        'domain': [0.0, 1.0],
                                        'zeroline': False},
                              'yaxis': {'anchor': 'free',
                                        'domain': [0.0, 1],
                                        'position': 0.0}}
        self.assert_fig_equal(dp['layout'], expected_dp_layout)

        expected_dp_data_hist_1 = {'autobinx': False,
                                   'histnorm': 'probability',
                                   'legendgroup': '2012',
                                   'marker': {'color': 'rgb(31, 119, 180)'},
                                   'name': '2012',
                                   'opacity': 0.7,
                                   'type': 'histogram',
                                   'x': [0.8, 1.2, 0.2, 0.6, 1.6, -0.9, -0.07,
                                         1.95, 0.9, -0.2, -0.5, 0.3, 0.4,
                                         -0.37, 0.6],
                                   'xaxis': 'x',
                                   'xbins': {'end': 1.95, 'size': 0.2,
                                             'start': -0.9},
                                   'yaxis': 'y'}
        self.assert_fig_equal(dp['data'][0], expected_dp_data_hist_1)

        expected_dp_data_hist_2 = {'autobinx': False,
                                   'histnorm': 'probability',
                                   'legendgroup': '2013',
                                   'marker': {'color': 'rgb(255, 127, 14)'},
                                   'name': '2013',
                                   'opacity': 0.7,
                                   'type': 'histogram',
                                   'x': [0.8, 1.5, 1.5, 0.6, 0.59, 1.0, 0.8,
                                         1.7, 0.5, 0.8, -0.3, 1.2, 0.56, 0.3,
                                         2.2],
                                   'xaxis': 'x',
                                   'xbins': {'end': 2.2, 'size': 0.2,
                                             'start': -0.3},
                                   'yaxis': 'y'}
        self.assert_fig_equal(dp['data'][1], expected_dp_data_hist_2)

        def test_distplot_binsize_array_prob(self):
            hist1_x = [0.8, 1.2, 0.2, 0.6, 1.6, -0.9, -0.07, 1.95, 0.9, -0.2,
                       -0.5, 0.3, 0.4, -0.37, 0.6]
            hist2_x = [0.8, 1.5, 1.5, 0.6, 0.59, 1.0, 0.8, 1.7, 0.5, 0.8, -0.3,
                       1.2, 0.56, 0.3, 2.2]

            hist_data = [hist1_x, hist2_x]
            group_labels = ['2012', '2013']

            dp = ff.create_distplot(hist_data, group_labels,
                                    histnorm='probability',
                                    show_rug=False,
                                    bin_size=[.2, .2])

            expected_dp_data_hist_1 = {'autobinx': False,
                                       'histnorm': 'probability density',
                                       'legendgroup': '2012',
                                       'marker':
                                       {'color': 'rgb(31,119,180)'},
                                       'name': '2012',
                                       'opacity': 0.7,
                                       'type': 'histogram',
                                       'x': [0.8, 1.2, 0.2, 0.6, 1.6, -0.9,
                                             -0.07, 1.95, 0.9, -0.2, -0.5, 0.3,
                                             0.4, -0.37, 0.6],
                                       'xaxis': 'x',
                                       'xbins': {'end': 1.95, 'size': 0.2,
                                                 'start': -0.9},
                                       'yaxis': 'y'}
            self.assert_fig_equal(dp['data'][0], expected_dp_data_hist_1)

            expected_dp_data_hist_2 = {'autobinx': False,
                                       'histnorm': 'probability density',
                                       'legendgroup': '2013',
                                       'marker':
                                       {'color': 'rgb(255,127,14)'},
                                       'name': '2013',
                                       'opacity': 0.7,
                                       'type': 'histogram',
                                       'x': [0.8, 1.5, 1.5, 0.6, 0.59, 1.0,
                                             0.8, 1.7, 0.5, 0.8, -0.3, 1.2,
                                             0.56, 0.3, 2.2],
                                       'xaxis': 'x',
                                       'xbins': {'end': 2.2, 'size': 0.2,
                                                 'start': -0.3},
                                       'yaxis': 'y'}
            self.assert_fig_equal(dp['data'][1], expected_dp_data_hist_2)

        def test_distplot_binsize_array_prob_density(self):
            hist1_x = [0.8, 1.2, 0.2, 0.6, 1.6, -0.9, -0.07, 1.95, 0.9, -0.2,
                       -0.5, 0.3, 0.4, -0.37, 0.6]
            hist2_x = [0.8, 1.5, 1.5, 0.6, 0.59, 1.0, 0.8, 1.7, 0.5, 0.8, -0.3,
                       1.2, 0.56, 0.3, 2.2]

            hist_data = [hist1_x, hist2_x]
            group_labels = ['2012', '2013']

            dp = ff.create_distplot(hist_data, group_labels,
                                    histnorm='probability',
                                    show_rug=False,
                                    bin_size=[.2, .2])

            expected_dp_data_hist_1 = {'autobinx': False,
                                       'histnorm': 'probability density',
                                       'legendgroup': '2012',
                                       'marker':
                                       {'color': 'rgb(31,119,180)'},
                                       'name': '2012',
                                       'opacity': 0.7,
                                       'type': 'histogram',
                                       'x': [0.8, 1.2, 0.2, 0.6, 1.6, -0.9,
                                             -0.07, 1.95, 0.9, -0.2, -0.5, 0.3,
                                             0.4, -0.37, 0.6],
                                       'xaxis': 'x',
                                       'xbins': {'end': 1.95, 'size': 0.2,
                                                 'start': -0.9},
                                       'yaxis': 'y'}
            self.assert_fig_equal(dp['data'][0], expected_dp_data_hist_1)

            expected_dp_data_hist_2 = {'autobinx': False,
                                       'histnorm': 'probability density',
                                       'legendgroup': '2013',
                                       'marker':
                                       {'color': 'rgb(255,127,14)'},
                                       'name': '2013',
                                       'opacity': 0.7,
                                       'type': 'histogram',
                                       'x': [0.8, 1.5, 1.5, 0.6, 0.59, 1.0,
                                             0.8, 1.7, 0.5, 0.8, -0.3, 1.2,
                                             0.56, 0.3, 2.2],
                                       'xaxis': 'x',
                                       'xbins': {'end': 2.2, 'size': 0.2,
                                                 'start': -0.3},
                                       'yaxis': 'y'}
            self.assert_fig_equal(dp['data'][1], expected_dp_data_hist_2)


class TestStreamline(TestCase):

    def test_wrong_arrow_scale(self):

        # check for ValueError if arrow_scale is <= 0

        kwargs = {'x': [0, 2], 'y': [0, 2],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]],
                  'arrow_scale': 0}
        self.assertRaises(ValueError, ff.create_streamline, **kwargs)

    def test_wrong_density(self):

        # check for ValueError if density is <= 0

        kwargs = {'x': [0, 2], 'y': [0, 2],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]],
                  'density': 0}
        self.assertRaises(ValueError, ff.create_streamline, **kwargs)

    def test_uneven_x(self):

        # check for PlotlyError if x is not evenly spaced

        kwargs = {'x': [0, 2, 7, 9], 'y': [0, 2, 4, 6],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, ff.create_streamline, **kwargs)

    def test_uneven_y(self):

        # check for PlotlyError if y is not evenly spaced

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3, 3.5],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, ff.create_streamline, **kwargs)

    def test_unequal_length_xy(self):

        # check for PlotlyError if u and v are not the same length

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3.5],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, ff.create_streamline, **kwargs)

    def test_unequal_length_uv(self):

        # check for PlotlyError if u and v are not the same length

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3, 3.5],
                  'u': [[-1, -5], [-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, ff.create_streamline, **kwargs)

    def test_simple_streamline(self):

        # Need np to check streamline data,
        # this checks that the first 101 x and y values from streamline are
        # what we expect for a simple streamline where:
        # x = np.linspace(-1, 1, 3)
        # y = np.linspace(-1, 1, 3)
        # Y, X = np.meshgrid(x, y)
        # u = X**2
        # v = Y**2
        # u = u.T #transpose
        # v = v.T #transpose

        strln = ff.create_streamline(x=[-1., 0., 1.],
                                     y=[-1., 0., 1.],
                                     u=[[1., 0., 1.],
                                        [1., 0., 1.],
                                        [1., 0., 1.]],
                                     v=[[1., 1., 1.],
                                        [0., 0., 0.],
                                        [1., 1., 1.]])
        expected_strln_0_100 = {
            'y': [-1.0, -0.9788791845863757, -0.9579399744939614, -0.9371777642073374, -0.9165881396413338, -0.8961668671832106, -0.8759098835283448, -0.8558132862403048, -0.835873324973195, -0.8160863933003534, -0.7964490210989816, -0.7769578674451656, -0.7576097139780906, -0.7384014586961288, -0.7193301101509343, -0.7003927820087748, -0.681586687951103, -0.6629091368888596, -0.64435752846723, -0.6259293488396024, -0.6076221666912738, -0.5894336294951057, -0.5713614599827976, -0.5534034528167977, -0.5355574714490806, -0.5178214451541254, -0.5001933662244311, -0.4826712873178177, -0.4652533189465894, -0.44793762709939944, -0.4307224309873414, -0.4136060009064273, -0.39658665620919065, -0.3796627633786812, -0.3628327341986042, -0.34609502401380254, -0.3294481300756896, -0.31289058996761565, -0.2964209801054992, -0.28003791430937197, -0.2637400424417804, -0.24752604910925968, -0.23139465242334434, -0.21534460281781365, -0.19937468191908325, -0.18348370146685278, -0.1676705022823033, -0.15193395328130999, -0.13627295053029143, -0.1206864163424669, -0.10517329841242584, -0.08973256898704507, -0.07436322407090357, -0.05906428266445696, -0.04383478603333624, -0.028673797007230273, -0.013580399306900914, 0.0014484211645073852, 0.01648792568956914, 0.03159429687713278, 0.04676843461935776, 0.062011259175942746, 0.07732371182540754, 0.09270675554339824, 0.10816137570939799, 0.12368858084331191, 0.1392894033734846, 0.1549649004378033, 0.1707161547196483, 0.1865442753205595, 0.20245039867161063, 0.21843568948560943, 0.23450134175238246, 0.25064857977955146, 0.26687865928136767, 0.2831928685183458, 0.29959252949062387, 0.3160789991881776, 0.33265367090123643, 0.3493179755944802, 0.366073383348855, 0.3829214048751186, 0.39986359310352526, 0.41690154485438513, 0.4340369025945845, 0.4512713562855355, 0.46860664532844054, 0.4860445606132082, 0.5035869466778524, 0.5212357039857456, 0.5389927913286829, 0.5568602283643591, 0.5748400982975623, 0.5929345507151613, 0.6111458045858065, 0.6294761514361948, 0.6479279587167714, 0.6665036733708583, 0.6852058256224467, 0.704037032999252],
            'x': [-1.0, -0.9788791845863756, -0.9579399744939614, -0.9371777642073374, -0.9165881396413338, -0.8961668671832106, -0.8759098835283448, -0.8558132862403048, -0.835873324973195, -0.8160863933003534, -0.7964490210989816, -0.7769578674451656, -0.7576097139780906, -0.7384014586961289, -0.7193301101509344, -0.7003927820087748, -0.6815866879511031, -0.6629091368888596, -0.6443575284672302, -0.6259293488396025, -0.6076221666912739, -0.5894336294951058, -0.5713614599827976, -0.5534034528167978, -0.5355574714490807, -0.5178214451541254, -0.5001933662244312, -0.4826712873178177, -0.4652533189465894, -0.44793762709939944, -0.4307224309873414, -0.4136060009064273, -0.39658665620919065, -0.3796627633786812, -0.3628327341986042, -0.34609502401380254, -0.3294481300756896, -0.31289058996761565, -0.2964209801054992, -0.28003791430937197, -0.2637400424417804, -0.24752604910925968, -0.23139465242334434, -0.21534460281781365, -0.19937468191908325, -0.18348370146685278, -0.1676705022823033, -0.15193395328130999, -0.13627295053029143, -0.1206864163424669, -0.10517329841242584, -0.08973256898704507, -0.07436322407090357, -0.05906428266445696, -0.04383478603333624, -0.028673797007230273, -0.013580399306900914, 0.0014484211645073852, 0.01648792568956914, 0.03159429687713278, 0.04676843461935776, 0.062011259175942746, 0.07732371182540754, 0.09270675554339824, 0.10816137570939799, 0.12368858084331191, 0.1392894033734846, 0.1549649004378033, 0.1707161547196483, 0.1865442753205595, 0.20245039867161063, 0.21843568948560943, 0.23450134175238246, 0.25064857977955146, 0.26687865928136767, 0.2831928685183458, 0.29959252949062387, 0.3160789991881776, 0.33265367090123643, 0.3493179755944802, 0.366073383348855, 0.3829214048751186, 0.39986359310352526, 0.41690154485438513, 0.4340369025945845, 0.4512713562855355, 0.46860664532844054, 0.4860445606132082, 0.5035869466778524, 0.5212357039857456, 0.5389927913286829, 0.5568602283643591, 0.5748400982975623, 0.5929345507151613, 0.6111458045858065, 0.6294761514361948, 0.6479279587167714, 0.6665036733708583, 0.6852058256224467, 0.704037032999252],
            'type': 'scatter',
            'mode': 'lines'
        }
        self.assertListEqual(list(strln['data'][0]['y'][0:100]),
                             expected_strln_0_100['y'])
        self.assertListEqual(list(strln['data'][0]['x'][0:100]),
                             expected_strln_0_100['x'])


class TestDendrogram(NumpyTestUtilsMixin, TestCase):

    def test_default_dendrogram(self):
        X = np.array([[1, 2, 3, 4], [1, 1, 3, 4], [1, 2, 1, 4], [1, 2, 3, 1]])
        dendro = ff.create_dendrogram(X=X)

        expected_dendro = go.Figure(
            data=[
                go.Scatter(
                    x=np.array([25., 25., 35., 35.]),
                    y=np.array([0., 1., 1., 0.]),
                    marker=go.scatter.Marker(color='rgb(61,153,112)'),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                ),
                go.Scatter(
                    x=np.array([15., 15., 30., 30.]),
                    y=np.array([0., 2.23606798, 2.23606798, 1.]),
                    marker=go.scatter.Marker(color='rgb(61,153,112)'),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                ),
                go.Scatter(
                    x=np.array([5., 5., 22.5, 22.5]),
                    y=np.array([0., 3.60555128, 3.60555128, 2.23606798]),
                    marker=go.scatter.Marker(color='rgb(0,116,217)'),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                )
            ],
            layout=go.Layout(
                autosize=False,
                height=np.inf,
                hovermode='closest',
                showlegend=False,
                width=np.inf,
                xaxis=go.layout.XAxis(
                    mirror='allticks',
                    rangemode='tozero',
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    tickmode='array',
                    ticks='outside',
                    ticktext=np.array(['3', '2', '0', '1']),
                    tickvals=[5.0, 15.0, 25.0, 35.0],
                    type='linear',
                    zeroline=False
                ),
                yaxis=go.layout.YAxis(
                    mirror='allticks',
                    rangemode='tozero',
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    ticks='outside',
                    type='linear',
                    zeroline=False
                )
            )
        )

        self.assertEqual(len(dendro['data']), 3)

        # this is actually a bit clearer when debugging tests.
        self.assert_fig_equal(dendro['data'][0],
                              expected_dendro['data'][0])
        self.assert_fig_equal(dendro['data'][1],
                              expected_dendro['data'][1])
        self.assert_fig_equal(dendro['data'][2],
                              expected_dendro['data'][2])

        self.assert_fig_equal(dendro['layout'],
                              expected_dendro['layout'])

    def test_dendrogram_random_matrix(self):

        # create a random uncorrelated matrix
        X = np.random.rand(5, 5)

        # variable 2 is correlated with all the other variables
        X[2, :] = sum(X, 0)

        names = ['Jack', 'Oxana', 'John', 'Chelsea', 'Mark']
        dendro = ff.create_dendrogram(X, labels=names)

        expected_dendro = go.Figure(
            data=[
                go.Scatter(
                    marker=go.scatter.Marker(color='rgb(61,153,112)'),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                ),
                go.Scatter(
                    marker=go.scatter.Marker(
                        color='rgb(61,153,112)'
                    ),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                ),
                go.Scatter(
                    marker=go.scatter.Marker(color='rgb(61,153,112)'),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                ),
                go.Scatter(
                    marker=go.scatter.Marker(color='rgb(0,116,217)'),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                )
            ],
            layout=go.Layout(
                autosize=False,
                height=np.inf,
                hovermode='closest',
                showlegend=False,
                width=np.inf,
                xaxis=go.layout.XAxis(
                    mirror='allticks',
                    rangemode='tozero',
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    tickmode='array',
                    ticks='outside',
                    tickvals=[5.0, 15.0, 25.0, 35.0, 45.0],
                    type='linear',
                    zeroline=False
                ),
                yaxis=go.layout.YAxis(
                    mirror='allticks',
                    rangemode='tozero',
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    ticks='outside',
                    type='linear',
                    zeroline=False
                )
            )
        )

        self.assertEqual(len(dendro['data']), 4)

        # it's random, so we can only check that the values aren't equal
        y_vals = [dendro['data'][0].to_plotly_json().pop('y'),
                  dendro['data'][1].to_plotly_json().pop('y'),
                  dendro['data'][2].to_plotly_json().pop('y'),
                  dendro['data'][3].to_plotly_json().pop('y')]
        for i in range(len(y_vals)):
            for j in range(len(y_vals)):
                if i != j:
                    self.assertFalse(np.allclose(y_vals[i], y_vals[j]))

        x_vals = [dendro['data'][0].to_plotly_json().pop('x'),
                  dendro['data'][1].to_plotly_json().pop('x'),
                  dendro['data'][2].to_plotly_json().pop('x'),
                  dendro['data'][3].to_plotly_json().pop('x')]
        for i in range(len(x_vals)):
            for j in range(len(x_vals)):
                if i != j:
                    self.assertFalse(np.allclose(x_vals[i], x_vals[j]))

        # we also need to check the ticktext manually
        xaxis_ticktext = dendro['layout'].to_plotly_json()['xaxis'].pop('ticktext')
        self.assertEqual(xaxis_ticktext[0], 'John')

        # this is actually a bit clearer when debugging tests.
        self.assert_fig_equal(dendro['data'][0],
                              expected_dendro['data'][0],
                              ignore=['uid', 'x', 'y'])
        self.assert_fig_equal(dendro['data'][1],
                              expected_dendro['data'][1],
                              ignore=['uid', 'x', 'y'])
        self.assert_fig_equal(dendro['data'][2],
                              expected_dendro['data'][2],
                              ignore=['uid', 'x', 'y'])
        self.assert_fig_equal(dendro['data'][3],
                              expected_dendro['data'][3],
                              ignore=['uid', 'x', 'y'])

        # layout except xaxis
        self.assert_fig_equal(dendro['layout'],
                              expected_dendro['layout'],
                              ignore=['xaxis'])

        # xaxis
        self.assert_fig_equal(dendro['layout']['xaxis'],
                              expected_dendro['layout']['xaxis'],
                              ignore=['ticktext'])

    def test_dendrogram_orientation(self):
        X = np.random.rand(5, 5)

        dendro_left = ff.create_dendrogram(X, orientation='left')
        self.assertEqual(len(dendro_left['layout']['yaxis']['ticktext']), 5)
        tickvals_left = np.array(dendro_left['layout']['yaxis']['tickvals'])
        self.assertTrue((tickvals_left <= 0).all())

        dendro_right = ff.create_dendrogram(X, orientation='right')
        tickvals_right = np.array(dendro_right['layout']['yaxis']['tickvals'])
        self.assertTrue((tickvals_right >= 0).all())

        dendro_bottom = ff.create_dendrogram(X, orientation='bottom')
        self.assertEqual(len(dendro_bottom['layout']['xaxis']['ticktext']), 5)
        tickvals_bottom = np.array(
            dendro_bottom['layout']['xaxis']['tickvals']
        )
        self.assertTrue((tickvals_bottom >= 0).all())

        dendro_top = ff.create_dendrogram(X, orientation='top')
        tickvals_top = np.array(dendro_top['layout']['xaxis']['tickvals'])
        self.assertTrue((tickvals_top <= 0).all())

    def test_dendrogram_colorscale(self):
        X = np.array([[1, 2, 3, 4],
                      [1, 1, 3, 4],
                      [1, 2, 1, 4],
                      [1, 2, 3, 1]])
        greyscale = [
            'rgb(0,0,0)',  # black
            'rgb(05,105,105)',  # dim grey
            'rgb(128,128,128)',  # grey
            'rgb(169,169,169)',  # dark grey
            'rgb(192,192,192)',  # silver
            'rgb(211,211,211)',  # light grey
            'rgb(220,220,220)',  # gainsboro
            'rgb(245,245,245)'  # white smoke
        ]

        dendro = ff.create_dendrogram(X, colorscale=greyscale)

        expected_dendro = go.Figure(
            data=[
                go.Scatter(
                    x=np.array([25., 25., 35., 35.]),
                    y=np.array([0., 1., 1., 0.]),
                    marker=go.scatter.Marker(color='rgb(128,128,128)'),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                ),
                go.Scatter(
                    x=np.array([15., 15., 30., 30.]),
                    y=np.array([0., 2.23606798, 2.23606798, 1.]),
                    marker=go.scatter.Marker(color='rgb(128,128,128)'),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                ),
                go.Scatter(
                    x=np.array([5., 5., 22.5, 22.5]),
                    y=np.array([0., 3.60555128, 3.60555128, 2.23606798]),
                    marker=go.scatter.Marker(color='rgb(0,0,0)'),
                    mode='lines',
                    xaxis='x',
                    yaxis='y',
                    hoverinfo='text',
                    text=None
                )
            ],
            layout=go.Layout(
                autosize=False,
                height=np.inf,
                hovermode='closest',
                showlegend=False,
                width=np.inf,
                xaxis=go.layout.XAxis(
                    mirror='allticks',
                    rangemode='tozero',
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    tickmode='array',
                    ticks='outside',
                    ticktext=np.array(['3', '2', '0', '1']),
                    tickvals=[5.0, 15.0, 25.0, 35.0],
                    type='linear',
                    zeroline=False
                ),
                yaxis=go.layout.YAxis(
                    mirror='allticks',
                    rangemode='tozero',
                    showgrid=False,
                    showline=True,
                    showticklabels=True,
                    ticks='outside',
                    type='linear',
                    zeroline=False
                )
            )
        )

        self.assertEqual(len(dendro['data']), 3)

        # this is actually a bit clearer when debugging tests.
        self.assert_fig_equal(dendro['data'][0], expected_dendro['data'][0])
        self.assert_fig_equal(dendro['data'][1], expected_dendro['data'][1])
        self.assert_fig_equal(dendro['data'][2], expected_dendro['data'][2])

    def test_dendrogram_ticklabels(self):
        X = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 3, 5, 6], [1, 4, 2, 3]])
        dendro = ff.create_dendrogram(X=X)

        expected_ticktext = ['2', '3', '0', '1']
        expected_tickvals = [5, 15, 25, 35]

        self.assertEqual(len(dendro.layout.xaxis.ticktext), 4)
        self.assertEqual(len(dendro.layout.xaxis.tickvals), 4)

class TestTrisurf(NumpyTestUtilsMixin, TestCase):

    def test_vmin_and_vmax(self):

        # check if vmin is greater than or equal to vmax
        u = np.linspace(0, 2, 2)
        v = np.linspace(0, 2, 2)
        u, v = np.meshgrid(u, v)
        u = u.flatten()
        v = v.flatten()

        x = u
        y = v
        z = u*v

        points2D = np.vstack([u, v]).T
        tri = Delaunay(points2D)
        simplices = tri.simplices

        pattern = (
            "Incorrect relation between vmin and vmax. The vmin value cannot "
            "be bigger than or equal to the value of vmax."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_trisurf,
                                x, y, z, simplices)

    def test_valid_colormap(self):

        # create data for trisurf plot
        u = np.linspace(-np.pi, np.pi, 3)
        v = np.linspace(-np.pi, np.pi, 3)
        u, v = np.meshgrid(u, v)
        u = u.flatten()
        v = v.flatten()

        x = u
        y = u*np.cos(v)
        z = u*np.sin(v)

        points2D = np.vstack([u, v]).T
        tri = Delaunay(points2D)
        simplices = tri.simplices

        # check that a valid plotly colorscale string is entered

        pattern = (
            "If your colors variable is a string, it must be a Plotly scale, "
            "an rgb color or a hex color."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_trisurf,
                                x, y, z, simplices, colormap='foo')

        # check: if colormap is a list of rgb color strings, make sure the
        # entries of each color are no greater than 255.0

        pattern2 = (
            "Whoops! The elements in your rgb colors tuples "
            "cannot exceed 255.0."
        )

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_trisurf,
                                x, y, z, simplices,
                                colormap=['rgb(4, 5, 600)'])

        # check: if colormap is a list of tuple colors, make sure the entries
        # of each tuple are no greater than 1.0

        pattern3 = (
            "Whoops! The elements in your colors tuples cannot exceed 1.0."
        )

        self.assertRaisesRegexp(PlotlyError, pattern3,
                                ff.create_trisurf,
                                x, y, z, simplices,
                                colormap=[(0.8, 1.0, 1.2)])

    def test_trisurf_all_args(self):

        # check if trisurf plot matches with expected output
        u = np.linspace(-1, 1, 3)
        v = np.linspace(-1, 1, 3)
        u, v = np.meshgrid(u, v)
        u = u.flatten()
        v = v.flatten()

        x = u
        y = v
        z = u*v

        points2D = np.vstack([u, v]).T
        tri = Delaunay(points2D)
        simplices = tri.simplices

        test_trisurf_plot = ff.create_trisurf(
            x, y, z, simplices
        )

        exp_trisurf_plot = {
            'data': [{'facecolor': ['rgb(143, 123, 97)', 'rgb(255, 127, 14)',
                                    'rgb(143, 123, 97)', 'rgb(31, 119, 180)',
                                    'rgb(143, 123, 97)', 'rgb(31, 119, 180)',
                                    'rgb(143, 123, 97)', 'rgb(255, 127, 14)'],
                     'i': [3, 1, 1, 5, 7, 3, 5, 7],
                     'j': [1, 3, 5, 1, 3, 7, 7, 5],
                     'k': [4, 0, 4, 2, 4, 6, 4, 8],
                     'name': '',
                     'type': 'mesh3d',
                     'x': [-1.,  0.,  1., -1.,  0.,  1., -1.,  0.,  1.],
                     'y': [-1., -1., -1.,  0.,  0.,  0.,  1.,  1.,  1.],
                     'z': [1., -0., -1., -0.,  0.,  0., -1.,  0.,  1.]},
                     {'line': {'color': 'rgb(50, 50, 50)', 'width': 1.5},
                      'mode': 'lines',
                      'showlegend': False,
                      'type': 'scatter3d',
                      'x': [-1.0, 0.0, 0.0, -1.0, None, 0.0, -1.0, -1.0, 0.0,
                            None, 0.0, 1.0, 0.0, 0.0, None, 1.0, 0.0, 1.0,
                            1.0, None, 0.0, -1.0, 0.0, 0.0, None, -1.0, 0.0,
                            -1.0, -1.0, None, 1.0, 0.0, 0.0, 1.0, None, 0.0,
                            1.0, 1.0, 0.0, None],
                      'y': [0.0, -1.0, 0.0, 0.0, None, -1.0, 0.0, -1.0, -1.0,
                            None, -1.0, 0.0, 0.0, -1.0, None, 0.0, -1.0, -1.0,
                            0.0, None, 1.0, 0.0, 0.0, 1.0, None, 0.0, 1.0,
                            1.0, 0.0, None, 0.0, 1.0, 0.0, 0.0, None, 1.0,
                            0.0, 1.0, 1.0, None],
                      'z': [-0.0, -0.0, 0.0, -0.0, None, -0.0, -0.0, 1.0,
                            -0.0, None, -0.0, 0.0, 0.0, -0.0, None, 0.0, -0.0,
                            -1.0, 0.0, None, 0.0, -0.0, 0.0, 0.0, None, -0.0,
                            0.0, -1.0, -0.0, None, 0.0, 0.0, 0.0, 0.0, None,
                            0.0, 0.0, 1.0, 0.0, None]},
                     {'hoverinfo': 'none',
                      'marker': {'color': [-0.33333333333333331,
                                           0.33333333333333331],
                                 'colorscale': [[0.0, 'rgb(31, 119, 180)'],
                                                [1.0, 'rgb(255, 127, 14)']],
                                 'showscale': True,
                                 'size': 0.1},
                      'mode': 'markers',
                      'showlegend': False,
                      'type': 'scatter3d',
                      'x': [-1.],
                      'y': [-1.],
                      'z': [1.]}],
            'layout': {'height': 800,
                       'scene': {'aspectratio': {'x': 1, 'y': 1, 'z': 1},
                                 'xaxis': {'backgroundcolor': 'rgb(230, 230, 230)',
                                           'gridcolor': 'rgb(255, 255, 255)',
                                           'showbackground': True,
                                           'zerolinecolor': 'rgb(255, 255, 255)'},
                                 'yaxis': {'backgroundcolor': 'rgb(230, 230, 230)',
                                           'gridcolor': 'rgb(255, 255, 255)',
                                           'showbackground': True,
                                           'zerolinecolor': 'rgb(255, 255, 255)'},
                                 'zaxis': {'backgroundcolor': 'rgb(230, 230, 230)',
                                           'gridcolor': 'rgb(255, 255, 255)',
                                           'showbackground': True,
                                           'zerolinecolor': 'rgb(255, 255, 255)'}},
                       'title': 'Trisurf Plot',
                       'width': 800}
        }

        self.assert_fig_equal(test_trisurf_plot['data'][0],
                               exp_trisurf_plot['data'][0])

        self.assert_fig_equal(test_trisurf_plot['data'][1],
                               exp_trisurf_plot['data'][1])

        self.assert_fig_equal(test_trisurf_plot['data'][2],
                              exp_trisurf_plot['data'][2])

        self.assert_fig_equal(test_trisurf_plot['layout'],
                              exp_trisurf_plot['layout'])

        # Test passing custom colors
        colors_raw = np.random.randn(simplices.shape[0])
        colors_str = ['rgb(%s, %s, %s)' % (i, j, k)
                      for i, j, k in np.random.randn(simplices.shape[0], 3)]

        # Color == strings should be kept the same
        test_colors_plot = ff.create_trisurf(
            x, y, z, simplices, color_func=colors_str
        )
        self.assertListEqual(list(test_colors_plot['data'][0]['facecolor']),
                             list(colors_str))
        # Colors must match length of simplices
        colors_bad = colors_str[:-1]
        self.assertRaises(ValueError, ff.create_trisurf, x, y,
                          z, simplices, color_func=colors_bad)
        # Check converting custom colors to strings
        test_colors_plot = ff.create_trisurf(
            x, y, z, simplices, color_func=colors_raw
        )
        self.assertTrue(isinstance(test_colors_plot['data'][0]['facecolor'][0],
                                   str))


class TestScatterPlotMatrix(NumpyTestUtilsMixin, TestCase):

    def test_dataframe_input(self):

        # check: dataframe is imported
        df = 'foo'

        pattern = (
            "Dataframe not inputed. Please use a pandas dataframe to produce "
            "a scatterplot matrix."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df)

    def test_one_column_dataframe(self):

        # check: dataframe has 1 column or less
        df = pd.DataFrame([1, 2, 3])

        pattern = (
            "Dataframe has only one column. To use the scatterplot matrix, "
            "use at least 2 columns."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df)

    def test_valid_diag_choice(self):

        # make sure that the diagonal param is valid
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])

        self.assertRaises(PlotlyError,
                          ff.create_scatterplotmatrix,
                          df, diag='foo')

    def test_forbidden_params(self):

        # check: the forbidden params of 'marker' in **kwargs
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])

        kwargs = {'marker': {'size': 15}}

        pattern = (
            "Your kwargs dictionary cannot include the 'size', 'color' or "
            "'colorscale' key words inside the marker dict since 'size' is "
            "already an argument of the scatterplot matrix function and both "
            "'color' and 'colorscale are set internally."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df, **kwargs)

    def test_valid_index_choice(self):

        # check: index is a column name
        df = pd.DataFrame([[1, 2], [3, 4]], columns=['apple', 'pear'])

        pattern = (
            "Make sure you set the index input variable to one of the column "
            "names of your dataframe."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df, index='grape')

    def test_same_data_in_dataframe_columns(self):

        # check: either all numbers or strings in each dataframe column
        df = pd.DataFrame([['a', 2], [3, 4]])

        pattern = (
            "Error in dataframe. Make sure all entries of each column are "
            "either numbers or strings."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df)

        df = pd.DataFrame([[1, 2], ['a', 4]])

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df)

    def test_same_data_in_index(self):

        # check: either all numbers or strings in index column
        df = pd.DataFrame([['a', 2], [3, 4]], columns=['apple', 'pear'])

        pattern = (
            "Error in indexing column. Make sure all entries of each column "
            "are all numbers or all strings."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df, index='apple')

        df = pd.DataFrame([[1, 2], ['a', 4]], columns=['apple', 'pear'])

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df, index='apple')

    def test_valid_colormap(self):

        # check: the colormap argument is in a valid form
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                          columns=['a', 'b', 'c'])

        # check: valid plotly scalename is entered
        self.assertRaises(PlotlyError,
                          ff.create_scatterplotmatrix,
                          df, index='a', colormap='fake_scale')

        pattern_rgb = (
            "Whoops! The elements in your rgb colors tuples cannot "
            "exceed 255.0."
        )

        # check: proper 'rgb' color
        self.assertRaisesRegexp(PlotlyError, pattern_rgb,
                                ff.create_scatterplotmatrix,
                                df, colormap='rgb(500, 1, 1)', index='c')

        self.assertRaisesRegexp(PlotlyError, pattern_rgb,
                                ff.create_scatterplotmatrix,
                                df, colormap=['rgb(500, 1, 1)'], index='c')

        pattern_tuple = (
            "Whoops! The elements in your colors tuples cannot "
            "exceed 1.0."
        )

        # check: proper color tuple
        self.assertRaisesRegexp(PlotlyError, pattern_tuple,
                                ff.create_scatterplotmatrix,
                                df, colormap=(2, 1, 1), index='c')

        self.assertRaisesRegexp(PlotlyError, pattern_tuple,
                                ff.create_scatterplotmatrix,
                                df, colormap=[(2, 1, 1)], index='c')

    def test_valid_endpts(self):

        # check: the endpts is a list or a tuple
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                          columns=['a', 'b', 'c'])

        pattern = (
            "The intervals_endpts argument must be a list or tuple of a "
            "sequence of increasing numbers."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df, index='a', colormap='Hot', endpts='foo')

        # check: the endpts are a list of numbers
        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df, index='a', colormap='Hot', endpts=['a'])

        # check: endpts is a list of INCREASING numbers
        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df, index='a', colormap='Hot', endpts=[2, 1])

    def test_dictionary_colormap(self):

        # if colormap is a dictionary, make sure it all the values in the
        # index column are keys in colormap
        df = pd.DataFrame([['apple', 'happy'], ['pear', 'sad']],
                          columns=['Fruit', 'Emotion'])

        colormap = {'happy': 'rgb(5, 5, 5)'}

        pattern = (
            "If colormap is a dictionary, all the names in the index "
            "must be keys."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_scatterplotmatrix,
                                df, index='Emotion', colormap=colormap)

    def test_scatter_plot_matrix(self):

        # check if test scatter plot matrix without index or theme matches
        # with the expected output
        df = pd.DataFrame([[2, 'Apple'], [6, 'Pear'],
                          [-15, 'Apple'], [5, 'Pear'],
                          [-2, 'Apple'], [0, 'Apple']],
                          columns=['Numbers', 'Fruit'])

        test_scatter_plot_matrix = ff.create_scatterplotmatrix(
            df=df, diag='box', height=1000, width=1000, size=13,
            title='Scatterplot Matrix'
        )

        exp_scatter_plot_matrix = {
            'data': [{'showlegend': False,
                      'type': 'box',
                      'xaxis': 'x',
                      'y': [2, 6, -15, 5, -2, 0],
                      'yaxis': 'y'},
                     {'marker': {'size': 13},
                      'mode': 'markers',
                      'showlegend': False,
                      'type': 'scatter',
                      'x': ['Apple', 'Pear', 'Apple',
                            'Pear', 'Apple', 'Apple'],
                      'xaxis': 'x2',
                      'y': [2, 6, -15, 5, -2, 0],
                      'yaxis': 'y2'},
                     {'marker': {'size': 13},
                      'mode': 'markers',
                      'showlegend': False,
                      'type': 'scatter',
                      'x': [2, 6, -15, 5, -2, 0],
                      'xaxis': 'x3',
                      'y': ['Apple', 'Pear', 'Apple',
                            'Pear', 'Apple', 'Apple'],
                      'yaxis': 'y3'},
                     {'name': None,
                      'showlegend': False,
                      'type': 'box',
                      'xaxis': 'x4',
                      'y': ['Apple', 'Pear', 'Apple',
                            'Pear', 'Apple', 'Apple'],
                      'yaxis': 'y4'}],
            'layout': {'height': 1000,
                       'showlegend': True,
                       'title': 'Scatterplot Matrix',
                       'width': 1000,
                       'xaxis': {'anchor': 'y',
                                  'domain': [0.0, 0.45],
                                  'showticklabels': False},
                       'xaxis2': {'anchor': 'y2',
                                  'domain': [0.55, 1.0]},
                       'xaxis3': {'anchor': 'y3',
                                  'domain': [0.0, 0.45],
                                  'title': 'Numbers'},
                       'xaxis4': {'anchor': 'y4',
                                  'domain': [0.55, 1.0],
                                  'showticklabels': False,
                                  'title': 'Fruit'},
                       'yaxis': {'anchor': 'x',
                                  'domain': [0.575, 1.0],
                                  'title': 'Numbers'},
                       'yaxis2': {'anchor': 'x2',
                                  'domain': [0.575, 1.0]},
                       'yaxis3': {'anchor': 'x3',
                                  'domain': [0.0, 0.425],
                                  'title': 'Fruit'},
                       'yaxis4': {'anchor': 'x4',
                                  'domain': [0.0, 0.425]}}
        }

        self.assert_fig_equal(test_scatter_plot_matrix['data'][0],
                              exp_scatter_plot_matrix['data'][0])

        self.assert_fig_equal(test_scatter_plot_matrix['data'][1],
                              exp_scatter_plot_matrix['data'][1])

        self.assert_fig_equal(test_scatter_plot_matrix['layout'],
                              exp_scatter_plot_matrix['layout'])

    def test_scatter_plot_matrix_kwargs(self):

        # check if test scatter plot matrix matches with
        # the expected output
        df = pd.DataFrame([[2, 'Apple'], [6, 'Pear'],
                          [-15, 'Apple'], [5, 'Pear'],
                          [-2, 'Apple'], [0, 'Apple']],
                          columns=['Numbers', 'Fruit'])

        test_scatter_plot_matrix = ff.create_scatterplotmatrix(
            df, index='Fruit', endpts=[-10, -1], diag='histogram',
            height=1000, width=1000, size=13, title='Scatterplot Matrix',
            colormap='YlOrRd', marker=dict(symbol=136)
        )

        exp_scatter_plot_matrix = {
            'data': [{'marker': {'color': 'rgb(128, 0, 38)'},
                      'showlegend': False,
                      'type': 'histogram',
                      'x': [2, -15, -2, 0],
                      'xaxis': 'x',
                      'yaxis': 'y'},
                     {'marker': {'color': 'rgb(255, 255, 204)'},
                      'showlegend': False,
                      'type': 'histogram',
                      'x': [6, 5],
                      'xaxis': 'x',
                      'yaxis': 'y'}],
            'layout': {'barmode': 'stack',
                       'height': 1000,
                       'showlegend': True,
                       'title': 'Scatterplot Matrix',
                       'width': 1000,
                       'xaxis': {'anchor': 'y',
                                  'domain': [0.0, 1.0],
                                  'title': 'Numbers'},
                       'yaxis': {'anchor': 'x',
                                  'domain': [0.0, 1.0],
                                  'title': 'Numbers'}}
        }

        self.assert_fig_equal(test_scatter_plot_matrix['data'][0],
                              exp_scatter_plot_matrix['data'][0])

        self.assert_fig_equal(test_scatter_plot_matrix['data'][1],
                               exp_scatter_plot_matrix['data'][1])

        self.assert_fig_equal(test_scatter_plot_matrix['layout'],
                               exp_scatter_plot_matrix['layout'])


class TestGantt(NumpyTestUtilsMixin, TestCase):

    def test_df_dataframe(self):

        # validate dataframe has correct column names
        df1 = pd.DataFrame([[2, 'Apple']], columns=['Numbers', 'Fruit'])
        self.assertRaises(PlotlyError, ff.create_gantt, df1)

    def test_df_dataframe_all_args(self):

        # check if gantt chart matches with expected output

        df = pd.DataFrame([['Job A', '2009-01-01', '2009-02-30'],
                           ['Job B', '2009-03-05', '2009-04-15']],
                          columns=['Task', 'Start', 'Finish'])

        test_gantt_chart = ff.create_gantt(df)

        exp_gantt_chart = {'data': [{'marker': {'color': 'white'},
                                     'name': '',
                                     'type': 'scatter',
                                     'x': ['2009-01-01', '2009-02-30'],
                                     'y': [0, 0]},
                                    {'marker': {'color': 'white'},
                                    'name': '',
                                    'type': 'scatter',
                                    'x': ['2009-03-05', '2009-04-15'],
                                    'y': [1, 1]}],
                            'layout': {'height': 600,
                                       'hovermode': 'closest',
                                       'shapes': [{'fillcolor': 'rgb(31, 119, 180)',
                                                   'line': {'width': 0},
                                                   'opacity': 1,
                                                   'type': 'rect',
                                                   'x0': '2009-01-01',
                                                   'x1': '2009-02-30',
                                                   'xref': 'x',
                                                   'y0': -0.2,
                                                   'y1': 0.2,
                                                   'yref': 'y'},
                                                  {'fillcolor': 'rgb(255, 127, 14)',
                                                   'line': {'width': 0},
                                                   'opacity': 1,
                                                   'type': 'rect',
                                                   'x0': '2009-03-05',
                                                   'x1': '2009-04-15',
                                                   'xref': 'x',
                                                   'y0': 0.8,
                                                   'y1': 1.2,
                                                   'yref': 'y'}],
                                       'showlegend': False,
                                       'title': 'Gantt Chart',
                                       'width': 900,
                                       'xaxis': {'rangeselector': {'buttons': [{'count': 7,
                                       'label': '1w',
                                       'step': 'day',
                                       'stepmode': 'backward'},
                                       {'count': 1,
                                        'label': '1m',
                                        'step': 'month',
                                        'stepmode': 'backward'},
                                       {'count': 6,
                                        'label': '6m',
                                        'step': 'month',
                                        'stepmode': 'backward'},
                                       {'count': 1,
                                        'label': 'YTD',
                                        'step': 'year',
                                        'stepmode': 'todate'},
                                       {'count': 1,
                                        'label': '1y',
                                        'step': 'year',
                                        'stepmode': 'backward'},
                                       {'step': 'all'}]},
                                       'showgrid': False,
                                       'type': 'date',
                                       'zeroline': False},
                                       'yaxis': {'autorange': False,
                                       'range': [-1, 3],
                                       'showgrid': False,
                                       'ticktext': ['Job A', 'Job B'],
                                       'tickvals': [0, 1],
                                       'zeroline': False}}}

        self.assert_fig_equal(test_gantt_chart['data'][0],
                              exp_gantt_chart['data'][0])

        self.assert_fig_equal(test_gantt_chart['layout'],
                               exp_gantt_chart['layout'])


class TestViolin(NumpyTestUtilsMixin, TestCase):

    def test_colors_validation(self):

        # check: colors is in an acceptable form

        data = [1, 5, 8]

        pattern = ("Whoops! The elements in your rgb colors tuples cannot "
                   "exceed 255.0.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_violin,
                                data, colors='rgb(300, 2, 3)')

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_violin,
                                data, colors=['rgb(300, 2, 3)'])

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_violin,
                                data, colors={'apple': 'rgb(300, 2, 3)'})

        pattern2 = ("Whoops! The elements in your colors tuples cannot "
                    "exceed 1.0.")

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_violin,
                                data, colors=(1.1, 1, 1))

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_violin,
                                data, colors=[(1.1, 1, 1)])

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_violin,
                                data, colors={'apple': (1.1, 1, 1)})

        # check: if valid string color is inputted
        self.assertRaises(PlotlyError, ff.create_violin,
                          data, colors='foo')

    def test_data_header(self):

        # make sure data_header is entered

        data = pd.DataFrame([['apple', 2], ['pear', 4]],
                            columns=['a', 'b'])

        pattern = ("data_header must be the column name with the desired "
                   "numeric data for the violin plot.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_violin, data,
                                group_header='a', colors=['rgb(1, 2, 3)'])

    def test_data_as_list(self):

        # check: data is a non empty list of numbers

        data = []

        pattern = ("If data is a list, it must be nonempty and contain "
                   "either numbers or dictionaries.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_violin,
                                data)

        data = [1, 'foo']

        pattern2 = ("If data is a list, it must contain only numbers.")

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_violin, data)

    def test_dataframe_input(self):

        # check: dataframe is entered if group_header is True

        data = [1, 2, 3]

        pattern = ("Error. You must use a pandas DataFrame if you are using "
                   "a group header.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_violin, data,
                                group_header=True)

    def test_colors_dict(self):

        # check: if colorscale is True, make sure colors is not a dictionary

        data = pd.DataFrame([['apple', 2], ['pear', 4]],
                            columns=['a', 'b'])

        pattern = ("The colors param cannot be a dictionary if you are "
                   "using a colorscale.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_violin, data,
                                data_header='b', group_header='a',
                                use_colorscale=True,
                                colors={'a': 'rgb(1, 2, 3)'})

        # check: colors contains all group names as keys

        pattern2 = ("If colors is a dictionary, all the group names must "
                    "appear as keys in colors.")

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_violin, data,
                                data_header='b', group_header='a',
                                use_colorscale=False,
                                colors={'a': 'rgb(1, 2, 3)'})

    def test_valid_colorscale(self):

        # check: if colorscale is enabled, colors is a list with 2+ items

        data = pd.DataFrame([['apple', 2], ['pear', 4]],
                            columns=['a', 'b'])

        pattern = ("colors must be a list with at least 2 colors. A Plotly "
                   "scale is allowed.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_violin, data,
                                data_header='b', group_header='a',
                                use_colorscale=True,
                                colors='rgb(1, 2, 3)')

    def test_group_stats(self):

        # check: group_stats is a dictionary

        data = pd.DataFrame([['apple', 2], ['pear', 4]],
                            columns=['a', 'b'])

        pattern = ("Your group_stats param must be a dictionary.")

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_violin, data,
                                data_header='b', group_header='a',
                                use_colorscale=True,
                                colors=['rgb(1, 2, 3)', 'rgb(4, 5, 6)'],
                                group_stats=1)

        # check: all groups are represented as keys in group_stats

        pattern2 = ("All values/groups in the index column must be "
                    "represented as a key in group_stats.")

        self.assertRaisesRegexp(PlotlyError, pattern2,
                                ff.create_violin, data,
                                data_header='b', group_header='a',
                                use_colorscale=True,
                                colors=['rgb(1, 2, 3)', 'rgb(4, 5, 6)'],
                                group_stats={'apple': 1})

    def test_violin_fig(self):

        # check: test violin fig matches expected fig

        test_violin = ff.create_violin(data=[1, 2])

        exp_violin = {
            'data': [{'fill': 'tonextx',
                     'fillcolor': 'rgb(31, 119, 180)',
                     'hoverinfo': 'text',
                     'line': {'color': 'rgb(0, 0, 0)',
                              'shape': 'spline',
                              'width': 0.5},
                     'mode': 'lines',
                     'name': '',
                     'opacity': 0.5,
                     'text': ['(pdf(y), y)=(-0.41, 1.00)',
                              '(pdf(y), y)=(-0.41, 1.01)',
                              '(pdf(y), y)=(-0.42, 1.02)',
                              '(pdf(y), y)=(-0.42, 1.03)',
                              '(pdf(y), y)=(-0.42, 1.04)',
                              '(pdf(y), y)=(-0.42, 1.05)',
                              '(pdf(y), y)=(-0.42, 1.06)',
                              '(pdf(y), y)=(-0.43, 1.07)',
                              '(pdf(y), y)=(-0.43, 1.08)',
                              '(pdf(y), y)=(-0.43, 1.09)',
                              '(pdf(y), y)=(-0.43, 1.10)',
                              '(pdf(y), y)=(-0.43, 1.11)',
                              '(pdf(y), y)=(-0.43, 1.12)',
                              '(pdf(y), y)=(-0.44, 1.13)',
                              '(pdf(y), y)=(-0.44, 1.14)',
                              '(pdf(y), y)=(-0.44, 1.15)',
                              '(pdf(y), y)=(-0.44, 1.16)',
                              '(pdf(y), y)=(-0.44, 1.17)',
                              '(pdf(y), y)=(-0.44, 1.18)',
                              '(pdf(y), y)=(-0.45, 1.19)',
                              '(pdf(y), y)=(-0.45, 1.20)',
                              '(pdf(y), y)=(-0.45, 1.21)',
                              '(pdf(y), y)=(-0.45, 1.22)',
                              '(pdf(y), y)=(-0.45, 1.23)',
                              '(pdf(y), y)=(-0.45, 1.24)',
                              '(pdf(y), y)=(-0.45, 1.25)',
                              '(pdf(y), y)=(-0.45, 1.26)',
                              '(pdf(y), y)=(-0.45, 1.27)',
                              '(pdf(y), y)=(-0.46, 1.28)',
                              '(pdf(y), y)=(-0.46, 1.29)',
                              '(pdf(y), y)=(-0.46, 1.30)',
                              '(pdf(y), y)=(-0.46, 1.31)',
                              '(pdf(y), y)=(-0.46, 1.32)',
                              '(pdf(y), y)=(-0.46, 1.33)',
                              '(pdf(y), y)=(-0.46, 1.34)',
                              '(pdf(y), y)=(-0.46, 1.35)',
                              '(pdf(y), y)=(-0.46, 1.36)',
                              '(pdf(y), y)=(-0.46, 1.37)',
                              '(pdf(y), y)=(-0.46, 1.38)',
                              '(pdf(y), y)=(-0.46, 1.39)',
                              '(pdf(y), y)=(-0.46, 1.40)',
                              '(pdf(y), y)=(-0.46, 1.41)',
                              '(pdf(y), y)=(-0.46, 1.42)',
                              '(pdf(y), y)=(-0.47, 1.43)',
                              '(pdf(y), y)=(-0.47, 1.44)',
                              '(pdf(y), y)=(-0.47, 1.45)',
                              '(pdf(y), y)=(-0.47, 1.46)',
                              '(pdf(y), y)=(-0.47, 1.47)',
                              '(pdf(y), y)=(-0.47, 1.48)',
                              '(pdf(y), y)=(-0.47, 1.49)',
                              '(pdf(y), y)=(-0.47, 1.51)',
                              '(pdf(y), y)=(-0.47, 1.52)',
                              '(pdf(y), y)=(-0.47, 1.53)',
                              '(pdf(y), y)=(-0.47, 1.54)',
                              '(pdf(y), y)=(-0.47, 1.55)',
                              '(pdf(y), y)=(-0.47, 1.56)',
                              '(pdf(y), y)=(-0.47, 1.57)',
                              '(pdf(y), y)=(-0.46, 1.58)',
                              '(pdf(y), y)=(-0.46, 1.59)',
                              '(pdf(y), y)=(-0.46, 1.60)',
                              '(pdf(y), y)=(-0.46, 1.61)',
                              '(pdf(y), y)=(-0.46, 1.62)',
                              '(pdf(y), y)=(-0.46, 1.63)',
                              '(pdf(y), y)=(-0.46, 1.64)',
                              '(pdf(y), y)=(-0.46, 1.65)',
                              '(pdf(y), y)=(-0.46, 1.66)',
                              '(pdf(y), y)=(-0.46, 1.67)',
                              '(pdf(y), y)=(-0.46, 1.68)',
                              '(pdf(y), y)=(-0.46, 1.69)',
                              '(pdf(y), y)=(-0.46, 1.70)',
                              '(pdf(y), y)=(-0.46, 1.71)',
                              '(pdf(y), y)=(-0.46, 1.72)',
                              '(pdf(y), y)=(-0.45, 1.73)',
                              '(pdf(y), y)=(-0.45, 1.74)',
                              '(pdf(y), y)=(-0.45, 1.75)',
                              '(pdf(y), y)=(-0.45, 1.76)',
                              '(pdf(y), y)=(-0.45, 1.77)',
                              '(pdf(y), y)=(-0.45, 1.78)',
                              '(pdf(y), y)=(-0.45, 1.79)',
                              '(pdf(y), y)=(-0.45, 1.80)',
                              '(pdf(y), y)=(-0.45, 1.81)',
                              '(pdf(y), y)=(-0.44, 1.82)',
                              '(pdf(y), y)=(-0.44, 1.83)',
                              '(pdf(y), y)=(-0.44, 1.84)',
                              '(pdf(y), y)=(-0.44, 1.85)',
                              '(pdf(y), y)=(-0.44, 1.86)',
                              '(pdf(y), y)=(-0.44, 1.87)',
                              '(pdf(y), y)=(-0.43, 1.88)',
                              '(pdf(y), y)=(-0.43, 1.89)',
                              '(pdf(y), y)=(-0.43, 1.90)',
                              '(pdf(y), y)=(-0.43, 1.91)',
                              '(pdf(y), y)=(-0.43, 1.92)',
                              '(pdf(y), y)=(-0.43, 1.93)',
                              '(pdf(y), y)=(-0.42, 1.94)',
                              '(pdf(y), y)=(-0.42, 1.95)',
                              '(pdf(y), y)=(-0.42, 1.96)',
                              '(pdf(y), y)=(-0.42, 1.97)',
                              '(pdf(y), y)=(-0.42, 1.98)',
                              '(pdf(y), y)=(-0.41, 1.99)',
                              '(pdf(y), y)=(-0.41, 2.00)'],
                      'type': 'scatter',
                      'x': np.array([-0.41064744, -0.41293151, -0.41516635,
                                     -0.41735177, -0.41948764, -0.42157385,
                                     -0.42361031, -0.42559697, -0.42753381,
                                     -0.42942082, -0.43125804, -0.43304552,
                                     -0.43478334, -0.4364716, -0.4381104,
                                     -0.4396999, -0.44124025, -0.44273162,
                                     -0.4441742, -0.4455682, -0.44691382,
                                     -0.44821129, -0.44946086, -0.45066275,
                                     -0.45181723, -0.45292454, -0.45398495,
                                     -0.45499871, -0.45596609, -0.45688735,
                                     -0.45776275, -0.45859254, -0.45937698,
                                     -0.46011631, -0.46081078, -0.46146061,
                                     -0.46206603, -0.46262726, -0.46314449,
                                     -0.46361791, -0.4640477, -0.46443404,
                                     -0.46477705, -0.46507689, -0.46533367,
                                     -0.46554749, -0.46571845, -0.4658466,
                                     -0.46593201, -0.4659747, -0.4659747,
                                     -0.46593201, -0.4658466, -0.46571845,
                                     -0.46554749, -0.46533367, -0.46507689,
                                     -0.46477705, -0.46443404, -0.4640477,
                                     -0.46361791, -0.46314449, -0.46262726,
                                     -0.46206603, -0.46146061, -0.46081078,
                                     -0.46011631, -0.45937698, -0.45859254,
                                     -0.45776275, -0.45688735, -0.45596609,
                                     -0.45499871, -0.45398495, -0.45292454,
                                     -0.45181723, -0.45066275, -0.44946086,
                                     -0.44821129, -0.44691382, -0.4455682,
                                     -0.4441742, -0.44273162, -0.44124025,
                                     -0.4396999, -0.4381104, -0.4364716,
                                     -0.43478334, -0.43304552, -0.43125804,
                                     -0.42942082, -0.42753381, -0.42559697,
                                     -0.42361031, -0.42157385, -0.41948764,
                                     -0.41735177, -0.41516635, -0.41293151,
                                     -0.41064744]),
                      'y': np.array([1.,           1.01010101,  1.02020202,
                                     1.03030303,  1.04040404, 1.05050505,
                                     1.06060606,  1.07070707,  1.08080808,
                                     1.09090909, 1.1010101,  1.11111111,
                                     1.12121212,  1.13131313,  1.14141414,
                                     1.15151515,  1.16161616,  1.17171717,
                                     1.18181818,  1.19191919, 1.2020202,
                                     1.21212121,  1.22222222,  1.23232323,
                                     1.24242424, 1.25252525,  1.26262626,
                                     1.27272727,  1.28282828,  1.29292929,
                                     1.3030303,  1.31313131,  1.32323232,
                                     1.33333333,  1.34343434, 1.35353535,
                                     1.36363636,  1.37373737,  1.38383838,
                                     1.39393939, 1.4040404,  1.41414141,
                                     1.42424242,  1.43434343,  1.44444444,
                                     1.45454545,  1.46464646,  1.47474747,
                                     1.48484848,  1.49494949, 1.50505051,
                                     1.51515152,  1.52525253,  1.53535354,
                                     1.54545455, 1.55555556,  1.56565657,
                                     1.57575758,  1.58585859,  1.5959596,
                                     1.60606061,  1.61616162,  1.62626263,
                                     1.63636364,  1.64646465, 1.65656566,
                                     1.66666667,  1.67676768,  1.68686869,
                                     1.6969697, 1.70707071,  1.71717172,
                                     1.72727273,  1.73737374,  1.74747475,
                                     1.75757576,  1.76767677,  1.77777778,
                                     1.78787879,  1.7979798, 1.80808081,
                                     1.81818182,  1.82828283,  1.83838384,
                                     1.84848485, 1.85858586,  1.86868687,
                                     1.87878788,  1.88888889,  1.8989899,
                                     1.90909091,  1.91919192,  1.92929293,
                                     1.93939394,  1.94949495, 1.95959596,
                                     1.96969697,  1.97979798,  1.98989899,
                                     2.])},
                     {'fill': 'tonextx',
                      'fillcolor': 'rgb(31, 119, 180)',
                      'hoverinfo': 'text',
                      'line': {'color': 'rgb(0, 0, 0)',
                               'shape': 'spline',
                               'width': 0.5},
                      'mode': 'lines',
                      'name': '',
                      'opacity': 0.5,
                      'text': ['(pdf(y), y)=(0.41, 1.00)',
                               '(pdf(y), y)=(0.41, 1.01)',
                               '(pdf(y), y)=(0.42, 1.02)',
                               '(pdf(y), y)=(0.42, 1.03)',
                               '(pdf(y), y)=(0.42, 1.04)',
                               '(pdf(y), y)=(0.42, 1.05)',
                               '(pdf(y), y)=(0.42, 1.06)',
                               '(pdf(y), y)=(0.43, 1.07)',
                               '(pdf(y), y)=(0.43, 1.08)',
                               '(pdf(y), y)=(0.43, 1.09)',
                               '(pdf(y), y)=(0.43, 1.10)',
                               '(pdf(y), y)=(0.43, 1.11)',
                               '(pdf(y), y)=(0.43, 1.12)',
                               '(pdf(y), y)=(0.44, 1.13)',
                               '(pdf(y), y)=(0.44, 1.14)',
                               '(pdf(y), y)=(0.44, 1.15)',
                               '(pdf(y), y)=(0.44, 1.16)',
                               '(pdf(y), y)=(0.44, 1.17)',
                               '(pdf(y), y)=(0.44, 1.18)',
                               '(pdf(y), y)=(0.45, 1.19)',
                               '(pdf(y), y)=(0.45, 1.20)',
                               '(pdf(y), y)=(0.45, 1.21)',
                               '(pdf(y), y)=(0.45, 1.22)',
                               '(pdf(y), y)=(0.45, 1.23)',
                               '(pdf(y), y)=(0.45, 1.24)',
                               '(pdf(y), y)=(0.45, 1.25)',
                               '(pdf(y), y)=(0.45, 1.26)',
                               '(pdf(y), y)=(0.45, 1.27)',
                               '(pdf(y), y)=(0.46, 1.28)',
                               '(pdf(y), y)=(0.46, 1.29)',
                               '(pdf(y), y)=(0.46, 1.30)',
                               '(pdf(y), y)=(0.46, 1.31)',
                               '(pdf(y), y)=(0.46, 1.32)',
                               '(pdf(y), y)=(0.46, 1.33)',
                               '(pdf(y), y)=(0.46, 1.34)',
                               '(pdf(y), y)=(0.46, 1.35)',
                               '(pdf(y), y)=(0.46, 1.36)',
                               '(pdf(y), y)=(0.46, 1.37)',
                               '(pdf(y), y)=(0.46, 1.38)',
                               '(pdf(y), y)=(0.46, 1.39)',
                               '(pdf(y), y)=(0.46, 1.40)',
                               '(pdf(y), y)=(0.46, 1.41)',
                               '(pdf(y), y)=(0.46, 1.42)',
                               '(pdf(y), y)=(0.47, 1.43)',
                               '(pdf(y), y)=(0.47, 1.44)',
                               '(pdf(y), y)=(0.47, 1.45)',
                               '(pdf(y), y)=(0.47, 1.46)',
                               '(pdf(y), y)=(0.47, 1.47)',
                               '(pdf(y), y)=(0.47, 1.48)',
                               '(pdf(y), y)=(0.47, 1.49)',
                               '(pdf(y), y)=(0.47, 1.51)',
                               '(pdf(y), y)=(0.47, 1.52)',
                               '(pdf(y), y)=(0.47, 1.53)',
                               '(pdf(y), y)=(0.47, 1.54)',
                               '(pdf(y), y)=(0.47, 1.55)',
                               '(pdf(y), y)=(0.47, 1.56)',
                               '(pdf(y), y)=(0.47, 1.57)',
                               '(pdf(y), y)=(0.46, 1.58)',
                               '(pdf(y), y)=(0.46, 1.59)',
                               '(pdf(y), y)=(0.46, 1.60)',
                               '(pdf(y), y)=(0.46, 1.61)',
                               '(pdf(y), y)=(0.46, 1.62)',
                               '(pdf(y), y)=(0.46, 1.63)',
                               '(pdf(y), y)=(0.46, 1.64)',
                               '(pdf(y), y)=(0.46, 1.65)',
                               '(pdf(y), y)=(0.46, 1.66)',
                               '(pdf(y), y)=(0.46, 1.67)',
                               '(pdf(y), y)=(0.46, 1.68)',
                               '(pdf(y), y)=(0.46, 1.69)',
                               '(pdf(y), y)=(0.46, 1.70)',
                               '(pdf(y), y)=(0.46, 1.71)',
                               '(pdf(y), y)=(0.46, 1.72)',
                               '(pdf(y), y)=(0.45, 1.73)',
                               '(pdf(y), y)=(0.45, 1.74)',
                               '(pdf(y), y)=(0.45, 1.75)',
                               '(pdf(y), y)=(0.45, 1.76)',
                               '(pdf(y), y)=(0.45, 1.77)',
                               '(pdf(y), y)=(0.45, 1.78)',
                               '(pdf(y), y)=(0.45, 1.79)',
                               '(pdf(y), y)=(0.45, 1.80)',
                               '(pdf(y), y)=(0.45, 1.81)',
                               '(pdf(y), y)=(0.44, 1.82)',
                               '(pdf(y), y)=(0.44, 1.83)',
                               '(pdf(y), y)=(0.44, 1.84)',
                               '(pdf(y), y)=(0.44, 1.85)',
                               '(pdf(y), y)=(0.44, 1.86)',
                               '(pdf(y), y)=(0.44, 1.87)',
                               '(pdf(y), y)=(0.43, 1.88)',
                               '(pdf(y), y)=(0.43, 1.89)',
                               '(pdf(y), y)=(0.43, 1.90)',
                               '(pdf(y), y)=(0.43, 1.91)',
                               '(pdf(y), y)=(0.43, 1.92)',
                               '(pdf(y), y)=(0.43, 1.93)',
                               '(pdf(y), y)=(0.42, 1.94)',
                               '(pdf(y), y)=(0.42, 1.95)',
                               '(pdf(y), y)=(0.42, 1.96)',
                               '(pdf(y), y)=(0.42, 1.97)',
                               '(pdf(y), y)=(0.42, 1.98)',
                               '(pdf(y), y)=(0.41, 1.99)',
                               '(pdf(y), y)=(0.41, 2.00)'],
                      'type': 'scatter',
                      'x': np.array([0.41064744,  0.41293151,  0.41516635,
                                     0.41735177,  0.41948764, 0.42157385,
                                     0.42361031,  0.42559697,  0.42753381,
                                     0.42942082, 0.43125804,  0.43304552,
                                     0.43478334,  0.4364716,  0.4381104,
                                     0.4396999,  0.44124025,  0.44273162,
                                     0.4441742,  0.4455682, 0.44691382,
                                     0.44821129,  0.44946086,  0.45066275,
                                     0.45181723, 0.45292454,  0.45398495,
                                     0.45499871,  0.45596609,  0.45688735,
                                     0.45776275,  0.45859254,  0.45937698,
                                     0.46011631,  0.46081078, 0.46146061,
                                     0.46206603,  0.46262726,  0.46314449,
                                     0.46361791, 0.4640477,  0.46443404,
                                     0.46477705,  0.46507689,  0.46533367,
                                     0.46554749,  0.46571845,  0.4658466,
                                     0.46593201,  0.4659747, 0.4659747,
                                     0.46593201,  0.4658466,  0.46571845,
                                     0.46554749, 0.46533367,  0.46507689,
                                     0.46477705,  0.46443404,  0.4640477,
                                     0.46361791,  0.46314449,  0.46262726,
                                     0.46206603,  0.46146061, 0.46081078,
                                     0.46011631,  0.45937698,  0.45859254,
                                     0.45776275, 0.45688735,  0.45596609,
                                     0.45499871,  0.45398495,  0.45292454,
                                     0.45181723,  0.45066275,  0.44946086,
                                     0.44821129,  0.44691382, 0.4455682,
                                     0.4441742,  0.44273162,  0.44124025,
                                     0.4396999, 0.4381104,  0.4364716,
                                     0.43478334,  0.43304552,  0.43125804,
                                     0.42942082,  0.42753381,  0.42559697,
                                     0.42361031,  0.42157385, 0.41948764,
                                     0.41735177,  0.41516635,  0.41293151,
                                     0.41064744]),
                      'y': np.array([1.,          1.01010101,  1.02020202,
                                     1.03030303,  1.04040404, 1.05050505,
                                     1.06060606,  1.07070707,  1.08080808,
                                     1.09090909, 1.1010101,  1.11111111,
                                     1.12121212,  1.13131313,  1.14141414,
                                     1.15151515,  1.16161616,  1.17171717,
                                     1.18181818,  1.19191919, 1.2020202,
                                     1.21212121,  1.22222222,  1.23232323,
                                     1.24242424, 1.25252525,  1.26262626,
                                     1.27272727,  1.28282828,  1.29292929,
                                     1.3030303,  1.31313131,  1.32323232,
                                     1.33333333,  1.34343434, 1.35353535,
                                     1.36363636,  1.37373737,  1.38383838,
                                     1.39393939, 1.4040404,  1.41414141,
                                     1.42424242,  1.43434343,  1.44444444,
                                     1.45454545,  1.46464646,  1.47474747,
                                     1.48484848,  1.49494949, 1.50505051,
                                     1.51515152,  1.52525253,  1.53535354,
                                     1.54545455, 1.55555556,  1.56565657,
                                     1.57575758,  1.58585859,  1.5959596,
                                     1.60606061,  1.61616162,  1.62626263,
                                     1.63636364,  1.64646465, 1.65656566,
                                     1.66666667,  1.67676768,  1.68686869,
                                     1.6969697, 1.70707071,  1.71717172,
                                     1.72727273,  1.73737374,  1.74747475,
                                     1.75757576,  1.76767677,  1.77777778,
                                     1.78787879,  1.7979798, 1.80808081,
                                     1.81818182,  1.82828283,  1.83838384,
                                     1.84848485, 1.85858586,  1.86868687,
                                     1.87878788,  1.88888889,  1.8989899,
                                     1.90909091,  1.91919192,  1.92929293,
                                     1.93939394,  1.94949495, 1.95959596,
                                     1.96969697,  1.97979798,  1.98989899,
                                     2.])},
                     {'line': {'color': 'rgb(0, 0, 0)', 'width': 1.5},
                      'mode': 'lines',
                      'name': '',
                      'type': 'scatter',
                      'x': [0, 0],
                      'y': [1.0, 2.0]},
                     {'hoverinfo': 'text',
                      'line': {'color': 'rgb(0, 0, 0)', 'width': 4},
                      'mode': 'lines',
                      'text': ['lower-quartile: 1.00',
                               'upper-quartile: 2.00'],
                      'type': 'scatter',
                      'x': [0, 0],
                      'y': [1.0, 2.0]},
                     {'hoverinfo': 'text',
                      'marker': {'color': 'rgb(255, 255, 255)',
                                 'symbol': 'square'},
                      'mode': 'markers',
                      'text': ['median: 1.50'],
                      'type': 'scatter',
                      'x': [0],
                      'y': [1.5]},
                     {'hoverinfo': 'y',
                      'marker': {'color': 'rgb(31, 119, 180)',
                                 'symbol': 'line-ew-open'},
                      'mode': 'markers',
                      'name': '',
                      'showlegend': False,
                      'type': 'scatter',
                      'x': [-0.55916964093970667, -0.55916964093970667],
                      'y': np.array([1., 2.])}],
            'layout': {'autosize': False,
                       'font': {'size': 11},
                       'height': 450,
                       'hovermode': 'closest',
                       'showlegend': False,
                       'title': 'Violin and Rug Plot',
                       'width': 600,
                       'xaxis': {'mirror': False,
                                 'range': [-0.65916964093970665,
                                           0.56597470078308887],
                                 'showgrid': False,
                                 'showline': False,
                                 'showticklabels': False,
                                 'ticks': '',
                                 'title': '',
                                 'zeroline': False},
                       'yaxis': {'autorange': True,
                                 'mirror': False,
                                 'showgrid': False,
                                 'showline': False,
                                 'showticklabels': False,
                                 'ticklen': 4,
                                 'ticks': '',
                                 'title': '',
                                 'zeroline': False}}}

        # test both items in 'data'
        for i in [0, 1]:
            self.assert_fig_equal(
                test_violin['data'][i],
                exp_violin['data'][i]
            )

        self.assert_fig_equal(test_violin['layout'],
                              exp_violin['layout'])


class TestFacetGrid(NumpyTestUtilsMixin, TestCase):

    def test_data_must_be_dataframe(self):
        data = []

        pattern = ('You must input a pandas DataFrame.')

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_facet_grid,
                                data, 'a', 'b')

    def test_x_and_y_for_scatter(self):
        data = pd.DataFrame([[0, 0], [1, 1]], columns=['a', 'b'])

        pattern = (
            "You need to input 'x' and 'y' if you are you are using a "
            "trace_type of 'scatter' or 'scattergl'."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_facet_grid,
                                data, 'a')

    def test_valid_col_selection(self):
        data = pd.DataFrame([[0, 0], [1, 1]], columns=['a', 'b'])

        pattern = (
            "x, y, facet_row, facet_col and color_name must be keys in your "
            "dataframe."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_facet_grid,
                                data, 'a', 'c')

    def test_valid_trace_type(self):
        data = pd.DataFrame([[0, 0], [1, 1]], columns=['a', 'b'])

        self.assertRaises(PlotlyError, ff.create_facet_grid,
                          data, 'a', 'b', trace_type='foo')

    def test_valid_scales(self):
        data = pd.DataFrame([[0, 0], [1, 1]], columns=['a', 'b'])

        pattern = (
            "'scales' must be set to 'fixed', 'free_x', 'free_y' and 'free'."
        )

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_facet_grid,
                                data, 'a', 'b', scales='not_free')

    def test_valid_plotly_color_scale_name(self):
        data = pd.DataFrame([[0, 0], [1, 1]], columns=['a', 'b'])

        self.assertRaises(PlotlyError, ff.create_facet_grid,
                          data, 'a', 'b', color_name='a', colormap='wrong one')

    def test_facet_labels(self):
        data = pd.DataFrame([['a1', 0], ['a2', 1]], columns=['a', 'b'])

        self.assertRaises(PlotlyError, ff.create_facet_grid,
                          data, 'a', 'b', facet_row='a', facet_row_labels={})

        self.assertRaises(PlotlyError, ff.create_facet_grid,
                          data, 'a', 'b', facet_col='a', facet_col_labels={})

    def test_valid_color_dict(self):
        data = pd.DataFrame([[0, 0, 'foo'], [1, 1, 'foo']],
                            columns=['a', 'b', 'foo'])

        pattern = (
            "If using 'colormap' as a dictionary, make sure "
            "all the values of the colormap column are in "
            "the keys of your dictionary."
        )

        color_dict = {'bar': '#ffffff'}

        self.assertRaisesRegexp(PlotlyError, pattern,
                                ff.create_facet_grid,
                                data, 'a', 'b', color_name='a',
                                colormap=color_dict)

    def test_valid_colorscale_name(self):
        data = pd.DataFrame([[0, 1, 2], [3, 4, 5]],
                            columns=['a', 'b', 'c'])

        colormap='foo'

        self.assertRaises(PlotlyError, ff.create_facet_grid, data, 'a', 'b',
                          color_name='c', colormap=colormap)

    def test_valid_facet_grid_fig(self):
        mpg = [
            ["audi", "a4", 1.8, 1999, 4, "auto(15)", "f", 18, 29, "p", "compact"],
            ["audi", "a4", 1.8, 1999, 4, "auto(l5)", "f", 18, 29, "p", "compact"],
            ["audi", "a4", 2, 2008, 4, "manual(m6)", "f", 20, 31, "p", "compact"],
            ["audi", "a4", 2, 2008, 4, "auto(av)", "f", 21, 30, "p", "compact"],
            ["audi", "a4", 2.8, 1999, 6, "auto(l5)", "f", 16, 26, "p", "compact"],
            ["audi", "a4", 2.8, 1999, 6, "manual(m5)", "f", 18, 26, "p", "compact"],
            ["audi", "a4", 3.1, 2008, 6, "auto(av)", "f", 18, 27, "p", "compact"],
            ["audi", "a4 quattro", 1.8, 1999, 4, "manual(m5)", "4", 18, 26, "p", "compact"],
            ["audi", "a4 quattro", 1.8, 1999, 4, "auto(l5)", "4", 16, 25, "p", "compact"],
            ["audi", "a4 quattro", 2, 2008, 4, "manual(m6)", "4", 20, 28, "p", "compact"],
        ]

        df = pd.DataFrame(
            mpg,
            columns=["manufacturer", "model", "displ", "year", "cyl", "trans",
                     "drv", "cty", "hwy", "fl", "class"]
        )
        test_facet_grid = ff.create_facet_grid(
            df,
            x='displ',
            y='cty',
            facet_col='cyl',
        )

        exp_facet_grid = {
            'data': [
              {'marker': {'color': 'rgb(31, 119, 180)',
               'line': {'color': 'darkgrey', 'width': 1},
               'size': 8},
               'mode': 'markers',
               'opacity': 0.6,
               'type': 'scatter',
               'x': [1.8, 1.8, 2.0, 2.0, 1.8, 1.8, 2.0],
               'xaxis': 'x',
               'y': [18, 18, 20, 21, 18, 16, 20],
               'yaxis': 'y'},
              {'marker': {'color': 'rgb(31, 119, 180)',
                'line': {'color': 'darkgrey', 'width': 1},
                'size': 8},
               'mode': 'markers',
               'opacity': 0.6,
               'type': 'scatter',
               'x': [2.8, 2.8, 3.1],
               'xaxis': 'x2',
               'y': [16, 18, 18],
               'yaxis': 'y'}],
             'layout': {'annotations': [{'font': {'color': '#0f0f0f', 'size': 13},
                'showarrow': False,
                'text': '4',
                'textangle': 0,
                'x': 0.24625,
                'xanchor': 'center',
                'xref': 'paper',
                'y': 1.03,
                'yanchor': 'middle',
                'yref': 'paper'},
               {'font': {'color': '#0f0f0f', 'size': 13},
                'showarrow': False,
                'text': '6',
                'textangle': 0,
                'x': 0.7537499999999999,
                'xanchor': 'center',
                'xref': 'paper',
                'y': 1.03,
                'yanchor': 'middle',
                'yref': 'paper'},
               {'font': {'color': '#000000', 'size': 12},
                'showarrow': False,
                'text': 'displ',
                'textangle': 0,
                'x': 0.5,
                'xanchor': 'center',
                'xref': 'paper',
                'y': -0.1,
                'yanchor': 'middle',
                'yref': 'paper'},
               {'font': {'color': '#000000', 'size': 12},
                'showarrow': False,
                'text': 'cty',
                'textangle': -90,
                'x': -0.1,
                'xanchor': 'center',
                'xref': 'paper',
                'y': 0.5,
                'yanchor': 'middle',
                'yref': 'paper'}],
              'height': 600,
              'legend': {'bgcolor': '#efefef',
               'borderwidth': 1,
               'x': 1.05,
               'y': 1,
               'yanchor': 'top'},
              'paper_bgcolor': 'rgb(251, 251, 251)',
              'showlegend': False,
              'title': '',
              'width': 600,
              'xaxis': {'anchor': 'y',
               'domain': [0.0, 0.4925],
               'dtick': 0.0,
               'range': [0.85, 4.1575],
               'ticklen': 0,
               'zeroline': False},
              'xaxis2': {'anchor': 'free',
               'domain': [0.5075, 1.0],
               'dtick': 0.0,
               'position': 0.0,
               'range': [0.85, 4.1575],
               'ticklen': 0,
               'zeroline': False},
              'yaxis': {'anchor': 'x',
               'domain': [0.0, 1.0],
               'dtick': 1.0,
               'range': [15.75, 21.2625],
               'ticklen': 0,
               'zeroline': False}}}

        for j in [0, 1]:
            self.assert_fig_equal(
                test_facet_grid['data'][j],
                exp_facet_grid['data'][j]
            )

        self.assert_fig_equal(
            test_facet_grid['layout'],
            exp_facet_grid['layout']
        )


class TestBullet(NumpyTestUtilsMixin, TestCase):

    def test_df_as_list(self):
        df = [
            {'titles': 'Revenue'},
            'foo'
        ]

        pattern = (
            'Every entry of the data argument (list, tuple, etc) must '
            'be a dictionary.'
        )
        self.assertRaisesRegexp(PlotlyError, pattern, ff.create_bullet, df)

    def test_not_df_or_list(self):
        df = 'foo'

        pattern = ('You must input a pandas DataFrame, or a list of dictionaries.')
        self.assertRaisesRegexp(PlotlyError, pattern, ff.create_bullet, df)

    def test_valid_color_lists_of_2_rgb_colors(self):
        df = [
            {'title': 'Revenue'}
        ]

        range_colors = ['rgb(0, 0, 0)']
        measure_colors = ['rgb(0, 0, 0)']

        pattern = ("Both 'range_colors' or 'measure_colors' must be a list "
                   "of two valid colors.")
        self.assertRaisesRegexp(
            PlotlyError, pattern, ff.create_bullet, df,
            range_colors=range_colors
        )

        self.assertRaisesRegexp(
            PlotlyError, pattern, ff.create_bullet, df,
            measure_colors=measure_colors
        )

    def test_full_bullet(self):
        data = [
            {
                "title": "Revenue",
                "subtitle": "US$, in thousands",
                "ranges": [150, 225, 300],
                "measures":[220, 270],
                "markers":[250]
            },
            {
                "title": "Profit",
                "subtitle": "%",
                "ranges": [20, 25, 30],
                "measures": [21, 23],
                "markers": [26]
            },
            {
                "title": "Order Size",
                "subtitle": "US$, average",
                "ranges": [350, 500, 600],
                "measures": [100, 320],
                "markers": [550]
            },
            {
                "title": "New Customers",
                "subtitle": "count",
                "ranges": [1400, 2000, 2500],
                "measures":[1000, 1650],
                "markers": [2100]
            },
            {
                "title": "Satisfaction",
                "subtitle": "out of 5",
                "ranges": [3.5, 4.25, 5],
                "measures": [3.2, 4.7],
                "markers": [4.4]
            }
        ]

        df = pd.DataFrame(data)

        measure_colors = ['rgb(255, 127, 14)', 'rgb(44, 160, 44)']
        range_colors = ['rgb(255, 127, 14)', 'rgb(44, 160, 44)']

        fig = ff.create_bullet(
            df, orientation='v', markers='markers', measures='measures',
            ranges='ranges', subtitles='subtitle', titles='title',
            range_colors=range_colors, measure_colors=measure_colors,
            title='new title',
            scatter_options={'marker': {'size': 30,
                                        'symbol': 'hourglass'}}
        )

        exp_fig = {
            'data': [{'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x',
                      'y': [300],
                      'yaxis': 'y'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(149.5, 143.5, 29.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x',
                      'y': [225],
                      'yaxis': 'y'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x',
                      'y': [150],
                      'yaxis': 'y'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x',
                      'y': [270],
                      'yaxis': 'y'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x',
                      'y': [220],
                      'yaxis': 'y'},
                     {'hoverinfo': 'y',
                      'marker': {'color': 'rgb(0, 0, 0)',
                                 'size': 30,
                                 'symbol': 'hourglass'},
                      'name': 'markers',
                      'type': 'scatter',
                      'x': [0.5],
                      'xaxis': 'x',
                      'y': [250],
                      'yaxis': 'y'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x2',
                      'y': [30],
                      'yaxis': 'y2'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(149.5, 143.5, 29.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x2',
                      'y': [25],
                      'yaxis': 'y2'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x2',
                      'y': [20],
                      'yaxis': 'y2'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x2',
                      'y': [23],
                      'yaxis': 'y2'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x2',
                      'y': [21],
                      'yaxis': 'y2'},
                     {'hoverinfo': 'y',
                      'marker': {'color': 'rgb(0, 0, 0)',
                                 'size': 30,
                                 'symbol': 'hourglass'},
                      'name': 'markers',
                      'type': 'scatter',
                      'x': [0.5],
                      'xaxis': 'x2',
                      'y': [26],
                      'yaxis': 'y2'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x3',
                      'y': [600],
                      'yaxis': 'y3'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(149.5, 143.5, 29.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x3',
                      'y': [500],
                      'yaxis': 'y3'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x3',
                      'y': [350],
                      'yaxis': 'y3'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x3',
                      'y': [320],
                      'yaxis': 'y3'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x3',
                      'y': [100],
                      'yaxis': 'y3'},
                     {'hoverinfo': 'y',
                      'marker': {'color': 'rgb(0, 0, 0)',
                                 'size': 30,
                                 'symbol': 'hourglass'},
                      'name': 'markers',
                      'type': 'scatter',
                      'x': [0.5],
                      'xaxis': 'x3',
                      'y': [550],
                      'yaxis': 'y3'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x4',
                      'y': [2500],
                      'yaxis': 'y4'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(149.5, 143.5, 29.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x4',
                      'y': [2000],
                      'yaxis': 'y4'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x4',
                      'y': [1400],
                      'yaxis': 'y4'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x4',
                      'y': [1650],
                      'yaxis': 'y4'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x4',
                      'y': [1000],
                      'yaxis': 'y4'},
                     {'hoverinfo': 'y',
                      'marker': {'color': 'rgb(0, 0, 0)',
                                 'size': 30,
                                 'symbol': 'hourglass'},
                      'name': 'markers',
                      'type': 'scatter',
                      'x': [0.5],
                      'xaxis': 'x4',
                      'y': [2100],
                      'yaxis': 'y4'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x5',
                      'y': [5],
                      'yaxis': 'y5'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(149.5, 143.5, 29.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x5',
                      'y': [4.25],
                      'yaxis': 'y5'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'ranges',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 2,
                      'x': [0],
                      'xaxis': 'x5',
                      'y': [3.5],
                      'yaxis': 'y5'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(44.0, 160.0, 44.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x5',
                      'y': [4.7],
                      'yaxis': 'y5'},
                     {'base': 0,
                      'hoverinfo': 'y',
                      'marker': {'color': 'rgb(255.0, 127.0, 14.0)'},
                      'name': 'measures',
                      'orientation': 'v',
                      'type': 'bar',
                      'width': 0.4,
                      'x': [0.5],
                      'xaxis': 'x5',
                      'y': [3.2],
                      'yaxis': 'y5'},
                     {'hoverinfo': 'y',
                      'marker': {'color': 'rgb(0, 0, 0)',
                                 'size': 30,
                                 'symbol': 'hourglass'},
                      'name': 'markers',
                      'type': 'scatter',
                      'x': [0.5],
                      'xaxis': 'x5',
                      'y': [4.4],
                      'yaxis': 'y5'}],
            'layout': {'annotations': [{'font': {'color': '#0f0f0f', 'size': 13},
                                        'showarrow': False,
                                        'text': '<b>Revenue</b>',
                                        'textangle': 0,
                                        'x': 0.019999999999999997,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 1.03,
                                        'yanchor': 'middle',
                                        'yref': 'paper'},
                                       {'font': {'color': '#0f0f0f', 'size': 13},
                                        'showarrow': False,
                                        'text': '<b>Profit</b>',
                                        'textangle': 0,
                                        'x': 0.26,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 1.03,
                                        'yanchor': 'middle',
                                        'yref': 'paper'},
                                       {'font': {'color': '#0f0f0f', 'size': 13},
                                        'showarrow': False,
                                        'text': '<b>Order Size</b>',
                                        'textangle': 0,
                                        'x': 0.5,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 1.03,
                                        'yanchor': 'middle',
                                        'yref': 'paper'},
                                       {'font': {'color': '#0f0f0f', 'size': 13},
                                        'showarrow': False,
                                        'text': '<b>New Customers</b>',
                                        'textangle': 0,
                                        'x': 0.74,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 1.03,
                                        'yanchor': 'middle',
                                        'yref': 'paper'},
                                       {'font': {'color': '#0f0f0f', 'size': 13},
                                        'showarrow': False,
                                        'text': '<b>Satisfaction</b>',
                                        'textangle': 0,
                                        'x': 0.98,
                                        'xanchor': 'center',
                                        'xref': 'paper',
                                        'y': 1.03,
                                        'yanchor': 'middle',
                                        'yref': 'paper'}],
                       'barmode': 'stack',
                       'height': 600,
                       'margin': {'l': 80},
                       'shapes': [],
                       'showlegend': False,
                       'title': 'new title',
                       'width': 1000,
                       'xaxis1': {'anchor': 'y',
                                  'domain': [0.0, 0.039999999999999994],
                                  'range': [0, 1],
                                  'showgrid': False,
                                  'showticklabels': False,
                                  'zeroline': False},
                       'xaxis2': {'anchor': 'y2',
                                  'domain': [0.24, 0.27999999999999997],
                                  'range': [0, 1],
                                  'showgrid': False,
                                  'showticklabels': False,
                                  'zeroline': False},
                       'xaxis3': {'anchor': 'y3',
                                  'domain': [0.48, 0.52],
                                  'range': [0, 1],
                                  'showgrid': False,
                                  'showticklabels': False,
                                  'zeroline': False},
                       'xaxis4': {'anchor': 'y4',
                                  'domain': [0.72, 0.76],
                                  'range': [0, 1],
                                  'showgrid': False,
                                  'showticklabels': False,
                                  'zeroline': False},
                       'xaxis5': {'anchor': 'y5',
                                  'domain': [0.96, 1.0],
                                  'range': [0, 1],
                                  'showgrid': False,
                                  'showticklabels': False,
                                  'zeroline': False},
                       'yaxis1': {'anchor': 'x',
                                  'domain': [0.0, 1.0],
                                  'showgrid': False,
                                  'tickwidth': 1,
                                  'zeroline': False},
                       'yaxis2': {'anchor': 'x2',
                                  'domain': [0.0, 1.0],
                                  'showgrid': False,
                                  'tickwidth': 1,
                                  'zeroline': False},
                       'yaxis3': {'anchor': 'x3',
                                  'domain': [0.0, 1.0],
                                  'showgrid': False,
                                  'tickwidth': 1,
                                  'zeroline': False},
                       'yaxis4': {'anchor': 'x4',
                                  'domain': [0.0, 1.0],
                                  'showgrid': False,
                                  'tickwidth': 1,
                                  'zeroline': False},
                       'yaxis5': {'anchor': 'x5',
                                  'domain': [0.0, 1.0],
                                  'showgrid': False,
                                  'tickwidth': 1,
                                  'zeroline': False}}
        }

        for i in range(len(fig['data'])):
            self.assert_fig_equal(fig['data'][i],
                                  exp_fig['data'][i])


class TestChoropleth(NumpyTestUtilsMixin, TestCase):

    # run tests if required packages are installed
    if shapely and shapefile and gp:
        def test_fips_values_same_length(self):
            pattern = 'fips and values must be the same length'
            self.assertRaisesRegexp(
                PlotlyError, pattern, ff.create_choropleth,
                fips=[1001], values=[4004, 40004]
            )

        def test_correct_order_param(self):
            pattern = (
                'if you are using a custom order of unique values from '
                'your color column, you must: have all the unique values '
                'in your order and have no duplicate items'
            )

            self.assertRaisesRegexp(
                PlotlyError, pattern, ff.create_choropleth,
                fips=[1], values=[1], order=[1, 1, 1]
            )

        def test_colorscale_and_levels_same_length(self):
            self.assertRaises(
                PlotlyError, ff.create_choropleth,
                fips=[1001, 1003, 1005], values=[5, 2, 1],
                colorscale=['rgb(0,0,0)']
            )

        def test_scope_is_not_list(self):

            pattern = "'scope' must be a list/tuple/sequence"

            self.assertRaisesRegexp(
                PlotlyError, pattern, ff.create_choropleth,
                fips=[1001, 1003], values=[5, 2], scope='foo',
            )

        def test_full_choropleth(self):
            fips = [1001]
            values = [1]
            fig = ff.create_choropleth(
                fips=fips, values=values,
                simplify_county=1
            )

            exp_fig_head = [
                -88.053375,
                -88.02916499999999,
                -88.02432999999999,
                -88.04504299999999,
                -88.053375,
                np.nan,
                -88.211209,
                -88.209999,
                -88.208733,
                -88.209559,
                -88.211209,
                np.nan,
                -88.22511999999999,
                -88.22128099999999,
                -88.218694,
                -88.22465299999999,
                -88.22511999999999,
                np.nan,
                -88.264659,
                -88.25782699999999,
                -88.25947,
                -88.255659,
                -88.264659,
                np.nan,
                -88.327302,
                -88.20146799999999,
                -88.141143,
                -88.124658,
                -88.074854,
                -88.12493599999999,
                -88.10665399999999,
                -88.149812,
                -88.327302,
                np.nan,
                -88.346745,
                -88.341235,
                -88.33288999999999,
                -88.346823,
                -88.346745,
                np.nan,
                -88.473227,
                -88.097888,
                -88.154617,
                -88.20295899999999,
                -85.605165,
                -85.18440000000001,
                -85.12218899999999,
                -85.142567,
                -85.113329,
                -85.10533699999999
            ]

            self.assertEqual(fig['data'][2]['x'][:50], exp_fig_head)

class TestQuiver(TestCase):

    def test_scaleratio_param(self):
        x,y = np.meshgrid(np.arange(0.5, 3.5, .5), np.arange(0.5, 4.5, .5))
        u = x
        v = y
        angle = np.arctan(v / u)
        norm = 0.25
        u = norm * np.cos(angle)
        v = norm * np.sin(angle)
        fig = ff.create_quiver(x, y, u, v, scale = 1, scaleratio = 0.5)

        exp_fig_head = [(
            0.5, 
            0.5883883476483185, 
            None,
            1.0, 
            1.1118033988749896, 
            None, 
            1.5, 
            1.6185854122563141, 
            None, 
            2.0),
            (0.5,
            0.6767766952966369,
            None,
            0.5, 
            0.6118033988749895, 
            None, 
            0.5, 
            0.5790569415042095, 
            None, 
            0.5)]

        fig_head = [fig['data'][0]['x'][:10], fig['data'][0]['y'][:10]]

        self.assertEqual(fig_head, exp_fig_head)


