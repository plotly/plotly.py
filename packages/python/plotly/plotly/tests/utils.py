import copy
from numbers import Number as Num
from unittest import TestCase
import plotly.io as pio


class TestCaseNoTemplate(TestCase):
    def setUp(self):
        pio.templates.default = None

    def tearDown(self):
        pio.templates.default = "plotly"


def compare_dict(dict1, dict2, equivalent=True, msg="", tol=10e-8):
    for key in dict1:
        if key not in dict2:
            return (
                False,
                "{0} should be {1}".format(list(dict1.keys()), list(dict2.keys())),
            )
    for key in dict1:
        if isinstance(dict1[key], dict):
            equivalent, msg = compare_dict(dict1[key], dict2[key], tol=tol)
        elif isinstance(dict1[key], Num) and isinstance(dict2[key], Num):
            if not comp_nums(dict1[key], dict2[key], tol):
                return (
                    False,
                    "['{0}'] = {1} should be {2}".format(key, dict1[key], dict2[key]),
                )
        elif is_num_list(dict1[key]) and is_num_list(dict2[key]):
            if not comp_num_list(dict1[key], dict2[key], tol):
                return (
                    False,
                    "['{0}'] = {1} should be {2}".format(key, dict1[key], dict2[key]),
                )
        elif not (dict1[key] == dict2[key]):
            return (
                False,
                "['{0}'] = {1} should be {2}".format(key, dict1[key], dict2[key]),
            )
        if not equivalent:
            return False, "['{0}']".format(key) + msg
    return equivalent, msg


def strip_dict_params(d1, d2, ignore=["uid"]):
    """
    Helper function for assert_dict_equal

    Nearly duplicate of assert_fig_equal in plotly/tests/test_optional/optional_utils.py
    Removes `ignore` params from d1 and/or d2 if they exist
    then returns stripped dictionaries

    :param (list|tuple) ignore: sequence of key names as
        strings that are removed from both d1 and d2 if
        they exist
    """
    # deep copy d1 and d2
    if "to_plotly_json" in dir(d1):
        d1_copy = copy.deepcopy(d1.to_plotly_json())
    else:
        d1_copy = copy.deepcopy(d1)

    if "to_plotly_json" in dir(d2):
        d2_copy = copy.deepcopy(d2.to_plotly_json())
    else:
        d2_copy = copy.deepcopy(d2)

    for key in ignore:
        if key in d1_copy.keys():
            del d1_copy[key]
        if key in d2_copy.keys():
            del d2_copy[key]

    return d1_copy, d2_copy


def comp_nums(num1, num2, tol=10e-8):
    return abs(num1 - num2) < tol


def comp_num_list(list1, list2, tol=10e-8):
    for item1, item2 in zip(list1, list2):
        if not comp_nums(item1, item2, tol):
            return False
    return True


def is_num_list(item):
    try:
        for thing in item:
            if not isinstance(thing, Num):
                raise TypeError
    except TypeError:
        return False
    return True
