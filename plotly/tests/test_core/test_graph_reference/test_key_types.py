"""
test_key_types:
===============

A module intended for use with Nose.

"""
from __future__ import absolute_import

import plotly.graph_objs.graph_objs as go


def test_style_exists():
    checks = True
    for obj, stuff in list(go.INFO.items()):
        if obj not in ['plotlylist', 'data', 'annotations', 'plotlydict', 'plotlytrace', 'trace']:
            for attr_key, attr in list(stuff['keymeta'].items()):
                if 'key_type' not in attr:
                    checks = False
                    print(obj_key, attr_key)
    if not checks:
        raise Exception
