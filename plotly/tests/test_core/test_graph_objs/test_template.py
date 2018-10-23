from __future__ import absolute_import

import copy
from unittest import TestCase
from nose.tools import raises

import plotly.io as pio
import plotly.graph_objs as go


class TemplateTest(TestCase):

    # Fixtures
    # --------
    def setUp(self):
        pio.templates['test_template'] = {
            'layout': {'font': {'family': 'Rockwell'}}}

    def tearDown(self):
        try:
            del pio.templates['test_template']
        except KeyError:
            pass

    # template graph_objs tests
    # -------------------------
    def test_starts_as_empty(self):
        fig = go.Figure()
        self.assertEqual(fig.layout.template, go.layout.Template())

    def test_init_in_figure_constructor(self):
        fig = go.Figure(layout={
            'template': {'layout': {'title': 'Hello, world'}}})

        self.assertEqual(fig.layout.template,
                         go.layout.Template(layout={'title': 'Hello, world'}))

        self.assertEqual(fig.to_dict(),
                         {'data': [],
                          'layout': {
                              'template': {
                                  'layout': {'title': 'Hello, world'}}}})

    def test_init_in_property_assignment(self):
        fig = go.Figure()

        fig.layout.template = go.layout.Template(
            layout={'title': 'Hello, world'})

        self.assertEqual(fig.layout.template,
                         go.layout.Template(layout={'title': 'Hello, world'}))

        self.assertEqual(fig.to_dict(),
                         {'data': [],
                          'layout': {
                              'template': {
                                  'layout': {'title': 'Hello, world'}}}})

    def test_defaults_in_constructor(self):
        fig = go.Figure(layout={
            'template': {
                'layout': {
                    'imagedefaults': {'sizex': 500}}}})

        self.assertEqual(fig.layout.template.layout.imagedefaults,
                         go.layout.Image(sizex=500))

        self.assertEqual(fig.to_dict(),
                         {'data': [],
                          'layout': {
                             'template': {
                                 'layout': {
                                     'imagedefaults': {'sizex': 500}}}}})

    def test_defaults_in_property_assignment(self):
        fig = go.Figure()

        fig.layout.template.layout.sliderdefaults = \
            go.layout.Slider(bgcolor='green')

        self.assertEqual(fig.layout.template.layout.sliderdefaults,
                         go.layout.Slider(bgcolor='green'))

        self.assertEqual(fig.to_dict(),
                         {'data': [],
                          'layout': {
                             'template': {
                                 'layout': {
                                     'sliderdefaults': {
                                         'bgcolor': 'green'}}}}})

    @raises(ValueError)
    def test_invalid_defaults_property_name_constructor(self):
        go.Figure(layout={
            'template': {
                'layout': {
                    'imagedefaults': {'bogus': 500}}}})

    @raises(ValueError)
    def test_invalid_defaults_property_value_constructor(self):
        go.Figure(layout={
            'template': {
                'layout': {
                    'imagedefaults': {'sizex': 'str not number'}}}})

    @raises(ValueError)
    def test_invalid_defaults_property_name_constructor(self):
        go.Figure(layout={
            'template': {
                'layout': {
                    'xaxis': {'bogus': 500}}}})

    @raises(ValueError)
    def test_invalid_defaults_property_value_constructor(self):
        go.Figure(layout={
            'template': {
                'layout': {
                    'xaxis': {'range': 'str not tuple'}}}})

    # plotly.io.template tests
    # ------------------------
    def test_template_as_name_constructor(self):
        fig = go.Figure(layout={'template': 'test_template'})
        self.assertEqual(fig.layout.template, pio.templates['test_template'])

    def test_template_as_name_assignment(self):
        fig = go.Figure()
        self.assertEqual(fig.layout.template, go.layout.Template())

        fig.layout.template = 'test_template'
        self.assertEqual(fig.layout.template, pio.templates['test_template'])

    def test_template_default(self):
        pio.templates.default = 'test_template'
        fig = go.Figure()
        self.assertEqual(fig.layout.template, pio.templates['test_template'])

    def test_template_default_override(self):
        pio.templates.default = 'test_template'
        template = go.layout.Template(layout={'font': {'size': 30}})
        fig = go.Figure(layout={'template': template})
        self.assertEqual(fig.layout.template, template)

    def test_template_default_override_empty(self):
        pio.templates.default = 'test_template'
        fig = go.Figure(layout={'template': {}})
        self.assertEqual(fig.layout.template, go.layout.Template())

    def test_delete_default_template(self):
        pio.templates.default = 'test_template'
        self.assertEqual(pio.templates.default, 'test_template')

        del pio.templates['test_template']
        self.assertIsNone(pio.templates.default)

    def test_template_in(self):
        self.assertTrue('test_template' in pio.templates)
        self.assertFalse('bogus' in pio.templates)
        self.assertFalse(42 in pio.templates)

    def test_template_iter(self):
        self.assertIn('test_template', set(pio.templates))


class TestToTemplated(TestCase):

    def test_move_layout_nested_properties(self):
        fig = go.Figure(layout={'font': {'family': 'Courier New'},
                                'paper_bgcolor': 'yellow',
                                'title': 'Hello'})
        templated_fig = pio.to_templated(fig)

        # Note that properties named 'title' are not moved to template by
        # default
        expected_fig = go.Figure(layout={
            'template': {'layout': {'font': {'family': 'Courier New'},
                                    'paper_bgcolor': 'yellow'}},
            'title': 'Hello'})
        self.assertEqual(templated_fig, expected_fig)

    def test_move_layout_nested_properties_no_skip(self):
        fig = go.Figure(layout={'font': {'family': 'Courier New'},
                                'paper_bgcolor': 'yellow',
                                'title': 'Hello'})
        templated_fig = pio.to_templated(fig, skip=None)

        # With skip=None properties named 'title' should be moved to template
        expected_fig = go.Figure(layout={
            'template': {'layout': {'font': {'family': 'Courier New'},
                                    'paper_bgcolor': 'yellow',
                                    'title': 'Hello'}}})
        self.assertEqual(templated_fig, expected_fig)

    def test_move_layout_nested_with_existing_template(self):
        fig = go.Figure(layout={'font': {'family': 'Courier New'},
                                'title': 'Hello',
                                'template': {'layout': {
                                    'font': {'family': 'Arial',
                                             'size': 10}}}})

        templated_fig = pio.to_templated(fig)

        expected_fig = go.Figure(layout={
            'template': {'layout': {'font': {'family': 'Courier New',
                                             'size': 10}}},
            'title': 'Hello'})
        self.assertEqual(templated_fig, expected_fig)

    def test_move_unnamed_annotation_property(self):
        fig = go.Figure(layout={
            'annotations': [{'arrowcolor': 'blue',
                             'text': 'First one',
                             'font': {'size': 23}},
                            {'arrowcolor': 'green',
                             'text': 'Second one',
                             'font': {'family': 'Rockwell'}}]})

        templated_fig = pio.to_templated(fig)

        # Note that properties named 'text' are not moved to template by
        # default, unless they are part of a named array element
        expected_fig = go.Figure(layout={
            'annotations': [{'text': 'First one'}, {'text': 'Second one'}],
            'template': {'layout': {'annotationdefaults': {
                'arrowcolor': 'green',
                'font': {'size': 23, 'family': 'Rockwell'}
            }}}
        })
        self.assertEqual(templated_fig, expected_fig)

    def test_move_named_annotation_property(self):
        fig = go.Figure(layout={
            'annotations': [{'arrowcolor': 'blue',
                             'text': 'First one',
                             'font': {'size': 23}},
                            {'arrowcolor': 'green',
                             'text': 'Second one',
                             'font': {'family': 'Rockwell'},
                             'name': 'First'}]})

        templated_fig = pio.to_templated(fig)

        expected_fig = go.Figure(layout={
            'annotations': [{'text': 'First one'}, {'name': 'First'}],
            'template': {'layout': {
                'annotationdefaults': {
                    'arrowcolor': 'blue',
                    'font': {'size': 23}
                },
                'annotations': [{'arrowcolor': 'green',
                                 'font': {'family': 'Rockwell'},
                                 'text': 'Second one',
                                 'name': 'First'}]
            }}
        })
        self.assertEqual(templated_fig, expected_fig)

    def test_move_nested_trace_properties(self):
        fig = go.Figure(
            data=[
                go.Bar(y=[1, 2, 3],
                       marker={'opacity': 0.6,
                               'color': 'green'}),
                go.Scatter(x=[1, 3, 2],
                           marker={'size': 30,
                                   'color': [1, 1, 0]}),
                go.Bar(y=[3, 2, 1],
                       marker={'opacity': 0.4,
                               'color': [1, 0.5, 0]})
            ],
            layout={'barmode': 'group'}
        )

        templated_fig = pio.to_templated(fig)

        expected_fig = go.Figure(
            data=[
                go.Bar(y=[1, 2, 3]),
                go.Scatter(x=[1, 3, 2], marker={'color': [1, 1, 0]}),
                go.Bar(y=[3, 2, 1], marker={'color': [1, 0.5, 0]})
            ],
            layout={
                'template': {
                    'data': {
                        'scatter': [go.Scatter(marker={'size': 30})],
                        'bar': [
                            go.Bar(marker={'opacity': 0.6,
                                           'color': 'green'}),
                            go.Bar(marker={'opacity': 0.4})
                        ]},
                    'layout': {
                        'barmode': 'group'
                    }
                }
            }
        )

        self.assertEqual(pio.to_json(templated_fig),
                         pio.to_json(expected_fig))

    def test_move_nested_trace_properties_existing_traces(self):
        fig = go.Figure(
            data=[
                go.Bar(y=[1, 2, 3],
                       marker={'opacity': 0.6,
                               'color': 'green'}),
                go.Scatter(x=[1, 3, 2],
                           marker={'size': 30,
                                   'color': [1, 1, 0]}),
                go.Bar(y=[3, 2, 1],
                       marker={'opacity': 0.4,
                               'color': [1, 0.5, 0]})
            ],
            layout={'barmode': 'group',
                    'template': {
                        'data': {
                            'bar': [go.Bar(marker={
                                'line': {'color': 'purple'}})]
                        }
                    }}
        )

        templated_fig = pio.to_templated(fig)

        expected_fig = go.Figure(
            data=[
                go.Bar(y=[1, 2, 3]),
                go.Scatter(x=[1, 3, 2], marker={'color': [1, 1, 0]}),
                go.Bar(y=[3, 2, 1], marker={'color': [1, 0.5, 0]})
            ],
            layout={
                'template': {
                    'data': {
                        'scatter': [go.Scatter(marker={'size': 30})],
                        'bar': [
                            go.Bar(marker={'opacity': 0.6,
                                           'color': 'green',
                                           'line': {
                                               'color': 'purple'
                                           }}),
                            go.Bar(marker={'opacity': 0.4})
                        ]},
                    'layout': {
                        'barmode': 'group'
                    }
                }
            }
        )

        self.assertEqual(pio.to_json(templated_fig),
                         pio.to_json(expected_fig))


class TestMergeTemplates(TestCase):

    def setUp(self):

        self.template1 = go.layout.Template(
            layout={'font': {'size': 20, 'family': 'Rockwell'}},
            data={
                'scatter': [go.Scatter(line={'dash': 'solid'}),
                            go.Scatter(line={'dash': 'dot'})],
                'bar': [go.Bar(marker={'opacity': 0.7}),
                        go.Bar(marker={'opacity': 0.4})],
                'parcoords': [
                    go.Parcoords(dimensiondefaults={'multiselect': True})
                ]
                # no 'scattergl'
            }
        )
        pio.templates['template1'] = self.template1
        self.template1_orig = copy.deepcopy(self.template1)

        self.template2 = go.layout.Template(
            layout={'paper_bgcolor': 'green',
                    'font': {'size': 14, 'color': 'yellow'}},
            data={
                'scatter': [go.Scatter(marker={'color': 'red'}),
                            go.Scatter(marker={'color': 'green'}),
                            go.Scatter(marker={'color': 'blue'})],
                # no 'bar'
                'parcoords': [
                    go.Parcoords(line={'colorscale': 'Viridis'}),
                    go.Parcoords(line={'colorscale': 'Blues'})
                ],
                'scattergl': [go.Scattergl(hoverinfo='x+y')]
            }
        )
        pio.templates['template2'] = self.template2
        self.template2_orig = copy.deepcopy(self.template2)

        self.expected1_2 = go.layout.Template(
            layout={'paper_bgcolor': 'green',
                    'font': {'size': 14,
                             'color': 'yellow',
                             'family': 'Rockwell'}},
            data={
                'scatter': [
                    go.Scatter(marker={'color': 'red'},
                               line={'dash': 'solid'}),
                    go.Scatter(marker={'color': 'green'},
                               line={'dash': 'dot'}),
                    go.Scatter(marker={'color': 'blue'},
                               line={'dash': 'solid'}),
                    go.Scatter(marker={'color': 'red'},
                               line={'dash': 'dot'}),
                    go.Scatter(marker={'color': 'green'},
                               line={'dash': 'solid'}),
                    go.Scatter(marker={'color': 'blue'},
                               line={'dash': 'dot'}),
                ],
                'bar': [go.Bar(marker={'opacity': 0.7}),
                        go.Bar(marker={'opacity': 0.4})],
                'parcoords': [
                    go.Parcoords(dimensiondefaults={'multiselect': True},
                                 line={'colorscale': 'Viridis'}),
                    go.Parcoords(dimensiondefaults={'multiselect': True},
                                 line={'colorscale': 'Blues'})
                ],
                'scattergl': [go.Scattergl(hoverinfo='x+y')]
            }
        )

    def test_merge_0(self):
        self.assertEqual(pio.templates.merge_templates(),
                         go.layout.Template())

    def test_merge_1(self):
        self.assertEqual(pio.templates.merge_templates(self.template1),
                         self.template1)

    def test_merge_2(self):
        result = pio.templates.merge_templates(self.template1, self.template2)
        expected = self.expected1_2

        self.assertEqual(result, expected)

        # Make sure input templates weren't modified
        self.assertEqual(self.template1, self.template1_orig)
        self.assertEqual(self.template2, self.template2_orig)

    def test_merge_3(self):
        template3 = go.layout.Template(layout={'margin': {'l': 0, 'r': 0}})
        result = pio.templates.merge_templates(
            self.template1,
            self.template2,
            template3)

        expected = self.expected1_2
        expected.update(template3)
        self.assertEqual(result, expected)

        # Make sure input templates weren't modified
        self.assertEqual(self.template1, self.template1_orig)
        self.assertEqual(self.template2, self.template2_orig)

    def test_merge_by_flaglist_string(self):
        layout = go.Layout()
        layout.template = 'template1+template2'
        result = layout.template
        expected = self.expected1_2

        self.assertEqual(result, expected)

        # Make sure input templates weren't modified
        self.assertEqual(self.template1, self.template1_orig)
        self.assertEqual(self.template2, self.template2_orig)
