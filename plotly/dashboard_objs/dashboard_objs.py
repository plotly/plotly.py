"""
dashboard_objs
==========

A module for creating and manipulating dashboard content. You can create
a Dashboard object, insert boxes, swap boxes, remove a box and get an HTML
preview of the Dashboard.
```
"""

import pprint

from plotly import exceptions, optional_imports
from plotly.utils import node_generator

IPython = optional_imports.get_module('IPython')

# default parameters for HTML preview
MASTER_WIDTH = 500
MASTER_HEIGHT = 500
FONT_SIZE = 9


ID_NOT_VALID_MESSAGE = (
    "Your box_id must be a number in your dashboard. To view a "
    "representation of your dashboard run get_preview()."
)


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

def _container(box_1=None, box_2=None,
               size=50, sizeUnit='%',
               direction='vertical'):
    if box_1 is None:
        box_1 = _empty_box()
    if box_2 is None:
        box_2 = _empty_box()

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
      }}
    </style>
  </head>
  <body>
    <canvas id="myCanvas" width="{width}" height="{height}"></canvas>
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
""".format(width=MASTER_WIDTH, height=MASTER_HEIGHT))


def _draw_line_through_box(dashboard_html, top_left_x, top_left_y, box_w,
                           box_h, is_horizontal, direction, fill_percent=50):
    if is_horizontal:
        new_top_left_x = top_left_x + box_w * (fill_percent / 100.)
        new_top_left_y = top_left_y
        new_box_w = 1
        new_box_h = box_h
    else:
        new_top_left_x = top_left_x
        new_top_left_y = top_left_y + box_h * (fill_percent / 100.)
        new_box_w = box_w
        new_box_h = 1

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


def _add_html_text(dashboard_html, text, top_left_x, top_left_y, box_w,
                   box_h):
    html_text = """<!-- Insert box numbers -->
          context.font = '{}pt Times New Roman';
          context.textAlign = 'center';
          context.fillText({}, {} + 0.5*{}, {} + 0.5*{});
    """.format(FONT_SIZE, text, top_left_x, box_w, top_left_y, box_h)

    index_to_add_text = dashboard_html.find('</script>') - 1
    dashboard_html = (dashboard_html[:index_to_add_text] + html_text +
                      dashboard_html[index_to_add_text:])
    return dashboard_html


class Dashboard(dict):
    """
    Dashboard class for creating interactive dashboard objects.

    Dashboards are dicts that contain boxes which hold plot information.
    These boxes can be arranged in various ways. The most basic form of
    a box is:

    ```
    {
        'type': 'box',
        'boxType': 'plot'
    }
    ```

    where 'fileId' can be set to the 'username:#' of your plot. The other
    parameters a box takes are `shareKey` (default is None) and `title`
    (default is '').

    `.get_preview()` should be called quite regularly to get an HTML
    representation of the dashboard in which the boxes in the HTML
    are labelled with on-the-fly-generated numbers or box ids which
    change after each modification to the dashboard.

    `.get_box()` returns the box located in the dashboard by calling
    its box id as displayed via `.get_preview()`.

    Example 1: Create a simple Dashboard object
    ```
    import plotly.dashboard_objs as dashboard

    box_a = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': 'username:some#',
        'title': 'box a'
    }

    box_b = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': 'username:some#',
        'title': 'box b'
    }

    box_c = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': 'username:some#',
        'title': 'box c'
    }

    my_dboard = dashboard.Dashboard()
    my_dboard.insert(box_a)
    # my_dboard.get_preview()
    my_dboard.insert(box_b, 'above', 1)
    # my_dboard.get_preview()
    my_dboard.insert(box_c, 'left', 2)
    # my_dboard.get_preview()
    my_dboard.swap(1, 2)
    # my_dboard.get_preview()
    my_dboard.remove(1)
    # my_dboard.get_preview()
    ```

    Example 2: 4 vertical boxes of equal height
    ```
    import plotly.dashboard_objs as dashboard

    box_a = {
        'type': 'box',
        'boxType': 'plot',
        'fileId': 'username:some#',
        'title': 'box a'
    }

    my_dboard = dashboard.Dashboard()
    my_dboard.insert(box_a)
    my_dboard.insert(box_a, 'below', 1)
    my_dboard.insert(box_a, 'below', 1)
    my_dboard.insert(box_a, 'below', 3)
    # my_dboard.get_preview()
    ```
    """
    def __init__(self, content=None):
        if content is None:
            content = {}

        if not content:
            self['layout'] = None
            self['version'] = 2
            self['settings'] = {}
        else:
            self['layout'] = content['layout']
            self['version'] = content['version']
            self['settings'] = content['settings']

    def _compute_box_ids(self):
        box_ids_to_path = {}
        all_nodes = list(node_generator(self['layout']))
        all_nodes.sort(key=lambda x: x[1])
        for node in all_nodes:
            if (node[1] != () and node[0]['type'] == 'box'
                    and node[0]['boxType'] != 'empty'):
                try:
                    max_id = max(box_ids_to_path.keys())
                except ValueError:
                    max_id = 0
                box_ids_to_path[max_id + 1] = node[1]

        return box_ids_to_path

    def _insert(self, box_or_container, path):
        if any(first_second not in ['first', 'second']
               for first_second in path):
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

    def _make_all_nodes_and_paths(self):
        all_nodes = list(node_generator(self['layout']))
        all_nodes.sort(key=lambda x: x[1])

        # remove path 'second' as it's always an empty box
        all_paths = []
        for node in all_nodes:
            all_paths.append(node[1])
        path_second = ('second',)
        if path_second in all_paths:
            all_paths.remove(path_second)
        return all_nodes, all_paths

    def _path_to_box(self, path):
        loc_in_dashboard = self['layout']
        for first_second in path:
            loc_in_dashboard = loc_in_dashboard[first_second]
        return loc_in_dashboard

    def _set_dashboard_size(self):
        # set dashboard size to keep consistent with GUI
        num_of_boxes = len(self._compute_box_ids())
        if num_of_boxes == 0:
            pass
        elif num_of_boxes == 1:
            self['layout']['size'] = 800
            self['layout']['sizeUnit'] = 'px'
        elif num_of_boxes == 2:
            self['layout']['size'] = 1500
            self['layout']['sizeUnit'] = 'px'
        else:
            self['layout']['size'] = 1500 + 350 * (num_of_boxes - 2)
            self['layout']['sizeUnit'] = 'px'

    def get_box(self, box_id):
        """Returns box from box_id number."""
        box_ids_to_path = self._compute_box_ids()
        loc_in_dashboard = self['layout']

        if box_id not in box_ids_to_path.keys():
            raise exceptions.PlotlyError(ID_NOT_VALID_MESSAGE)
        for first_second in box_ids_to_path[box_id]:
            loc_in_dashboard = loc_in_dashboard[first_second]
        return loc_in_dashboard

    def get_preview(self):
        """
        Returns JSON or HTML respresentation of the dashboard.

        If IPython is not imported, returns a pretty print of the dashboard
        dict. Otherwise, returns an IPython.core.display.HTML display of the
        dashboard.

        The algorithm used to build the HTML preview involves going through
        the paths of the node generator of the dashboard. The paths of the
        dashboard are sequenced through from shorter to longer and whether
        it's a box or container that lies at the end of the path determines
        the action.

        If it's a container, draw a line in the figure to divide the current
        box into two and store the specs of the resulting two boxes. If the
        path points to a terminal box (often containing a plot), then draw
        the box id in the center of the box.

        It's important to note that these box ids are generated on-the-fly and
        they do not necessarily stay assigned to the boxes they were once
        assigned to.
        """
        if IPython is None:
            pprint.pprint(self)
            return

        elif self['layout'] is None:
            return IPython.display.HTML(dashboard_html)

        top_left_x = 0
        top_left_y = 0
        box_w = MASTER_WIDTH
        box_h = MASTER_HEIGHT
        html_figure = dashboard_html
        box_ids_to_path = self._compute_box_ids()
        # used to store info about box dimensions
        path_to_box_specs = {}
        first_box_specs = {
            'top_left_x': top_left_x,
            'top_left_y': top_left_y,
            'box_w': box_w,
            'box_h': box_h
        }
        # uses tuples to store paths as for hashable keys
        path_to_box_specs[('first',)] = first_box_specs

        # generate all paths
        all_nodes, all_paths = self._make_all_nodes_and_paths()

        max_path_len = max(len(path) for path in all_paths)
        for path_len in range(1, max_path_len + 1):
            for path in [path for path in all_paths if len(path) == path_len]:
                current_box_specs = path_to_box_specs[path]

                if self._path_to_box(path)['type'] == 'split':
                    fill_percent = self._path_to_box(path)['size']
                    direction = self._path_to_box(path)['direction']
                    is_horizontal = (direction == 'horizontal')

                    top_left_x = current_box_specs['top_left_x']
                    top_left_y = current_box_specs['top_left_y']
                    box_w = current_box_specs['box_w']
                    box_h = current_box_specs['box_h']

                    html_figure = _draw_line_through_box(
                        html_figure, top_left_x, top_left_y, box_w, box_h,
                        is_horizontal=is_horizontal, direction=direction,
                        fill_percent=fill_percent
                    )

                    # determine the specs for resulting two box split
                    if is_horizontal:
                        new_top_left_x = top_left_x
                        new_top_left_y = top_left_y
                        new_box_w = box_w * (fill_percent / 100.)
                        new_box_h = box_h

                        new_top_left_x_2 = top_left_x + new_box_w
                        new_top_left_y_2 = top_left_y
                        new_box_w_2 = box_w * ((100 - fill_percent) / 100.)
                        new_box_h_2 = box_h
                    else:
                        new_top_left_x = top_left_x
                        new_top_left_y = top_left_y
                        new_box_w = box_w
                        new_box_h = box_h * (fill_percent / 100.)

                        new_top_left_x_2 = top_left_x
                        new_top_left_y_2 = (top_left_y +
                                            box_h * (fill_percent / 100.))
                        new_box_w_2 = box_w
                        new_box_h_2 = box_h * ((100 - fill_percent) / 100.)

                    first_box_specs = {
                        'top_left_x': top_left_x,
                        'top_left_y': top_left_y,
                        'box_w': new_box_w,
                        'box_h': new_box_h
                    }
                    second_box_specs = {
                        'top_left_x': new_top_left_x_2,
                        'top_left_y': new_top_left_y_2,
                        'box_w': new_box_w_2,
                        'box_h': new_box_h_2
                    }

                    path_to_box_specs[path + ('first',)] = first_box_specs
                    path_to_box_specs[path + ('second',)] = second_box_specs

                elif self._path_to_box(path)['type'] == 'box':
                    for box_id in box_ids_to_path:
                        if box_ids_to_path[box_id] == path:
                            number = box_id
                    html_figure = _add_html_text(
                        html_figure, number,
                        path_to_box_specs[path]['top_left_x'],
                        path_to_box_specs[path]['top_left_y'],
                        path_to_box_specs[path]['box_w'],
                        path_to_box_specs[path]['box_h'],
                    )

        # display HTML representation
        return IPython.display.HTML(html_figure)

    def insert(self, box, side='above', box_id=None, fill_percent=50):
        """
        Insert a box into your dashboard layout.

        :param (dict) box: the box you are inserting into the dashboard.
        :param (str) side: specifies where your new box is going to be placed
            relative to the given 'box_id'. Valid values are 'above', 'below',
            'left', and 'right'.
        :param (int) box_id: the box id which is used as a reference for the
            insertion of the new box. Box ids are memoryless numbers that are
            generated on-the-fly and assigned to boxes in the layout each time
            .get_preview() is run.
        :param (float) fill_percent: specifies the percentage of the container
            box from the given 'side' that the new box occupies. For example
            if you apply the method\n
            .insert(box=new_box, box_id=2, side='left', fill_percent=20)\n
            to a dashboard object, a new box is inserted 20% from the left
            side of the box with id #2. Run .get_preview() to see the box ids
            assigned to each box in the dashboard layout.
            Default = 50
        Example:
        ```
        import plotly.dashboard_objs as dashboard

        box_a = {
            'type': 'box',
            'boxType': 'plot',
            'fileId': 'username:some#',
            'title': 'box a'
        }

        my_dboard = dashboard.Dashboard()
        my_dboard.insert(box_a)
        my_dboard.insert(box_a, 'left', 1)
        my_dboard.insert(box_a, 'below', 2)
        my_dboard.insert(box_a, 'right', 3)
        my_dboard.insert(box_a, 'above', 4, fill_percent=20)

        my_dboard.get_preview()
        ```
        """
        box_ids_to_path = self._compute_box_ids()

        # doesn't need box_id or side specified for first box
        if self['layout'] is None:
            self['layout'] = _container(
                box, _empty_box(), size=MASTER_HEIGHT, sizeUnit='px'
            )
        else:
            if box_id is None:
                raise exceptions.PlotlyError(
                    "Make sure the box_id is specfied if there is at least "
                    "one box in your dashboard."
                )
            if box_id not in box_ids_to_path:
                raise exceptions.PlotlyError(ID_NOT_VALID_MESSAGE)

            if fill_percent < 0 or fill_percent > 100:
                raise exceptions.PlotlyError(
                    'fill_percent must be a number between 0 and 100 '
                    'inclusive'
                )
            if side == 'above':
                old_box = self.get_box(box_id)
                self._insert(
                    _container(box, old_box, direction='vertical',
                               size=fill_percent),
                    box_ids_to_path[box_id]
                )
            elif side == 'below':
                old_box = self.get_box(box_id)
                self._insert(
                    _container(old_box, box, direction='vertical',
                               size=100 - fill_percent),
                    box_ids_to_path[box_id]
                )
            elif side == 'left':
                old_box = self.get_box(box_id)
                self._insert(
                    _container(box, old_box, direction='horizontal',
                               size=fill_percent),
                    box_ids_to_path[box_id]
                )
            elif side == 'right':
                old_box = self.get_box(box_id)
                self._insert(
                    _container(old_box, box, direction='horizontal',
                               size =100 - fill_percent),
                    box_ids_to_path[box_id]
                )
            else:
                raise exceptions.PlotlyError(
                    "If there is at least one box in your dashboard, you "
                    "must specify a valid side value. You must choose from "
                    "'above', 'below', 'left', and 'right'."
                )

        self._set_dashboard_size()

    def remove(self, box_id):
        """
        Remove a box from the dashboard by its box_id.

        Example:
        ```
        import plotly.dashboard_objs as dashboard

        box_a = {
            'type': 'box',
            'boxType': 'plot',
            'fileId': 'username:some#',
            'title': 'box a'
        }

        my_dboard = dashboard.Dashboard()
        my_dboard.insert(box_a)
        my_dboard.remove(1)
        my_dboard.get_preview()
        ```
        """
        box_ids_to_path = self._compute_box_ids()
        if box_id not in box_ids_to_path:
            raise exceptions.PlotlyError(ID_NOT_VALID_MESSAGE)

        path = box_ids_to_path[box_id]
        if path != ('first',):
            container_for_box_id = self._path_to_box(path[:-1])
            if path[-1] == 'first':
                adjacent_path = 'second'
            elif path[-1] == 'second':
                adjacent_path = 'first'
            adjacent_box = container_for_box_id[adjacent_path]

            self._insert(adjacent_box, path[:-1])
        else:
            self['layout'] = None

        self._set_dashboard_size()

    def swap(self, box_id_1, box_id_2):
        """
        Swap two boxes with their specified ids.

        Example:
        ```
        import plotly.dashboard_objs as dashboard

        box_a = {
            'type': 'box',
            'boxType': 'plot',
            'fileId': 'username:first#',
            'title': 'box a'
        }

        box_b = {
            'type': 'box',
            'boxType': 'plot',
            'fileId': 'username:second#',
            'title': 'box b'
        }

        my_dboard = dashboard.Dashboard()
        my_dboard.insert(box_a)
        my_dboard.insert(box_b, 'above', 1)

        # check box at box id 1
        box_at_1 = my_dboard.get_box(1)
        print(box_at_1)

        my_dboard.swap(1, 2)

        box_after_swap = my_dboard.get_box(1)
        print(box_after_swap)
        ```
        """
        box_ids_to_path = self._compute_box_ids()
        box_a = self.get_box(box_id_1)
        box_b = self.get_box(box_id_2)

        box_a_path = box_ids_to_path[box_id_1]
        box_b_path = box_ids_to_path[box_id_2]

        for pairs in [(box_a_path, box_b), (box_b_path, box_a)]:
            loc_in_dashboard = self['layout']
            for first_second in pairs[0][:-1]:
                loc_in_dashboard = loc_in_dashboard[first_second]
            loc_in_dashboard[pairs[0][-1]] = pairs[1]
