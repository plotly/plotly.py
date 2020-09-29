def compute_anchors(position, vertical):
    xanchor = None
    yanchor = None
    if vertical:
        if position in ["n", "sw", "se"]:
            yanchor = "bottom"
        if position in ["nw", "ne", "s"]:
            yanchor = "top"
        if position in ["w", "e"]:
            yanchor = "middle"
        if position in ["ne", "e", "se"]:
            xanchor = "left"
        if position in ["sw", "w", "nw"]:
            xanchor = "right"
        if position in ["n", "s"]:
            xanchor = "center"
    else:
        if position in ["nw", "n", "ne"]:
            yanchor = "bottom"
        if position in ["se", "s", "sw"]:
            yanchor = "top"
        if position in ["w", "e"]:
            yanchor = "middle"
        if position in ["e", "sw", "nw"]:
            xanchor = "left"
        if position in ["ne", "se", "w"]:
            xanchor = "right"
        if position in ["n", "s"]:
            xanchor = "center"
    return xanchor, yanchor


def compute_coord(annotype, position):
    # If annotype is vline, this is y value, if hline, this is x value
    if annotype == "vline":
        if position in ["nw", "n", "ne"]:
            return 1
        if position in ["w", "e"]:
            return 0.5
        if position in ["sw", "s", "se"]:
            return 0
    if annotype == "hline":
        if position in ["nw", "sw", "w", "nw"]:
            return 0
        if position in ["n", "s"]:
            return 0.5
        if position in ["ne", "e", "se"]:
            return 1
