import copy
from numbers import Number as Num
from unittest import TestCase

from plotly import files, session, utils


class PlotlyTestCase(TestCase):

    # parent test case to assist with clean up of local credentials/config

    def __init__(self, *args, **kwargs):
        self._credentials = None
        self._config = None
        self._graph_reference = None
        self._session = None
        super(PlotlyTestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        session._session = {
            'credentials': {},
            'config': {},
            'plot_options': {}
        }

    def setUp(self):
        self.stash_session()
        self.stash_files()
        defaults = dict(files.FILE_CONTENT[files.CREDENTIALS_FILE],
                        **files.FILE_CONTENT[files.CONFIG_FILE])
        session.sign_in(**defaults)

    def tearDown(self):
        self.restore_files()
        self.restore_session()

    def stash_files(self):
        if files.check_file_permissions():
            self._credentials = utils.load_json_dict(files.CREDENTIALS_FILE)
            self._config = utils.load_json_dict(files.CONFIG_FILE)

    def restore_files(self):
        if files.check_file_permissions():
            if self._credentials is not None:
                utils.save_json_dict(files.CREDENTIALS_FILE, self._credentials)
            if self._config is not None:
                utils.save_json_dict(files.CONFIG_FILE, self._config)

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
