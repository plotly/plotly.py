from __future__ import absolute_import
import warnings
import plotly.colors as clrs
from plotly.graph_objs import graph_objs as go
from plotly import exceptions, optional_imports

np = optional_imports.get_module('numpy')
sk = optional_imports.get_module('skimage')
scipy_interp = optional_imports.get_module('scipy.interpolate')


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


def replace_zero_coords(ternary_data, delta=0.001):
    """Replaces zero ternary coordinates with delta
    and normalize the new triplets (a, b, c); implements a method
    by J. A. Martin-Fernandez,  C. Barcelo-Vidal, V. Pawlowsky-Glahn,
    Dealing with zeros and missing values in compositional data sets
    using nonparametric imputation,
    Mathematical Geology  35 (2003), pp 253-278
    """
    # ternary_data: array (n, 3)
    # delta:  small float (close to zero)
    #Returns a new data set of normalized ternary coords

    ternary_data = central_proj(ternary_data)
    bool_array = (ternary_data == 0)

    n_comp = ternary_data.shape[-1]
    info_row_zero = bool_array.sum(axis=-1, keepdims=True)

    if delta is None:
        delta = 0.001
    unity_complement = 1 -  delta * info_row_zero
    if np.any(unity_complement) < 0:
        raise ValueError('Your  delta led to negative ternary coords.Set a smaller delta')
    ternary_data = np.where(bool_array, delta, unity_complement * ternary_data)
    return ternary_data.squeeze()


def dir_ilr(barycentric):  #ilr: S^2 ---> R^2 identified to x_1+x2+x3=0 in R^3
    barycentric = np.asarray(barycentric)
    if barycentric.shape[-1] != 3:
        raise ValueError(f'barycentric coordinates are 3 floats, not {barycentric.shape[-1]}')
    if len(barycentric.shape) == 1:
        barycentric = barycentric.reshape(1,3)
    x0 = np.log(barycentric[:,0]/barycentric[:,1]) / np.sqrt(2)
    x1 = np.log(barycentric[:,0]*barycentric[:,1]/barycentric[:, 2]**2) / np.sqrt(6)
    ilr_tdata = np.stack((x0,x1)).T
    return ilr_tdata if  barycentric.shape[0] > 1 else ilr_tdata.squeeze()


def ilr_inverse (x): #ilr: R^2 -->S^2 (2 simplex)
    #x an n  list of 2-lists or an array of shape (n,2),
    # implementation of a method presented in:
    # An algebraic method to compute isometric logratio transformation and back transformation of compositional data
    # Jarauta-Bragulat, E.; Buenestado, P.; Hervada-Sala, C.
    # in Proc of the Annual Conf of the Intl Assoc for Math Geology, 2003, pp 31-30
    #x should ne an array of shape (n,2)
    x = np.array(x)
    if x.shape[-1] != 2:
        raise ValueError(f'your data must be 2d points, not {x.shape[-1]}-points')
    if len(x.shape) == 1:
        x = x.reshape(1, 2)
    matrix = np.array([[ 0.5,  1 ,  1. ],
                       [-0.5,  1 ,  1. ],
                       [ 0. ,  0. ,  1. ]])
    s = np.sqrt(2)/2
    t = np.sqrt(3/2)
    Sk = np.einsum('ik, kj -> ij', np.array([[s, t],[-s, t]]), x.T)
    Z = -np.log(1+np.exp(Sk).sum(axis=0))
    log_barycentric = np.einsum('ik, kj -> ij', matrix, np.stack((2*s*x[:, 0], t*x[:, 1], Z)))
    iilr_tdata = np.exp(log_barycentric).T
    return iilr_tdata if x.shape[0] > 1 else iilr_tdata.squeeze()


def _transform_barycentric_cartesian():
    """
    Returns the transformation matrix from barycentric to cartesian
    coordinates and conversely.
    """
    # reference triangle
    tri_verts = np.array([[0.5, np.sqrt(3) / 2], [0, 0], [1, 0]])
    M = np.array([tri_verts[:, 0], tri_verts[:, 1], np.ones(3)])
    return M, np.linalg.inv(M)


def _colors(ncontours, colormap=None):
    if isinstance(colormap, str):
        if colormap in clrs.PLOTLY_SCALES.keys():
            cmap = clrs.PLOTLY_SCALES[colormap]
        else:
            raise exceptions.PlotlyError(
                "If 'colormap' is a string, it must be the name "
                "of a Plotly Colorscale. The available colorscale "
                "names are {}".format(clrs.PLOTLY_SCALES.keys()))
    elif isinstance(colormap, dict):
        cmap = colormap
        clrs.validate_colors_dict(cmap, 'rgb')
    else:
        raise ValueError("""Colormap has to be a dictionary or a valid
                         Plotly colormap string""")
    values = np.linspace(0, 1, ncontours)
    keys = np.array([pair[0] for pair in cmap])
    cols = np.array([pair[1] for pair in cmap])
    inds = np.searchsorted(keys, values)
    colors = [cols[0]]
    for ind, val in zip(inds[1:], values[1:]):
        key1, key2 = keys[ind - 1], keys[ind]
        interm = (val - key1) / (key2 - key1)
        col = clrs.find_intermediate_color(cols[ind - 1],
                                           cols[ind], interm, colortype='rgb')
        colors.append(col)
    return colors


def _contour_trace(x, y, z, ncontours=None, 
                   colorscale='Electric',
                   linecolor='rgb(150,150,150)', interp_mode='cartesian'):
    """
    Contour trace in Cartesian coordinates.

    Parameters
    ==========

    x, y : array-like
        Cartesian coordinates
    z : array-like
        Field to be represented as contours.
    """
    if ncontours is None:
        ncontours = 5
    colors = _colors(ncontours, colorscale)
    traces = []
    mask_nan = np.isnan(z)
    mask_ok = np.logical_not(mask_nan)
    values = np.linspace(z[mask_ok].min(), z[mask_ok].max(), 
                            ncontours + 2)[1:-1]
    M, invM = _transform_barycentric_cartesian()
    dx = (x.max() - x.min())/x.size
    dy = (y.max() - y.min())/y.size
    zz = np.copy(z)
    zz[np.isnan(z)] = (z[mask_ok].min()
            - 10. * (z[mask_ok].max() - z[mask_ok].min()))
    for i, val in enumerate(values):
        contour_level = sk.measure.find_contours(zz, val)
        # stop
        for contour in contour_level:
            yy, xx = contour.T
            if interp_mode == 'cartesian':
                bar_coords = np.dot(invM,
                        np.stack((dx * xx, dy * yy, np.ones(xx.shape))))
            elif interp_mode == 'ilr':
                bar_coords = ilr_inverse(np.stack((dx * xx + x.min(),
                                                   dy * yy + y.min())).T).T
            a = bar_coords[0]
            b = bar_coords[1]
            c = bar_coords[2]
            trace = dict(
                type='scatterternary', text=val,
                a=a, b=b, c=c, mode='lines',
                line=dict(color=colors[i], shape='spline'),
                fill='toself',
                showlegend=True,
                name=str(val),
                # fillcolor = colors_iterator.next()
            )
            traces.append(trace)
    return traces



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
                ternary=dict(sum=1,
                             aaxis=dict(title=pole_labels[0],
                                        min=0.01, linewidth=2,
                                        ticks='outside'),
                             baxis=dict(title=pole_labels[1],
                                        min=0.01, linewidth=2,
                                        ticks='outside'),
                             caxis=dict(title=pole_labels[2],
                                        min=0.01, linewidth=2,
                                        ticks='outside')),
                showlegend=True
                )

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


def central_proj(mdata):

    #array of shape(n,3) or a n-list of 3-lists of positive numbers,
    #returns for each row [a, b, c]--> np.array([a,b,c])/(a+b+c)

    mdata=np.asarray(mdata)
    if mdata.ndim > 2:
        raise ValueError("this function requires 2d arrays")
    if mdata.shape[-1] != 3:
        raise ValueError('data must have 3 coordinates')

    if mdata.ndim == 1:
         mdata = np.atleast_2d(mdata)

    if np.any(mdata < 0):
        raise ValueError("Data should be positive")

    if np.all(mdata == 0, axis=1).sum() > 0:
        raise ValueError("this projection can be applied only to non zero triplets")
    barycentric = mdata / mdata.sum(axis=1, keepdims=True)
    return barycentric.squeeze()



def _compute_grid(coordinates, values, tooltip_mode, interp_mode='cartesian'):
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
    if interp_mode == 'cartesian':
        M, invM = _transform_barycentric_cartesian()
        coord_points = np.einsum('ik, kj -> ij', M, np.stack((A, B, C)))
    elif interp_mode == 'ilr':
        mdata = replace_zero_coords(np.stack((A, B, C)).T)
        coord_points = dir_ilr(mdata).T
    else:
        raise ValueError("interp_mode should be cartesian or ilr")
    xx, yy = coord_points[:2]
    x_min, x_max = xx.min(), xx.max()
    y_min, y_max = yy.min(), yy.max()
    n_interp = max(400, int(np.sqrt(len(values))))
    gr_x = np.linspace(x_min, x_max, n_interp)
    gr_y = np.linspace(y_min, y_max, n_interp)
    grid_x, grid_y = np.meshgrid(gr_x, gr_y)
    grid_z = scipy_interp.griddata(coord_points[:2].T, values, (grid_x, grid_y),
                    method='cubic')
    return grid_z, gr_x, gr_y


def create_ternarycontour(coordinates, values, pole_labels=['a', 'b', 'c'],
                          tooltip_mode='proportions', width=500, height=500,
                          ncontours=None,
                          showscale=False, coloring=None,
                          showlabels=False, colorscale=None,
                          reversescale=False,
                          plot_bgcolor='rgb(240,240,240)',
                          title=None,
                          smoothing=False,
                          interp_mode='cartesian'):
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
    showlabels : bool, default False
        For line contours (coloring='lines'), the value of the contour is
        displayed if showlabels is True.
    colorscale : None or array-like
        colorscale of the contours.
    reversescale : bool
        Reverses the color mapping if true. If true, `zmin`
        will correspond to the last color in the array and
        `zmax` will correspond to the first color.
    plot_bgcolor :
        color of figure background
    title : str or None
        Title of ternary plot
    smoothing : bool
        If True, contours are smoothed.

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
    fig = ff.create_ternarycontour(np.stack((a, b, c)), z)

    It is also possible to give only two barycentric coordinates for each
    point, since the sum of the three coordinates is one:

    fig = ff.create_ternarycontour(np.stack((a, b)), z)

    Example 2: ternary contour plot with line contours

    fig = ff.create_ternarycontour(np.stack((a, b)), z, coloring='lines')

    Labels of contour plots can be displayed on the contours:

    fig = ff.create_ternarycontour(np.stack((a, b)), z, coloring='lines',
                                   showlabels=True)

    """
    grid_z, gr_x, gr_y = _compute_grid(coordinates, values,
                                                tooltip_mode, 
                                                interp_mode=interp_mode)

    #x_ticks, y_ticks, posx, posy = _cart_coord_ticks(t=0.01)

    layout = _ternary_layout(pole_labels=pole_labels,
                             width=width, height=height, title=title,
                             plot_bgcolor=plot_bgcolor)
    #annotations = _set_ticklabels(layout['annotations'], posx, posy,
    #                              proportions=True)
    if colorscale is None:
        colorscale = _pl_deep()

    contour_trace = _contour_trace(gr_x, gr_y, grid_z,
                                   ncontours=ncontours,
                                   colorscale=colorscale,
                                   interp_mode=interp_mode)
    fig = go.Figure(data=contour_trace, layout=layout)
    return fig
