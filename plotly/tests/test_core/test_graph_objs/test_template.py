from __future__ import absolute_import
from unittest import TestCase
from nose.tools import raises

import plotly.graph_objs as go


class TemplateTest(TestCase):

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
