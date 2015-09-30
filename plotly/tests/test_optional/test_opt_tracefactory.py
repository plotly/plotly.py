from unittest import TestCase
from plotly.graph_objs import graph_objs, Line
from plotly.exceptions import PlotlyError

import plotly.tools as tls
import math
from nose.tools import raises

import numpy as np


class TestDistplot(TestCase):

    def test_wrong_curve_type(self):

        # check: PlotlyError (and specific message) is raised if curve_type is
        # not 'kde' or 'normal'

        kwargs = {'hist_data': [[1, 2, 3]], 'group_labels': ['group'],
                  'curve_type': 'curve'}
        self.assertRaisesRegexp(PlotlyError, "curve_type must be defined as "
                                             "'kde' or 'normal'",
                                tls.FigureFactory.create_distplot, **kwargs)

    def test_wrong_histdata_format(self):

        # check: PlotlyError if hist_data is not a list of lists or list of
        # np.ndarrays (if hist_data is entered as just a list the function
        # will fail)

        kwargs = {'hist_data': [1, 2, 3], 'group_labels': ['group']}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_distplot,
                          **kwargs)

    def test_unequal_data_label_length(self):
        kwargs = {'hist_data': [[1, 2]], 'group_labels': ['group', 'group2']}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_distplot,
                          **kwargs)

        kwargs = {'hist_data': [[1, 2], [1, 2, 3]], 'group_labels': ['group']}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_distplot,
                          **kwargs)

    def test_simple_distplot(self):

        # we should be able to create a single distplot with a simple dataset
        # and default kwargs

        dp = tls.FigureFactory.create_distplot(hist_data=[[1, 2, 2, 3]],
                                               group_labels=['distplot'])
        expected_dp_layout = {'barmode': 'overlay',
                              'hovermode': 'closest',
                              'legend': {'traceorder': 'reversed'},
                              'xaxis1': {'anchor': 'y2', 'domain': [0.0, 1.0], 'zeroline': False},
                              'yaxis1': {'anchor': 'free', 'domain': [0.35, 1], 'position': 0.0},
                              'yaxis2': {'anchor': 'x1',
                                         'domain': [0, 0.25],
                                         'dtick': 1,
                                         'showticklabels': False}}
        self.assertEqual(dp['layout'], expected_dp_layout)

        expected_dp_data_hist = {'autobinx': False,
                                 'histnorm': 'probability',
                                 'legendgroup': 'distplot',
                                 'marker': {'color': 'rgb(31, 119, 180)'},
                                 'name': 'distplot',
                                 'opacity': 0.7,
                                 'type': 'histogram',
                                 'x': [1, 2, 2, 3],
                                 'xaxis': 'x1',
                                 'xbins': {'end': 3.0, 'size': 1.0, 'start': 1.0},
                                 'yaxis': 'y1'}
        self.assertEqual(dp['data'][0], expected_dp_data_hist)

        expected_dp_data_rug = {'legendgroup': 'distplot',
                                'marker': {'color': 'rgb(31, 119, 180)',
                                           'symbol': 'line-ns-open'},
                                'mode': 'markers',
                                'name': 'distplot',
                                'showlegend': False,
                                'text': None,
                                'type': 'scatter',
                                'x': [1, 2, 2, 3],
                                'xaxis': 'x1',
                                'y': ['distplot', 'distplot',
                                      'distplot', 'distplot'],
                                'yaxis': 'y2'}
        self.assertEqual(dp['data'][2], expected_dp_data_rug)

    def test_distplot_more_args(self):

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

        dp = tls.FigureFactory.create_distplot(hist_data, group_labels,
                                               show_rug=False, bin_size=.2)
        dp['layout'].update(title='Dist Plot')

        expected_dp_layout = {'barmode': 'overlay',
                              'hovermode': 'closest',
                              'legend': {'traceorder': 'reversed'},
                              'title': 'Dist Plot',
                              'xaxis1': {'anchor': 'y2', 'domain': [0.0, 1.0],
                                         'zeroline': False},
                              'yaxis1': {'anchor': 'free', 'domain': [0.0, 1],
                                         'position': 0.0}}
        self.assertEqual(dp['layout'], expected_dp_layout)

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
                                   'xaxis': 'x1',
                                   'xbins': {'end': 1.95, 'size': 0.2,
                                             'start': -0.9},
                                   'yaxis': 'y1'}
        self.assertEqual(dp['data'][0], expected_dp_data_hist_1)

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
                                   'xaxis': 'x1',
                                   'xbins': {'end': 2.2, 'size': 0.2,
                                             'start': -0.3},
                                   'yaxis': 'y1'}
        self.assertEqual(dp['data'][1], expected_dp_data_hist_2)


class TestStreamline(TestCase):

    def test_wrong_arrow_scale(self):

        # check for ValueError if arrow_scale is <= 0

        kwargs = {'x': [0, 2], 'y': [0, 2],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]],
                  'arrow_scale': 0}
        self.assertRaises(ValueError, tls.FigureFactory.create_streamline,
                          **kwargs)

    def test_wrong_density(self):

        # check for ValueError if density is <= 0

        kwargs = {'x': [0, 2], 'y': [0, 2],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]],
                  'density': 0}
        self.assertRaises(ValueError, tls.FigureFactory.create_streamline,
                          **kwargs)

    def test_uneven_x(self):

        # check for PlotlyError if x is not evenly spaced

        kwargs = {'x': [0, 2, 7, 9], 'y': [0, 2, 4, 6],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_streamline,
                          **kwargs)

    def test_uneven_y(self):

        # check for PlotlyError if y is not evenly spaced

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3, 3.5],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_streamline,
                          **kwargs)

    def test_unequal_length_xy(self):

        # check for PlotlyError if u and v are not the same length

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3.5],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_streamline,
                          **kwargs)

    def test_unequal_length_uv(self):

        # check for PlotlyError if u and v are not the same length

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3, 3.5],
                  'u': [[-1, -5], [-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.FigureFactory.create_streamline,
                          **kwargs)

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

        strln = tls.FigureFactory.create_streamline(x=[-1., 0., 1.],
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
        self.assertListEqual(strln['data'][0]['y'][0:100],
                             expected_strln_0_100['y'])
        self.assertListEqual(strln['data'][0]['x'][0:100],
                             expected_strln_0_100['x'])


class TestDendrogram(TestCase):

    def test_default_dendrogram(self):
        dendro = tls.FigureFactory.create_dendrogram(X=np.array([[1, 2, 3, 4],
                                                                 [1, 1, 3, 4],
                                                                 [1, 2, 1, 4],
                                                                 [1, 2, 3, 1]]))
        expected_data = [{'marker': {'color': 'rgb(255,133,27)'},
                          'mode': 'lines', 'xaxis': 'xs',
                          'yaxis': 'y',
                          'y': np.array([0.,  1.,  1.,  0.]),
                          'x': np.array([25.,  25.,  35.,  35.]),
                          'type': u'scatter'},
                         {'marker': {'color': 'rgb(255,133,27)'},
                          'mode': 'lines',
                          'xaxis': 'x',
                          'yaxis': 'y',
                          'y': np.array([0., 2.23606798,
                                        2.23606798, 1.]),
                          'x': np.array([15., 15., 30., 30.]),
                          'type': u'scatter'},
                         {'marker': {'color': 'blue'},
                          'mode': 'lines',
                          'xaxis': 'x',
                          'yaxis': 'y',
                          'y': np.array([0., 3.60555128,
                                        3.60555128, 2.23606798]),
                          'x': np.array([5., 5., 22.5, 22.5]),
                          'type': u'scatter'}]
        expected_layout = {'width': '100%',
                           'showlegend': False,
                           'autoscale': False,
                           'xaxis': {'showticklabels': True,
                                     'tickmode': 'array',
                                     'ticks': 'outside',
                                     'showgrid': False,
                                     'mirror': 'allticks',
                                     'zeroline': False,
                                     'showline': True,
                                     'ticktext': np.array(['3', '2',
                                                           '0', '1'],
                                                          dtype='|S1'),
                                     'rangemode': 'tozero',
                                     'type': 'linear',
                                     'tickvals': np.array([5.0, 15.0,
                                                          25.0, 35.0])},
                           'yaxis': {'showticklabels': True,
                                     'ticks': 'outside',
                                     'showgrid': False,
                                     'mirror': 'allticks',
                                     'zeroline': False,
                                     'showline': True,
                                     'rangemode': 'tozero',
                                     'type': 'linear'},
                           'hovermode': 'closest'}  

        # Make sure data is as expected
        self.assertEqual(len(dendro['data']), len(expected_data))
        for i in range(1, len(dendro['data'])):
            self.assertTrue(np.allclose(dendro['data'][i]['x'],
                            expected_data[i]['x']))
            self.assertTrue(np.allclose(dendro['data'][i]['y'],
                            expected_data[i]['y']))

        # Make sure layout is as expected
        self.assertTrue(np.array_equal(dendro['layout']['xaxis']['ticktext'],
                                       expected_layout['xaxis']['ticktext']))
        self.assertTrue(np.array_equal(dendro['layout']['xaxis']['tickvals'],
                                       expected_layout['xaxis']['tickvals']))
        self.assertEqual(dendro['layout']['xaxis']['ticks'], 'outside')
        self.assertEqual(dendro['layout']['yaxis']['ticks'], 'outside')
        self.assertEqual(dendro['layout']['width'], expected_layout['width'])

    def test_dendrogram_random_matrix(self):
        # create a random uncorrelated matrix
        X = np.random.rand(5, 5)
        # variable 2 is correlated with all the other variables
        X[2, :] = sum(X, 0)

        names = ['Jack', 'Oxana', 'John', 'Chelsea', 'Mark']
        dendro = tls.FigureFactory.create_dendrogram(X, labels=names)

        # Check that 2 is in a separate cluster and it's labelled correctly
        self.assertEqual(dendro['layout']['xaxis']['ticktext'][0], 'John')

    def test_dendrogram_orientation(self):
        X = np.random.rand(5, 5) 

        dendro_left = tls.FigureFactory.create_dendrogram(
                       X, orientation='left')
        self.assertEqual(len(dendro_left['layout']['yaxis']['ticktext']), 5)
        tickvals_left = np.array(dendro_left['layout']['yaxis']['tickvals'])
        self.assertTrue((tickvals_left <= 0).all())

        dendro_right = tls.FigureFactory.create_dendrogram(
                        X, orientation='right')
        tickvals_right = np.array(dendro_right['layout']['yaxis']['tickvals'])
        self.assertTrue((tickvals_right >= 0).all())

        dendro_bottom = tls.FigureFactory.create_dendrogram(
                        X, orientation='bottom')
        self.assertEqual(len(dendro_bottom['layout']['xaxis']['ticktext']), 5)
        tickvals_bottom = np.array(dendro_bottom['layout']['xaxis']['tickvals'])
        self.assertTrue((tickvals_bottom >= 0).all())

        dendro_top = tls.FigureFactory.create_dendrogram(X, orientation='top')
        tickvals_top = np.array(dendro_top['layout']['xaxis']['tickvals'])
        self.assertTrue((tickvals_top <= 0).all())

    def test_dendrogram_orientation(self):
        X = np.array([[1, 2, 3, 4],
                      [1, 1, 3, 4],
                      [1, 2, 1, 4],
                      [1, 2, 3, 1]])
        greyscale = [
                'rgb(0,0,0)',        # black
                'rgb(05,105,105)',   # dim grey
                'rgb(128,128,128)',  # grey
                'rgb(169,169,169)',  # dark grey
                'rgb(192,192,192)',  # silver
                'rgb(211,211,211)',  # light grey
                'rgb(220,220,220)',  # gainsboro
                'rgb(245,245,245)']  # white smoke

        dendro = tls.FigureFactory.create_dendrogram(X, colorscale=greyscale)
        self.assertEqual(dendro["data"][0]['marker']['color'],
                         'rgb(128,128,128)')
        self.assertEqual(dendro["data"][1]['marker']['color'],
                         'rgb(128,128,128)')
        self.assertEqual(dendro["data"][2]['marker']['color'],
                         'rgb(0,0,0)')
