from __future__ import absolute_import

from plotly import optional_imports
import plotly.graph_objects as go
import plotly.express as px

pd = optional_imports.get_module("pandas")
np = optional_imports.get_module("numpy")

VALID_PLOT_TYPES = ["bar", "box", "violin"]


def create_upset(
    data_frame,
    x=None,
    color=None,
    title=None,
    plot_type="bar",
    sort_by="Counts",
    asc=False,
    mode="Counts",
    max_subsets=20,
    subset_column=None,
    subset_order=None,
    subset_bgcolor="#C9C9C9",
    subset_fgcolor="#000000",
    category_orders=None,
    color_discrete_sequence=None,
    color_discrete_map=None,
    log_y=False,
    show_yaxis=False,
    barmode="group",
    textangle=0,
    boxmode="group",
    points="outliers",
    notched=False,
    violinmode="group",
    box=False,
):
    """
    Creates an UpSet plot, a scalable alternative to Venn diagrams. The interface supports a flexible range of use cases
    input data formats.

    :param (pandas.DataFrame) data_frame: a DataFrame either in wide format with subset/intersection inclusion data, or
    with a column in condensed format; see the tutorial for more details
    :param (str) x: (optional) column name in data_frame for data point labels, e.g. sample name to cluster intersection
    observations by
    :param (str) color: (optional) column name in data_frame for grouping intersection counts, similar to plotly.express
    inputs
    :param (str) title: (optional) title for plot
    :param (str) plot_type: (default="bar") type of plot to visualize intersection count data; must be one of "bar", "box", or "violin";
    the latter two should only be used if x is provided, in which case they represent the distribution of intersection
    counts (across color groups)
    :param (str) sort_by: (default="Counts") order in which counts are displayed; must be one of "Counts" or "Intersections";
    ignored if color is provided
    :param (bool) asc: (default=False) sort in ascending order
    :param (str) mode: (default="Counts") how to represent counts; must be one of "Counts" or "Percent"
    :param (int) max_subsets: (default=20) maximum number of intersection subsets to display
    :param (str) subset_column: (optional) if data is formatted in condensed form, input column name here with that data;
    do not use if data is already formatted in wide format
    :param (list) subset_order: (optional) if subset_column is provided, use this list of entries to specify order of labels
    :param (str) subset_bgcolor: (default="#C9C9C9") color for background dots on switchboard
    :param (str) subset_fgcolor: (default="#000000") color for foreground dots on switchboard
    :param (dict) category_orders: (optional) specify order for groups in color, as in plotly.express inputs
    :param (list) color_discrete_sequence: (optional) list of colors to use for color input, as in plotly.express inputs
    :param (dict) color_discrete_map: (optional) map of color categories to color, as in plotly.express inputs
    :param (bool) log_y: (default=False) use logarithmic y scale
    :param (bool) show_yaxis: (default=False) show y-axis tickmarks
    :param (str) barmode: (default="group") argument passed to plotly.express.bar when selected for plotting
    :param (int) textangle: (default=0) angle to use when displaying counts above bars in a bar chart
    :param (str) boxmode: (default="group") argument passed to plotly.express.box when selected for plotting
    :param (str) points: (default="outliers") argument passed to plotly.express.box when selected for plotting
    :param (bool) notched: (default=False) argument passed to plotly.express.box when selected for plotting
    :param (str) violinmode: (default="group") argument passed to plotly.express.violin when selected for plotting
    :param (bool) box: (default=False) argument passed to plotly.express.violin when selected for plotting

    :rtype (plotly.graph_objects.Figure): returns UpSet plot rendered according to input settings.

    Example 1: Simple Counts

    >>> import plotly.express as px
    >>> import plotly.figure_factory as ff

    >>> df = px.data.iris()
    >>> # Create 4 subsets defined by qualitative "large" conditions
    >>> df['SL'] = df['sepal_length'].apply(lambda x: int(x > 6))
    >>> df['SW'] = df['sepal_width'].apply(lambda x: int(x > 3))
    >>> df['PL'] = df['petal_length'].apply(lambda x: int(x > 3))
    >>> df['PW'] = df['petal_width'].apply(lambda x: int(x > 1))

    >>> df = df[['species', 'SL', 'SW', 'PL', 'PW']]
    >>> # Only use columns with inclusion in subset (0/1) values for this example
    >>> fig = ff.create_upset(df.drop(columns=['species']), color_discrete_sequence=['#000000'])
    >>> fig.show()

    Example 2: Counting by Group

    >>> # Continued from Example 1
    >>> fig = ff.create_upset(df, color='species', asc=True)
    >>> fig.show()

    Example 3: Tracking Variance of Counts Across a Category

    >>> # Continued from Example 1
    >>> import numpy as np

    >>> np.random.seed(100)
    >>> # Add a dummy variable for "day entry was observed" to track variation of subset counts across the days
    >>> df['day'] = np.random.randint(0, 5, len(df))
    >>> fig = ff.create_upset(df.drop(columns=['species']), x='day', plot_type='box', show_yaxis=True)
    >>> fig.update_layout(yaxis_side="right")
    >>> fig.show()
    """
    plot_obj = _Upset(**locals())
    upset_plot = plot_obj.make_upset_plot()
    return upset_plot


def _expand_subset_column(df, subset_column, subset_order=None):
    """
    Takes a column of iterables and expands into binary columns representing inclusion. Also returns subset_names.
    """
    subset_names = (
        subset_order
        if subset_order is not None
        else [
            x for x in df[subset_column].explode().unique() if not pd.isnull(x)
        ]  # Remove empty subset = NaN
    )
    new_df = df.copy()
    for name in subset_names:
        new_df[name] = new_df[subset_column].apply(lambda x: int(name in x))
    new_df = new_df[subset_names]
    return new_df, subset_names


def _transform_upset_data(df):
    """
    Takes raw data of binary vectors for set inclusion and produces counts over each.
    """
    intersect_counts = pd.DataFrame(
        {
            "Intersections": list(df.value_counts().to_dict().keys()),
            "Counts": list(df.value_counts().to_dict().values()),
        }
    )
    return intersect_counts


def _make_binary(t):
    """
    Converts tuple of 0,1s to binary number. Used in _transform_upset_data for sort order.
    """
    return sum([t[i] * 2**i for i in range(len(t))])


def _sort_intersect_counts(df, sort_by="Counts", asc=True):
    """
    Takes output from _transform_upset_data and sorts by method requested.
    """
    key = (
        None
        if (sort_by == "Counts")
        else lambda x: x.apply(lambda y: (sum(y), _make_binary(y)))
    )
    df = df.sort_values(by=sort_by, key=key, ascending=asc)
    return df


class _Upset:
    """
    Represents builder object for UpSet plot. Refer to figure_factory.create_upset() for full docstring.
    """

    def __init__(
        self,
        data_frame,
        x=None,
        color=None,
        title=None,
        plot_type="bar",
        sort_by="Counts",
        asc=False,
        mode="Counts",
        max_subsets=20,
        subset_column=None,
        subset_order=None,
        subset_bgcolor="#C9C9C9",
        subset_fgcolor="#000000",
        category_orders=None,
        color_discrete_sequence=None,
        color_discrete_map=None,
        log_y=False,
        show_yaxis=False,
        barmode="group",
        textangle=0,
        boxmode="group",
        points="outliers",
        notched=False,
        violinmode="group",
        box=False,
    ):

        # Plot inputs and settings
        self.df = data_frame
        self.x = x
        self.color = color
        self.title = title
        self.plot_type = plot_type
        self.sort_by = sort_by
        self.asc = asc
        self.mode = mode
        self.max_subsets = max_subsets
        self.subset_column = subset_column
        self.subset_order = subset_order
        self.subset_bgcolor = subset_bgcolor
        self.subset_fgcolor = subset_fgcolor
        self.category_orders = category_orders
        self.color_discrete_sequence = color_discrete_sequence
        self.color_discrete_map = color_discrete_map
        self.log_y = log_y
        self.show_yaxis = show_yaxis
        self.barmode = barmode
        self.textangle = textangle
        self.boxmode = boxmode
        self.points = points
        self.notched = notched
        self.violinmode = violinmode
        self.box = box

        # Aggregate common plotting args
        self.common_plot_args = {
            "color": self.color,
            "category_orders": self.category_orders,
            "color_discrete_sequence": self.color_discrete_sequence,
            "color_discrete_map": self.color_discrete_map,
            "log_y": self.log_y,
        }

        # Collect plot specific args
        self.bar_args = {
            "barmode": self.barmode,
        }

        self.box_args = {
            "boxmode": self.boxmode,
            "points": self.points,
            "notched": self.notched,
        }

        self.violin_args = {
            "violinmode": self.violinmode,
            "box": self.box,
            "points": self.points,
        }

        # Figure-building specific attributes
        self.fig = go.Figure()
        self.intersect_counts = pd.DataFrame()
        self.subset_names = None
        self.switchboard_heights = []

        # Validate inputs
        self.validate_upset_inputs()

    def make_upset_plot(self):
        # If subset_column provided, expand into standard wider format
        if self.subset_column is not None:
            color_column = self.df[self.color] if self.color is not None else None
            x_column = self.df[self.x] if self.x is not None else None
            self.df, self.subset_names = _expand_subset_column(
                self.df, self.subset_column, self.subset_order
            )
            if self.color is not None:
                self.df = pd.concat([self.df, color_column], axis=1)
            if self.x is not None:
                self.df = pd.concat([self.df, x_column], axis=1)
        else:
            self.subset_names = [
                c for c in self.df.columns if c != self.x and c != self.color
            ]

        # Create intersect_counts df depending on if color provided
        groups = [x for x in [self.color, self.x] if x is not None]
        if len(groups) > 0:
            intersect_df = self.df.groupby(groups).apply(
                lambda df: _transform_upset_data(df.drop(columns=groups)).reset_index(
                    drop=True
                )
            )

            # Fill in counts for subsets where count is zero for certain color groups
            filled_df = (
                intersect_df.pivot_table(
                    index="Intersections",
                    columns=groups,
                    values="Counts",
                    fill_value=0,
                )
                .unstack()
                .reset_index()
                .rename(columns={0: "Counts"})
            )

            # Perform sorting within each color group
            # WARNING: If sort_by="Counts" it will be ignored here since this won't make sense when using groups
            # TODO: Make sensible behavior for sort by "Counts" in this case
            self.intersect_counts = (
                filled_df.groupby(groups)
                .apply(
                    lambda df: _sort_intersect_counts(
                        df.drop(columns=groups),
                        sort_by="Intersections",
                        asc=self.asc,
                    ).reset_index()
                )
                .reset_index()
                .drop(columns=["index"])
                .rename(
                    columns={"level_1": "index", "level_2": "index"}
                )  # Not sure how to tell the two apart...
            )

            # Truncate subsets if necessary
            self.intersect_counts = self.intersect_counts.groupby(groups).head(
                self.max_subsets
            )

        else:
            self.intersect_counts = _transform_upset_data(self.df)
            self.intersect_counts = _sort_intersect_counts(
                self.intersect_counts, sort_by=self.sort_by, asc=self.asc
            )
            self.intersect_counts = self.intersect_counts.reset_index(
                drop=True
            ).reset_index()

            self.intersect_counts = self.intersect_counts.head(self.max_subsets)

        # Rescale for percents if requested
        mode = self.mode
        if mode == "Percent":
            if self.color is not None:
                denom = self.intersect_counts.groupby(self.color).sum().reset_index()
                denom_dict = dict(zip(denom[self.color], denom["Counts"]))
                self.intersect_counts["Counts"] = round(
                    self.intersect_counts["Counts"]
                    / self.intersect_counts[self.color].map(denom_dict),
                    2,
                )
            else:
                self.intersect_counts["Counts"] = round(
                    self.intersect_counts["Counts"]
                    / self.intersect_counts["Counts"].sum(),
                    2,
                )

        # Create 3 main components for figure
        self.make_primary_plot()
        self.make_switchboard()
        self.make_margin_plot()

        # Add title
        self.fig.update_layout(title=self.title, title_x=0.5)

        return self.fig

    def validate_upset_inputs(self):
        # Check sorting inputs are valid
        sort_by = self.sort_by
        try:
            assert (sort_by == "Counts") or (sort_by == "Intersections")
        except AssertionError:
            raise ValueError(
                f'Invalid input for "sort_by". Must be either "Counts" or "Intersections" but you provided {sort_by}'
            )

        # Check mode is either Counts or Percent
        mode = self.mode
        try:
            assert (mode == "Counts") or (mode == "Percent")
        except AssertionError:
            raise ValueError(
                f'Invalid input for "mode". Must be either "Counts" or "Percent" but you provided {mode}'
            )

        # Check plot_type is valid
        plot_type = self.plot_type
        try:
            assert plot_type in VALID_PLOT_TYPES
        except AssertionError:
            raise ValueError(
                f'Invalid input for "plot_type". Must be one of "bar", "box", or "violin" but you provided {plot_type}'
            )

    def make_primary_plot(self):
        plot_function = None
        args = {}
        update_traces = {}

        if self.plot_type == "bar":
            plot_function = px.bar
            args = {**self.common_plot_args, **self.bar_args, "text": "Counts"}
            update_traces = {
                "textposition": "outside",
                "cliponaxis": False,
                "textangle": self.textangle,
            }
        elif self.plot_type == "box":
            plot_function = px.box
            args = {**self.common_plot_args, **self.box_args}
        elif self.plot_type == "violin":
            plot_function = px.violin
            args = {**self.common_plot_args, **self.violin_args}

        self.fig = plot_function(self.intersect_counts, x="index", y="Counts", **args)
        self.fig.update_traces(**update_traces)

        self.fig.update_layout(
            plot_bgcolor="#FFFFFF",
            xaxis_visible=False,
            xaxis_showticklabels=False,
            yaxis_visible=self.show_yaxis,
            yaxis_showticklabels=self.show_yaxis,
        )

    def make_switchboard(self):
        """
        Method to add subset points to input fig px.bar chart in the style of UpSet plot.
        Returns updated figure, and list of heights of dots for downstream convenience.
        """
        # Pull out full list of possible intersection combinations
        intersections = list(self.intersect_counts["Intersections"].unique())

        # Compute coordinates for bg subset scatter points
        d = len(self.subset_names)
        num_bars = len(intersections)
        x_bg_scatter = np.repeat(range(num_bars), d)
        y_scatter_offset = (
            0.2  # Offsetting ensures bars will hover just above the subset scatterplot
        )
        y_max = (1 + y_scatter_offset) * max([max(bar["y"]) for bar in self.fig.data])
        self.switchboard_heights = [
            -y_max / d * i - y_scatter_offset * y_max for i in list(range(d))
        ]
        y_bg_scatter = num_bars * self.switchboard_heights

        # Add bg subset scatter points to figure below bar chart
        labels = np.repeat(
            [
                "+".join([x for x, y in zip(self.subset_names, s) if y != 0])
                for s in intersections
            ],
            d,
        )
        labels = ["None" if x == "" else x for x in labels]
        self.fig.add_trace(
            go.Scatter(
                x=x_bg_scatter,
                y=y_bg_scatter,
                mode="markers",
                showlegend=False,
                marker=dict(size=16, color=self.subset_bgcolor, showscale=False),
                text=labels,
                hovertemplate="<b>%{text}</b><extra></extra>",
            )
        )
        self.fig.update_layout(
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=True, zeroline=False),
            margin=dict(t=40, l=40),
        )

        # Then fill in subset markers with fg color
        x = 0
        for s in intersections:
            x_subsets = []
            y_subsets = []
            y = 0
            for e in s:
                if e:
                    x_subsets += [x]
                    y_subsets += [-y_max / d * y - y_scatter_offset * y_max]
                y += 1
            x += 1
            self.fig.add_trace(
                go.Scatter(
                    x=x_subsets,
                    y=y_subsets,
                    mode="markers+lines",
                    showlegend=False,
                    marker=dict(size=16, color=self.subset_fgcolor, showscale=False),
                    text=["+".join([x for x, y in zip(self.subset_names, s) if y != 0])]
                    * sum(s),
                    hovertemplate="<b>%{text}</b><extra></extra>",
                )
            )

    def make_margin_plot(self):
        """
        Method to add left margin count px.bar chart in style of UpSet plot.
        """
        # Group and count according to inputs
        color = self.color
        groups = [x for x in [self.color, self.x] if x is not None]
        # if len(groups) > 0:
        #     counts_df = self.df.groupby(groups).sum().reset_index()
        if self.color is not None:
            counts_df = self.df.groupby(self.color).sum().reset_index()
            if self.x is not None:
                counts_df = counts_df.drop(columns=[self.x])
        else:
            counts_df = (
                self.df.sum()
                .reset_index()
                .rename(columns={"index": "variable", 0: "value"})
            )

        # Create counts px.bar chart
        plot_df = (
            counts_df.melt(id_vars=[self.color])
            if self.color is not None
            else counts_df
        )
        if self.mode == "Percent":
            if color is not None:
                denom = (
                    self.df.groupby(color)
                    .apply(lambda df: len(df))
                    .reset_index()
                    .rename(columns={0: "value"})
                )
                denom_dict = dict(zip(denom[color], denom["value"]))
                plot_df["value"] = round(
                    plot_df["value"] / plot_df[color].map(denom_dict), 2
                )
            else:
                plot_df["value"] = round(plot_df["value"] / len(self.df), 2)

        plot_function = px.bar
        update_traces = {"textposition": "outside", "cliponaxis": False}
        args = {
            **self.common_plot_args,
            **self.bar_args,
            "text": "value",
            "hover_data": {"variable": False},
        }

        counts_fig = plot_function(
            plot_df, x="value", y="variable", orientation="h", **args
        )
        counts_fig.update_traces(**update_traces)

        # Add subset names as text into plot
        max_name_len = max([len(s) for s in self.subset_names])
        annotation_center = -1 + -0.01 * max_name_len
        for i, s in enumerate(self.subset_names):
            self.fig.add_annotation(
                x=annotation_center,
                y=self.switchboard_heights[i],
                text=s,
                showarrow=False,
                font=dict(size=12, color="#000000"),
                align="left",
            )

        # Reflect horizontally the bars while preserving labels; Shift heights to match input subset scatter heights
        max_x = max([max(t["x"]) for t in counts_fig.data])
        for trace in counts_fig.data:
            trace["x"] = -trace["x"] / max_x
            trace["y"] = self.switchboard_heights
        counts_fig.update_traces(base=annotation_center - 1, showlegend=False)

        # Add counts chart traces to main fig
        for trace in counts_fig.data:
            self.fig.add_trace(trace)
