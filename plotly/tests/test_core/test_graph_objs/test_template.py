from __future__ import absolute_import
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
    def test_starts_as_none(self):
        fig = go.Figure()
        self.assertIsNone(fig.layout.template)

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

        fig.layout.template = {}
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

        fig.layout.template = {}
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
        self.assertIsNone(fig.layout.template)

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
        self.assertEqual(set(pio.templates), {'test_template'})
