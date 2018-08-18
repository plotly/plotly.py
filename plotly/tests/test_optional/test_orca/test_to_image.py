from unittest import TestCase
import plotly.io as pio
import plotly.graph_objs as go
import os

images_dir = 'plotly/tests/test_optional/test_orca/images/'

# These formats are deterministic. PDF and svg don't seem to be
image_formats = ['png', 'jpg', 'jpeg', 'webp', 'eps']


class ToImageTests(TestCase):
    def setUp(self):
        pio.orca.reset_orca_status()
        pio.orca.config.restore_defaults()

    def assertImg(self, img_bytes, file_name, _raise=True):
        expected_img_path = images_dir + file_name

        try:
            with open(expected_img_path, 'rb') as f:
                expected = f.read()

            self.assertEqual(expected, img_bytes)
        except (FileNotFoundError, AssertionError) as e:
            failed_dir = images_dir + 'failed/'
            if not os.path.exists(failed_dir):
                os.mkdir(failed_dir)

            with open(failed_dir + file_name, 'wb') as f:
                f.write(img_bytes)

            if _raise:
                raise e

    def testSimpleToPng(self):
        fig = go.Figure(data=[
            go.Bar(y=[2, 1, 4],
                   marker=go.bar.Marker(color='purple',
                                        opacity=0.7)),
            go.Scattergl(y=[3, 4, 2])
        ])

        for ext in image_formats:
            img_bytes = pio.to_image(fig, format=ext)
            self.assertImg(img_bytes, 'fig1.' + ext)


