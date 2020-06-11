from unittest import TestCase

import plotly.graph_objs as go
from plotly.subplots import make_subplots

__doc__ = """
To test:
We need to test add_annotation, add_shape, add_layout_image

The possible entries for row and col are:

code, type
ia: (int,'all')
lea: (list,'all')
a: 'all'
i: int
le: list, len equals other list len
lu: list, len unequal

# Rather than test this huge space of function inputs, let's break it down:

Test if (int,'all') (list,'all') ('all',int) ('all',list) set an "all" flag (also test that not this doesn't set the all flag e.g., int, list (int,'notall'),etc.)

Test the combinations formed by taking the cartesian product {a,i,l}x{a,i,l} and just see if they give the predicted index pairs.

Test to see if the part of the code that iterates through the plots works, e.g., check that empty list does nothing and list of (row,col) pairs does work.

Check to see that range is converted to list when passed in these forms (range,'all') range etc.
"""


class TestAddForEachAnnotationType(TestCase):
    pass
