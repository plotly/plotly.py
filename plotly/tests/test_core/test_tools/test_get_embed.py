from __future__ import absolute_import

from unittest import TestCase

from nose.tools import raises

import plotly.tools as tls
from plotly.exceptions import PlotlyError


def test_get_valid_embed():
    url = 'https://plot.ly/~PlotBot/82/'
    tls.get_embed(url)


@raises(PlotlyError)
def test_get_invalid_embed():
    url = 'https://plot.ly/~PlotBot/a/'
    tls.get_embed(url)


class TestGetEmbed(TestCase):

    def test_get_embed_url_with_share_key(self):

        # Check the embed url for url with share_key included

        get_embed_return = tls.get_embed('https://plot.ly/~neda/6572' +
                                         '?share_key=AH4MyPlyDyDWYA2cM2kj2m')
        expected_get_embed = ("<iframe id=\"igraph\" scrolling=\"no\" "
                              "style=\"border:none;\" seamless=\"seamless\" "
                              "src=\"{plotly_rest_url}/"
                              "~{file_owner}/{file_id}.embed?"
                              "share_key={share_key}\" "
                              "height=\"{iframe_height}\" "
                              "width=\"{iframe_width}\">"
                              "</iframe>").format(plotly_rest_url="https://" +
                                                                  "plot.ly",
                                                  file_owner="neda",
                                                  file_id="6572",
                                                  share_key="AH4MyPlyDyDWYA2" +
                                                            "cM2kj2m",
                                                  iframe_height=525,
                                                  iframe_width="100%")
        self.assertEqual(get_embed_return, expected_get_embed)
