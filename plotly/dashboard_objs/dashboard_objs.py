import plotly
from plotly.api.v2.utils import build_url

import json
import requests
import webbrowser
from IPython import display

username = plotly.tools.get_credentials_file()['username']
api_key = plotly.tools.get_credentials_file()['api_key']
headers = {'Plotly-Client-Platform': 'nteract'}


# little wrapper around requests.get
def get(*args, **kwargs):
    return requests.get(
        *args, auth=(username, api_key), headers=headers, **kwargs
    )

width = 350
height = 350
dashboard_html = """
<!DOCTYPE HTML>
<html>
  <head>
    <style>
      body {{
        margin: 0px;
        padding: 0px;
      /}}
    </style>
  </head>
  <body>
    <canvas id="myCanvas" width="400" height="400"></canvas>
    <script>
      var canvas = document.getElementById('myCanvas');
      var context = canvas.getContext('2d');
      <!-- Dashboard -->
      context.beginPath();
      context.rect(0, 0, {width}, {height});
      context.lineWidth = 2;
      context.strokeStyle = 'black';
      context.stroke();
      <!-- Draw some lines in -->
      context.beginPath();
      context.rect(0, {height}/2, {width}/2, {height}/2);
      context.lineWidth = 2;
      context.strokeStyle = 'black';
      context.stroke();
      <!-- Draw the box_ids -->
      context.font = '12pt Times New Roman';
      context.textAlign = 'center';
      context.fillText('0', 50, 50);
    </script>
  </body>
</html>
""".format(width=350, height=350)

box_html = """
      <!-- Draw some lines in -->
      context.beginPath();
      context.rect(0, {height}/2, {width}/2, {height}/2);
      context.lineWidth = 2;
      context.strokeStyle = 'black';
      context.stroke();
""".format(width=350, height=350)


class FirstEmptyBox(dict):
    def __init__(self):
        self['type'] = 'box'
        self['boxType'] = 'empty'


class EmptyBox(dict):
    def __init__(self):
        self['type'] = 'box'
        self['boxType'] = 'empty'
        self['fileId'] = ''
        self['shareKey'] = None
        self['title'] = ''


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


box_ids_to_paths = {}


class Dashboard(dict):
    def __init__(self, backgroundColor='#FFFFFF', boxBackgroundColor='#ffffff',
                 boxBorderColor='#d8d8d8', boxHeaderBackgroundColor='#f8f8f8',
                 foregroundColor='#333333', headerBackgroundColor='#2E3A46',
                 headerForegroundColor='#FFFFFF', links=[], logoUrl='',
                 title='Untitled Dashboard'):
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
        self['layout'] = FirstEmptyBox()

    def insert(self, box_or_container, array_of_paths):
        if any(path not in ['first', 'second'] for path in array_of_paths):
            return "Invalid path."

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
            max_id = len(box_ids_to_paths)
            box_ids_to_paths[max_id] = array_of_paths

    def _get_box(self, box_id):
        loc_in_dashboard = self['layout']
        for path in box_ids_to_paths[box_id]:
            loc_in_dashboard = loc_in_dashboard[path]
        return loc_in_dashboard


def create_dashboard(dashboard_object, filename, world_readable, auto_open=True):
    """
    BETA Function for creating a dashboard.
    """
    res = requests.post(
        build_url('dashboards'),
        auth=(username, api_key),
        headers=headers,
        data={
            'content': json.dumps(dashboard_object),
            'filename': filename,
            'world_readable': world_readable
        }
    )

    res.raise_for_status()

    url = res.json()['web_url']
    webbrowser.open_new(res.json()['web_url'])
    return url
