import plotly.graph_objects as go
from _plotly_utils.exceptions import PlotlyKeyError
import pytest


def error_substr(s, r):
    """ remove a part of the error message we don't want to compare """
    return s.replace(r, "")


@pytest.fixture
def some_fig():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[]))
    fig.add_shape(type="rect", x0=1, x1=2, y0=3, y1=4)
    fig.add_shape(type="rect", x0=10, x1=20, y0=30, y1=40)
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
    return fig


def test_raises_on_bad_index(some_fig):
    # Check indexing errors can be detected when path used as key to go.Figure
    raised = False
    try:
        x0 = some_fig["layout.shapes[2].x0"]
    except KeyError as e:
        raised = True
        assert (
            e.args[0].find(
                """Bad property path:
layout.shapes[2].x0
              ^"""
            )
            >= 0
        )
    assert raised


def test_raises_on_bad_dot_property(some_fig):

    # Check . property lookup errors can be detected when path used as key to
    # go.Figure
    raised = False
    try:
        x2000 = some_fig["layout.shapes[1].x2000"]
    except KeyError as e:
        raised = True
        assert (
            e.args[0].find(
                """Bad property path:
layout.shapes[1].x2000
                 ^^^^^"""
            )
            and (e.args[0].find("""Did you mean "x0"?""") >= 0) >= 0
        )
    assert raised


def test_raises_on_bad_ancestor_dot_property(some_fig):

    # Check . property lookup errors but not on the last part of the path
    raised = False
    try:
        x2000 = some_fig["layout.shapa[1].x2000"]
    except KeyError as e:
        raised = True
        assert (
            e.args[0].find(
                """Bad property path:
layout.shapa[1].x2000
       ^^^^^"""
            )
            and (e.args[0].find("""Did you mean "shapes"?""") >= 0) >= 0
        )
    assert raised


def test_raises_on_bad_indexed_underscore_property(some_fig):

    # The way these tests work is first the error is raised without using
    # underscores to get the Exception we expect, then the string showing the
    # bad property path is removed (because it will not match the string
    # returned when the same error is thrown using underscores).
    # Then the error is thrown using underscores and the Exceptions are
    # compared, but we adjust the expected bad property error because it will be
    # different when underscores are used.

    # finds bad part when using the path as a key to figure and throws the error
    # for the last good property it found in the path
    raised = False
    try:
        # get the error without using a path-like key, we compare with this error
        some_fig.data[0].line["colr"] = "blue"
    except ValueError as e_correct:
        raised = True
        # remove "Bad property path:
        e_correct_substr = error_substr(
            e_correct.args[0],
            """
Bad property path:
colr
^^^^""",
        )
    # if the string starts with "Bad property path:" then this test cannot work
    # this way.
    assert len(e_correct_substr) > 0
    assert raised

    raised = False
    try:
        some_fig["data[0].line_colr"] = "blue"
    except ValueError as e:
        raised = True
        e_substr = error_substr(
            e.args[0],
            """
Bad property path:
data[0].line_colr
             ^^^^""",
        )
        assert (
            (
                e.args[0].find(
                    """Bad property path:
data[0].line_colr
             ^^^^"""
                )
                >= 0
            )
            and (e.args[0].find("""Did you mean "color"?""") >= 0)
            and (e_substr == e_correct_substr)
        )
    assert raised

    raised = False
    try:
        # get the error without using a path-like key
        some_fig.add_trace(go.Scatter(x=[1, 2], y=[3, 4], line=dict(colr="blue")))
    except ValueError as e_correct:
        raised = True
        e_correct_substr = error_substr(
            e_correct.args[0],
            """
Bad property path:
colr
^^^^""",
        )
    assert raised

    raised = False
    # finds bad part when using the path as a keyword argument to a subclass of
    # BasePlotlyType and throws the error for the last good property found in
    # the path
    try:
        some_fig.add_trace(go.Scatter(x=[1, 2], y=[3, 4], line_colr="blue"))
    except ValueError as e:
        raised = True
        e_substr = error_substr(
            e.args[0],
            """
Bad property path:
line_colr
     ^^^^""",
        )
        assert (
            (
                e.args[0].find(
                    """Bad property path:
line_colr
     ^^^^"""
                )
                and (e.args[0].find("""Did you mean "color"?""") >= 0) >= 0
            )
            and (e_substr == e_correct_substr)
        )
    assert raised

    raised = False
    # finds bad part when using the path as a keyword argument to a subclass of
    # BaseFigure and throws the error for the last good property found in
    # the path
    try:
        fig2 = go.Figure(layout=dict(title=dict(txt="two")))
    except ValueError as e_correct:
        raised = True
        e_correct_substr = error_substr(
            e_correct.args[0],
            """
Bad property path:
txt
^^^""",
        )
    assert raised

    raised = False
    try:
        fig2 = go.Figure(layout_title_txt="two")
    except TypeError as e:
        raised = True
        # when the Figure constructor sees the same ValueError above, a
        # ValueError is raised and adds an error message in front of the same
        # ValueError thrown above
        e_substr = error_substr(
            e.args[0],
            """
Bad property path:
layout_title_txt
             ^^^""",
        )
        # also remove the invalid Figure property string added by the Figure constructor
        e_substr = error_substr(
            e_substr,
            """invalid Figure property: layout_title_txt
""",
        )
        assert (
            (
                e.args[0].find(
                    """Bad property path:
layout_title_txt
             ^^^""",
                )
                >= 0
            )
            and (e.args[0].find("""Did you mean "text"?""") >= 0)
            and (e_substr == e_correct_substr)
        )
    assert raised

    raised = False
    # this is like the above test for subclasses of BasePlotlyType but makes sure it
    # works when the bad part is not the last part in the path
    try:
        some_fig.update_layout(geo=dict(ltaxis=dict(showgrid=True)))
    except ValueError as e_correct:
        raised = True
        e_correct_substr = error_substr(
            e_correct.args[0],
            """
Bad property path:
ltaxis
^^^^^^""",
        )
    assert raised

    raised = False
    try:
        some_fig.update_layout(geo_ltaxis_showgrid=True)
    except ValueError as e:
        raised = True
        e_substr = error_substr(
            e.args[0],
            """
Bad property path:
geo_ltaxis_showgrid
    ^^^^^^""",
        )
        assert (
            (
                e.args[0].find(
                    """Bad property path:
geo_ltaxis_showgrid
    ^^^^^^"""
                )
                >= 0
            )
            and (e.args[0].find("""Did you mean "lataxis"?""") >= 0)
            and (e_substr == e_correct_substr)
        )
    assert raised


def test_describes_subscripting_error(some_fig):
    # This test works like test_raises_on_bad_indexed_underscore_property but
    # removes the error raised because the property does not support
    # subscripting.
    # Note that, to raise the error, we try to access the value rather than
    # assign something to it. We have to do this, because Plotly.py tries to
    # access the value to see if it is valid, so the error raised has to do with
    # subscripting and not assignment (even though we are trying to assign it a
    # value).
    raised = False
    try:
        # some_fig.update_traces(text_yo="hey") but without using underscores
        some_fig.data[0].text["yo"]
    except TypeError as e:
        raised = True
        e_correct_substr = e.args[0]
    assert raised
    raised = False
    try:
        some_fig.update_traces(text_yo="hey")
    except ValueError as e:
        raised = True
        print(e.args[0])
        e_substr = error_substr(
            e.args[0],
            """

Invalid value received for the 'text' property of scatter

    The 'text' property is a string and must be specified as:
      - A string
      - A number that will be converted to a string
      - A tuple, list, or one-dimensional numpy array of the above

Property does not support subscripting:
text_yo
^^^^""",
        )
        assert (
            (
                e.args[0].find(
                    """
Property does not support subscripting:
text_yo
^^^^"""
                )
                >= 0
            )
            and (e_substr == e_correct_substr)
        )
    assert raised

    # Same as previous test but tests deeper path
    raised = False
    try:
        # go.Figure(go.Scatter()).update_traces(textfont_family_yo="hey") but
        # without using underscores
        some_fig.data[0].textfont.family["yo"]
    except TypeError as e:
        raised = True
        e_correct_substr = e.args[0]
    assert raised
    raised = False
    try:
        go.Figure(go.Scatter()).update_traces(textfont_family_yo="hey")
    except ValueError as e:
        raised = True
        e_substr = error_substr(
            e.args[0],
            """

Invalid value received for the 'family' property of scatter.textfont

    The 'family' property is a string and must be specified as:
      - A non-empty string
      - A tuple, list, or one-dimensional numpy array of the above

Property does not support subscripting:
textfont_family_yo
         ^^^^^^""",
        )
        assert (
            (
                e.args[0].find(
                    """
Property does not support subscripting:
textfont_family_yo
         ^^^^^^"""
                )
                >= 0
            )
            and (e_substr == e_correct_substr)
        )
    assert raised


def test_described_subscript_error_on_type_error(some_fig):
    # The above tests for subscripting errors did not test for when we attempt
    # to subscript an object that is not None, such as a string or a number.
    # These do that.
    raised = False
    try:
        # Trying to address with a key an object that doesn't support it (as we
        # do below) reports an error listing what are valid assignments to the
        # object, like when we try and assign a number to something that expects as string.
        some_fig["layout_template_layout_plot_bgcolor"] = 1
    except ValueError as e:
        raised = True
        # Trim off the beginning of the error string because it is related to
        # trying to assign a number to something expecting a string, whereas
        # below the error will be due to trying to subscript something that
        # doesn't support it. But the list of valid properties should be shown
        # for both errors and this is what we extract.
        # Trimmed like this because this string is different in Python2 than
        # Python3
        e_correct_substr = e.args[0]
        start_at = e_correct_substr.find("    The 'plot_bgcolor'")
        e_correct_substr = e_correct_substr[start_at:]
        e_correct_substr += """

Property does not support subscripting:
template_layout_plot_bgcolor_x
                ^^^^^^^^^^^^"""
    assert raised
    raised = False
    try:
        some_fig.update_layout(template_layout_plot_bgcolor_x=1)
    except ValueError as e:
        raised = True
        print(e.args[0])
        e_substr = error_substr(
            e.args[0],
            """string indices must be integers

Invalid value received for the 'plot_bgcolor' property of layout

""",
        )
        assert e_substr == e_correct_substr
    assert raised


def test_subscript_error_exception_types(some_fig):
    # Assert that these raise the expected error types
    # when width is None
    with pytest.raises(ValueError):
        some_fig.update_layout(width_yo=100)
    with pytest.raises(KeyError):
        yo = some_fig["layout_width_yo"]

    some_fig.update_layout(width=100)
    # when width is specified
    with pytest.raises(ValueError):
        some_fig.update_layout(width_yo=100)
    with pytest.raises(KeyError):
        yo = some_fig["layout_width_yo"]


def form_error_string(call, exception, subs):
    """
    call is a function that raises exception.
    exception is an exception class, e.g., KeyError.
    subs is a list of replacements to be performed on the exception string. Each
    replacement is only performed once on the exception string so the
    replacement of multiple occurences of a pattern is specified by repeating a
    (pattern,relacement) pair in the list.
    returns modified exception string 
    """
    raised = False
    try:
        call()
    except exception as e:
        raised = True
        msg = e.args[0]
        for pat, rep in subs:
            msg = msg.replace(pat, rep, 1)
    assert raised
    return msg


def check_error_string(call, exception, correct_str, subs):
    raised = False
    try:
        call()
    except exception as e:
        raised = True
        msg = e.args[0]
        for pat, rep in subs:
            msg = msg.replace(pat, rep, 1)
        print("MSG")
        print(msg)
        print("CORRECT")
        print(correct_str)
        assert msg == correct_str
    assert raised


def test_leading_underscore_errors(some_fig):
    # get error string but alter it to form the final expected string
    def _raise_bad_property_path_form():
        some_fig.update_layout(bogus=7)

    def _raise_bad_property_path_real():
        some_fig.update_layout(_hey_yall=7)

    correct_err_str = form_error_string(
        _raise_bad_property_path_form,
        ValueError,
        # change last boxgap to geo because bogus is closest to boxgap but _hey
        # closest to geo, but remember that boxgap is in the list of valid keys
        # displayed by the error string
        [
            ("bogus", "_hey"),
            ("bogus", "_hey_yall"),
            ("^^^^^", "^^^^"),
            ('Did you mean "boxgap"', 'Did you mean "geo"'),
            ('Did you mean "boxgap"', 'Did you mean "geo"'),
        ],
    )
    check_error_string(_raise_bad_property_path_real, ValueError, correct_err_str, [])


def test_trailing_underscore_errors(some_fig):
    # get error string but alter it to form the final expected string
    def _raise_bad_property_path_form():
        some_fig.update_layout(title_text_bogus="hi")

    def _raise_bad_property_path_real():
        some_fig.update_layout(title_text_="hi")

    correct_err_str = form_error_string(
        _raise_bad_property_path_form,
        ValueError,
        [
            (
                "Property does not support subscripting",
                "Property does not support subscripting and path has trailing underscores",
            ),
            ("text_bogus", "text_"),
            ("^^^^", "^^^^^"),
        ],
    )
    # no need to replace ^^^^^ because bogus and text_ are same length
    check_error_string(_raise_bad_property_path_real, ValueError, correct_err_str, [])


def test_embedded_underscore_errors(some_fig):
    # get error string but alter it to form the final expected string
    def _raise_bad_property_path_form():
        some_fig.update_layout(title_font_bogusey="hi")

    def _raise_bad_property_path_real():
        some_fig.update_layout(title_font__family="hi")

    correct_err_str = form_error_string(
        _raise_bad_property_path_form,
        ValueError,
        [
            ("bogusey", "_family"),
            ("bogusey", "_family"),
            ('Did you mean "color"?', 'Did you mean "family"?'),
            ('Did you mean "color"?', 'Did you mean "family"?'),
        ],
    )
    # no need to replace ^^^^^ because bogus and font_ are same length
    check_error_string(_raise_bad_property_path_real, ValueError, correct_err_str, [])


def test_solo_underscore_errors(some_fig):
    # get error string but alter it to form the final expected string
    def _raise_bad_property_path_form():
        some_fig.update_layout(bogus="hi")

    def _raise_bad_property_path_real():
        some_fig.update_layout(_="hi")

    correct_err_str = form_error_string(
        _raise_bad_property_path_form,
        ValueError,
        [
            ("bogus", "_"),
            ("bogus", "_"),
            ("^^^^^", "^"),
            ('Did you mean "boxgap"', 'Did you mean "geo"'),
            ('Did you mean "boxgap"', 'Did you mean "geo"'),
        ],
    )
    check_error_string(_raise_bad_property_path_real, ValueError, correct_err_str, [])


def test_repeated_underscore_errors(some_fig):
    # get error string but alter it to form the final expected string
    def _raise_bad_property_path_form():
        some_fig.update_layout(bogus="hi")

    def _raise_bad_property_path_real():
        some_fig.update_layout(__="hi")

    correct_err_str = form_error_string(
        _raise_bad_property_path_form,
        ValueError,
        [
            ("bogus", "__"),
            ("bogus", "__"),
            ("^^^^^", "^^"),
            ('Did you mean "boxgap"', 'Did you mean "geo"'),
            ('Did you mean "boxgap"', 'Did you mean "geo"'),
        ],
    )
    check_error_string(_raise_bad_property_path_real, ValueError, correct_err_str, [])


def test_leading_underscore_errors_dots_and_subscripts(some_fig):
    # get error string but alter it to form the final expected string
    some_fig.add_annotation(text="hi")

    def _raise_bad_property_path_form():
        some_fig["layout.annotations[0].bogus_family"] = "hi"

    def _raise_bad_property_path_real():
        some_fig["layout.annotations[0]._font_family"] = "hi"

    correct_err_str = form_error_string(
        _raise_bad_property_path_form,
        ValueError,
        [("bogus", "_font"), ("bogus", "_font"), ("^^^^^", "^^^^^")],
    )
    check_error_string(_raise_bad_property_path_real, ValueError, correct_err_str, [])


def test_trailing_underscore_errors_dots_and_subscripts(some_fig):
    # get error string but alter it to form the final expected string
    some_fig.add_annotation(text="hi")

    def _raise_bad_property_path_form():
        some_fig["layout.annotations[0].font_family_bogus"] = "hi"

    def _raise_bad_property_path_real():
        some_fig["layout.annotations[0].font_family_"] = "hi"

    correct_err_str = form_error_string(
        _raise_bad_property_path_form,
        ValueError,
        [
            (
                "Property does not support subscripting",
                "Property does not support subscripting and path has trailing underscores",
            ),
            ("family_bogus", "family_"),
            ("^^^^^^", "^^^^^^^"),
        ],
    )
    check_error_string(_raise_bad_property_path_real, ValueError, correct_err_str, [])


def test_repeated_underscore_errors_dots_and_subscripts(some_fig):
    # get error string but alter it to form the final expected string
    some_fig.add_annotation(text="hi")

    def _raise_bad_property_path_form():
        some_fig["layout.annotations[0].font_bogusey"] = "hi"

    def _raise_bad_property_path_real():
        some_fig["layout.annotations[0].font__family"] = "hi"

    correct_err_str = form_error_string(
        _raise_bad_property_path_form,
        ValueError,
        [
            ("bogusey", "_family"),
            ("bogusey", "_family"),
            ('Did you mean "color"?', 'Did you mean "family"?'),
            ('Did you mean "color"?', 'Did you mean "family"?'),
        ],
    )
    check_error_string(_raise_bad_property_path_real, ValueError, correct_err_str, [])


def test_single_prop_path_key_guess(some_fig):
    raised = False
    try:
        some_fig.layout.shapes[0]["typ"] = "sandwich"
    except ValueError as e:
        raised = True
        assert e.args[0].find('Did you mean "type"?') >= 0
    assert raised
