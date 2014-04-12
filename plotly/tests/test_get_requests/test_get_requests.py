"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import requests
from copy import copy
import json


default_headers = {'plotly-username': '',
                   'plotly-apikey': '',
                   'plotly-version': '2.0',
                   'plotly-platform': 'pythonz'}


def get_figure(file_owner='get_test_user', file_id=0,
               headers=default_headers):

    server = "http://ec2-54-196-84-85.compute-1.amazonaws.com"
    resource = "/apigetfile/"\
    "{username}/{file_id}/"\
        .format(username=file_owner, file_id=file_id)

    print server+resource

    response = requests.get(server + resource, headers=headers)

    return response

# User Does Not Exist
def test_RequestorDoesNotExist():
    hd = copy(default_headers)
    hd['plotly-username'] = 'this_username_doesnt_exist'
    res = get_figure(headers=hd)
    if res.status_code != 404:
        print 'ERROR'

    return res

# File Does Not Exist
def test_FileDoesNotExist():
    res = get_figure('this_username_doesnt_exist', 0, default_headers)
    if res.status_code != 404:
        print 'ERROR'

    return res

# Wrong API Key
def test_WrongAPIKey():
    hd = copy(default_headers)
    hd['plotly-apikey'] = 'this_is_the_wrong_api_key'
    res = get_figure(headers=hd)
    if res.status_code != 401:
        print 'ERROR'

    return res

# Locked File
# TODO

# Private File
def test_PrivatePermissionDefined():
    file_owner = 'get_test_user'
    file_id = 1
    res = get_figure(file_owner, file_id)
    if res.status_code != 403:
        print 'ERROR'
    return res

# Private File that is shared
# TODO

# Missing Headers
def test_MissingHeaders():
    hd = copy(default_headers)
    del hd['plotly-apikey']
    res = get_figure(headers=hd)
    if res.status_code != 422:
        print 'ERROR'

    return res

# Valid Retrieval - Self
def test_ValidRetrieval():
    res = get_figure()
    if res.status_code != 200:
        print 'ERROR'
        return res
    content = json.loads(res.content)
    response_payload = content['payload']
    figure = response_payload['figure']
    if figure['data'][0]['x'] != [u'1', u'2', u'3']:
        print 'ERROR'
    return res

test_RequestorDoesNotExist()
test_FileDoesNotExist()
test_WrongAPIKey()
test_PrivatePermissionDefined()
test_MissingHeaders()
test_ValidRetrieval()
