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

        self.assertRaisesRegexp(
            PlotlyError, pres.presentation_objs.STYLE_ERROR,
            pres.Presentation, markdown_string, style='foo'
        )

    def test_open_code_block(self):
        markdown_string = """
        # one slide

        ```python
        x = 2 + 2
        print x
        """

        self.assertRaisesRegexp(
            PlotlyError, pres.presentation_objs.CODE_ENV_ERROR,
            pres.Presentation, markdown_string, style='moods'
        )

    def test_invalid_code_language(self):
        markdown_string = """
        ```foo
        x = 2 + 2
        print x
        ```
        """

        self.assertRaisesRegexp(
            PlotlyError, pres.presentation_objs.LANG_ERROR, pres.Presentation,
            markdown_string, style='moods'
        )

    def test_expected_pres(self):
        markdown_string = "# title\n---\ntransition: zoom, fade, fade\n# Colors\nColors are everywhere around us.\nPlotly(https://plot.ly/~AdamKulidjian/3564/)\nImage(https://raw.githubusercontent.com/jackparmer/gradient-backgrounds/master/moods1.png)\n```python\nx=1\n```\n---\nPlotly(https://plot.ly/~AdamKulidjian/3564/)\nPlotly(https://plot.ly/~AdamKulidjian/3564/)\nPlotly(https://plot.ly/~AdamKulidjian/3564/)\nPlotly(https://plot.ly/~AdamKulidjian/3564/)\nPlotly(https://plot.ly/~AdamKulidjian/3564/)\nPlotly(https://plot.ly/~AdamKulidjian/3564/)\nPlotly(https://plot.ly/~AdamKulidjian/3564/)\n---\n"

        my_pres = pres.Presentation(
            markdown_string, style='moods', imgStretch=True
        )

        exp_pres = {'presentation': {'paragraphStyles': {'Body': {'color': '#000016',
                                               'fontFamily': 'Roboto',
                                               'fontSize': 16,
                                               'fontStyle': 'normal',
                                               'fontWeight': 100,
                                               'lineHeight': 'normal',
                                               'minWidth': 20,
                                               'opacity': 1,
                                               'textAlign': 'center',
                                               'textDecoration': 'none',
                                               'wordBreak': 'break-word'},
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
                                      'Heading 1': {'color': '#000016',
                                                    'fontFamily': 'Roboto',
                                                    'fontSize': 55,
                                                    'fontStyle': 'normal',
                                                    'fontWeight': 900,
                                                    'lineHeight': 'normal',
                                                    'minWidth': 20,
                                                    'opacity': 1,
                                                    'textAlign': 'center',
                                                    'textDecoration': 'none'},
                                      'Heading 2': {'color': '#000016',
                                                    'fontFamily': 'Roboto',
                                                    'fontSize': 36,
                                                    'fontStyle': 'normal',
                                                    'fontWeight': 900,
                                                    'lineHeight': 'normal',
                                                    'minWidth': 20,
                                                    'opacity': 1,
                                                    'textAlign': 'center',
                                                    'textDecoration': 'none'},
                                      'Heading 3': {'color': '#000016',
                                                    'fontFamily': 'Roboto',
                                                    'fontSize': 30,
                                                    'fontStyle': 'normal',
                                                    'fontWeight': 900,
                                                    'lineHeight': 'normal',
                                                    'minWidth': 20,
                                                    'opacity': 1,
                                                    'textAlign': 'center',
                                                    'textDecoration': 'none'}},
                  'slidePreviews': [None for _ in range(496)],
                  'slides': [{'children': [{'children': ['title'],
                                            'defaultHeight': 36,
                                            'defaultWidth': 52,
                                            'id': 'CfaAzcSZE',
                                            'props': {'isQuote': False,
                                                      'listType': None,
                                                      'paragraphStyle': 'Heading 1',
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
                                                                'width': 1000.0}},
                                            'resizeVertical': False,
                                            'type': 'Text'}],
                              'id': 'ibvfOQeNy',
                              'props': {'style': {'backgroundColor': '#F7F7F7'},
                                        'transition': ['slide']}},
                             {'children': [{'children': ['Colors'],
                                            'defaultHeight': 36,
                                            'defaultWidth': 52,
                                            'id': 'YcGQJ21AY',
                                            'props': {'isQuote': False,
                                                      'listType': None,
                                                      'paragraphStyle': 'Heading 1',
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
                                                                'top': 0.0,
                                                                'width': 1000.0}},
                                            'resizeVertical': False,
                                            'type': 'Text'},
                                           {'children': ['Colors are everywhere around us.'],
                                            'defaultHeight': 36,
                                            'defaultWidth': 52,
                                            'id': 'G0tcGP89U',
                                            'props': {'isQuote': False,
                                                      'listType': None,
                                                      'paragraphStyle': 'Body',
                                                      'size': 4,
                                                      'style': {'color': '#000016',
                                                                'fontFamily': 'Roboto',
                                                                'fontSize': 16,
                                                                'fontStyle': 'normal',
                                                                'fontWeight': 100,
                                                                'height': 14.0,
                                                                'left': 25.0,
                                                                'lineHeight': 'normal',
                                                                'minWidth': 20,
                                                                'opacity': 1,
                                                                'position': 'absolute',
                                                                'textAlign': 'left',
                                                                'textDecoration': 'none',
                                                                'top': 663.0810810810812,
                                                                'width': 950.0000000000001,
                                                                'wordBreak': 'break-word'}},
                                            'resizeVertical': False,
                                            'type': 'Text'},
                                           {'children': [],
                                            'id': 'c4scRvuIe',
                                            'props': {'frameBorder': 0,
                                                      'scrolling': 'no',
                                                      'src': 'https://plot.ly/~AdamKulidjian/3564/.embed?link=false',
                                                      'style': {'height': 280.0,
                                                                'left': 0.0,
                                                                'position': 'absolute',
                                                                'top': 70.0,
                                                                'width': 330.66666666666663}},
                                            'type': 'Plotly'},
                                           {'children': [],
                                            'id': 'yScDKejKG',
                                            'props': {'height': 512,
                                                      'imageName': None,
                                                      'src': 'https://raw.githubusercontent.com/jackparmer/gradient-backgrounds/master/moods1.png',
                                                      'style': {'height': 280.0,
                                                                'left': 334.66666666666663,
                                                                'opacity': 1,
                                                                'position': 'absolute',
                                                                'top': 70.0,
                                                                'width': 330.66666666666663},
                                                      'width': 512},
                                            'type': 'Image'},
                                           {'children': [],
                                            'defaultText': 'Code',
                                            'id': 'fuUrIyVrv',
                                            'props': {'language': 'python',
                                                      'source': 'x=1\n',
                                                      'style': {'fontFamily': "Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace",
                                                                'fontSize': 13,
                                                                'height': 280.0,
                                                                'left': 669.3333333333333,
                                                                'margin': 0,
                                                                'position': 'absolute',
                                                                'textAlign': 'left',
                                                                'top': 70.0,
                                                                'width': 330.66666666666663},
                                                      'theme': 'tomorrowNight'},
                                            'type': 'CodePane'}],
                              'id': '7eG6TvKqU',
                              'props': {'style': {'backgroundColor': '#FFFFFF'},
                                        'transition': ['zoom', 'fade']}},
                             {'children': [{'children': [],
                                            'id': '83EtFjFKM',
                                            'props': {'frameBorder': 0,
                                                      'scrolling': 'no',
                                                      'src': 'https://plot.ly/~AdamKulidjian/3564/.embed?link=false',
                                                      'style': {'height': 96.57142857142857,
                                                                'left': 400.0,
                                                                'position': 'absolute',
                                                                'top': 0.0,
                                                                'width': 600.0}},
                                            'type': 'Plotly'},
                                           {'children': [],
                                            'id': 'V9vJYk8bF',
                                            'props': {'frameBorder': 0,
                                                      'scrolling': 'no',
                                                      'src': 'https://plot.ly/~AdamKulidjian/3564/.embed?link=false',
                                                      'style': {'height': 96.57142857142857,
                                                                'left': 400.0,
                                                                'position': 'absolute',
                                                                'top': 100.57142857142856,
                                                                'width': 600.0}},
                                            'type': 'Plotly'},
                                           {'children': [],
                                            'id': 'DzCfXMyhv',
                                            'props': {'frameBorder': 0,
                                                      'scrolling': 'no',
                                                      'src': 'https://plot.ly/~AdamKulidjian/3564/.embed?link=false',
                                                      'style': {'height': 96.57142857142857,
                                                                'left': 400.0,
                                                                'position': 'absolute',
                                                                'top': 201.1428571428571,
                                                                'width': 600.0}},
                                            'type': 'Plotly'},
                                           {'children': [],
                                            'id': 'YFf7M2BON',
                                            'props': {'frameBorder': 0,
                                                      'scrolling': 'no',
                                                      'src': 'https://plot.ly/~AdamKulidjian/3564/.embed?link=false',
                                                      'style': {'height': 96.57142857142857,
                                                                'left': 400.0,
                                                                'position': 'absolute',
                                                                'top': 301.71428571428567,
                                                                'width': 600.0}},
                                            'type': 'Plotly'},
                                           {'children': [],
                                            'id': 'CARvApdzw',
                                            'props': {'frameBorder': 0,
                                                      'scrolling': 'no',
                                                      'src': 'https://plot.ly/~AdamKulidjian/3564/.embed?link=false',
                                                      'style': {'height': 96.57142857142857,
                                                                'left': 400.0,
                                                                'position': 'absolute',
                                                                'top': 402.2857142857142,
                                                                'width': 600.0}},
                                            'type': 'Plotly'},
                                           {'children': [],
                                            'id': '194ZxaSko',
                                            'props': {'frameBorder': 0,
                                                      'scrolling': 'no',
                                                      'src': 'https://plot.ly/~AdamKulidjian/3564/.embed?link=false',
                                                      'style': {'height': 96.57142857142857,
                                                                'left': 400.0,
                                                                'position': 'absolute',
                                                                'top': 502.85714285714283,
                                                                'width': 600.0}},
                                            'type': 'Plotly'},
                                           {'children': [],
                                            'id': 'SOwRH1rLV',
                                            'props': {'frameBorder': 0,
                                                      'scrolling': 'no',
                                                      'src': 'https://plot.ly/~AdamKulidjian/3564/.embed?link=false',
                                                      'style': {'height': 96.57142857142857,
                                                                'left': 400.0,
                                                                'position': 'absolute',
                                                                'top': 603.4285714285713,
                                                                'width': 600.0}},
                                            'type': 'Plotly'}],
                              'id': 'S6VmZlI5Q',
                              'props': {'style': {'backgroundColor': '#FFFFFF'},
                                        'transition': ['slide']}}],
                  'version': '0.1.3'}}

        for k in ['version', 'paragraphStyles', 'slidePreviews']:
            self.assertEqual(
                my_pres['presentation'][k],
                exp_pres['presentation'][k]
            )

        self.assertEqual(
            len(my_pres['presentation']['slides']),
            len(exp_pres['presentation']['slides'])
        )

        for slide_idx in range(len(my_pres['presentation']['slides'])):
            childs = my_pres['presentation']['slides'][slide_idx]['children']
            # transitions and background color
            self.assertEqual(
                my_pres['presentation']['slides'][slide_idx]['props'],
                exp_pres['presentation']['slides'][slide_idx]['props']
            )
            for child_idx in range(len(childs)):
                # check urls
                if (my_pres['presentation']['slides'][slide_idx]['children']
                    [child_idx]['type'] in ['Image', 'Plotly']):
                    self.assertEqual(
                        (my_pres['presentation']['slides'][slide_idx]
                         ['children'][child_idx]['props']),
                        (exp_pres['presentation']['slides'][slide_idx]
                         ['children'][child_idx]['props'])
                    )

                # styles in children
                self.assertEqual(
                    (my_pres['presentation']['slides'][slide_idx]
                     ['children'][child_idx]['props']),
                    (exp_pres['presentation']['slides'][slide_idx]
                     ['children'][child_idx]['props'])
                )
