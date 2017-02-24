"""
dashboard_objs
==========

A module which is meant to create and manipulate dashboard content.
"""

import pprint
import copy
from IPython import display

from plotly import exceptions
from plotly.utils import node_generator


# default variables
master_width = 400
master_height = 400
container_size = master_height
font_size = 10


def _empty_box():
    empty_box = {
        'type': 'box',
        'boxType': 'empty'
    }
    return empty_box


def _box(fileId='', shareKey=None, title=''):
    box = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': fileId,
        'shareKey': shareKey,
        'title': title
    }
    return box


def _container(box_1=_empty_box(), box_2=_empty_box(), size=container_size,
               sizeUnit='px', direction='vertical'):
    container = {
        'type': 'split',
        'size': size,
        'sizeUnit': sizeUnit,
        'direction': direction,
        'first': box_1,
        'second': box_2
    }
    return container

dashboard_html = ("""
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
      </script>
  </body>
</html>
""".format(width=master_width, height=master_height))


def draw_line_through_box(dashboard_html, top_left_x, top_left_y, box_w,
                          box_h, direction='vertical', size=200):
    """
    Draw a line to divide a box rendered in the HTML preview of dashboard.

    :param (str) direction: is the opposite of the direction of the line that
        is draw in the HTML representation. It represents the direction that
        will result from the two boxes resulting in the line dividing up an
        HTML box in the preview of the dashboard.
    :param (float) size: determins how big the first of the two boxes that
        result in a split will be. This is in units of pixels.
    """
    is_horizontal = (direction == 'horizontal')
    new_top_left_x = top_left_x + is_horizontal*0.5*box_w
    new_top_left_y = top_left_y + (not is_horizontal)*0.5*box_h
    new_box_w = (not is_horizontal)*box_w + is_horizontal
    new_box_h = (not is_horizontal) + is_horizontal*box_h

    html_box = """<!-- Draw some lines in -->
          context.beginPath();
          context.rect({top_left_x}, {top_left_y}, {box_w}, {box_h});
          context.lineWidth = 1;
          context.strokeStyle = 'black';
          context.stroke();
    """.format(top_left_x=new_top_left_x, top_left_y=new_top_left_y,
               box_w=new_box_w, box_h=new_box_h)

    index_for_new_box = dashboard_html.find('</script>') - 1
    dashboard_html = (dashboard_html[:index_for_new_box] + html_box +
                      dashboard_html[index_for_new_box:])
    return dashboard_html


def add_html_text(dashboard_html, text, top_left_x, top_left_y, box_w, box_h):
    """
    Add a number to the middle of an HTML box.
    """
    html_text = """<!-- Insert box numbers -->
          context.font = '{font_size}pt Times New Roman';
          context.textAlign = 'center';
          context.fillText({text}, {top_left_x} + 0.5*{box_w}, {top_left_y} + 0.5*{box_h});
    """.format(text=text, top_left_x=top_left_x, top_left_y=top_left_y,
               box_w=box_w, box_h=box_h, font_size=font_size)

    index_to_add_text = dashboard_html.find('</script>') - 1
    dashboard_html = (dashboard_html[:index_to_add_text] + html_text +
                      dashboard_html[index_to_add_text:])
    return dashboard_html


class Dashboard(dict):
    def __init__(self, content=None):
        if content is None:
            content = {}

        self.box_ids_to_path = {}
        if not content:
            self['layout'] = _empty_box()
            self['version'] = 2
            self['settings'] = {}
        else:
            self['layout'] = content['layout']
            self['version'] = content['version']
            self['settings'] = content['settings']

            self._assign_boxes_to_ids()

    def _assign_boxes_to_ids(self):
        self.box_ids_to_path = {}
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
                    max_id = max(self.box_ids_to_path.keys())
                except ValueError:
                    max_id = 0
                self.box_ids_to_path[max_id + 1] = list(node[1])

    def _insert(self, box_or_container, path):
        """Performs user-unfriendly box and container manipulations."""
        if any(first_second not in ['first', 'second'] for first_second in path):
            raise exceptions.PlotlyError(
                "Invalid path. Your 'path' list must only contain "
                "the strings 'first' and 'second'."
            )

        if 'first' in self['layout']:
            loc_in_dashboard = self['layout']
            for index, first_second in enumerate(path):
                if index != len(path) - 1:
                    loc_in_dashboard = loc_in_dashboard[first_second]
                else:
                    loc_in_dashboard[first_second] = box_or_container

        else:
            self['layout'] = box_or_container

    def get_box(self, box_id):
        """Returns box from box_id number."""
        self._assign_boxes_to_ids()

        loc_in_dashboard = self['layout']
        for first_second in self.box_ids_to_path[box_id]:
            loc_in_dashboard = loc_in_dashboard[first_second]
        return loc_in_dashboard

    def _path_to_box(self, path):
        """Returns box from specified path."""
        self._assign_boxes_to_ids()

        loc_in_dashboard = self['layout']
        for first_second in path:
            loc_in_dashboard = loc_in_dashboard[first_second]
        return loc_in_dashboard

    def get_preview(self):
        """Returns JSON and HTML respresentation of the dashboard."""
        # assign box_ids
        self._assign_boxes_to_ids()

        # print JSON
        pprint.pprint(self)

        # construct HTML dashboard
        x = 0
        y = 0
        box_w = master_width
        box_h = master_height
        html_figure = copy.deepcopy(dashboard_html)
        path_to_box_specs = {}  # used to store info about box dimensions
        # add first path
        first_box_specs = {
            'top_left_x': x,
            'top_left_y': y,
            'box_w': box_w,
            'box_h': box_h
        }
        path_to_box_specs[tuple(['first'])] = first_box_specs

        # generate all paths
        all_nodes = []
        node_gen = node_generator(self['layout'])

        finished_iteration = False
        while not finished_iteration:
            try:
                all_nodes.append(node_gen.next())
            except StopIteration:
                finished_iteration = True

        all_paths = []
        for node in all_nodes:
            all_paths.append(list(node[1]))
        if ['second'] in all_paths:
            all_paths.remove(['second'])

        max_path_len = max(len(path) for path in all_paths)
        # search all paths of the same length
        for path_len in range(1, max_path_len + 1):
            for path in [path for path in all_paths if len(path) == path_len]:
                current_box_specs = path_to_box_specs[tuple(path)]

                if self._path_to_box(path)['type'] == 'split':
                    html_figure = draw_line_through_box(
                        html_figure,
                        current_box_specs['top_left_x'],
                        current_box_specs['top_left_y'],
                        current_box_specs['box_w'],
                        current_box_specs['box_h'],
                        direction=self._path_to_box(path)['direction']
                    )

                    # determine the specs for resulting two boxes from split
                    is_horizontal = (
                        self._path_to_box(path)['direction'] == 'horizontal'
                    )
                    x = current_box_specs['top_left_x']
                    y = current_box_specs['top_left_y']
                    box_w = current_box_specs['box_w']
                    box_h = current_box_specs['box_h']

                    new_box_w = box_w*(1 - is_horizontal*0.5)
                    new_box_h = box_h*(1 - (not is_horizontal)*0.5)

                    box_1_specs = {
                        'top_left_x': x,
                        'top_left_y': y,
                        'box_w': new_box_w,
                        'box_h': new_box_h
                    }
                    box_2_specs = {
                        'top_left_x': (x + is_horizontal*0.5*box_w),
                        'top_left_y': (y + (not is_horizontal)*0.5*box_h),
                        'box_w': new_box_w,
                        'box_h': new_box_h
                    }

                    path_to_box_specs[tuple(path) + ('first',)] = box_1_specs
                    path_to_box_specs[tuple(path) + ('second',)] = box_2_specs

                elif self._path_to_box(path)['type'] == 'box':
                    for box_id in self.box_ids_to_path:
                        if self.box_ids_to_path[box_id] == path:
                            number = box_id

                    html_figure = add_html_text(
                        html_figure, number,
                        path_to_box_specs[tuple(path)]['top_left_x'],
                        path_to_box_specs[tuple(path)]['top_left_y'],
                        path_to_box_specs[tuple(path)]['box_w'],
                        path_to_box_specs[tuple(path)]['box_h'],
                    )

        # display HTML representation
        return display.HTML(html_figure)

    def insert(self, box, side='above', box_id=None):
        """
        The user-friendly method for inserting boxes into the Dashboard.

        box: the box you are inserting into the dashboard.
        box_id: pre-existing box you use as a reference point.
        """
        self._assign_boxes_to_ids()
        init_box = {
            'type': 'box',
            'boxType': 'plot',
            'fileId': '',
            'shareKey': None,
            'title': ''
        }

        # force box to have all valid box keys
        for key in init_box.keys():
            if key not in box.keys():
                box[key] = init_box[key]

        # doesn't need box_id or side specified for first box
        if 'first' not in self['layout']:
            self._insert(_container(), [])
            self._insert(box, ['first'])
        else:
            if box_id is None:
                raise exceptions.PlotlyError(
                    "Make sure the box_id is specfied if there is at least "
                    "one box in your dashboard."
                )
            if box_id not in self.box_ids_to_path:
                raise exceptions.PlotlyError(
                    "Your box_id must a number in your dashboard. To view a "
                    "representation of your dashboard run 'get_preview()'."
                )
            if side == 'above':
                old_box = self.get_box(box_id)
                self._insert(
                    _container(box, old_box, direction='vertical'),
                    self.box_ids_to_path[box_id]
                )
            elif side == 'below':
                old_box = self.get_box(box_id)
                self._insert(
                    _container(old_box, box, direction='vertical'),
                    self.box_ids_to_path[box_id]
                )
            elif side == 'left':
                old_box = self.get_box(box_id)
                self._insert(
                    _container(box, old_box, direction='horizontal'),
                    self.box_ids_to_path[box_id]
                )
            elif side == 'right':
                old_box = self.get_box(box_id)
                self._insert(
                    _container(old_box, box, direction='horizontal'),
                    self.box_ids_to_path[box_id]
                )
            else:
                raise exceptions.PlotlyError(
                    "If there is at least one box in your dashboard, you "
                    "must specify a valid side value. You must choose from "
                    "'above', 'below', 'left', and 'right'."
                )

    def swap(self, box_id_1, box_id_2):
        """Swap two boxes with their specified ids."""
        self._assign_boxes_to_ids()

        box_1 = self.get_box(box_id_1)
        box_2 = self.get_box(box_id_2)

        box_1_path = self.box_ids_to_path[box_id_1]
        box_2_path = self.box_ids_to_path[box_id_2]

        for pairs in [(box_1_path, box_2), (box_2_path, box_1)]:
            loc_in_dashboard = self['layout']
            for first_second in pairs[0][:-1]:
                loc_in_dashboard = loc_in_dashboard[first_second]
            loc_in_dashboard[pairs[0][-1]] = pairs[1]
