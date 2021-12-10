from __future__ import absolute_import

import math

import numpy as np
import plotly.graph_objects as go

from plotly import exceptions
from plotly.graph_objs import graph_objs
from plotly.figure_factory import utils


def create_quiver(
    x, y, u, v, scale=0.1, arrow_scale=0.3, angle=math.pi / 9, scaleratio=None, **kwargs
):
    """
    Returns data for a quiver plot.

    :param (list|ndarray) x: x coordinates of the arrow locations
    :param (list|ndarray) y: y coordinates of the arrow locations
    :param (list|ndarray) u: x components of the arrow vectors
    :param (list|ndarray) v: y components of the arrow vectors
    :param (float in [0,1]) scale: scales size of the arrows(ideally to
        avoid overlap). Default = .1
    :param (float in [0,1]) arrow_scale: value multiplied to length of barb
        to get length of arrowhead. Default = .3
    :param (angle in radians) angle: angle of arrowhead. Default = pi/9
    :param (positive float) scaleratio: the ratio between the scale of the y-axis
        and the scale of the x-axis (scale_y / scale_x). Default = None, the
        scale ratio is not fixed.
    :param kwargs: kwargs passed through plotly.graph_objs.Scatter
        for more information on valid kwargs call
        help(plotly.graph_objs.Scatter)

    :rtype (dict): returns a representation of quiver figure.

    Example 1: Trivial Quiver

    >>> from plotly.figure_factory import create_quiver
    >>> import math

    >>> # 1 Arrow from (0,0) to (1,1)
    >>> fig = create_quiver(x=[0], y=[0], u=[1], v=[1], scale=1)
    >>> fig.show()


    Example 2: Quiver plot using meshgrid

    >>> from plotly.figure_factory import create_quiver

    >>> import numpy as np
    >>> import math

    >>> # Add data
    >>> x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
    >>> u = np.cos(x)*y
    >>> v = np.sin(x)*y

    >>> #Create quiver
    >>> fig = create_quiver(x, y, u, v)
    >>> fig.show()


    Example 3: Styling the quiver plot

    >>> from plotly.figure_factory import create_quiver
    >>> import numpy as np
    >>> import math

    >>> # Add data
    >>> x, y = np.meshgrid(np.arange(-np.pi, math.pi, .5),
    ...                    np.arange(-math.pi, math.pi, .5))
    >>> u = np.cos(x)*y
    >>> v = np.sin(x)*y

    >>> # Create quiver
    >>> fig = create_quiver(x, y, u, v, scale=.2, arrow_scale=.3, angle=math.pi/6,
    ...                     name='Wind Velocity', line=dict(width=1))

    >>> # Add title to layout
    >>> fig.update_layout(title='Quiver Plot') # doctest: +SKIP
    >>> fig.show()


    Example 4: Forcing a fix scale ratio to maintain the arrow length

    >>> from plotly.figure_factory import create_quiver
    >>> import numpy as np

    >>> # Add data
    >>> x,y = np.meshgrid(np.arange(0.5, 3.5, .5), np.arange(0.5, 4.5, .5))
    >>> u = x
    >>> v = y
    >>> angle = np.arctan(v / u)
    >>> norm = 0.25
    >>> u = norm * np.cos(angle)
    >>> v = norm * np.sin(angle)

    >>> # Create quiver with a fix scale ratio
    >>> fig = create_quiver(x, y, u, v, scale = 1, scaleratio = 0.5)
    >>> fig.show()
    """
    utils.validate_equal_length(x, y, u, v)
    utils.validate_positive_scalars(arrow_scale=arrow_scale, scale=scale)

    if scaleratio is None:
        quiver_obj = _Quiver(x, y, u, v, scale, arrow_scale, angle)
    else:
        quiver_obj = _Quiver(x, y, u, v, scale, arrow_scale, angle, scaleratio)

    barb_x, barb_y = quiver_obj.get_barbs()
    arrow_x, arrow_y = quiver_obj.get_quiver_arrows()

    quiver_plot = graph_objs.Scatter(
        x=barb_x + arrow_x, y=barb_y + arrow_y, mode="lines", **kwargs
    )

    data = [quiver_plot]

    if scaleratio is None:
        layout = graph_objs.Layout(hovermode="closest")
    else:
        layout = graph_objs.Layout(
            hovermode="closest", yaxis=dict(scaleratio=scaleratio, scaleanchor="x")
        )

    return graph_objs.Figure(data=data, layout=layout)


##### ADD #########################################################################################################
# Constant:
r2 = np.sqrt(2)


# Score functions :

# Return 0, no impact on color
def zero_score(u1, v1):
    return 0


# Size function, return the squar of the quiver size
def size_score(u1, v1):
    return u1 ** 2 + v1 ** 2


# Return cos(a) with a the angle between a vector of coordinates (1,1) and therefore of norm square root of 2
def orientation_score(u1, v1):
    return (u1 + v1) / ((np.sqrt(size_score(u1, v1))) * r2)


# Insertion sorting function to order the arrows and assign them a gradual coloring
def tri_insertion_each(tab):
    for i in range(1, len(tab)):
        k = tab[i]
        j = i - 1
        while j >= 0 and k[4][0] < tab[j][4][0]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = k
    return tab


# Function that generates the colorbars for our diagram.
# Plotly being designed to display the components present in the figure,
# it is necessary to create invisible components that generate this bar. To do this,
# we create here about forty invisible points (opacity = 1) which follow the desired color bar to create the colorbar.
def colorbar_quiv(x1, y1, fig, colorbar_title, colorscale, n_color):
    max_x = np.max(x1)
    max_y = np.max(y1)
    values_x = [i * max_x / 40 for i in range(40)]
    values_y = [i * max_y / 40 for i in range(40)]

    fig.add_trace(
        go.Scatter(
            x=values_x,
            y=values_y,
            opacity=0,
            showlegend=False,
            marker=dict(
                size=16,
                cmax=max_x,
                cmin=0,
                color=values_x,
                colorbar=dict(title=colorbar_title, x=1 + n_color * 0.15),
                colorscale=colorscale,
            ),
            mode="markers",
        )
    )


# This function is used to give the color of each buttock
# so that it follows a 1D gradient chosen according to their order in the list sorted by score.
def gradient_1D(r, g, b, each_col, it, length_2, each_col_2):

    color = [r, g, b]

    # We use the 3 colors
    if 0 not in color:

        # Colors have gradient types given by the int associated with their variable
        # (r for red, g for green and b for blue)
        for i in range(3):

            if color[i] == 3:
                color[i] = round(each_col * it)

            elif color[i] == 1:
                color[i] = round(256 - each_col * it)

            # middle color
            if color[i] == 2:
                if it < length_2:
                    color[i] = round(each_col_2 * it)
                else:
                    color[i] = round(256 - each_col_2 * (it - length_2))

    # We only use two colors, the one with an assigned 0 is not used
    else:

        # Colors have gradient types given by the int associated with their variable
        # (r for red, g for green and b for blue)
        for i in range(3):

            if color[i] == 1:
                color[i] = round(each_col * it)

            elif color[i] == 2:
                color[i] = round(255 - each_col * it)

    # returns the color for the arrow
    return "rgba(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ",1)"


# This function gives the color for an arrow in a figure using 2 dimensions for the colors.
# One main and one secondary.
def gradient_2D(r, g, b, each_col, it, it_2, length):

    color = [r, g, b]

    # Colors have gradient types given by the int associated with their variable
    # (r for red, g for green and b for blue)
    for i in range(3):
        if color[i] == 2:
            color[i] = round(each_col * it)

        elif color[i] == 1:
            color[i] = round(256 - each_col * it)
        else:
            color[i] = round(each_col * it_2)

    return "rgba(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ",1)"


def create_colorised_quiver(x1, y1, u1, v1, **kwargs):
    color = kwargs.get("color", None)
    color_bar = kwargs.get("color_bar", None)
    colorscale = kwargs.get("colorscale", None)
    inv = kwargs.get("inv", None)

    colorbar_title = ""

    if color:
        # Forme de la fonction color (u1,v1) -> int :
        if color == "size_gradient":
            color = size_score
            mode = "1D"

        if isinstance(color, list):
            mode = color[0]
            color_1 = color[1]
            if mode == "2D":
                color_2 = color[2]

        if (inv) == None:
            inv = [0, 0, 0]

        if (colorscale) == None:

            if mode == "1D":
                colorscale = ["green", "red"]

        if mode == "1D":
            quivers_data = []

            for i in range(len(x1)):
                for j in range(len(u1[i])):

                    each_size = color_1(u1[i][j], v1[i][j])

                    quivers_data.append(
                        [
                            [x1[i][j]],
                            [y1[i][j]],
                            [u1[i][j]],
                            [v1[i][j]],
                            [[each_size], [i, j]],
                        ]
                    )

            A = quivers_data
            quivers_data = tri_insertion_each(quivers_data)

            each_col = 255 / len(quivers_data)

            r, g, b = inv

            if len(colorscale) == 2:

                add_value = 2
                for color in colorscale:
                    if color == "red":
                        r += add_value
                    if color == "green":
                        g += add_value
                    if color == "blue":
                        b += add_value
                    add_value += 1

                    if add_value == 3:
                        add_value = 1

            else:
                add_value = 1
                for color in colorscale:
                    if color == "red":
                        r += add_value
                    if color == "green":
                        g += add_value
                    if color == "blue":
                        b += add_value
                    add_value += 1

            # constants :
            length_2 = len(quivers_data) / 2
            each_col_2 = each_col * 2

            fig = create_quiver(
                quivers_data[0][0],
                quivers_data[0][1],
                quivers_data[0][2],
                quivers_data[0][3],
                showlegend=False,
            )

            for i in range(1, len(quivers_data)):

                if quivers_data[i][2] != []:
                    fig_each = create_quiver(
                        quivers_data[i][0],
                        quivers_data[i][1],
                        quivers_data[i][2],
                        quivers_data[i][3],
                        showlegend=False,
                    )

                    rgba_color = gradient_1D(r, g, b, each_col, i, length_2, each_col_2)

                    fig_each.update_traces(line_color=rgba_color)
                    fig.add_traces(data=fig_each.data)

        if mode == "2D":

            quivers_data = []

            dict_2 = {}
            quivers_data_2 = []

            for i in range(len(x1)):
                dict_2[i] = {}
                for j in range(len(u1[i])):

                    each_size = color_1(u1[i][j], v1[i][j])
                    each_2 = color_2(u1[i][j], v1[i][j])

                    quivers_data.append(
                        [
                            [x1[i][j]],
                            [y1[i][j]],
                            [u1[i][j]],
                            [v1[i][j]],
                            [[each_size], [i, j]],
                        ]
                    )
                    quivers_data_2.append(
                        [
                            [x1[i][j]],
                            [y1[i][j]],
                            [u1[i][j]],
                            [v1[i][j]],
                            [[each_2], [i, j]],
                        ]
                    )

            quivers_data = tri_insertion_each(quivers_data)
            quivers_data_2 = tri_insertion_each(quivers_data_2)

            each_col = 255 / len(quivers_data)

            r, g, b = inv

            add_value = 1
            for color in colorscale:
                if color == "red":
                    r += add_value
                if color == "green":
                    g += add_value
                if color == "blue":
                    b += add_value
                add_value += 1

                if 3 in (r, g, b):
                    add_value = 1

            fig = create_quiver(
                quivers_data[0][0],
                quivers_data[0][1],
                quivers_data[0][2],
                quivers_data[0][3],
                showlegend=False,
            )
            for i in range(1, len(quivers_data)):

                if quivers_data[i][2] != []:
                    fig_each = create_quiver(
                        quivers_data[i][0],
                        quivers_data[i][1],
                        quivers_data[i][2],
                        quivers_data[i][3],
                        showlegend=False,
                    )

                    i_2 = 0
                    while_condition = quivers_data[i][0:2]
                    while while_condition != quivers_data_2[i_2][0:2]:
                        i_2 += 1

                    rgba_color = gradient_2D(
                        r, g, b, each_col, i, i_2, len(quivers_data)
                    )

                    fig_each.update_traces(line_color=rgba_color)
                    fig.add_traces(data=fig_each.data)

        if color_bar:
            if color_bar == True:
                colorbar_quiv(x1, y1, fig, colorbar_title, ["green", "red"])
            if isinstance(color_bar, list):

                if mode == "1D":
                    # Forme de la liste attendue : [colorbar_title, colorbar_scale]
                    colorbar_quiv(x1, y1, fig, color_bar[0], colorscale, 1)
                if mode == "2D":
                    # Forme de la liste attendue : [colorbar_title, colorbar_scale]
                    colorbar_quiv(x1, y1, fig, color_bar[0], colorscale[:2], 1)
                    colorbar_quiv(
                        x1, y1, fig, color_bar[1], ["white"] + [colorscale[2]], 2
                    )

        fig.show()


############################################################################################


class _Quiver(object):
    """
    Refer to FigureFactory.create_quiver() for docstring
    """

    def __init__(self, x, y, u, v, scale, arrow_scale, angle, scaleratio=1, **kwargs):
        try:
            x = utils.flatten(x)
        except exceptions.PlotlyError:
            pass

        try:
            y = utils.flatten(y)
        except exceptions.PlotlyError:
            pass

        try:
            u = utils.flatten(u)
        except exceptions.PlotlyError:
            pass

        try:
            v = utils.flatten(v)
        except exceptions.PlotlyError:
            pass

        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.scale = scale
        self.scaleratio = scaleratio
        self.arrow_scale = arrow_scale
        self.angle = angle
        self.end_x = []
        self.end_y = []
        self.scale_uv()
        barb_x, barb_y = self.get_barbs()
        arrow_x, arrow_y = self.get_quiver_arrows()

    def scale_uv(self):
        """
        Scales u and v to avoid overlap of the arrows.

        u and v are added to x and y to get the
        endpoints of the arrows so a smaller scale value will
        result in less overlap of arrows.
        """
        self.u = [i * self.scale * self.scaleratio for i in self.u]
        self.v = [i * self.scale for i in self.v]

    def get_barbs(self):
        """
        Creates x and y startpoint and endpoint pairs

        After finding the endpoint of each barb this zips startpoint and
        endpoint pairs to create 2 lists: x_values for barbs and y values
        for barbs

        :rtype: (list, list) barb_x, barb_y: list of startpoint and endpoint
            x_value pairs separated by a None to create the barb of the arrow,
            and list of startpoint and endpoint y_value pairs separated by a
            None to create the barb of the arrow.
        """
        self.end_x = [i + j for i, j in zip(self.x, self.u)]
        self.end_y = [i + j for i, j in zip(self.y, self.v)]
        empty = [None] * len(self.x)
        barb_x = utils.flatten(zip(self.x, self.end_x, empty))
        barb_y = utils.flatten(zip(self.y, self.end_y, empty))
        return barb_x, barb_y

    def get_quiver_arrows(self):
        """
        Creates lists of x and y values to plot the arrows

        Gets length of each barb then calculates the length of each side of
        the arrow. Gets angle of barb and applies angle to each side of the
        arrowhead. Next uses arrow_scale to scale the length of arrowhead and
        creates x and y values for arrowhead point1 and point2. Finally x and y
        values for point1, endpoint and point2s for each arrowhead are
        separated by a None and zipped to create lists of x and y values for
        the arrows.

        :rtype: (list, list) arrow_x, arrow_y: list of point1, endpoint, point2
            x_values separated by a None to create the arrowhead and list of
            point1, endpoint, point2 y_values separated by a None to create
            the barb of the arrow.
        """
        dif_x = [i - j for i, j in zip(self.end_x, self.x)]
        dif_y = [i - j for i, j in zip(self.end_y, self.y)]

        # Get barb lengths(default arrow length = 30% barb length)
        barb_len = [None] * len(self.x)
        for index in range(len(barb_len)):
            barb_len[index] = math.hypot(dif_x[index] / self.scaleratio, dif_y[index])

        # Make arrow lengths
        arrow_len = [None] * len(self.x)
        arrow_len = [i * self.arrow_scale for i in barb_len]

        # Get barb angles
        barb_ang = [None] * len(self.x)
        for index in range(len(barb_ang)):
            barb_ang[index] = math.atan2(dif_y[index], dif_x[index] / self.scaleratio)

        # Set angles to create arrow
        ang1 = [i + self.angle for i in barb_ang]
        ang2 = [i - self.angle for i in barb_ang]

        cos_ang1 = [None] * len(ang1)
        for index in range(len(ang1)):
            cos_ang1[index] = math.cos(ang1[index])
        seg1_x = [i * j for i, j in zip(arrow_len, cos_ang1)]

        sin_ang1 = [None] * len(ang1)
        for index in range(len(ang1)):
            sin_ang1[index] = math.sin(ang1[index])
        seg1_y = [i * j for i, j in zip(arrow_len, sin_ang1)]

        cos_ang2 = [None] * len(ang2)
        for index in range(len(ang2)):
            cos_ang2[index] = math.cos(ang2[index])
        seg2_x = [i * j for i, j in zip(arrow_len, cos_ang2)]

        sin_ang2 = [None] * len(ang2)
        for index in range(len(ang2)):
            sin_ang2[index] = math.sin(ang2[index])
        seg2_y = [i * j for i, j in zip(arrow_len, sin_ang2)]

        # Set coordinates to create arrow
        for index in range(len(self.end_x)):
            point1_x = [i - j * self.scaleratio for i, j in zip(self.end_x, seg1_x)]
            point1_y = [i - j for i, j in zip(self.end_y, seg1_y)]
            point2_x = [i - j * self.scaleratio for i, j in zip(self.end_x, seg2_x)]
            point2_y = [i - j for i, j in zip(self.end_y, seg2_y)]

        # Combine lists to create arrow
        empty = [None] * len(self.end_x)
        arrow_x = utils.flatten(zip(point1_x, self.end_x, point2_x, empty))
        arrow_y = utils.flatten(zip(point1_y, self.end_y, point2_y, empty))
        return arrow_x, arrow_y
