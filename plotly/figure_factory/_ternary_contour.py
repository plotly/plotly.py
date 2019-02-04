from __future__ import absolute_import
import plotly.colors as clrs
from plotly.graph_objs import graph_objs as go
from plotly import exceptions, optional_imports
from plotly import optional_imports
from plotly.graph_objs import graph_objs as go

interpolate = optional_imports.get_module('scipy.interpolate')

np = optional_imports.get_module('numpy')
sk_measure = optional_imports.get_module('skimage.measure')
scipy_interp = optional_imports.get_module('scipy.interpolate')


# ----------- Layout and tooltip ------------------------------


def _ternary_layout(title='Ternary contour plot', width=550, height=525,
                    fontfamily='Balto, sans-serif',
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
    plot_bgcolor :
        color of figure background
    pole_labels : str, default ['a', 'b', 'c']
        Names of the three poles of the triangle.
    label_fontsize : int
        Font size of pole labels.
    """
    return dict(title=title,
                width=width, height=height,
                font=dict(family=fontfamily),
                plot_bgcolor=plot_bgcolor,
                ternary=dict(sum=1,
                             aaxis=dict(title=dict(text=pole_labels[0],
                                            font=dict(size=label_fontsize)),
                                        min=0.01, linewidth=2,
                                        ticks='outside'),
                             baxis=dict(title=dict(text=pole_labels[1],
                                            font=dict(size=label_fontsize)),
                                        min=0.01, linewidth=2,
                                        ticks='outside'),
                             caxis=dict(title=dict(text=pole_labels[2],
                                            font=dict(size=label_fontsize)),
                                        min=0.01, linewidth=2,
                                        ticks='outside')),
                showlegend=False,
               )


def _tooltip(a, b, c, z, mode='proportions'):
    """
    Tooltip annotations to be displayed on hover.

    Parameters
    ==========

    a, b, c : 1-D array-like 
        Barycentric coordinates.
    z : 1-D array
        Values (e.g. elevation values) at barycentric coordinates.
    mode : str, 'proportions' or 'percents'
        Coordinates inside the ternary plot can be displayed either as
        proportions (adding up to 1) or as percents (adding up to 100).
    """
    N = len(a)
    if np.isscalar(z):
        z = z * np.ones(N)
    if mode == 'proportions' or mode == 'proportion':
        tooltip = ['a: %.2f' % round(a[i], 2) +
                   '<br>b: %.2f' % round(b[i], 2) +
                   '<br>c: %.2f' % round(c[i], 2) +
                   '<br>z: %.2f' % round(z[i], 2) for i in range(N)]
    elif mode == 'percents' or mode == 'percent':
        tooltip = ['a: %d' % int(100 * a[i] + 0.5) +
                   '<br>b: %d' % int(100 * b[i] + 0.5) +
                   '<br>c: %d' % int(100 * c[i] + 0.5) +
                   '<br>z: %.2f' % round(z[i], 2) for i in range(N)]
    else:
        raise ValueError("""tooltip mode must be either "proportions" or
                          "percents".""")
    return tooltip

# ------------- Transformations of coordinates -------------------


def _replace_zero_coords(ternary_data, delta=0.0005):
    """
    Replaces zero ternary coordinates with delta and normalize the new
    triplets (a, b, c).

    Parameters
    ----------

    ternary_data : ndarray of shape (N, 3)

    delta : float
        Small float to regularize logarithm.

    Notes
    -----
    Implements a method
    by J. A. Martin-Fernandez,  C. Barcelo-Vidal, V. Pawlowsky-Glahn,
    Dealing with zeros and missing values in compositional data sets
    using nonparametric imputation, Mathematical Geology 35 (2003),
    pp 253-278.
    """
    zero_mask = (ternary_data == 0)
    is_any_coord_zero = np.any(zero_mask, axis=0)

    unity_complement = 1 - delta * is_any_coord_zero
    if np.any(unity_complement) < 0:
        raise ValueError('The provided value of delta led to negative'
                         'ternary coords.Set a smaller delta')
    ternary_data = np.where(zero_mask, delta, unity_complement * ternary_data)
    return ternary_data


def _ilr_transform(barycentric):
    """
    Perform Isometric Log-Ratio on barycentric (compositional) data.

    Parameters
    ----------
    barycentric: ndarray of shape (3, N)
        Barycentric coordinates.

    References
    ----------
    "An algebraic method to compute isometric logratio transformation and
    back transformation of compositional data", Jarauta-Bragulat, E.,
    Buenestado, P.; Hervada-Sala, C., in Proc. of the Annual Conf. of the
    Intl Assoc for Math Geology, 2003, pp 31-30.
    """
    barycentric = np.asarray(barycentric)
    x_0 = np.log(barycentric[0] / barycentric[1]) / np.sqrt(2)
    x_1 = 1. / np.sqrt(6) * np.log(barycentric[0] * barycentric[1] /
                                   barycentric[2] ** 2)
    ilr_tdata = np.stack((x_0, x_1))
    return ilr_tdata


def _ilr_inverse(x):
    """
    Perform inverse Isometric Log-Ratio (ILR) transform to retrieve
    barycentric (compositional) data.

    Parameters
    ----------
    x : array of shape (2, N)
        Coordinates in ILR space.

    References
    ----------
    "An algebraic method to compute isometric logratio transformation and
    back transformation of compositional data", Jarauta-Bragulat, E.,
    Buenestado, P.; Hervada-Sala, C., in Proc. of the Annual Conf. of the
    Intl Assoc for Math Geology, 2003, pp 31-30.
    """
    x = np.array(x)
    matrix = np.array([[0.5,  1,  1.],
                       [-0.5,  1,  1.],
                       [0., 0.,  1.]])
    s = np.sqrt(2)/2
    t = np.sqrt(3/2)
    Sk = np.einsum('ik, kj -> ij', np.array([[s, t], [-s, t]]), x)
    Z = -np.log(1 + np.exp(Sk).sum(axis=0))
    log_barycentric = np.einsum('ik, kj -> ij',
                                matrix,
                                np.stack((2*s*x[0], t*x[1], Z)))
    iilr_tdata = np.exp(log_barycentric)
    return iilr_tdata


def _transform_barycentric_cartesian():
    """
    Returns the transformation matrix from barycentric to Cartesian
    coordinates and conversely.
    """
    # reference triangle
    tri_verts = np.array([[0.5, np.sqrt(3) / 2], [0, 0], [1, 0]])
    M = np.array([tri_verts[:, 0], tri_verts[:, 1], np.ones(3)])
    return M, np.linalg.inv(M)


def _prepare_barycentric_coord(b_coords):
    """
    Check ternary coordinates and return the right barycentric coordinates.
    """
    if not isinstance(b_coords, (list, np.ndarray)):
        raise ValueError('Data  should be either an array of shape (n,m),'
                         'or a list of n m-lists, m=2 or 3')
    b_coords = np.asarray(b_coords)
    if b_coords.shape[0] not in (2, 3):
        raise ValueError('A point should have  2 (a, b) or 3 (a, b, c)'
                         'barycentric coordinates')
    if ((len(b_coords) == 3) and
         not np.allclose(b_coords.sum(axis=0), 1, rtol=0.01) and
         not np.allclose(b_coords.sum(axis=0), 100, rtol=0.01)):
        msg = "The sum of coordinates should be 1 or 100 for all data points"
        raise ValueError(msg)

    if len(b_coords) == 2:
        A, B = b_coords
        C = 1 - (A + B)
    else:
        A, B, C = b_coords / b_coords.sum(axis=0)
    if np.any(np.stack((A, B, C)) < 0):
        raise ValueError('Barycentric coordinates should be positive.')
    return np.stack((A, B, C))


def _compute_grid(coordinates, values, interp_mode='ilr'):
    """
    Transform data points with Cartesian or ILR mapping, then Compute
    interpolation on a regular grid.

    Parameters
    ==========

    coordinates : array-like
        Barycentric coordinates of data points.
    values : 1-d array-like
        Data points, field to be represented as contours.
    interp_mode : 'ilr' (default) or 'cartesian'
        Defines how data are interpolated to compute contours.
    """
    if interp_mode == 'cartesian':
        M, invM = _transform_barycentric_cartesian()
        coord_points = np.einsum('ik, kj -> ij', M, coordinates)
    elif interp_mode == 'ilr':
        coordinates = _replace_zero_coords(coordinates)
        coord_points = _ilr_transform(coordinates)
    else:
        raise ValueError("interp_mode should be cartesian or ilr")
    xx, yy = coord_points[:2]
    x_min, x_max = xx.min(), xx.max()
    y_min, y_max = yy.min(), yy.max()
    n_interp = max(200, int(np.sqrt(len(values))))
    gr_x = np.linspace(x_min, x_max, n_interp)
    gr_y = np.linspace(y_min, y_max, n_interp)
    grid_x, grid_y = np.meshgrid(gr_x, gr_y)
    # We use cubic interpolation, except outside of the convex hull
    # of data points where we use nearest neighbor values.
    grid_z = scipy_interp.griddata(coord_points[:2].T, values,
                                   (grid_x, grid_y),
                                   method='cubic')
    grid_z_other = scipy_interp.griddata(coord_points[:2].T, values,
                                         (grid_x, grid_y),
                                         method='nearest')
    mask_nan = np.isnan(grid_z)
    grid_z[mask_nan] = grid_z_other[mask_nan]
    return grid_z, gr_x, gr_y

# ----------------------- Contour traces ----------------------


def _colors(ncontours, colormap=None):
    """
    Return a list of ``ncontours`` colors from the ``colormap`` colorscale.
    """
    if colormap in clrs.PLOTLY_SCALES.keys():
        cmap = clrs.PLOTLY_SCALES[colormap]
    else:
        raise exceptions.PlotlyError(
            "Colorscale must be a valid Plotly Colorscale."
            "The available colorscale names are {}".format(
                                clrs.PLOTLY_SCALES.keys()))
    values = np.linspace(0, 1, ncontours)
    vals_cmap = np.array([pair[0] for pair in cmap])
    cols = np.array([pair[1] for pair in cmap])
    inds = np.searchsorted(vals_cmap, values)
    if '#'in cols[0]:  # for Viridis
        cols = [clrs.label_rgb(clrs.hex_to_rgb(col)) for col in cols]

    colors = [cols[0]]
    for ind, val in zip(inds[1:], values[1:]):
        val1, val2 = vals_cmap[ind - 1], vals_cmap[ind]
        interm = (val - val1) / (val2 - val1)
        col = clrs.find_intermediate_color(cols[ind - 1],
                                           cols[ind], interm,
                                           colortype='rgb')
        colors.append(col)
    return colors


def _is_invalid_contour(x, y):
    return (np.all(np.abs(x - x[0]) < 2) and np.all(np.abs(y - y[0]) < 2))


def _contour_trace(x, y, z, ncontours=None,
                   colorscale='Electric',
                   linecolor='rgb(150,150,150)', interp_mode='llr',
                   coloring=None, tooltip_mode='proportions'):
    """
    Contour trace in Cartesian coordinates.

    Parameters
    ==========

    x, y : array-like
        Cartesian coordinates
    z : array-like
        Field to be represented as contours.
    ncontours : int or None
        Number of contours to display (determined automatically if None).
    colorscale : None or str (Plotly colormap)
        colorscale of the contours.
    linecolor : rgb color
        Color used for lines. If ``colorscale`` is not None, line colors are
        determined from ``colorscale`` instead.
    interp_mode : 'ilr' (default) or 'cartesian'
        Defines how data are interpolated to compute contours. If 'irl',
        ILR (Isometric Log-Ratio) of compositional data is performed. If
        'cartesian', contours are determined in Cartesian space.
    coloring : None or 'lines'
        How to display contour. Filled contours if None, lines if ``lines``.
    tooltip_mode : str, 'proportions' or 'percents'
        Coordinates inside the ternary plot can be displayed either as
        proportions (adding up to 1) or as percents (adding up to 100).
    """
    if ncontours is None:
        ncontours = 5
    if colorscale is not None:
        colors = _colors(ncontours, colorscale)
    if linecolor is None:
        linecolor = 'rgb(150, 150, 150)'
    else:
        colors = [linecolor] * ncontours
    traces = []
    mask_nan = np.isnan(z)
    mask_ok = np.logical_not(mask_nan)
    values = np.linspace(z[mask_ok].min(), z[mask_ok].max(),
                         ncontours + 2)[1:-1]
    M, invM = _transform_barycentric_cartesian()
    dx = (x.max() - x.min()) / x.size
    dy = (y.max() - y.min()) / y.size
    for i, val in enumerate(values):
        contour_level = sk_measure.find_contours(z, val)
        fill = 'toself'
        for contour in contour_level: # several closed contours for 1 value
            y_contour, x_contour = contour.T
            if _is_invalid_contour(x_contour, y_contour):
                continue
            if interp_mode == 'cartesian':
                bar_coords = np.dot(invM,
                                    np.stack((dx * x_contour,
                                              dy * y_contour,
                                              np.ones(x_contour.shape))))
            elif interp_mode == 'ilr':
                bar_coords = _ilr_inverse(np.stack((dx * x_contour + x.min(),
                                                    dy * y_contour +
                                                    y.min())))
            a, b, c = bar_coords
            tooltip = _tooltip(a, b, c, val, mode=tooltip_mode)

            _col = colors[i] if coloring == 'lines' else linecolor

            trace = dict(
                type='scatterternary', text=tooltip,
                a=a, b=b, c=c, mode='lines',
                line=dict(color=_col, shape='spline', width=1),
                fill=fill,
                fillcolor=colors[i],
                hoverinfo='text',
                showlegend=True,
                name='%.2f' % val
            )
            if coloring == 'lines':
                trace['fill'] = None
            traces.append(trace)
    return traces

# -------------------- Figure Factory for ternary contour -------------


def create_ternary_contour(coordinates, values, pole_labels=['a', 'b', 'c'],
                           tooltip_mode='proportions', width=500, height=500,
                           ncontours=None,
                           showscale=False, coloring=None,
                           colorscale='Bluered',
                           linecolor=None,
                           plot_bgcolor='rgb(240,240,240)',
                           title=None,
                           interp_mode='ilr',
                           showmarkers=False,
                           label_fontsize=16):
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
    colorscale : None or str (Plotly colormap)
        colorscale of the contours.
    linecolor : None or rgb color
        Color used for lines. ``colorscale`` has to be set to None, otherwise
        line colors are determined from ``colorscale``.
    plot_bgcolor :
        color of figure background
    title : str or None
        Title of ternary plot
    interp_mode : 'ilr' (default) or 'cartesian'
        Defines how data are interpolated to compute contours. If 'irl',
        ILR (Isometric Log-Ratio) of compositional data is performed. If
        'cartesian', contours are determined in Cartesian space.
    showmarkers : bool, default False
        If True, markers corresponding to input compositional points are
        superimposed on contours, using the same colorscale.
    label_fontsize : int
        Font size of pole labels.

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
    plotly.iplot(fig)

    Example 2: ternary contour plot with line contours

    fig = ff.create_ternarycontour(np.stack((a, b, c)), z, coloring='lines')

    Example 3: customize number of contours

    fig = ff.create_ternarycontour(np.stack((a, b, c)), z, ncontours=8)

    Example 4: superimpose contour plot and original data as markers

    fig = ff.create_ternarycontour(np.stack((a, b, c)), z, coloring='lines',
                                   showmarkers=True)

    Example 5: customize title and pole labels

    fig = ff.create_ternarycontour(np.stack((a, b, c)), z,
                                   title='Ternary plot',
                                   pole_labels=['clay', 'quartz', 'fledspar'])
    """
    if interpolate is None:
        raise ImportError("""\
    The create_ternary_contour figure factory requires the scipy package""")
    if colorscale is None:
        showscale = False
    coordinates = _prepare_barycentric_coord(coordinates)
    grid_z, gr_x, gr_y = _compute_grid(coordinates, values,
                                       interp_mode=interp_mode)

    layout = _ternary_layout(pole_labels=pole_labels,
                             width=width, height=height, title=title,
                             plot_bgcolor=plot_bgcolor,
                             label_fontsize=label_fontsize)

    contour_trace = _contour_trace(gr_x, gr_y, grid_z,
                                   ncontours=ncontours,
                                   colorscale=colorscale,
                                   linecolor=linecolor,
                                   interp_mode=interp_mode,
                                   coloring=coloring,
                                   tooltip_mode=tooltip_mode)
    fig = go.Figure(data=contour_trace, layout=layout)

    if showmarkers:
        a, b, c = coordinates
        tooltip = _tooltip(a, b, c, values, mode=tooltip_mode)
        fig.add_scatterternary(a=a, b=b, c=c,
                               mode='markers',
                               marker={'color': values,
                                       'colorscale': colorscale},
                               text=tooltip,
                               hoverinfo='text')
    if showscale:
        colorbar = dict({'type': 'scatterternary',
                         'a': [None], 'b': [None],
                         'c': [None],
                         'marker': {'cmin': values.min(),
                                    'cmax': values.max(),
                                    'colorscale': colorscale,
                                    'showscale': True},
                         'mode': 'markers'})
        fig.add_trace(colorbar)

    return fig
