"""
test_dashboard:
==========

A module intended for use with Nose.

"""


from unittest import TestCase
from _plotly_utils.exceptions import PlotlyError
import chart_studio.dashboard_objs.dashboard_objs as dashboard


class TestDashboard(TestCase):
    def test_invalid_path(self):

        my_box = {
            "type": "box",
            "boxType": "plot",
            "fileId": "AdamKulidjian:327",
            "shareKey": None,
            "title": "box 1",
        }
        dash = dashboard.Dashboard()

        message = (
            "Invalid path. Your 'path' list must only contain "
            "the strings 'first' and 'second'."
        )

        self.assertRaisesRegex(PlotlyError, message, dash._insert, my_box, "third")

    def test_box_id_none(self):

        my_box = {
            "type": "box",
            "boxType": "plot",
            "fileId": "AdamKulidjian:327",
            "shareKey": None,
            "title": "box 1",
        }

        dash = dashboard.Dashboard()
        dash.insert(my_box, "above", None)

        message = (
            "Make sure the box_id is specfied if there is at least "
            "one box in your dashboard."
        )

        self.assertRaisesRegex(PlotlyError, message, dash.insert, my_box, "above", None)

    def test_id_not_valid(self):
        my_box = {
            "type": "box",
            "boxType": "plot",
            "fileId": "AdamKulidjian:327",
            "shareKey": None,
            "title": "box 1",
        }

        message = (
            "Your box_id must be a number in your dashboard. To view a "
            "representation of your dashboard run get_preview()."
        )

        dash = dashboard.Dashboard()
        dash.insert(my_box, "above", 1)

        # insert box
        self.assertRaisesRegex(PlotlyError, message, dash.insert, my_box, "above", 0)
        # get box by id
        self.assertRaisesRegex(PlotlyError, message, dash.get_box, 0)

        # remove box
        self.assertRaisesRegex(PlotlyError, message, dash.remove, 0)

    def test_invalid_side(self):
        my_box = {
            "type": "box",
            "boxType": "plot",
            "fileId": "AdamKulidjian:327",
            "shareKey": None,
            "title": "box 1",
        }

        message = (
            "If there is at least one box in your dashboard, you "
            "must specify a valid side value. You must choose from "
            "'above', 'below', 'left', and 'right'."
        )

        dash = dashboard.Dashboard()
        dash.insert(my_box, "above", 0)

        self.assertRaisesRegex(
            PlotlyError, message, dash.insert, my_box, "somewhere", 1
        )

    def test_dashboard_dict(self):
        my_box = {
            "type": "box",
            "boxType": "plot",
            "fileId": "AdamKulidjian:327",
            "shareKey": None,
            "title": "box 1",
        }

        dash = dashboard.Dashboard()
        dash.insert(my_box)
        dash.insert(my_box, "above", 1)

        expected_dashboard = {
            "layout": {
                "direction": "vertical",
                "first": {
                    "direction": "vertical",
                    "first": {
                        "boxType": "plot",
                        "fileId": "AdamKulidjian:327",
                        "shareKey": None,
                        "title": "box 1",
                        "type": "box",
                    },
                    "second": {
                        "boxType": "plot",
                        "fileId": "AdamKulidjian:327",
                        "shareKey": None,
                        "title": "box 1",
                        "type": "box",
                    },
                    "size": 50,
                    "sizeUnit": "%",
                    "type": "split",
                },
                "second": {"boxType": "empty", "type": "box"},
                "size": 1500,
                "sizeUnit": "px",
                "type": "split",
            },
            "settings": {},
            "version": 2,
        }

        self.assertEqual(dash["layout"], expected_dashboard["layout"])
