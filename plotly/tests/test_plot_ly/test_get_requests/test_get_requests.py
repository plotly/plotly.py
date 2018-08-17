"""
test_get_requests:
==================

A module intended for use with Nose.

"""
import copy

import requests
import six
from nose.plugins.attrib import attr
from requests.compat import json as _json

from plotly.tests.utils import PlotlyTestCase

default_headers = {'plotly-username': '',
                   'plotly-apikey': '',
                   'plotly-version': '2.0',
                   'plotly-platform': 'pythonz'}

server = "https://plot.ly"


class GetRequestsTest(PlotlyTestCase):

    @attr('slow')
    def test_user_does_not_exist(self):
        username = 'user_does_not_exist'
        api_key = 'invalid-apikey'
        file_owner = 'get_test_user'
        file_id = 0
        hd = copy.copy(default_headers)
        hd['plotly-username'] = username
        hd['plotly-apikey'] = api_key
        resource = "/apigetfile/{0}/{1}/".format(file_owner, file_id)
        response = requests.get(server + resource, headers=hd)
        if six.PY3:
            content = _json.loads(response.content.decode('unicode_escape'))
        else:
            content = _json.loads(response.content)
        error_message = ("Aw, snap! We don't have an account for {0}. Want to "
                         "try again? Sign in is not case sensitive."
                         .format(username))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(content['error'], error_message)

    @attr('slow')
    def test_file_does_not_exist(self):
        username = 'PlotlyImageTest'
        api_key = '786r5mecv0'
        file_owner = 'get_test_user'
        file_id = 1000
        hd = copy.copy(default_headers)
        hd['plotly-username'] = username
        hd['plotly-apikey'] = api_key
        resource = "/apigetfile/{0}/{1}/".format(file_owner, file_id)
        response = requests.get(server + resource, headers=hd)
        if six.PY3:
            content = _json.loads(response.content.decode('unicode_escape'))
        else:
            content = _json.loads(response.content)
        error_message = ("Aw, snap! It looks like this file does "
                         "not exist. Want to try again?")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(content['error'], error_message)

    @attr('slow')
    def test_wrong_api_key(self):  # TODO: does this test the right thing?
        username = 'PlotlyImageTest'
        api_key = 'invalid-apikey'
        file_owner = 'get_test_user'
        file_id = 0
        hd = copy.copy(default_headers)
        hd['plotly-username'] = username
        hd['plotly-apikey'] = api_key
        resource = "/apigetfile/{0}/{1}/".format(file_owner, file_id)
        response = requests.get(server + resource, headers=hd)
        self.assertEqual(response.status_code, 401)
        # TODO: check error message?

    # Locked File
    # TODO

    @attr('slow')
    def test_private_permission_defined(self):
        username = 'PlotlyImageTest'
        api_key = '786r5mecv0'
        file_owner = 'get_test_user'
        file_id = 1  # 1 is a private file
        hd = copy.copy(default_headers)
        hd['plotly-username'] = username
        hd['plotly-apikey'] = api_key
        resource = "/apigetfile/{0}/{1}/".format(file_owner, file_id)
        response = requests.get(server + resource, headers=hd)
        if six.PY3:
            content = _json.loads(response.content.decode('unicode_escape'))
        else:
            content = _json.loads(response.content)
        self.assertEqual(response.status_code, 403)

    # Private File that is shared
    # TODO

    @attr('slow')
    def test_missing_headers(self):
        file_owner = 'get_test_user'
        file_id = 0
        resource = "/apigetfile/{0}/{1}/".format(file_owner, file_id)
        headers = list(default_headers.keys())
        for header in headers:
            hd = copy.copy(default_headers)
            del hd[header]
            response = requests.get(server + resource, headers=hd)
            if six.PY3:
                content = _json.loads(response.content.decode('unicode_escape'))
            else:
                content = _json.loads(response.content)
            self.assertEqual(response.status_code, 422)

    @attr('slow')
    def test_valid_request(self):
        username = 'PlotlyImageTest'
        api_key = '786r5mecv0'
        file_owner = 'get_test_user'
        file_id = 0
        hd = copy.copy(default_headers)
        hd['plotly-username'] = username
        hd['plotly-apikey'] = api_key
        resource = "/apigetfile/{0}/{1}/".format(file_owner, file_id)
        response = requests.get(server + resource, headers=hd)
        if six.PY3:
            content = _json.loads(response.content.decode('unicode_escape'))
        else:
            content = _json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        # content = _json.loads(res.content)
        # response_payload = content['payload']
        # figure = response_payload['figure']
        # if figure['data'][0]['x'] != [u'1', u'2', u'3']:
        #     print('ERROR')
        # return res
