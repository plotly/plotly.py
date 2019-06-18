import copy
from unittest import TestCase

from chart_studio import session, files, utils
from plotly.files import ensure_writable_plotly_dir


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
        session._session = {"credentials": {}, "config": {}, "plot_options": {}}

    def setUp(self):
        self.stash_session()
        self.stash_files()
        defaults = dict(
            files.FILE_CONTENT[files.CREDENTIALS_FILE],
            **files.FILE_CONTENT[files.CONFIG_FILE]
        )
        session.sign_in(**defaults)

    def tearDown(self):
        self.restore_files()
        self.restore_session()

    def stash_files(self):
        self._credentials = utils.load_json_dict(files.CREDENTIALS_FILE)
        self._config = utils.load_json_dict(files.CONFIG_FILE)

    def restore_files(self):
        if self._credentials and ensure_writable_plotly_dir():
            utils.save_json_dict(files.CREDENTIALS_FILE, self._credentials)
        if self._config and ensure_writable_plotly_dir():
            utils.save_json_dict(files.CONFIG_FILE, self._config)

    def stash_session(self):
        self._session = copy.deepcopy(session._session)

    def restore_session(self):
        session._session.clear()  # clear and update to preserve references.
        session._session.update(self._session)
