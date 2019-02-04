from __future__ import absolute_import
from plotly import optional_imports
from plotly.graph_objs import graph_objs as go

import numpy as np
interpolate = optional_imports.get_module('scipy.interpolate')


def _pl_deep():
    return [[0.0, 'rgb(253, 253, 204)'],
            [0.1, 'rgb(201, 235, 177)'],
            [0.2, 'rgb(145, 216, 163)'],
            [0.3, 'rgb(102, 194, 163)'],
            [0.4, 'rgb(81, 168, 162)'],
            [0.5, 'rgb(72, 141, 157)'],
            [0.6, 'rgb(64, 117, 152)'],
            [0.7, 'rgb(61, 90, 146)'],
            [0.8, 'rgb(65, 64, 123)'],
            [0.9, 'rgb(55, 44, 80)'],
            [1.0, 'rgb(39, 26, 44)']]


def _transform_barycentric_cartesian():
    """
    Returns the transformation matrix from barycentric to cartesian
    coordinates and conversely.
    """
    # reference triangle
    tri_verts = np.array([[0.5, np.sqrt(3) / 2], [0, 0], [1, 0]])
    M = np.array([tri_verts[:, 0], tri_verts[:, 1], np.ones(3)])
    return M, np.linalg.inv(M)


def _contour_trace(x, y, z, tooltip, ncontours=None, colorscale='Viridis',
                   showscale=False, linewidth=0.5,
                   linecolor='rgb(150,150,150)',
                   coloring=None, fontcolor='blue',
                   fontsize=12):
    """
    Contour trace in Cartesian coordinates.

    Parameters
    ==========

    x, y : array-like
        Cartesian coordinates
    z : array-like
        Field to be represented as contours.
    tooltip : list of str
        Annotations to show on hover.
    ncontours : int or None
        Number of contours to display (determined automatically if None).
    colorscale : str o array, optional
        Colorscale to use for contours
    showscale : bool
        If True, a colorbar showing the color scale is displayed.
    linewidth : int
        Line width of contours
    linecolor : color string
        Color on contours
    coloring : None or 'lines'
        How to display contour. Filled contours if None, lines if ``lines``.
    colorscale : None or array-like
        Colorscale of the contours.
    fontcolor : color str
        Color of contour labels.
    fontsize : int
        Font size of contour labels.
    """

    c_dict = dict(type='contour',
                  x=x, y=y, z=z,
                  text=tooltip,
                  hoverinfo='text',
                  ncontours=ncontours,
                  colorscale=colorscale,
                  showscale=showscale,
                  line=dict(width=linewidth, color=linecolor),
                  colorbar=dict(thickness=20, ticklen=4)
                  )
    if coloring == 'lines':
        contours = dict(coloring=coloring)
        c_dict.update(contours=contours)
    return go.Contour(c_dict)


def barycentric_ticks(side):
    """
    Barycentric coordinates of ticks locations.

    Parameters
    ==========
    side : 0, 1 or  2
        side j has 0 in the  j^th position of barycentric coords of tick
        origin.
    """
    p = 10
    if side == 0:  # where a=0
        return np.array([(0, j/p, 1-j/p) for j in range(p - 2, 0, -2)])
    elif side == 1:  # b=0
        return np.array([(i/p, 0, 1-i/p) for i in range(2, p, 2)])
    elif side == 2:  # c=0
        return (np.array([(i/p, j/p, 0)
                          for i in range(p - 2, 0, -2)
                          for j in range(p - i, -1, -1) if i + j == p]))
    else:
        raise ValueError('The side can be only 0, 1, 2')


def _side_coord_ticks(side, t=0.01):
    """
    Cartesian coordinates of ticks loactions for one side (0, 1, 2) 
    of ternary diagram.

    Parameters
    ==========

    side : int, 0, 1 or 2
        Index of side
    t : float, default 0.01
        Length of tick

    Returns
    =======
    xt, yt : lists
        Lists of x, resp y-coords of tick segments
    posx, posy : lists
        Lists of ticklabel positions
    """
    M, invM = _transform_barycentric_cartesian()
    baryc = barycentric_ticks(side)
    xy1 = np.dot(M, baryc.T)
    xs, ys = xy1[:2]
    x_ticks, y_ticks, posx, posy = [], [], [], []
    if side == 0:
        for i in range(4):
            x_ticks.extend([xs[i], xs[i]+t, None])
            y_ticks.extend([ys[i], ys[i]-np.sqrt(3)*t, None])
        posx.extend([xs[i]+t for i in range(4)])
        posy.extend([ys[i]-np.sqrt(3)*t for i in range(4)])
    elif side == 1:
        for i in range(4):
            x_ticks.extend([xs[i], xs[i]+t, None])
            y_ticks.extend([ys[i], ys[i]+np.sqrt(3)*t, None])
        posx.extend([xs[i]+t for i in range(4)])
        posy.extend([ys[i]+np.sqrt(3)*t for i in range(4)])
    elif side == 2:
        for i in range(4):
            x_ticks.extend([xs[i], xs[i]-2*t, None])
            y_ticks.extend([ys[i], ys[i], None])
        posx.extend([xs[i]-2*t for i in range(4)])
        posy.extend([ys[i] for i in range(4)])
    else:
        raise ValueError('Side can be only 0, 1, 2')
    return x_ticks, y_ticks, posx, posy


def _cart_coord_ticks(t=0.01):
    """
    Cartesian coordinates of ticks loactions.

    Parameters
    ==========

    t : float, default 0.01
        Length of tick

    Returns
    =======
    xt, yt : lists
        Lists of x, resp y-coords of tick segments (all sides concatenated).
    posx, posy : lists
        Lists of ticklabel positions (all sides concatenated).
    """
    x_ticks, y_ticks, posx, posy = [], [], [], []
    for side in range(3):
        xt, yt, px, py = _side_coord_ticks(side, t)
        x_ticks.extend(xt)
        y_ticks.extend(yt)
        posx.extend(px)
        posy.extend(py)
    return x_ticks, y_ticks, posx, posy


def _set_ticklabels(annotations, posx, posy, proportions=True):
    """

    Parameters
    ==========

    annotations : list
        List of annotations previously defined in layout definition
        as a dict, not as an instance of go.Layout.
    posx, posy:  lists
        Lists containing ticklabel position coordinates
    proportions : bool
        True when ticklabels are 0.2, 0.4, ... False when they are
        20%, 40%...
    """
    if not isinstance(annotations, list):
        raise ValueError('annotations should be a list')

    ticklabel = [0.8, 0.6, 0.4, 0.2] if proportions \
                                     else ['80%', '60%', '40%', '20%']

    # Annotations for ticklabels on side 0
    annotations.extend([dict(showarrow=False,
                             text=str(ticklabel[j]),
                             x=posx[j],
                             y=posy[j],
                             align='center',
                             xanchor='center',
                             yanchor='top',
                             font=dict(size=12)) for j in range(4)])

    # Annotations for ticklabels on side 1
    annotations.extend([dict(showarrow=False,
                             text=str(ticklabel[j]),
                             x=posx[j+4],
                             y=posy[j+4],
                             align='center',
                             xanchor='left',
                             yanchor='middle',
                             font=dict(size=12)) for j in range(4)])

    # Annotations for ticklabels on side 2
    annotations.extend([dict(showarrow=False,
                             text=str(ticklabel[j]),
                             x=posx[j+8],
                             y=posy[j+8],
                             align='center',
                             xanchor='right',
                             yanchor='middle',
                             font=dict(size=12)) for j in range(4)])
    return annotations


def _styling_traces_ternary(x_ticks, y_ticks):
    """
    Traces for outer triangle of ternary plot, and corresponding ticks.

    Parameters
    ==========

    x_ticks : array_like, 1D
        x Cartesian coordinate of ticks
    y_ticks : array_like, 1D
        y Cartesian coordinate of ticks
    """
    side_trace = dict(type='scatter',
                      x=[0.5, 0, 1, 0.5],
                      y=[np.sqrt(3)/2, 0, 0, np.sqrt(3)/2],
                      mode='lines',
                      line=dict(width=2, color='#444444'),
                      hoverinfo='none')

    tick_trace = dict(type='scatter',
                      x=x_ticks,
                      y=y_ticks,
                      mode='lines',
                      line=dict(width=1, color='#444444'),
                      hoverinfo='none')

    return side_trace, tick_trace


def _ternary_layout(title='Ternary contour plot', width=550, height=525,
                    fontfamily='Balto, sans-serif', colorbar_fontsize=14,
                    plot_bgcolor='rgb(240,240,240)',
                    pole_labels=['a', 'b', 'c'], label_fontsize=16):
    """
    Layout of ternary contour plot, to be passed to ``go.FigureWidget``
    object.

    Parameters
    ==========
    title : str or None
        Title of ternary plot
    width : int
        Figure width.
    height : int
        Figure height.
    fontfamily : str
        Family of fonts
    colorbar_fontsize : int
        Font size of colorbar.
    plot_bgcolor :
        color of figure background
    pole_labels : str, default ['a', 'b', 'c']
        Names of the three poles of the triangle.
    label_fontsize : int
        Font size of pole labels.
    """
    return dict(title=title,
                font=dict(family=fontfamily, size=colorbar_fontsize),
                width=width, height=height,
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                plot_bgcolor=plot_bgcolor,
                showlegend=False,
                # annotations for strings placed at the triangle vertices
                annotations=[dict(showarrow=False,
                                  text=pole_labels[0],
                                  x=0.5,
                                  y=np.sqrt(3)/2,
                                  align='center',
                                  xanchor='center',
                                  yanchor='bottom',
                                  font=dict(size=label_fontsize)),
                             dict(showarrow=False,
                                  text=pole_labels[1],
                                  x=0,
                                  y=0,
                                  align='left',
                                  xanchor='right',
                                  yanchor='top',
                                  font=dict(size=label_fontsize)),
                             dict(showarrow=False,
                                  text=pole_labels[2],
                                  x=1,
                                  y=0,
                                  align='right',
                                  xanchor='left',
                                  yanchor='top',
                                  font=dict(size=label_fontsize))
                             ])


def _tooltip(N, bar_coords, grid_z, xy1, mode='proportions'):
    """
    Tooltip annotations to be displayed on hover.

    Parameters
    ==========

    N : int
        Number of annotations along each axis.
    bar_coords : array-like
        Barycentric coordinates.
    grid_z : array
        Values (e.g. elevation values) at barycentric coordinates.
    xy1 : array-like
        Cartesian coordinates.
    mode : str, 'proportions' or 'percents'
        Coordinates inside the ternary plot can be displayed either as
        proportions (adding up to 1) or as percents (adding up to 100).
    """
    if mode == 'proportions' or mode == 'proportion':
        tooltip = [
        ['a: %.2f' % round(bar_coords[0][i, j], 2) +
         '<br>b: %.2f' % round(bar_coords[1][i, j], 2) +
         '<br>c: %.2f' % (round(1-round(bar_coords[0][i, j], 2) -
                          round(bar_coords[1][i, j], 2), 2)) +
         '<br>z: %.2f' % round(grid_z[i, j], 2)
        if ~np.isnan(xy1[0][i, j]) else '' for j in range(N)]
                                           for i in range(N)]
    elif mode == 'percents' or mode == 'percent':
        tooltip = [
        ['a: %d' % int(100*bar_coords[0][i, j] + 0.5) +
         '<br>b: %d' % int(100*bar_coords[1][i, j] + 0.5) +
         '<br>c: %d' % (100-int(100*bar_coords[0][i, j] + 0.5) -
                        int(100*bar_coords[1][i, j] + 0.5)) +
         '<br>z: %.2f' % round(grid_z[i, j], 2)
         if ~np.isnan(xy1[0][i, j]) else '' for j in range(N)]
                                            for i in range(N)]
    else:
        raise ValueError("""tooltip mode must be either "proportions" or
                          "percents".""")
    return tooltip


def _prepare_barycentric_coord(b_coords):
    """
    Check ternary coordinates and return the right barycentric coordinates.
    """
    if not isinstance(b_coords, (list, np.ndarray)):
        raise ValueError('Data  should be either an array of shape (n,m), or a list of n m-lists, m=2 or 3')
    b_coords = np.asarray(b_coords)
    if b_coords.shape[0] not in (2, 3):
        raise ValueError('A point should have  2 (a, b) or 3 (a, b, c)  barycentric coordinates')
    if ((len(b_coords) == 3) and
         not np.allclose(b_coords.sum(axis=0), 1, rtol=0.01)):
        msg = "The sum of coordinates should be one for all data points"
        raise ValueError(msg)
    A, B = b_coords[:2]
    C = 1 - (A + B)
    if np.any(np.stack((A, B, C)) < 0):
        raise ValueError('Barycentric coordinates should be positive.')
    return A, B, C


def _compute_grid(coordinates, values, tooltip_mode):
    """
    Compute interpolation of data points on regular grid in Cartesian
    coordinates.

    Parameters
    ==========

    coordinates : array-like
        Barycentric coordinates of data points.
    values : 1-d array-like
        Data points, field to be represented as contours.
    tooltip_mode : str, 'proportions' or 'percents'
        Coordinates inside the ternary plot can be displayed either as
        proportions (adding up to 1) or as percents (adding up to 100).
    """
    A, B, C = _prepare_barycentric_coord(coordinates)
    M, invM = _transform_barycentric_cartesian()
    cartes_coord_points = np.einsum('ik, kj -> ij', M, np.stack((A, B, C)))
    xx, yy = cartes_coord_points[:2]
    x_min, x_max = xx.min(), xx.max()
    y_min, y_max = yy.min(), yy.max()
    # n_interp = max(100, int(np.sqrt(len(values))))
    n_interp = 20
    gr_x = np.linspace(x_min, x_max, n_interp)
    gr_y = np.linspace(y_min, y_max, n_interp)
    grid_x, grid_y = np.meshgrid(gr_x, gr_y)
    grid_z = interpolate.griddata(
        cartes_coord_points[:2].T, values, (grid_x, grid_y), method='cubic')
    bar_coords = np.einsum('ik, kmn -> imn', invM,
                           np.stack((grid_x, grid_y, np.ones(grid_x.shape))))
    # invalidate the points outside of the reference triangle
    bar_coords[np.where(bar_coords < 0)] = 0  # None
    # recompute back cartesian coordinates with invalid positions
    xy1 = np.einsum('ik, kmn -> imn', M, bar_coords)
    is_nan = np.where(np.isnan(xy1[0]))
    grid_z[is_nan] = 0  # None
    tooltip = _tooltip(n_interp, bar_coords, grid_z, xy1, tooltip_mode)
    return grid_z, gr_x, gr_y, tooltip


def create_ternary_contour(coordinates, values, pole_labels=['a', 'b', 'c'],
                           tooltip_mode='proportions', width=500, height=500,
                           ncontours=None,
                           showscale=False,
                           coloring=None,
                           colorscale=None,
                           plot_bgcolor='rgb(240,240,240)',
                           title=None):
    """
    Ternary contour plot.

    Parameters
    ----------

    coordinates : list or ndarray
        Barycentric coordinates of shape (2, N) or (3, N) where N is the
        number of data points. The sum of the 3 coordinates is expected
        to be 1 for all data points.
    values : array-like
        Data points of field to be represented as contours.
    pole_labels : str, default ['a', 'b', 'c']
        Names of the three poles of the triangle.
    tooltip_mode : str, 'proportions' or 'percents'
        Coordinates inside the ternary plot can be displayed either as
        proportions (adding up to 1) or as percents (adding up to 100).
    width : int
        Figure width.
    height : int
        Figure height.
    ncontours : int or None
        Number of contours to display (determined automatically if None).
    showscale : bool, default False
        If True, a colorbar showing the color scale is displayed.
    coloring : None or 'lines'
        How to display contour. Filled contours if None, lines if ``lines``.
    colorscale : None or array-like
        colorscale of the contours.
    plot_bgcolor :
        color of figure background
    title : str or None
        Title of ternary plot

    Examples
    ========

    Example 1: ternary contour plot with filled contours

    # Define coordinates
    a, b = np.mgrid[0:1:20j, 0:1:20j]
    mask = a + b <= 1
    a = a[mask].ravel()
    b = b[mask].ravel()
    c = 1 - a - b
    # Values to be displayed as contours
    z = a * b * c
    fig = ff.create_ternary_contour(np.stack((a, b, c)), z)

    It is also possible to give only two barycentric coordinates for each
    point, since the sum of the three coordinates is one:

    fig = ff.create_ternary_contour(np.stack((a, b)), z)

    Example 2: ternary contour plot with line contours

    fig = ff.create_ternary_contour(np.stack((a, b)), z, coloring='lines')
    """
    if interpolate is None:
        raise ImportError("""\
The create_ternary_contour figure factory requires the scipy package""")

    grid_z, gr_x, gr_y, tooltip = _compute_grid(coordinates, values,
                                                tooltip_mode)

    x_ticks, y_ticks, posx, posy = _cart_coord_ticks(t=0.01)

    layout = _ternary_layout(pole_labels=pole_labels,
                             width=width, height=height, title=title,
                             plot_bgcolor=plot_bgcolor)

    annotations = _set_ticklabels(layout['annotations'], posx, posy,
                                  proportions=True)
    if colorscale is None:
        colorscale = _pl_deep()

    contour_trace = _contour_trace(gr_x, gr_y, grid_z, tooltip,
                                   ncontours=ncontours,
                                   showscale=showscale,
                                   colorscale=colorscale,
                                   coloring=coloring)
    side_trace, tick_trace = _styling_traces_ternary(x_ticks, y_ticks)
    fig = go.Figure(data=[contour_trace,  tick_trace, side_trace],
                    layout=layout)
    fig.layout.annotations = annotations
    return fig
