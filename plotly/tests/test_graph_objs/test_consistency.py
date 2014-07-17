"""
test_consistency:
================

A module intended for use with Nose. Check that items in graph_objs_meta.json
are properly defined in both graph_objs.py and included in the mapping dicts.

"""
from ... graph_objs import graph_objs


def test_info_keys_in_key_to_name():
    for key in graph_objs.INFO:
        class_name = graph_objs.KEY_TO_NAME[key]


def test_names_in_name_to_key():
    for key in graph_objs.INFO:
        class_name = graph_objs.KEY_TO_NAME[key]
        key_name = graph_objs.NAME_TO_KEY[class_name]


def test_names_in_name_to_class():
    for key in graph_objs.INFO:
        class_name = graph_objs.KEY_TO_NAME[key]
        _class = graph_objs.NAME_TO_CLASS[class_name]
