import plotly.graph_objects as go
from numpy import argmax, argmin, mean


def compute_anchors_for_line(position, vertical):
    xanchor = None
    yanchor = None
    if vertical:
        if position in ["n", "top", "sw", "bottom left", "se", "bottom right"]:
            yanchor = "bottom"
        if position in ["nw", "top left", "ne", "top right", "s", "bottom"]:
            yanchor = "top"
        if position in ["w", "left", "e", "right"]:
            yanchor = "middle"
        if position in ["ne", "top right", "e", "right", "se", "bottom right"]:
            xanchor = "left"
        if position in ["sw", "bottom left", "w", "left", "nw", "top left"]:
            xanchor = "right"
        if position in ["n", "top", "s", "bottom"]:
            xanchor = "center"
    else:
        if position in ["nw", "top left", "n", "top", "ne", "top right"]:
            yanchor = "bottom"
        if position in ["se", "bottom right", "s", "bottom", "sw", "bottom left"]:
            yanchor = "top"
        if position in ["w", "left", "e", "right"]:
            yanchor = "middle"
        if position in ["e", "right", "sw", "bottom left", "nw", "top left"]:
            xanchor = "left"
        if position in ["ne", "top right", "se", "bottom right", "w", "left"]:
            xanchor = "right"
        if position in ["n", "top", "s", "bottom"]:
            xanchor = "center"
    return xanchor, yanchor


def compute_coord_for_line(position, vertical):
    # If vertical, this is y value, otherwise, this is x value
    if vertical:
        if position in ["nw", "top left", "n", "top", "ne", "top right"]:
            return 1
        if position in ["w", "left", "e", "right"]:
            return 0.5
        if position in ["sw", "bottom left", "s", "bottom", "se", "bottom right"]:
            return 0
    else:
        if position in [
            "nw",
            "top left",
            "sw",
            "bottom left",
            "w",
            "left",
            "nw",
            "top left",
        ]:
            return 0
        if position in ["n", "top", "s", "bottom"]:
            return 0.5
        if position in ["ne", "top right", "e", "right", "se", "bottom right"]:
            return 1


def annotation_params_for_line(shape_type, shape_args, position):
    # all x0, x1, y0, y1 are used to place the annotation, that way it could
    # work with a slanted line
    # even with a slanted line, there are the horizontal and vertical
    # conventions of placing a shape
    x0 = shape_args["x0"]
    x1 = shape_args["x1"]
    y0 = shape_args["y0"]
    y1 = shape_args["y1"]
    X = [x0, x1]
    Y = [y0, y1]
    R = "right"
    T = "top"
    L = "left"
    C = "center"
    B = "bottom"
    M = "middle"
    aY = max(Y)
    iY = min(Y)
    mY = mean(Y)
    aaY = argmax(Y)
    aiY = argmin(Y)
    aX = max(X)
    iX = min(X)
    mX = mean(X)
    aaX = argmax(X)
    aiX = argmin(X)

    def _d(xanchor, yanchor, x, y):
        return dict(xanchor=xanchor, yanchor=yanchor, x=x, y=y)

    if shape_type == "vline":
        if position == "top left":
            return _d(R, T, X[aaY], aY)
        if position == "top right":
            return _d(L, T, X[aaY], aY)
        if position == "top":
            return _d(C, B, X[aaY], aY)
        if position == "bottom left":
            return _d(R, B, X[aiY], iY)
        if position == "bottom right":
            return _d(L, B, X[aiY], iY)
        if position == "bottom":
            return _d(C, T, X[aiY], iY)
        if position == "left":
            return _d(R, M, eX, eY)
        if position == "right":
            return _d(L, M, eX, eY)
        return _d(L, T, X[aaY], aY)
    if shape_type == "hline":
        if position == "top left":
            return _d(L, B, iX, Y[aiX])
        if position == "top right":
            return _d(R, B, aX, Y[aaX])
        if position == "top":
            return _d(C, B, mX, mY)
        if position == "bottom left":
            return _d(L, T, iX, Y[aiX])
        if position == "bottom right":
            return _d(R, T, aX, Y[aaX])
        if position == "bottom":
            return _d(C, T, mX, mY)
        if position == "left":
            return _d(R, M, iX, Y[aiX])
        if position == "right":
            return _d(L, M, aX, Y[aaX])
        return _d(R, B, aX, Y[aaX])


def annotation_params_for_rect(shape_type, shape_args, position):
    x0 = shape_args["x0"]
    x1 = shape_args["x1"]
    y0 = shape_args["y0"]
    y1 = shape_args["y1"]

    def _d(xanchor, yanchor, x, y):
        return dict(xanchor=xanchor, yanchor=yanchor, x=x, y=y)

    if position == "inside top left":
        return _d("left", "top", min([x0, x1]), max([y0, y1]))
    if position == "inside top right":
        return _d("right", "top", max([x0, x1]), max([y0, y1]))
    if position == "inside top":
        return _d("center", "top", mean([x0, x1]), max([y0, y1]))
    if position == "inside bottom left":
        return _d("left", "bottom", min([x0, x1]), min([y0, y1]))
    if position == "inside bottom right":
        return _d("right", "bottom", max([x0, x1]), min([y0, y1]))
    if position == "inside bottom":
        return _d("center", "bottom", mean([x0, x1]), min([y0, y1]))
    if position == "inside left":
        return _d("left", "middle", min([x0, x1]), mean([y0, y1]))
    if position == "inside right":
        return _d("right", "middle", max([x0, x1]), mean([y0, y1]))
    if position == "inside":
        # TODO: Do we want this?
        return _d("center", "middle", mean([x0, x1]), mean([y0, y1]))
    if position == "outside top left":
        return _d("right", "bottom", min([x0, x1]), max([y0, y1]))
    if position == "outside top right":
        return _d("left", "bottom", max([x0, x1]), max([y0, y1]))
    if position == "outside top":
        return _d("center", "bottom", mean([x0, x1]), max([y0, y1]))
    if position == "outside bottom left":
        return _d("right", "top", min([x0, x1]), min([y0, y1]))
    if position == "outside bottom right":
        return _d("left", "top", max([x0, x1]), min([y0, y1]))
    if position == "outside bottom":
        return _d("center", "top", mean([x0, x1]), min([y0, y1]))
    if position == "outside left":
        return _d("right", "middle", min([x0, x1]), mean([y0, y1]))
    if position == "outside right":
        return _d("left", "middle", max([x0, x1]), mean([y0, y1]))
    # default is inside top right
    return _d("right", "top", max([x0, x1]), max([y0, y1]))


def axis_spanning_shape_annotation(annotation, shape_type, shape_args, kwargs):
    """
    annotation: a go.layout.Annotation object, a dict describing an annotation, or None
    shape_type: one of 'vline', 'hline', 'vrect', 'hrect' and determines how the
                x, y, xanchor, and yanchor values are set.
    shape_args: the parameters used to draw the shape, which are used to place the annotation
    kwargs:     a dictionary that was the kwargs of a
                _process_multiple_axis_spanning_shapes spanning shapes call. Items in this
                dict whose keys start with 'annotation_' will be extracted and the keys with
                the 'annotation_' part stripped off will be used to assign properties of the
                new annotation.

    Property precedence:
    The annotation's x, y, xanchor, and yanchor properties are set based on the
    shape_type argument. Each property already specified in the annotation or
    through kwargs will be left as is (not replaced by the value computed using
    shape_type). Note that the xref and yref properties will in general get
    overwritten if the result of this function is passed to an add_annotation
    called with the row and col parameters specified.
    """
    # Force to go.layout.Annotation, no matter if it is that already, a dict or None
    annotation = go.layout.Annotation(annotation)
    # set properties based on annotation_ prefixed kwargs
    prefix = "annotation_"
    len_prefix = len(prefix)
    annotation_keys = filter(lambda k: k.startswith(prefix), kwargs.keys())
    for k in annotation_keys:
        subk = k[len_prefix:]
        annotation[subk] = kwargs[k]
    # set x, y, xanchor, yanchor based on shape_type and position
    annotation_position = None
    if "annotation_position" in kwargs.keys():
        annotation_position = kwargs["annotation_position"]
