from numpy import argmax, argmin, mean


def _df_anno(xanchor, yanchor, x, y):
    """ Default annotation parameters """
    return dict(xanchor=xanchor, yanchor=yanchor, x=x, y=y, showarrow=False)


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

    if shape_type == "vline":
        if position == "top left":
            return _df_anno(R, T, X[aaY], aY)
        if position == "top right":
            return _df_anno(L, T, X[aaY], aY)
        if position == "top":
            return _df_anno(C, B, X[aaY], aY)
        if position == "bottom left":
            return _df_anno(R, B, X[aiY], iY)
        if position == "bottom right":
            return _df_anno(L, B, X[aiY], iY)
        if position == "bottom":
            return _df_anno(C, T, X[aiY], iY)
        if position == "left":
            return _df_anno(R, M, eX, eY)
        if position == "right":
            return _df_anno(L, M, eX, eY)
        return _df_anno(L, T, X[aaY], aY)
    if shape_type == "hline":
        if position == "top left":
            return _df_anno(L, B, iX, Y[aiX])
        if position == "top right":
            return _df_anno(R, B, aX, Y[aaX])
        if position == "top":
            return _df_anno(C, B, mX, mY)
        if position == "bottom left":
            return _df_anno(L, T, iX, Y[aiX])
        if position == "bottom right":
            return _df_anno(R, T, aX, Y[aaX])
        if position == "bottom":
            return _df_anno(C, T, mX, mY)
        if position == "left":
            return _df_anno(R, M, iX, Y[aiX])
        if position == "right":
            return _df_anno(L, M, aX, Y[aaX])
        return _df_anno(R, B, aX, Y[aaX])


def annotation_params_for_rect(shape_type, shape_args, position):
    x0 = shape_args["x0"]
    x1 = shape_args["x1"]
    y0 = shape_args["y0"]
    y1 = shape_args["y1"]

    if position == "inside top left":
        return _df_anno("left", "top", min([x0, x1]), max([y0, y1]))
    if position == "inside top right":
        return _df_anno("right", "top", max([x0, x1]), max([y0, y1]))
    if position == "inside top":
        return _df_anno("center", "top", mean([x0, x1]), max([y0, y1]))
    if position == "inside bottom left":
        return _df_anno("left", "bottom", min([x0, x1]), min([y0, y1]))
    if position == "inside bottom right":
        return _df_anno("right", "bottom", max([x0, x1]), min([y0, y1]))
    if position == "inside bottom":
        return _df_anno("center", "bottom", mean([x0, x1]), min([y0, y1]))
    if position == "inside left":
        return _df_anno("left", "middle", min([x0, x1]), mean([y0, y1]))
    if position == "inside right":
        return _df_anno("right", "middle", max([x0, x1]), mean([y0, y1]))
    if position == "inside":
        # TODO: Do we want this?
        return _df_anno("center", "middle", mean([x0, x1]), mean([y0, y1]))
    if position == "outside top left":
        return _df_anno("right", "bottom", min([x0, x1]), max([y0, y1]))
    if position == "outside top right":
        return _df_anno("left", "bottom", max([x0, x1]), max([y0, y1]))
    if position == "outside top":
        return _df_anno("center", "bottom", mean([x0, x1]), max([y0, y1]))
    if position == "outside bottom left":
        return _df_anno("right", "top", min([x0, x1]), min([y0, y1]))
    if position == "outside bottom right":
        return _df_anno("left", "top", max([x0, x1]), min([y0, y1]))
    if position == "outside bottom":
        return _df_anno("center", "top", mean([x0, x1]), min([y0, y1]))
    if position == "outside left":
        return _df_anno("right", "middle", min([x0, x1]), mean([y0, y1]))
    if position == "outside right":
        return _df_anno("left", "middle", max([x0, x1]), mean([y0, y1]))
    # default is inside top right
    return _df_anno("right", "top", max([x0, x1]), max([y0, y1]))


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

    Returns an annotation populated with fields based on the
    annotation_position, annotation_ prefixed kwargs or the original annotation
    passed in to this function.
    """
    # Force to go.layout.Annotation, no matter if it is that already, a dict or None
    # TODO: We can't import go.layout.Annotation so we initialize this as a
    # dict. This strategy is inferior to initializing as a go.layout.Annotation
    # because there's no checking if a key is valid. Eventually it'd be better
    # to use go.layout.Annotation.
    if annotation is None:
        annotation = dict()
    # set properties based on annotation_ prefixed kwargs
    prefix = "annotation_"
    len_prefix = len(prefix)
    annotation_keys = filter(lambda k: k.startswith(prefix), kwargs.keys())
    for k in annotation_keys:
        if k == "annotation_position":
            # don't set so that Annotation constructor doesn't complain
            continue
        subk = k[len_prefix:]
        annotation[subk] = kwargs[k]
    # set x, y, xanchor, yanchor based on shape_type and position
    annotation_position = None
    if "annotation_position" in kwargs.keys():
        annotation_position = kwargs["annotation_position"]
    if shape_type.endswith("line"):
        shape_dict = annotation_params_for_line(
            shape_type, shape_args, annotation_position
        )
    elif shape_type.endswith("rect"):
        shape_dict = annotation_params_for_rect(
            shape_type, shape_args, annotation_position
        )
    for k in shape_dict.keys():
        # only set property derived from annotation_position if it hasn't already been set
        # see above: this would be better as a go.layout.Annotation then the key
        # would be checked for validity here (otherwise it is checked later,
        # which I guess is ok too)
        if (k not in annotation) or (annotation[k] is None):
            annotation[k] = shape_dict[k]
    return annotation


def split_dict_by_key_prefix(d, prefix):
    """
    Returns two dictionaries, one containing all the items whose keys do not
    start with a prefix and another containing all the items whose keys do start
    with the prefix. Note that the prefix is not removed from the keys.
    """
    no_prefix = dict()
    with_prefix = dict()
    for k in d.keys():
        if k.startswith(prefix):
            with_prefix[k] = d[k]
        else:
            no_prefix[k] = d[k]
    return (no_prefix, with_prefix)
