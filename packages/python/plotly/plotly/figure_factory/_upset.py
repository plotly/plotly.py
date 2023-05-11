from __future__ import absolute_import

from plotly import exceptions, optional_imports
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
    barmode="group",
    textangle=0,
):
    # TODO: Add docstring and webpage documentation
    plot_obj = _Upset(**locals())
    upset_plot = plot_obj.make_upset_plot()
    # TODO: Create tests for plotter
    return upset_plot, plot_obj


def _expand_subset_column(df, subset_column, subset_order=None):
    """
    Takes a column of iterables and expands into binary columns representing inclusion. Also returns subset_names.
    """
    subset_names = (
        subset_order
        if subset_order is not None
        else list(df[subset_column].explode().unique())
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
        # TODO: Implement max_subsets in code
        self.max_subsets = max_subsets
        self.subset_column = subset_column
        self.subset_order = subset_order
        self.subset_bgcolor = subset_bgcolor
        self.subset_fgcolor = subset_fgcolor
        self.category_orders = category_orders
        self.color_discrete_sequence = color_discrete_sequence
        self.color_discrete_map = color_discrete_map
        self.log_y = log_y
        self.barmode = barmode
        self.textangle = textangle
        self.boxmode = (boxmode,)
        self.points = (points,)
        self.notched = (notched,)
        self.violinmode = (violinmode,)
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

        # DEBUG
        self.test = None

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

        self.test = self.df.copy()
        # Create intersect_counts df depending on if color provided
        color = self.color
        # TODO: Add grouping by x value input
        if self.color is not None:
            intersect_df = self.df.groupby(self.color).apply(
                lambda df: _transform_upset_data(
                    df.drop(columns=[self.color])
                ).reset_index(drop=True)
            )

            # Fill in counts for subsets where count is zero for certain color groups
            filled_df = (
                intersect_df.pivot_table(
                    index="Intersections",
                    columns=[self.color],
                    values="Counts",
                    fill_value=0,
                )
                .unstack()
                .reset_index()
                .rename(columns={0: "Counts"})
            )

            # Perform sorting within each color group
            # WARNING: If sort_by="Counts" it will be ignored here since this won't make sense when using groups
            self.intersect_counts = (
                filled_df.groupby(self.color)
                .apply(
                    lambda df: _sort_intersect_counts(
                        df.drop(columns=[self.color]),
                        sort_by="Intersections",
                        asc=self.asc,
                    ).reset_index()
                )
                .reset_index()
                .drop(columns=["index"])
                .rename(columns={"level_1": "index"})
            )
        else:
            self.intersect_counts = _transform_upset_data(self.df)
            self.intersect_counts = _sort_intersect_counts(
                self.intersect_counts, sort_by=self.sort_by, asc=self.asc
            )
            self.intersect_counts = self.intersect_counts.reset_index(
                drop=True
            ).reset_index()

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
        bar_args = {**self.common_plot_args, **self.bar_args}

        self.fig = px.bar(
            self.intersect_counts, x="index", y="Counts", text="Counts", **bar_args
        )
        self.fig.update_traces(
            textposition="outside", cliponaxis=False, textangle=self.textangle
        )
        self.fig.update_layout(
            plot_bgcolor="#FFFFFF",
            xaxis_visible=False,
            xaxis_showticklabels=False,
            yaxis_visible=False,
            yaxis_showticklabels=False,
        )

    def make_switchboard(self):
        """
        Method to add subset points to input fig px.bar chart in the style of UpSet plot.
        Returns updated figure, and list of heights of dots for downstream convenience.
        """
        # Compute list of intersections
        intersections = None
        if self.color is not None:
            # Pull out full list of possible intersection combinations from first color grouping
            query = (
                self.intersect_counts[self.color]
                == self.intersect_counts[self.color].iloc[0]
            )
            intersections = list(self.intersect_counts[query]["Intersections"])
        else:
            intersections = list(self.intersect_counts["Intersections"])

        # Compute coordinates for bg subset scatter points
        d = len(self.subset_names)
        num_bars = len(self.fig.data[0]["x"])
        x_bg_scatter = np.repeat(self.fig.data[0]["x"], d)
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
                marker=dict(size=16, color=self.subset_bgcolor),
                text=labels,
                hovertemplate="<b>%{text}</b><extra></extra>",
            )
        )
        self.fig.update_layout(
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=True, zeroline=False),
            margin=dict(t=40, l=150),
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
        # Group and count according to color input
        color = self.color
        counts_df = (
            self.df.groupby(color).sum().reset_index()
            if color is not None
            else self.df.sum()
            .reset_index()
            .rename(columns={"index": "variable", 0: "value"})
        )

        # Create counts px.bar chart
        plot_df = counts_df.melt(id_vars=color) if color is not None else counts_df
        if self.mode == "Percent":
            if color is not None:
                denom = plot_df.groupby(color).sum().reset_index()
                denom_dict = dict(zip(denom[color], denom["value"]))
                plot_df["value"] = round(
                    plot_df["value"] / plot_df[color].map(denom_dict), 2
                )
            else:
                plot_df["value"] = round(plot_df["value"] / plot_df["value"].sum(), 2)

        hover_data = {"variable": False}
        bar_args = {**self.common_plot_args, **self.bar_args}
        counts_bar = px.bar(
            plot_df,
            x="value",
            y="variable",
            orientation="h",
            text="value",
            hover_data=hover_data,
            **bar_args,
        )
        counts_bar.update_traces(textposition="outside", cliponaxis=False)

        # Add subset names as text into plot
        subset_names = self.subset_names
        # subset_names = counts_bar.data[0]['y']
        max_name_len = max([len(s) for s in subset_names])
        annotation_center = -1 + -0.01 * max_name_len
        for i, s in enumerate(subset_names):
            self.fig.add_annotation(
                x=annotation_center,
                y=self.switchboard_heights[i],
                text=s,
                showarrow=False,
                font=dict(size=12, color="#000000"),
                align="left",
            )

        # Reflect horizontally the bars while preserving labels; Shift heights to match input subset scatter heights
        for trace in counts_bar.data:
            trace["x"] = -trace["x"] / max(trace["x"])
            trace["y"] = self.switchboard_heights
        counts_bar.update_traces(base=annotation_center - 1, showlegend=False)

        # Add counts chart traces to main fig
        for trace in counts_bar.data:
            self.fig.add_trace(trace)
