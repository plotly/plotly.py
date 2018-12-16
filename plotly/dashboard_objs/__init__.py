"""
dashboard_objs
==========

A module for creating and manipulating dashboard content. You can create
a Dashboard object, insert boxes, swap boxes, remove a box and get an HTML
preview of the Dashboard.

The current workflow for making and manipulating dashboard follows:
1) Create a Dashboard
2) Modify the Dashboard (insert, swap, remove, etc)
3) Preview the Dashboard (run `.get_preview()`)
4) Repeat steps 2) and 3) as long as desired

The basic box object that your insert into a dashboard is just a `dict`.
The minimal dict for a box is:

```
{
    'type': 'box',
    'boxType': 'plot'
}
```

where 'fileId' can be set to the 'username:#' of your plot. The other
parameters
a box takes are `shareKey` (default is None) and `title` (default is '').

You will need to use the `.get_preview()` method quite regularly as this will
return an HTML representation of the dashboard in which the boxes in the HTML
are labelled with on-the-fly-generated numbers which change after each
modification to the dashboard.

Example: Create a simple Dashboard object
```
import plotly.dashboard_objs as dashboard

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'username:some#',
    'title': 'box 1'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'username:some#',
    'title': 'box 2'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 'username:some#',
    'title': 'box 3'
}

my_dboard = dashboard.Dashboard()
my_dboard.insert(box_1)
# my_dboard.get_preview()
my_dboard.insert(box_2, 'above', 1)
# my_dboard.get_preview()
my_dboard.insert(box_3, 'left', 2)
# my_dboard.get_preview()
my_dboard.swap(1, 2)
# my_dboard.get_preview()
my_dboard.remove(1)
# my_dboard.get_preview()
```
"""
from . dashboard_objs import Dashboard
