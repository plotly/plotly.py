"""
A module wrapping the Plotly API's REST resources.

"""
from __future__ import absolute_import

import base64
import json

import requests
import six

from plotly.version import __version__

api_domain = 'api.plot.ly'
api_version = 'v2'


class BaseResource(object):

    base_name = None
    resource = None

    def get_url(self, api_path, version='v2', **params):
        schema = 'https'
        str_params = {str(k): str(v) for k, v in params.items()}
        q = '&'.join('='.join(item) for item in str_params.items())
        d = {'schema': schema, 'domain': api_domain, 'version': version,
             'api_path': api_path, 'q': q}
        if q:
            return '{schema}://{domain}/{version}/{api_path}?{q}'.format(**d)
        else:
            return '{schema}://{domain}/{version}/{api_path}'.format(**d)

    def get_headers(self):
        # TODO: fix circular import
        from plotly.plotly.plotly import get_credentials, get_config
        credentials = get_credentials()

        # TODO: validate here?
        username, api_key = credentials['username'], credentials['api_key']
        encoded_api_auth = base64.b64encode(six.b('{0}:{1}'.format(
            username, api_key))).decode('utf8')

        header_dict = {
            'plotly-client-platform': 'python {0}'.format(__version__)
        }

        if get_config()['plotly_proxy_authorization']:
            proxy_username = credentials['proxy_username']
            proxy_password = credentials['proxy_password']
            encoded_proxy_auth = base64.b64encode(six.b('{0}:{1}'.format(
                proxy_username, proxy_password))).decode('utf8')
            header_dict['authorization'] = 'Basic ' + encoded_proxy_auth
            header_dict['plotly-authorization'] = 'Basic ' + encoded_api_auth
        else:
            header_dict['authorization'] = 'Basic ' + encoded_api_auth

        return header_dict

    def request(self, method, url, data=None):
        request_dict = {
            'headers': self.get_headers()
        }
        if data is not None:
            request_dict['data'] = data

        response = requests.request(method, url, **request_dict)
        response.raise_for_status()
        return response

    def get_response_data(self, method, url, data=None):
        response = self.request(method, url, data=data)
        if six.PY3:
            content = str(response.content, encoding='utf-8')
        else:
            content = response.content
        data = json.loads(content)

        if 'file' in data:
            return data['file']  # Create requests are enveloped.
        else:
            return data

    def get_create_url(self, version='v2', **params):
        api_path = '{}'.format(self.base_name)
        return self.get_url(api_path, version=version, **params)

    def get_detail_url(self, fid, version='v2', **params):
        api_path = '{}/{}'.format(self.base_name, fid)
        return self.get_url(api_path, version=version, **params)

    def get_trash_url(self, fid, version='v2', **params):
        api_path = '{}/{}/trash'.format(self.base_name, fid)
        return self.get_url(api_path, version=version, **params)

    def get_restore_url(self, fid, version='v2', **params):
        api_path = '{}/{}/restore'.format(self.base_name, fid)
        return self.get_url(api_path, version=version, **params)

    def get_permanent_delete_url(self, fid, version='v2', **params):
        api_path = '{}/{}/permanent_delete'.format(self.base_name, fid)
        return self.get_url(api_path, version=version, **params)


class FileResource(BaseResource):

    base_name = 'files'
    fid = None

    def __init__(self, fid=None, data=None):
        if fid is not None and data is not None:
            raise Exception('TBD')

        if fid is not None:
            self.fid = fid
            self.retrieve()
        elif data is not None:
            self.create(data=data)

    def create(self, data):
        """Standard CRUD 'create'."""
        url = self.get_create_url()
        self.resource = self.get_response_data('post', url, data=data)
        self.fid = self.resource['fid']
        return self.resource

    def retrieve(self):
        """Standard CRUD 'retrieve'."""
        url = self.get_detail_url(self.fid)
        self.resource = self.get_response_data('get', url)
        return self.resource

    def update(self):
        """Similar to CRUD 'update'."""
        url = self.get_detail_url(self.fid)
        self.resource = self.get_response_data('put', url)
        return self.resource

    def permanent_delete(self):
        """Similar to CRUD 'destroy'."""
        url = self.get_permanent_delete_url(self.fid)

        # TODO: how should non-object returns work?
        self.request('delete', url)
        self.resource = None
        return self.resource

    def trash(self):
        """Before destroying a resource, you need to trash it."""
        url = self.get_trash_url(self.fid)
        self.resource = self.get_response_data('post', url)
        return self.resource

    def patch(self, data):
        """Partial update on resource."""
        url = self.get_detail_url(self.fid)
        self.resource = self.get_response_data('patch', url, data=data)
        return self.resource


class PlotResource(FileResource):
    pass


class GridResource(FileResource):
    pass


class FolderResource(FileResource):
    pass
