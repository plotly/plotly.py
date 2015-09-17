"""
test_get_requests:
==================

A module intended for use with Nose.

"""
import copy
import json
import requests

import six
from nose.plugins.attrib import attr


default_headers = {'plotly-username': '',
                   'plotly-apikey': '',
                   'plotly-version': '2.0',
                   'plotly-platform': 'pythonz'}

server = "https://plot.ly"

# username = "get_test_user"
# password = "password"
# api_key = "vgs6e0cnoi" (currently...)


@attr('slow')
def test_user_does_not_exist():
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
        content = json.loads(response.content.decode('unicode_escape'))
    else:
        content = json.loads(response.content)
    print(response.status_code)
    print(content)
    assert response.status_code == 404
    assert (content['error'] == "Aw, snap! We don't have an account for {0}. "
                                "Want to try again? Sign in is not case "
                                "sensitive.".format(username))


@attr('slow')
def test_file_does_not_exist():
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
        content = json.loads(response.content.decode('unicode_escape'))
    else:
        content = json.loads(response.content)
    print(response.status_code)
    print(content)
    assert response.status_code == 404
    assert (content['error'] == "Aw, snap! It looks like this file does not "
                                "exist. Want to try again?")


@attr('slow')
def test_wrong_api_key():  # TODO: does this test the right thing?
    username = 'PlotlyImageTest'
    api_key = 'invalid-apikey'
    file_owner = 'get_test_user'
    file_id = 0
    hd = copy.copy(default_headers)
    hd['plotly-username'] = username
    hd['plotly-apikey'] = api_key
    resource = "/apigetfile/{0}/{1}/".format(file_owner, file_id)
    response = requests.get(server + resource, headers=hd)
    assert response.status_code == 401
    # TODO: check error message?


# Locked File
# TODO

@attr('slow')
def test_private_permission_defined():
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
        content = json.loads(response.content.decode('unicode_escape'))
    else:
        content = json.loads(response.content)
    print(response.status_code)
    print(content)
    assert response.status_code == 403

# Private File that is shared
# TODO


@attr('slow')
def test_missing_headers():
    file_owner = 'get_test_user'
    file_id = 0
    resource = "/apigetfile/{0}/{1}/".format(file_owner, file_id)
    headers = list(default_headers.keys())
    for header in headers:
        hd = copy.copy(default_headers)
        del hd[header]
        response = requests.get(server + resource, headers=hd)
        if six.PY3:
            content = json.loads(response.content.decode('unicode_escape'))
        else:
            content = json.loads(response.content)
        print(response.status_code)
        print(content)
        assert response.status_code == 422


@attr('slow')
def test_valid_request():
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
        content = json.loads(response.content.decode('unicode_escape'))
    else:
        content = json.loads(response.content)
    print(response.status_code)
    print(content)
    assert response.status_code == 200
    # content = json.loads(res.content)
    # response_payload = content['payload']
    # figure = response_payload['figure']
    # if figure['data'][0]['x'] != [u'1', u'2', u'3']:
    #     print('ERROR')
    # return res
