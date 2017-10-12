"""
test_spectacle_presentation:
==========

A module intended for use with Nose.

"""
from __future__ import absolute_import

from unittest import TestCase
from plotly.exceptions import PlotlyError
import plotly.presentation_objs as pres


class TestPresentation(TestCase):

    def test_invalid_style(self):
        markdown_string = """
        # one slide
        """

        message = 'Your presentation style must be moods or martik.'

        self.assertRaisesRegexp(PlotlyError, message, pres.Presentation,
                                markdown_string, style='foo')

    def test_open_code_block(self):
        markdown_string = """
        # one slide

        ```python
        x = 2 + 2
        print x
        """

        message = (
            "If you are putting a block of code into your markdown "
            "presentation, make sure your denote the start and end "
            "of the code environment with the '```' characters. For "
            "example, your markdown string would include something "
            "like:\n\n```python\nx = 2\ny = 1\nprint x\n```\n\n"
            "Notice how the language that you want the code to be "
            "displayed in is immediately to the right of first "
            "entering '```', i.e. '```python'."
        )

        self.assertRaisesRegexp(PlotlyError, message, pres.Presentation,
                                markdown_string, style='moods')

    def test_invalid_code_language(self):
        markdown_string = """
        ```foo
        x = 2 + 2
        print x
        ```
        """

        message = (
            "The language of your code block should be "
            "clearly indicated after the first ``` that "
            "begins the code block. The valid languages to "
            "choose from are" + pres.presentation_objs.list_of_options(
                pres.presentation_objs.VALID_LANGUAGES
            )
        )

        self.assertRaisesRegexp(PlotlyError, message, pres.Presentation,
                                markdown_string, style='moods')

    def test_expected_pres(self):
        markdown_string_empty = "\n#title\n"

        my_pres = pres.Presentation(markdown_string_empty, style='moods')

        exp_pres = {
            'presentation': {'paragraphStyles': {'Body': {'color': '#3d3d3d',
            'fontFamily': 'Open Sans',
            'fontSize': 11,
            'fontStyle': 'normal',
            'fontWeight': 400,
            'lineHeight': 'normal',
            'minWidth': 20,
            'opacity': 1,
            'textAlign': 'center',
            'textDecoration': 'none'},
           'Body Small': {'color': '#3d3d3d',
            'fontFamily': 'Open Sans',
            'fontSize': 10,
            'fontStyle': 'normal',
            'fontWeight': 400,
            'lineHeight': 'normal',
            'minWidth': 20,
            'opacity': 1,
            'textAlign': 'center',
            'textDecoration': 'none'},
           'Caption': {'color': '#3d3d3d',
            'fontFamily': 'Open Sans',
            'fontSize': 11,
            'fontStyle': 'italic',
            'fontWeight': 400,
            'lineHeight': 'normal',
            'minWidth': 20,
            'opacity': 1,
            'textAlign': 'center',
            'textDecoration': 'none'},
           'Heading 1': {'color': '#3d3d3d',
            'fontFamily': 'Open Sans',
            'fontSize': 26,
            'fontStyle': 'normal',
            'fontWeight': 400,
            'lineHeight': 'normal',
            'minWidth': 20,
            'opacity': 1,
            'textAlign': 'center',
            'textDecoration': 'none'},
           'Heading 2': {'color': '#3d3d3d',
            'fontFamily': 'Open Sans',
            'fontSize': 20,
            'fontStyle': 'normal',
            'fontWeight': 400,
            'lineHeight': 'normal',
            'minWidth': 20,
            'opacity': 1,
            'textAlign': 'center',
            'textDecoration': 'none'},
           'Heading 3': {'color': '#3d3d3d',
            'fontFamily': 'Open Sans',
            'fontSize': 11,
            'fontStyle': 'normal',
            'fontWeight': 700,
            'lineHeight': 'normal',
            'minWidth': 20,
            'opacity': 1,
            'textAlign': 'center',
            'textDecoration': 'none'}},
          'slidePreviews': [None for k in range(496)],
          'slides': [{'children': [{'children': ['title'],
                      'defaultHeight': 36,
                      'defaultWidth': 52,
                      'id': '9fBxmzeaD',
                      'props': {'isQuote': False,
                       'listType': None,
                       'paragraphStyle': 'Body',
                       'size': 4,
                       'style': {'color': '#000016',
                        'fontFamily': 'Roboto',
                        'fontSize': 55,
                        'fontStyle': 'normal',
                        'fontWeight': 900,
                        'height': 140.0,
                        'left': 0.0,
                        'lineHeight': 'normal',
                        'minWidth': 20,
                        'opacity': 1,
                        'position': 'absolute',
                        'textAlign': 'center',
                        'textDecoration': 'none',
                        'top': 350.0,
                        'width': 1000.0,
                        'wordBreak': 'break-word'}},
                      'resizeVertical': False,
                      'type': 'Text'}],
                    'id': 'ZtIZUDyv6',
                    'props': {'style': {'backgroundColor': '#F7F7F7'},
                     'transition': ['slide']}}],
          'version': '0.1.3'}
        }

        self.assertEqual(
            my_pres['presentation']['version'],
            exp_pres['presentation']['version']
        )

        self.assertEqual(
            my_pres['presentation']['paragraphStyles'],
            exp_pres['presentation']['paragraphStyles']
        )

        self.assertEqual(
            my_pres['presentation']['slidePreviews'],
            exp_pres['presentation']['slidePreviews']
        )

        self.assertEqual(
            len(my_pres['presentation']['slides']),
            len(exp_pres['presentation']['slides'])
        )

        self.assertEqual(
            my_pres['presentation']['slides'][0].keys(),
            exp_pres['presentation']['slides'][0].keys()
        )

        self.assertEqual(
            my_pres['presentation']['slides'][0]['props'],
            exp_pres['presentation']['slides'][0]['props']
        )

        for key in my_pres['presentation']['slides'][0]['children'][0].keys():
            if key not in ['id', 'props']:
                self.assertEqual(
                    my_pres['presentation']['slides'][0]['children'][0][key],
                    exp_pres['presentation']['slides'][0]['children'][0][key]
                )

        self.assertEqual(
            my_pres['presentation']['slides'][0]['children'][0]['props'],
            exp_pres['presentation']['slides'][0]['children'][0]['props']
        )
