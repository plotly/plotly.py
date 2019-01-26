from unittest import TestCase

import plotly.graph_objs as go
import plotly.graph_reference as gr

OLD_CLASS_NAMES = ['AngularAxis', 'Annotation', 'Annotations', 'Area',
                   'Bar', 'Box', 'ColorBar', 'Contour', 'Contours',
                   'Data', 'ErrorX', 'ErrorY', 'ErrorZ', 'Figure',
                   'Font', 'Frame', 'Frames', 'Heatmap', 'Histogram',
                   'Histogram2d', 'Histogram2dContour', 'Layout', 'Legend',
                   'Line', 'Margin', 'Marker', 'RadialAxis', 'Scatter',
                   'Scatter3d', 'Scene', 'Stream', 'Surface', 'Trace',
                   'XAxis', 'XBins', 'YAxis', 'YBins', 'ZAxis']


class TestBackwardsCompat(TestCase):

    def test_old_class_names(self):

        # these were all defined at one point, we want to maintain backwards
        # compat, so we basically just create a checkpoint with this test.

        for class_name in OLD_CLASS_NAMES:
            self.assertIn(class_name, go.__dict__.keys())

    def test_title_as_string_layout(self):
        """
        Prior to plotly.js 1.43.0 title properties were strings, in 1.43.0
        these title properties became compound objects with a text property.

        For backwards compatibility, we still need to support setting this
        title object as a string or number
        """
        layout_title_parents = [
            go.Layout(),
            go.layout.XAxis(),
            go.layout.YAxis(),
            go.layout.ternary.Aaxis(),
            go.layout.ternary.Baxis(),
            go.layout.ternary.Caxis(),
            go.layout.scene.XAxis(),
            go.layout.scene.YAxis(),
            go.layout.scene.ZAxis(),
            go.layout.polar.RadialAxis(),
            go.scatter.marker.ColorBar(),
            go.cone.ColorBar()
         ]

        for obj in layout_title_parents:
            obj.title = 'A title'

            self.assertEqual(obj.title.text, 'A title')
            self.assertEqual(obj.to_plotly_json(),
                             {'title': {'text': 'A title'}})

            # And update
            obj.update(title='A title 2')
            self.assertEqual(obj.title.text, 'A title 2')
            self.assertEqual(obj.to_plotly_json(),
                             {'title': {'text': 'A title 2'}})

            # Update titlefont
            obj.update(titlefont={'size': 23})
            self.assertEqual(obj.title.font.size, 23)
            self.assertEqual(obj.to_plotly_json(),
                             {'title':
                                  {'text': 'A title 2',
                                   'font': {'size': 23}}})

        # Pie
        obj = go.Pie()
        obj.title = 'A title'
        self.assertEqual(obj.title.text, 'A title')
        self.assertEqual(obj.to_plotly_json(),
                         {'title': {'text': 'A title'},
                          'type': 'pie'})

        # And update
        obj.update(title='A title 2')
        self.assertEqual(obj.title.text, 'A title 2')
        self.assertEqual(obj.to_plotly_json(),
                         {'type': 'pie',
                          'title': {'text': 'A title 2'}})

        # Update titlefont
        obj.update(titlefont={'size': 23})
        self.assertEqual(obj.title.font.size, 23)
        self.assertEqual(obj.to_plotly_json(),
                         {'type': 'pie',
                          'title':
                              {'text': 'A title 2',
                               'font': {'size': 23}}})

    def test_legacy_title_props_remapped(self):

        # plain Layout
        obj = go.Layout()
        self.assertIs(obj.titlefont, obj.title.font)
        self.assertIsNone(obj.title.font.family)

        # Set titlefont in constructor
        obj = go.Layout(titlefont={'family': 'Courier'})
        self.assertIs(obj.titlefont, obj.title.font)
        self.assertEqual(obj.titlefont.family, 'Courier')
        self.assertEqual(obj.title.font.family, 'Courier')

        # Property assignment
        obj = go.Layout()
        obj.titlefont.family = 'Courier'
        self.assertIs(obj.titlefont, obj.title.font)
        self.assertEqual(obj['titlefont.family'], 'Courier')
        self.assertEqual(obj.title.font.family, 'Courier')

        # In/Iter
        self.assertIn('titlefont', obj)
        self.assertIn('titlefont.family', obj)
        self.assertIn('titlefont', iter(obj))


class TestGraphObjs(TestCase):

    def test_traces_should_be_defined(self):

        # we *always* want to create classes for traces

        class_names = [gr.string_to_class_name(object_name)
                       for object_name in gr.TRACE_NAMES]
        for class_name in class_names:
            self.assertIn(class_name, go.__dict__.keys())

    def test_no_new_classes(self):

        # for maintenance reasons, we don't want to generate new class defs

        expected_class_names = {gr.string_to_class_name(object_name)
                                for object_name in gr.TRACE_NAMES}
        expected_class_names.update(OLD_CLASS_NAMES)

        # assume that CapitalCased keys are the classes we defined
        current_class_names = {key for key in go.__dict__.keys()
                               if key[0].isupper()}
        if 'FigureWidget' in go.__dict__.keys():
            expected_class_names.add('FigureWidget')
        self.assertEqual(current_class_names, expected_class_names)
