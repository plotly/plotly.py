import copy
import json
from numbers import Number as Num
from unittest import TestCase

from plotly import session
from plotly.tools import CREDENTIALS_FILE, CONFIG_FILE, _file_permissions


class PlotlyTestCase(TestCase):

    # parent test case to assist with clean up of local credentials/config

    def __init__(self, **kwargs):
        self._file_credentials = None
        self._file_config = None
        self._session = None
        super(PlotlyTestCase, self).__init__(**kwargs)

    def setUp(self):
        self.stash_file_credentials_and_config()

    def tearDown(self):
        self.restore_file_credentials_and_config()

    def stash_file_credentials_and_config(self):
        if _file_permissions:
            with open(CREDENTIALS_FILE, 'r') as f:
                self._file_credentials = json.load(f)
            with open(CONFIG_FILE, 'r') as f:
                self._file_config = json.load(f)

    def restore_file_credentials_and_config(self):
        if _file_permissions:
            if self._file_credentials is not None:
                with open(CREDENTIALS_FILE, 'w') as f:
                    json.dump(self._file_credentials, f)
            if self._file_config is not None:
                with open(CONFIG_FILE, 'w') as f:
                    json.load(self._file_config, f)

    def stash_session(self):
        self._session = copy.deepcopy(session._session)

    def restore_session(self):
        session._session.clear()  # clear and update to preserve references.
        session._session.update(self._session)


def compare_dict(dict1, dict2, equivalent=True, msg='', tol=10e-8):
    for key in dict1:
        if key not in dict2:
            return (False,
                    "{0} should be {1}".format(
                        list(dict1.keys()), list(dict2.keys())))
    for key in dict1:
        if isinstance(dict1[key], dict):
            equivalent, msg = compare_dict(dict1[key],
                                           dict2[key],
                                           tol=tol)
        elif isinstance(dict1[key], Num) and isinstance(dict2[key], Num):
            if not comp_nums(dict1[key], dict2[key], tol):
                return False, "['{0}'] = {1} should be {2}".format(key,
                                                                   dict1[key],
                                                                   dict2[key])
        elif is_num_list(dict1[key]) and is_num_list(dict2[key]):
            if not comp_num_list(dict1[key], dict2[key], tol):
                return False, "['{0}'] = {1} should be {2}".format(key,
                                                                   dict1[key],
                                                                   dict2[key])
        elif not (dict1[key] == dict2[key]):
                return False, "['{0}'] = {1} should be {2}".format(key,
                                                                   dict1[key],
                                                                   dict2[key])
        if not equivalent:
            return False, "['{0}']".format(key) + msg
    return equivalent, msg


def comp_nums(num1, num2, tol=10e-8):
    return abs(num1-num2) < tol


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
