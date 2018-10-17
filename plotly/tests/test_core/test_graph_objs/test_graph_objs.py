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
