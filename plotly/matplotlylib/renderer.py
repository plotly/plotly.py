"""
Renderer Module

This module defines the PlotlyRenderer class and a single function,
fig_to_plotly, which is intended to be the main way that user's will interact
with the matplotlylib package.

"""
import warnings
from . mplexporter import Exporter, Renderer
from . import mpltools
from .. graph_objs import *


class PlotlyRenderer(Renderer):
    """A renderer class inheriting from base for rendering mpl plots in plotly.

    A renderer class to be used with an exporter for rendering matplotlib
    plots in Plotly. This module defines the PlotlyRenderer class which handles
    the creation of the JSON structures that get sent to plotly.

    All class attributes available are defined in __init__().

    Basic Usage:

    # (mpl code) #
    fig = gcf()
    renderer = PlotlyRenderer(fig)
    exporter = Exporter(renderer)
    exporter.run(fig)  # ... et voila

    """
    def __init__(self):
        """Initialize PlotlyRenderer obj.

        PlotlyRenderer obj is called on by an Exporter object to draw
        matplotlib objects like figures, axes, text, etc.

        All class attributes are listed here in the __init__ method.

        """
        self.plotly_fig = Figure(data=Data(), layout=Layout())
        self.mpl_fig = None
        self.current_ax_patches = []
        self.axis_ct = 0
        self.mpl_x_bounds = (0, 1)
        self.mpl_y_bounds = (0, 1)
        self.msg = "Initialized PlotlyRenderer\n"

    def open_figure(self, fig, props):
        """Creates a new figure by beginning to fill out layout dict.

        The 'autosize' key is set to false so that the figure will mirror
        sizes set by mpl. The 'hovermode' key controls what shows up when you
        mouse around a figure in plotly, it's set to show the 'closest' point.

        Positional agurments:
        fig -- a matplotlib.figure.Figure object.
        props.keys(): [
            'figwidth',
            'figheight',
            'dpi'
            ]

        """
        self.msg += "Opening figure\n"
        self.mpl_fig = fig
        self.plotly_fig['layout'] = Layout(
            width=int(props['figwidth']*props['dpi']),
            height=int(props['figheight']*props['dpi']),
            autosize=False,
            hovermode='closest')
        self.mpl_x_bounds, self.mpl_y_bounds = mpltools.get_axes_bounds(fig)
        margin = Margin(
            l=int(self.mpl_x_bounds[0]*self.plotly_fig['layout']['width']),
            r=int((1-self.mpl_x_bounds[1])*self.plotly_fig['layout']['width']),
            t=int((1-self.mpl_y_bounds[1])*self.plotly_fig['layout']['height']),
            b=int(self.mpl_y_bounds[0]*self.plotly_fig['layout']['height']),
            pad=0)
        self.plotly_fig['layout']['margin'] = margin

    def close_figure(self, fig):
        """Closes figure by cleaning up data and layout dictionaries.

        The PlotlyRenderer's job is to create an appropriate set of data and
        layout dictionaries. When the figure is closed, some cleanup and
        repair is necessary. This method removes inappropriate dictionary
        entries, freeing up Plotly to use defaults and best judgements to
        complete the entries. This method is called by an Exporter object.

        Positional arguments:
        fig -- a matplotlib.figure.Figure object.

        """
        self.plotly_fig.force_clean()
        self.plotly_fig['layout']['showlegend'] = False
        self.msg += "Closing figure\n"

    def open_axes(self, ax, props):
        """Setup a new axes object (subplot in plotly).

        Plotly stores information about subplots in different 'xaxis' and
        'yaxis' objects which are numbered. These are just dictionaries
        included in the layout dictionary. This function takes information
        from the Exporter, fills in appropriate dictionary entries,
        and updates the layout dictionary. PlotlyRenderer keeps track of the
        number of plots by incrementing the axis_ct attribute.

        Setting the proper plot domain in plotly is a bit tricky. Refer to
        the documentation for mpltools.convert_x_domain and
        mpltools.convert_y_domain.

        Positional arguments:
        ax -- an mpl axes object. This will become a subplot in plotly.
        props.keys() -- [
            'axesbg',           (background color for axes obj)
            'axesbgalpha',      (alpha, or opacity for background)
            'bounds',           ((x0, y0, width, height) for axes)
            'dynamic',          (zoom/pan-able?)
            'axes',             (list: [xaxis, yaxis])
            'xscale',           (log, linear, or date)
            'yscale',
            'xlim',             (range limits for x)
            'ylim',
            'xdomain'           (xdomain=xlim, unless it's a date)
            'ydomain'
            ]

        """
        self.msg += "  Opening axes\n"
        self.axis_ct += 1
        # set defaults in axes
        xaxis = XAxis(
            anchor='y{}'.format(self.axis_ct),
            zeroline=False,
            showline=True,
            mirror='ticks',
            ticks='inside')
        yaxis = YAxis(
            anchor='x{}'.format(self.axis_ct),
            zeroline=False,
            showline=True,
            mirror='ticks',
            ticks='inside')
        # update defaults with things set in mpl
        mpl_xaxis, mpl_yaxis = mpltools.prep_xy_axis(ax=ax,
                                                     props=props,
                                                     x_bounds=self.mpl_x_bounds,
                                                     y_bounds=self.mpl_y_bounds)
        xaxis.update(mpl_xaxis)
        yaxis.update(mpl_yaxis)
        # put axes in our figure
        self.plotly_fig['layout']['xaxis{}'.format(self.axis_ct)] = xaxis
        self.plotly_fig['layout']['yaxis{}'.format(self.axis_ct)] = yaxis

    def close_axes(self, ax):
        """Close the axes object and clean up.

        Bars from bar charts are given to PlotlyRenderer one-by-one,
        thus they need to be taken care of at the close of each axes object.
        The self.current_ax_patches variable should be empty unless a bar
        chart has been created or a rectangle object has been drawn that has
        an edge exactly on the lines x=0 or y=0.

        Positional arguments:
        ax -- an mpl axes object, not required at this time.

        """
        for patch_coll in self.current_ax_patches:
            self.draw_bar(patch_coll)
        self.current_ax_patches = []  # clear this for next axes obj
        self.msg += "  Closing axes\n"

    def draw_bar(self, patch_coll):
        """Draw a collection of similar patches as a bar chart.

        After bars are sorted, an appropriate data dictionary must be created
        to tell plotly about this data. Just like draw_line or draw_markers,
        draw_bar translates patch/path information into something plotly
        understands.

        Positional arguments:
        patch_coll -- a collection of patches to be drawn as a bar chart.

        """
        orientation = patch_coll[0]['orientation']
        if orientation == 'v':
            self.msg += "    Attempting to draw a vertical bar chart\n"
            patch_coll.sort(key=lambda b: b['x0'])
            x = [bar['x0']+(bar['x1']-bar['x0'])/2 for bar in patch_coll]
            y = [bar['y1'] for bar in patch_coll]
        else:
            self.msg += "    Attempting to draw a horizontal bar chart\n"
            patch_coll.sort(key=lambda b: b['y0'])
            x = [bar['x1'] for bar in patch_coll]
            y = [bar['y0']+(bar['y1']-bar['y0'])/2 for bar in patch_coll]
        bar = Bar(orientation=orientation,
                  x=x,
                  y=y,
                  xaxis='x{}'.format(self.axis_ct),
                  yaxis='y{}'.format(self.axis_ct),
                  opacity=patch_coll[0]['alpha'],
                  marker=Marker(
                      color=patch_coll[0]['facecolor'],
                      line=Line(width=patch_coll[0]['edgewidth'])))
        if len(bar['x']) > 1:
            self.msg += "    Heck yeah, I drew that bar chart\n"
            self.plotly_fig['data'] += bar,
        else:
            self.msg += "    Bar chart not drawn\n"
            warnings.warn('found box chart data with length <= 1, '
                          'assuming data redundancy, not plotting.')

    def draw_marked_line(self, **props):
        """Create a data dict for a line obj.

        This will draw 'lines', 'markers', or 'lines+markers'.

        props.keys() -- [
        'coordinates',  ('data', 'axes', 'figure', or 'display')
        'data',         (a list of xy pairs)
        'mplobj',       (the matplotlib.lines.Line2D obj being rendered)
        'label',        (the name of the Line2D obj being rendered)
        'linestyle',    (linestyle dict, can be None, see below)
        'markerstyle',  (markerstyle dict, can be None, see below)
        ]

        props['linestyle'].keys() -- [
        'alpha',        (opacity of Line2D obj)
        'color',        (color of the line if it exists, not the marker)
        'linewidth',
        'dasharray',    (code for linestyle, see DASH_MAP in mpltools.py)
        'zorder',       (viewing precedence when stacked with other objects)
        ]

        props['markerstyle'].keys() -- [
        'alpha',        (opacity of Line2D obj)
        'marker',       (the mpl marker symbol, see SYMBOL_MAP in mpltools.py)
        'facecolor',    (color of the marker face)
        'edgecolor',    (color of the marker edge)
        'edgewidth',    (width of marker edge)
        'markerpath',   (an SVG path for drawing the specified marker)
        'zorder',       (viewing precedence when stacked with other objects)
        ]

        """
        self.msg += "    Attempting to draw a line "
        line, marker = {}, {}
        if props['linestyle'] and props['markerstyle']:
            self.msg += "... with both lines+markers\n"
            mode = "lines+markers"
        elif props['linestyle']:
            self.msg += "... with just lines\n"
            mode = "lines"
        elif props['markerstyle']:
            self.msg += "... with just markers\n"
            mode = "markers"
        if props['linestyle']:
            line = Line(
                opacity=props['linestyle']['alpha'],
                color=props['linestyle']['color'],
                width=props['linestyle']['linewidth'],
                dash=mpltools.convert_dash(props['linestyle']['dasharray'])
            )
        if props['markerstyle']:
            marker = Marker(
                opacity=props['markerstyle']['alpha'],
                color=props['markerstyle']['facecolor'],
                symbol=mpltools.convert_symbol(props['markerstyle']['marker']),
                size=props['markerstyle']['markersize'],
                line=Line(
                    color=props['markerstyle']['edgecolor'],
                    width=props['markerstyle']['edgewidth']
                )
            )
        if props['coordinates'] == 'data':
            marked_line = Scatter(mode=mode,
                                  name=props['label'],
                                  x=[xy_pair[0] for xy_pair in props['data']],
                                  y=[xy_pair[1] for xy_pair in props['data']],
                                  xaxis='x{}'.format(self.axis_ct),
                                  yaxis='y{}'.format(self.axis_ct),
                                  line=line,
                                  marker=marker)
            self.plotly_fig['data'] += marked_line,
            self.msg += "    Heck yeah, I drew that line\n"
        else:
            self.msg += "    Line didn't have 'data' coordinates, " \
                        "not drawing\n"
            warnings.warn("Bummer! Plotly can currently only draw Line2D "
                          "objects from matplotlib that are in 'data' "
                          "coordinates!")

    def draw_image(self, **props):
        """Draw image.

        Not implemented yet!

        """
        self.msg += "    Attempting to draw image\n"
        self.msg += "    Not drawing image\n"
        warnings.warn("Aw. Snap! You're gonna have to hold off on "
                      "the selfies for now. Plotly can't import "
                      "images from matplotlib yet!")

    def draw_path_collection(self, **props):
        """Add a path collection to data list as a scatter plot.

        Current implementation defaults such collections as scatter plots.
        Matplotlib supports collections that have many of the same parameters
        in common like color, size, path, etc. However, they needn't all be
        the same. Plotly does not currently support such functionality and
        therefore, the style for the first object is taken and used to define
        the remaining paths in the collection.

        props.keys() -- [
        'paths',                (structure: [vertices, path_code])
        'path_coordinates',     ('data', 'axes', 'figure', or 'display')
        'path_transforms',      (mpl transform, including Affine2D matrix)
        'offsets',              (offset from axes, helpful if in 'data')
        'offset_coordinates',   ('data', 'axes', 'figure', or 'display')
        'offset_order',
        'styles',               (style dict, see below)
        'mplobj'                (the collection obj being drawn)
        ]

        props['styles'].keys() -- [
        'linewidth',            (one or more linewidths)
        'facecolor',            (one or more facecolors for path)
        'edgecolor',            (one or more edgecolors for path)
        'alpha',                (one or more opacites for path)
        'zorder',               (precedence when stacked)
        ]

        """
        self.msg += "    Attempting to draw a path collection\n"
        if props['offset_coordinates'] is 'data':
            alpha_face = props['styles']['facecolor'][0][3]
            rgb_face = [int(c*255)
                        for c in props['styles']['facecolor'][0][:3]]
            alpha_edge = props['styles']['edgecolor'][0][3]
            rgb_edge = [int(c*255)
                        for c in props['styles']['edgecolor'][0][:3]]
            data = props['offsets']
            marker = mpltools.convert_path(props['paths'][0])
            style = {
                'alpha': alpha_face,
                'facecolor': 'rgb({},{},{})'.format(*rgb_face),
                'marker': marker,
                'edgecolor': 'rgb({},{},{})'.format(*rgb_edge),
                'edgewidth': props['styles']['linewidth'][0],
                'markersize': mpltools.convert_affine_trans(
                    dpi=self.mpl_fig.get_dpi(),
                    aff=props['path_transforms'][0])
            }
            scatter_props = {
                'coordinates': 'data',
                'data': data,
                'label': None,
                'markerstyle': style,
                'linestyle': None
            }
            self.msg += "    Drawing path collection as markers\n"
            self.draw_marked_line(**scatter_props)
        else:
            self.msg += "    Path collection not linked to 'data', " \
                        "not drawing\n"
            warnings.warn("Dang! That path collection is out of this "
                          "world. I totally don't know what to do with "
                          "it yet! Plotly can only import path "
                          "collections linked to 'data' coordinates")

    def draw_path(self, **props):
        """Draw path, currently only attempts to draw bar charts.

        This function attempts to sort a given path into a collection of
        horizontal or vertical bar charts. Most of the actual code takes
        place in functions from mpltools.py.

        props.keys() -- [
        'data',         (a list of verticies for the path)
        'coordinates',  ('data', 'axes', 'figure', or 'display')
        'pathcodes',    (code for the path, structure: ['M', 'L', 'Z', etc.])
        'style',        (style dict, see below)
        'mplobj'        (the mpl path object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of path obj)
        'edgecolor',
        'facecolor',
        'edgewidth',
        'dasharray',    (style for path's enclosing line)
        'zorder'        (precedence of obj when stacked)
        ]

        """
        self.msg += "    Attempting to draw a path\n"
        is_bar = mpltools.is_bar(**props)
        is_barh = mpltools.is_barh(**props)
        if is_bar:  # if we think it's a bar, add it!
            self.msg += "      Assuming path is a vertical bar\n"
            bar = mpltools.make_bar(orientation='v', **props)
            self.file_bar(bar)
        if is_barh:  # perhaps a horizontal bar?
            self.msg += "      Assuming path is a horizontal bar\n"
            bar = mpltools.make_bar(orientation='h', **props)
            self.file_bar(bar)
        if not (is_bar or is_barh):
            self.msg += "    This path isn't a bar, not drawing\n"
            warnings.warn("I found a path object that I don't think is part "
                          "of a bar chart. Ignoring.")

    def file_bar(self, bar):
        """Puts a given bar into an appropriate bar or barh collection.

        Bars come from the mplexporter one-by-one. To try to put them into
        appropriate data sets, we must compare them to existing data.

        Positional arguments:
        bar -- a bar dictionary created in mpltools.make_bar.py.

        bar.keys() -- [
        'bar',          (mpl path object)
        'orientation',  (bar direction, 'v' or 'h' for horizontal or vertical)
        'x0',           ([x0, y0] = bottom-left corner of rectangle)
        'y0',
        'x1',           ([x1, y1] = top-right corner of rectangle):
        'y1',
        'alpha',        (opacity of rectangle)
        'edgecolor',    (boundary line color)
        'facecolor',    (rectangle color)
        'edgewidth',    (boundary line width)
        'dasharray',    (linestyle for boundary line)
        'zorder',       (precedence when stacked)
        ]

        """
        self.msg += "        Putting a bar into the proper bar collection\n"
        if len(self.current_ax_patches) == 0:
            self.msg += "          Started a new bar collection with this " \
                        "bar\n"
            self.current_ax_patches.append([])
            self.current_ax_patches[-1] += bar,
        else:
            match = False
            for patch_collection in self.current_ax_patches:
                if mpltools.check_bar_match(patch_collection[0], bar):
                    match = True
                    patch_collection += bar,
                    self.msg += "          Filed bar into existing bar " \
                                "collection\n"
            if not match:
                self.msg += "          Started a new bar collection with " \
                            "this bar\n"
                self.current_ax_patches.append([])
                self.current_ax_patches[-1] += bar,

    def draw_text(self, **props):
        """Create an annotation dict for a text obj.

        Currently, plotly uses either 'page' or 'data' to reference
        annotation locations. These refer to 'display' and 'data',
        respectively for the 'coordinates' key used in the Exporter.
        Appropriate measures are taken to transform text locations to
        reference one of these two options.

        props.keys() -- [
        'text',         (actual content string, not the text obj)
        'position',     (an x, y pair, not an mpl Bbox)
        'coordinates',  ('data', 'axes', 'figure', 'display')
        'text_type',    ('title', 'xlabel', or 'ylabel')
        'style',        (style dict, see below)
        'mplobj'        (actual mpl text object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of text)
        'fontsize',     (size in points of text)
        'color',        (hex color)
        'halign',       (horizontal alignment, 'left', 'center', or 'right')
        'valign',       (vertical alignment, 'baseline', 'center', or 'top')
        'rotation',
        'zorder',       (precedence of text when stacked with other objs)
        ]

        """
        self.msg += "    Attempting to draw an mpl text object\n"
        if 'annotations' not in self.plotly_fig['layout']:
            self.plotly_fig['layout']['annotations'] = Annotations()
        if props['text_type'] == 'xlabel':
            self.msg += "      Text object is an xlabel\n"
            self.draw_xlabel(**props)
        elif props['text_type'] == 'ylabel':
            self.msg += "      Text object is a ylabel\n"
            self.draw_ylabel(**props)
        elif props['text_type'] == 'title':
            self.msg += "      Text object is a title\n"
            self.draw_title(**props)
        else:  # just a regular text annotation...
            self.msg += "      Text object is a normal annotation\n"
            if props['coordinates'] is not 'data':
                self.msg += "        Text object isn't linked to 'data' " \
                            "coordinates\n"
                x_px, y_px = props['mplobj'].get_transform().transform(
                    props['position'])
                x, y = mpltools.display_to_paper(x_px, y_px,
                                              self.plotly_fig['layout'])
                xref = 'paper'
                yref = 'paper'
                xanchor = props['style']['halign']  # no difference here!
                yanchor = mpltools.convert_va(props['style']['valign'])
            else:
                self.msg += "        Text object is linked to 'data' " \
                            "coordinates\n"
                x, y = props['position']
                xref = 'x{}'.format(self.axis_ct)
                yref = 'y{}'.format(self.axis_ct)
                xanchor = 'center'
                yanchor = 'middle'
            annotation = Annotation(
                text=props['text'],
                opacity=props['style']['alpha'],
                x=x,
                y=y,
                xref=xref,
                yref=yref,
                xanchor=xanchor,
                yanchor=yanchor,
                showarrow=False,  # change this later?
                font=Font(
                    color=props['style']['color'],
                    size=props['style']['fontsize']
                )
            )
            self.plotly_fig['layout']['annotations'] += annotation,
            self.msg += "    Heck, yeah I drew that annotation\n"

    def draw_title(self, **props):
        """Add a title to the current subplot in layout dictionary.

        If there exists more than a single plot in the figure, titles revert
        to 'page'-referenced annotations.

        props.keys() -- [
        'text',         (actual content string, not the text obj)
        'position',     (an x, y pair, not an mpl Bbox)
        'coordinates',  ('data', 'axes', 'figure', 'display')
        'text_type',    ('title', 'xlabel', or 'ylabel')
        'style',        (style dict, see below)
        'mplobj'        (actual mpl text object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of text)
        'fontsize',     (size in points of text)
        'color',        (hex color)
        'halign',       (horizontal alignment, 'left', 'center', or 'right')
        'valign',       (vertical alignment, 'baseline', 'center', or 'top')
        'rotation',
        'zorder',       (precedence of text when stacked with other objs)
        ]

        """
        self.msg += "        Attempting to draw a title\n"
        if len(self.mpl_fig.axes) > 1:
            self.msg += "          More than one subplot, adding title as " \
                        "annotation\n"
            x_px, y_px = props['mplobj'].get_transform().transform(props[
                'position'])
            x, y = mpltools.display_to_paper(x_px, y_px,
                                             self.plotly_fig['layout'])
            annotation = Annotation(
                text=props['text'],
                font=Font(color=props['style']['color'],
                         size=props['style']['fontsize']
                ),
                xref='paper',
                yref='paper',
                x=x,
                y=y,
                xanchor='center',
                yanchor='bottom',
                showarrow=False  # no arrow for a title!
            )
            self.plotly_fig['layout']['annotations'] += annotation,
        else:
            self.msg += "          Only one subplot found, adding as a " \
                        "plotly title\n"
            self.plotly_fig['layout']['title'] = props['text']
            titlefont = Font(size=props['style']['fontsize'],
                             color=props['style']['color']
            )
            self.plotly_fig['layout']['titlefont'] = titlefont

    def draw_xlabel(self, **props):
        """Add an xaxis label to the current subplot in layout dictionary.

        props.keys() -- [
        'text',         (actual content string, not the text obj)
        'position',     (an x, y pair, not an mpl Bbox)
        'coordinates',  ('data', 'axes', 'figure', 'display')
        'text_type',    ('title', 'xlabel', or 'ylabel')
        'style',        (style dict, see below)
        'mplobj'        (actual mpl text object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of text)
        'fontsize',     (size in points of text)
        'color',        (hex color)
        'halign',       (horizontal alignment, 'left', 'center', or 'right')
        'valign',       (vertical alignment, 'baseline', 'center', or 'top')
        'rotation',
        'zorder',       (precedence of text when stacked with other objs)
        ]

        """
        self.msg += "        Adding xlabel\n"
        axis_key = 'xaxis{}'.format(self.axis_ct)
        self.plotly_fig['layout'][axis_key]['title'] = props['text']
        titlefont = Font(size=props['style']['fontsize'],
                         color=props['style']['color'])
        self.plotly_fig['layout'][axis_key]['titlefont'] = titlefont

    def draw_ylabel(self, **props):
        """Add a yaxis label to the current subplot in layout dictionary.

        props.keys() -- [
        'text',         (actual content string, not the text obj)
        'position',     (an x, y pair, not an mpl Bbox)
        'coordinates',  ('data', 'axes', 'figure', 'display')
        'text_type',    ('title', 'xlabel', or 'ylabel')
        'style',        (style dict, see below)
        'mplobj'        (actual mpl text object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of text)
        'fontsize',     (size in points of text)
        'color',        (hex color)
        'halign',       (horizontal alignment, 'left', 'center', or 'right')
        'valign',       (vertical alignment, 'baseline', 'center', or 'top')
        'rotation',
        'zorder',       (precedence of text when stacked with other objs)
        ]

        """
        self.msg += "        Adding ylabel\n"
        axis_key = 'yaxis{}'.format(self.axis_ct)
        self.plotly_fig['layout'][axis_key]['title'] = props['text']
        titlefont = Font(size=props['style']['fontsize'],
                         color=props['style']['color'])
        self.plotly_fig['layout'][axis_key]['titlefont'] = titlefont

    def resize(self):
        """Revert figure layout to allow plotly to resize.

        By default, PlotlyRenderer tries its hardest to precisely mimic an
        mpl figure. However, plotly is pretty good with aesthetics. By
        running PlotlyRenderer.resize(), layout parameters are deleted. This
        lets plotly choose them instead of mpl.

        """
        self.msg += "Resizing figure, deleting keys from layout\n"
        for key in ['width', 'height', 'autosize', 'margin']:
            try:
                del self.plotly_fig['layout'][key]
            except KeyError:
                pass

    def strip_style(self):
        self.msg += "Stripping mpl style, deleting keys from data and layout\n"
        self.plotly_fig.strip_style()
