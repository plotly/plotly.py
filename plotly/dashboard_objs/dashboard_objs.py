"""
dashboard_objs
==========

A module which is used to create dashboard objects, manipulate them and then
upload them.

"""

import copy
import json
import requests
import pprint
import webbrowser

import plotly

from plotly import exceptions
from plotly.utils import node_generator
from plotly.api.v2.utils import build_url

username = plotly.tools.get_credentials_file()['username']
api_key = plotly.tools.get_credentials_file()['api_key']
headers = {'Plotly-Client-Platform': 'nteract'}


class EmptyBox(dict):
    def __init__(self):
        self['type'] = 'box'
        self['boxType'] = 'empty'


class Box(dict):
    def __init__(self, fileId='', shareKey=None, title=''):
        self['type'] = 'box'
        self['boxType'] = 'plot'
        self['fileId'] = fileId
        self['shareKey'] = shareKey
        self['title'] = title


class Container(dict):
    def __init__(self, box_1=EmptyBox(), box_2=EmptyBox(), size=400,
                 sizeUnit='px', direction='vertical'):
        self['type'] = 'split'
        self['size'] = size
        self['sizeUnit'] = sizeUnit
        self['direction'] = direction
        self['first'] = box_1
        self['second'] = box_2


class Dashboard(dict):
    def __init__(self, dashboard_json=None, backgroundColor='#FFFFFF',
                 boxBackgroundColor='#ffffff', boxBorderColor='#d8d8d8',
                 boxHeaderBackgroundColor='#f8f8f8', foregroundColor='#333333',
                 headerBackgroundColor='#2E3A46', headerForegroundColor='#FFFFFF',
                 links=[], logoUrl='', title='Untitled Dashboard'):
        # TODO: change name to box_id_to_path
        self.box_ids_dict = {}
        if not dashboard_json:
            self['layout'] = EmptyBox()
            self['version'] = 2
            self['settings'] = {
                'backgroundColor': backgroundColor,
                'boxBackgroundColor': boxBackgroundColor,
                'boxBorderColor': boxBorderColor,
                'boxHeaderBackgroundColor': boxHeaderBackgroundColor,
                'foregroundColor': foregroundColor,
                'headerBackgroundColor': headerBackgroundColor,
                'headerForegroundColor': headerForegroundColor,
                'links': links,
                'logoUrl': logoUrl,
                'title': title
            }
        else:
            self['layout'] = dashboard_json['layout']
            self['version'] = dashboard_json['version']
            self['settings'] = dashboard_json['settings']

            self._assign_boxes_to_ids()

    def _assign_boxes_to_ids(self):
        self.box_ids_dict = {}
        all_nodes = []
        node_gen = node_generator(self['layout'])

        finished_iteration = False
        while not finished_iteration:
            try:
                all_nodes.append(node_gen.next())
            except StopIteration:
                finished_iteration = True

        for node in all_nodes:
            if (node[1] != () and node[0]['type'] == 'box'
                    and node[0]['boxType'] != 'empty'):
                try:
                    max_id = max(self.box_ids_dict.keys())
                except ValueError:
                    max_id = 0
                self.box_ids_dict[max_id + 1] = list(node[1])

    def _insert(self, box_or_container, array_of_paths):
        """Performs user-unfriendly box and container manipulations."""
        if any(path not in ['first', 'second'] for path in array_of_paths):
            raise exceptions.PlotlyError(
                "Invalid path. Your 'array_of_paths' list must only contain "
                "the strings 'first' and 'second'."
            )

        if 'first' in self['layout']:
            loc_in_dashboard = self['layout']
            for index, path in enumerate(array_of_paths):
                if index != len(array_of_paths) - 1:
                    loc_in_dashboard = loc_in_dashboard[path]
                else:
                    loc_in_dashboard[path] = box_or_container

        else:
            self['layout'] = box_or_container

        # update box_ids
        if isinstance(box_or_container, Box):
            # box -> container
            # if replacing a container, remove box_ids for
            # the boxes that belong there
            for first_or_second in ['first', 'second']:
                extended_box_path = copy.deepcopy(array_of_paths)
                extended_box_path.append(first_or_second)
                for key in self.box_ids_dict.keys():
                    if self.box_ids_dict[key] == extended_box_path:
                        self.box_ids_dict.pop(key)

            # box -> box
            for key in self.box_ids_dict.keys():
                if self.box_ids_dict[key] == array_of_paths:
                    self.box_ids_dict.pop(key)
            try:
                max_id = max(self.box_ids_dict.keys())
            except ValueError:
                max_id = 0
            self.box_ids_dict[max_id + 1] = array_of_paths

        elif isinstance(box_or_container, Container):
            # container -> box
            for key in self.box_ids_dict.keys():
                if self.box_ids_dict[key] == array_of_paths:
                    self.box_ids_dict.pop(key)

            # handles boxes already in container
            for first_or_second in ['first', 'second']:
                if box_or_container[first_or_second] != EmptyBox():
                    path_to_box = copy.deepcopy(array_of_paths)
                    path_to_box.append(first_or_second)
                    for key in self.box_ids_dict.keys():
                        if self.box_ids_dict[key] == path_to_box:
                            self.box_ids_dict.pop(key)

                    try:
                        max_id = max(self.box_ids_dict.keys())
                    except ValueError:
                        max_id = 0
                    self.box_ids_dict[max_id + 1] = path_to_box

    def _get_box(self, box_id):
        """Returns box from box_id number."""

        loc_in_dashboard = self['layout']
        for path in self.box_ids_dict[box_id]:
            loc_in_dashboard = loc_in_dashboard[path]
        return loc_in_dashboard

    def get_preview(self):
        """
        Returns JSON and HTML respresentation of the dashboard.

        HTML coming soon to a theater near you.
        """
        # print JSON figure
        pprint.pprint(self)

    def insert(self, box, box_id=None, side='above'):
        """
        The user-friendly method for inserting boxes into the Dashboard.

        box: the box you are inserting into the dashboard.
        box_id: pre-existing box you use as a reference point.
        """
        # doesn't need box_id or side specified
        if 'first' not in self['layout']:
            self._insert(Container(), [])
            self._insert(box, ['first'])
        else:
            if box_id is None:
                raise exceptions.PlotlyError(
                    "Make sure the box_id is specfied if there is at least "
                    "one box in your dashboard."
                )
            if box_id not in self.box_ids_dict:
                raise exceptions.PlotlyError(
                    "Your box_id must a number in your dashboard. To view a "
                    "representation of your dashboard run 'get_preview()'."
                )
            #self._assign_boxes_to_ids()
            if side == 'above':
                old_box = self._get_box(box_id)
                self._insert(
                    Container(box, old_box, direction='vertical'),
                    self.box_ids_dict[box_id]
                )
            elif side == 'below':
                old_box = self._get_box(box_id)
                self._insert(
                    Container(old_box, box, direction='vertical'),
                    self.box_ids_dict[box_id]
                )
            elif side == 'left':
                old_box = self._get_box(box_id)
                self._insert(
                    Container(box, old_box, direction='horizontal'),
                    self.box_ids_dict[box_id]
                )
            elif side == 'right':
                old_box = self._get_box(box_id)
                self._insert(
                    Container(old_box, box, direction='horizontal'),
                    self.box_ids_dict[box_id]
                )
            else:
                raise exceptions.PlotlyError(
                    "If there is at least one box in your dashboard, you "
                    "must specify a valid side value. You must choose from "
                    "'above', 'below', 'left', and 'right'."
                )


def upload_dashboard(dashboard_object, filename, world_readable,
                     auto_open=True):
    """
    BETA function for uploading dashboards.

    Functionality that we may need to consider adding:
    - filename needs to be able to support `/` to create or use folders.
      This'll require a few API calls.
    - this function only works if the filename is unique. Need to call
      `update` if this file already exists to overwrite the file.
    - world_readable really should be `sharing` and allow `public`, `private`,
      or `secret` like in `py.plot`.
    - auto_open parameter for opening the result.
    """
    res = requests.post(
        build_url('dashboards'),
        auth=(username, api_key),
        headers=headers,
        data = {
            'content': json.dumps(dashboard_object),
            'filename': filename,
            'world_readable': world_readable
        }
    )

    res.raise_for_status()

    url = res.json()['web_url']
    webbrowser.open_new(res.json()['web_url'])
    return url
