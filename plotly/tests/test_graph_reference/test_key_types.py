"""
test_key_types:
===============

A module intended for use with Nose.

"""
import plotly.graph_objs.graph_objs as go


def test_style_exists():
    checks = True
    for obj_key, obj in list(go.INFO.items()):
        if obj_key not in ['plotlylist', 'data', 'annotations', 'plotlydict', 'plotlytrace', 'trace']:
            for attr_key, attr in list(obj.items()):
                if 'type' not in attr:
                    checks = False
                    print(obj_key, attr_key)
    if not checks:
        raise Exception