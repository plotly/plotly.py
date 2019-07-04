from __future__ import absolute_import

from numbers import Number

from plotly import exceptions, optional_imports
import plotly.colors as clrs
from plotly.figure_factory import utils
from plotly.graph_objs import graph_objs

pd = optional_imports.get_module("pandas")

REQUIRED_GANTT_KEYS = ["Task", "Start", "Finish"]


def validate_gantt(df):
    """
    Validates the inputted dataframe or list
    """
    if pd and isinstance(df, pd.core.frame.DataFrame):
        # validate that df has all the required keys
        for key in REQUIRED_GANTT_KEYS:
            if key not in df:
                raise exceptions.PlotlyError(
                    "The columns in your dataframe must include the "
                    "following keys: {0}".format(", ".join(REQUIRED_GANTT_KEYS))
                )

        num_of_rows = len(df.index)
        chart = []
        for index in range(num_of_rows):
            task_dict = {}
            for key in df:
                task_dict[key] = df.ix[index][key]
            chart.append(task_dict)

        return chart

    # validate if df is a list
    if not isinstance(df, list):
        raise exceptions.PlotlyError(
            "You must input either a dataframe " "or a list of dictionaries."
        )

    # validate if df is empty
    if len(df) <= 0:
        raise exceptions.PlotlyError(
            "Your list is empty. It must contain " "at least one dictionary."
        )
    if not isinstance(df[0], dict):
        raise exceptions.PlotlyError("Your list must only " "include dictionaries.")
    return df


def gantt(
    chart,
    colors,
    title,
    bar_width,
    showgrid_x,
    showgrid_y,
    height,
    width,
    tasks=None,
    task_names=None,
    data=None,
    group_tasks=False,
):
    """
    Refer to create_gantt() for docstring
    """
    if tasks is None:
        tasks = []
    if task_names is None:
        task_names = []
    if data is None:
        data = []

    for index in range(len(chart)):
        task = dict(
            x0=chart[index]["Start"],
            x1=chart[index]["Finish"],
            name=chart[index]["Task"],
        )
        if "Description" in chart[index]:
            task["description"] = chart[index]["Description"]
        tasks.append(task)

    shape_template = {
        "type": "rect",
        "xref": "x",
        "yref": "y",
        "opacity": 1,
        "line": {"width": 0},
    }
    # create the list of task names
    for index in range(len(tasks)):
        tn = tasks[index]["name"]
        # Is added to task_names if group_tasks is set to False,
        # or if the option is used (True) it only adds them if the
        # name is not already in the list
        if not group_tasks or tn not in task_names:
            task_names.append(tn)
    # Guarantees that for grouped tasks the tasks that are inserted first
    # are shown at the top
    if group_tasks:
        task_names.reverse()

    color_index = 0
    for index in range(len(tasks)):
        tn = tasks[index]["name"]
        del tasks[index]["name"]
        tasks[index].update(shape_template)

        # If group_tasks is True, all tasks with the same name belong
        # to the same row.
        groupID = index
        if group_tasks:
            groupID = task_names.index(tn)
        tasks[index]["y0"] = groupID - bar_width
        tasks[index]["y1"] = groupID + bar_width

        # check if colors need to be looped
        if color_index >= len(colors):
            color_index = 0
        tasks[index]["fillcolor"] = colors[color_index]
        # Add a line for hover text and autorange
        entry = dict(
            x=[tasks[index]["x0"], tasks[index]["x1"]],
            y=[groupID, groupID],
            name="",
            marker={"color": "white"},
        )
        if "description" in tasks[index]:
            entry["text"] = tasks[index]["description"]
            del tasks[index]["description"]
        data.append(entry)
        color_index += 1

    layout = dict(
        title=title,
        showlegend=False,
        height=height,
        width=width,
        shapes=[],
        hovermode="closest",
        yaxis=dict(
            showgrid=showgrid_y,
            ticktext=task_names,
            tickvals=list(range(len(task_names))),
            range=[-1, len(task_names) + 1],
            autorange=False,
            zeroline=False,
        ),
        xaxis=dict(
            showgrid=showgrid_x,
            zeroline=False,
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=7, label="1w", step="day", stepmode="backward"),
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            type="date",
        ),
    )
    layout["shapes"] = tasks

    fig = graph_objs.Figure(data=data, layout=layout)
    return fig


def gantt_colorscale(
    chart,
    colors,
    title,
    index_col,
    show_colorbar,
    bar_width,
    showgrid_x,
    showgrid_y,
    height,
    width,
    tasks=None,
    task_names=None,
    data=None,
    group_tasks=False,
):
    """
    Refer to FigureFactory.create_gantt() for docstring
    """
    if tasks is None:
        tasks = []
    if task_names is None:
        task_names = []
    if data is None:
        data = []
    showlegend = False

    for index in range(len(chart)):
        task = dict(
            x0=chart[index]["Start"],
            x1=chart[index]["Finish"],
            name=chart[index]["Task"],
        )
        if "Description" in chart[index]:
            task["description"] = chart[index]["Description"]
        tasks.append(task)

    shape_template = {
        "type": "rect",
        "xref": "x",
        "yref": "y",
        "opacity": 1,
        "line": {"width": 0},
    }

    # compute the color for task based on indexing column
    if isinstance(chart[0][index_col], Number):
        # check that colors has at least 2 colors
        if len(colors) < 2:
            raise exceptions.PlotlyError(
                "You must use at least 2 colors in 'colors' if you "
                "are using a colorscale. However only the first two "
                "colors given will be used for the lower and upper "
                "bounds on the colormap."
            )

        # create the list of task names
        for index in range(len(tasks)):
            tn = tasks[index]["name"]
            # Is added to task_names if group_tasks is set to False,
            # or if the option is used (True) it only adds them if the
            # name is not already in the list
            if not group_tasks or tn not in task_names:
                task_names.append(tn)
        # Guarantees that for grouped tasks the tasks that are inserted
        # first are shown at the top
        if group_tasks:
            task_names.reverse()

        for index in range(len(tasks)):
            tn = tasks[index]["name"]
            del tasks[index]["name"]
            tasks[index].update(shape_template)

            # If group_tasks is True, all tasks with the same name belong
            # to the same row.
            groupID = index
            if group_tasks:
                groupID = task_names.index(tn)
            tasks[index]["y0"] = groupID - bar_width
            tasks[index]["y1"] = groupID + bar_width

            # unlabel color
            colors = clrs.color_parser(colors, clrs.unlabel_rgb)
            lowcolor = colors[0]
            highcolor = colors[1]

            intermed = (chart[index][index_col]) / 100.0
            intermed_color = clrs.find_intermediate_color(lowcolor, highcolor, intermed)
            intermed_color = clrs.color_parser(intermed_color, clrs.label_rgb)
            tasks[index]["fillcolor"] = intermed_color
            # relabel colors with 'rgb'
            colors = clrs.color_parser(colors, clrs.label_rgb)

            # add a line for hover text and autorange
            entry = dict(
                x=[tasks[index]["x0"], tasks[index]["x1"]],
                y=[groupID, groupID],
                name="",
                marker={"color": "white"},
            )
            if "description" in tasks[index]:
                entry["text"] = tasks[index]["description"]
                del tasks[index]["description"]
            data.append(entry)

        if show_colorbar is True:
            # generate dummy data for colorscale visibility
            data.append(
                dict(
                    x=[tasks[index]["x0"], tasks[index]["x0"]],
                    y=[index, index],
                    name="",
                    marker={
                        "color": "white",
                        "colorscale": [[0, colors[0]], [1, colors[1]]],
                        "showscale": True,
                        "cmax": 100,
                        "cmin": 0,
                    },
                )
            )

    if isinstance(chart[0][index_col], str):
        index_vals = []
        for row in range(len(tasks)):
            if chart[row][index_col] not in index_vals:
                index_vals.append(chart[row][index_col])

        index_vals.sort()

        if len(colors) < len(index_vals):
            raise exceptions.PlotlyError(
                "Error. The number of colors in 'colors' must be no less "
                "than the number of unique index values in your group "
                "column."
            )

        # make a dictionary assignment to each index value
        index_vals_dict = {}
        # define color index
        c_index = 0
        for key in index_vals:
            if c_index > len(colors) - 1:
                c_index = 0
            index_vals_dict[key] = colors[c_index]
            c_index += 1

        # create the list of task names
        for index in range(len(tasks)):
            tn = tasks[index]["name"]
            # Is added to task_names if group_tasks is set to False,
            # or if the option is used (True) it only adds them if the
            # name is not already in the list
            if not group_tasks or tn not in task_names:
                task_names.append(tn)
        # Guarantees that for grouped tasks the tasks that are inserted
        # first are shown at the top
        if group_tasks:
            task_names.reverse()

        for index in range(len(tasks)):
            tn = tasks[index]["name"]
            del tasks[index]["name"]
            tasks[index].update(shape_template)
            # If group_tasks is True, all tasks with the same name belong
            # to the same row.
            groupID = index
            if group_tasks:
                groupID = task_names.index(tn)
            tasks[index]["y0"] = groupID - bar_width
            tasks[index]["y1"] = groupID + bar_width

            tasks[index]["fillcolor"] = index_vals_dict[chart[index][index_col]]

            # add a line for hover text and autorange
            entry = dict(
                x=[tasks[index]["x0"], tasks[index]["x1"]],
                y=[groupID, groupID],
                name="",
                marker={"color": "white"},
            )
            if "description" in tasks[index]:
                entry["text"] = tasks[index]["description"]
                del tasks[index]["description"]
            data.append(entry)

        if show_colorbar is True:
            # generate dummy data to generate legend
            showlegend = True
            for k, index_value in enumerate(index_vals):
                data.append(
                    dict(
                        x=[tasks[index]["x0"], tasks[index]["x0"]],
                        y=[k, k],
                        showlegend=True,
                        name=str(index_value),
                        hoverinfo="none",
                        marker=dict(color=colors[k], size=1),
                    )
                )

    layout = dict(
        title=title,
        showlegend=showlegend,
        height=height,
        width=width,
        shapes=[],
        hovermode="closest",
        yaxis=dict(
            showgrid=showgrid_y,
            ticktext=task_names,
            tickvals=list(range(len(task_names))),
            range=[-1, len(task_names) + 1],
            autorange=False,
            zeroline=False,
        ),
        xaxis=dict(
            showgrid=showgrid_x,
            zeroline=False,
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=7, label="1w", step="day", stepmode="backward"),
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            type="date",
        ),
    )
    layout["shapes"] = tasks

    fig = graph_objs.Figure(data=data, layout=layout)
    return fig


def gantt_dict(
    chart,
    colors,
    title,
    index_col,
    show_colorbar,
    bar_width,
    showgrid_x,
    showgrid_y,
    height,
    width,
    tasks=None,
    task_names=None,
    data=None,
    group_tasks=False,
):
    """
    Refer to FigureFactory.create_gantt() for docstring
    """
    if tasks is None:
        tasks = []
    if task_names is None:
        task_names = []
    if data is None:
        data = []
    showlegend = False

    for index in range(len(chart)):
        task = dict(
            x0=chart[index]["Start"],
            x1=chart[index]["Finish"],
            name=chart[index]["Task"],
        )
        if "Description" in chart[index]:
            task["description"] = chart[index]["Description"]
        tasks.append(task)

    shape_template = {
        "type": "rect",
        "xref": "x",
        "yref": "y",
        "opacity": 1,
        "line": {"width": 0},
    }

    index_vals = []
    for row in range(len(tasks)):
        if chart[row][index_col] not in index_vals:
            index_vals.append(chart[row][index_col])

    index_vals.sort()

    # verify each value in index column appears in colors dictionary
    for key in index_vals:
        if key not in colors:
            raise exceptions.PlotlyError(
                "If you are using colors as a dictionary, all of its "
                "keys must be all the values in the index column."
            )

    # create the list of task names
    for index in range(len(tasks)):
        tn = tasks[index]["name"]
        # Is added to task_names if group_tasks is set to False,
        # or if the option is used (True) it only adds them if the
        # name is not already in the list
        if not group_tasks or tn not in task_names:
            task_names.append(tn)
    # Guarantees that for grouped tasks the tasks that are inserted first
    # are shown at the top
    if group_tasks:
        task_names.reverse()

    for index in range(len(tasks)):
        tn = tasks[index]["name"]
        del tasks[index]["name"]
        tasks[index].update(shape_template)

        # If group_tasks is True, all tasks with the same name belong
        # to the same row.
        groupID = index
        if group_tasks:
            groupID = task_names.index(tn)
        tasks[index]["y0"] = groupID - bar_width
        tasks[index]["y1"] = groupID + bar_width

        tasks[index]["fillcolor"] = colors[chart[index][index_col]]

        # add a line for hover text and autorange
        entry = dict(
            x=[tasks[index]["x0"], tasks[index]["x1"]],
            y=[groupID, groupID],
            showlegend=False,
            name="",
            marker={"color": "white"},
        )
        if "description" in tasks[index]:
            entry["text"] = tasks[index]["description"]
            del tasks[index]["description"]
        data.append(entry)

    if show_colorbar is True:
        # generate dummy data to generate legend
        showlegend = True
        for k, index_value in enumerate(index_vals):
            data.append(
                dict(
                    x=[tasks[index]["x0"], tasks[index]["x0"]],
                    y=[k, k],
                    showlegend=True,
                    hoverinfo="none",
                    name=str(index_value),
                    marker=dict(color=colors[index_value], size=1),
                )
            )

    layout = dict(
        title=title,
        showlegend=showlegend,
        height=height,
        width=width,
        shapes=[],
        hovermode="closest",
        yaxis=dict(
            showgrid=showgrid_y,
            ticktext=task_names,
            tickvals=list(range(len(task_names))),
            range=[-1, len(task_names) + 1],
            autorange=False,
            zeroline=False,
        ),
        xaxis=dict(
            showgrid=showgrid_x,
            zeroline=False,
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=7, label="1w", step="day", stepmode="backward"),
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            type="date",
        ),
    )
    layout["shapes"] = tasks

    fig = graph_objs.Figure(data=data, layout=layout)
    return fig


def create_gantt(
    df,
    colors=None,
    index_col=None,
    show_colorbar=False,
    reverse_colors=False,
    title="Gantt Chart",
    bar_width=0.2,
    showgrid_x=False,
    showgrid_y=False,
    height=600,
    width=800,
    tasks=None,
    task_names=None,
    data=None,
    group_tasks=False,
):
    """
    Returns figure for a gantt chart

    :param (array|list) df: input data for gantt chart. Must be either a
        a dataframe or a list. If dataframe, the columns must include
        'Task', 'Start' and 'Finish'. Other columns can be included and
        used for indexing. If a list, its elements must be dictionaries
        with the same required column headers: 'Task', 'Start' and
        'Finish'.
    :param (str|list|dict|tuple) colors: either a plotly scale name, an
        rgb or hex color, a color tuple or a list of colors. An rgb color
        is of the form 'rgb(x, y, z)' where x, y, z belong to the interval
        [0, 255] and a color tuple is a tuple of the form (a, b, c) where
        a, b and c belong to [0, 1]. If colors is a list, it must
        contain the valid color types aforementioned as its members.
        If a dictionary, all values of the indexing column must be keys in
        colors.
    :param (str|float) index_col: the column header (if df is a data
        frame) that will function as the indexing column. If df is a list,
        index_col must be one of the keys in all the items of df.
    :param (bool) show_colorbar: determines if colorbar will be visible.
        Only applies if values in the index column are numeric.
    :param (bool) reverse_colors: reverses the order of selected colors
    :param (str) title: the title of the chart
    :param (float) bar_width: the width of the horizontal bars in the plot
    :param (bool) showgrid_x: show/hide the x-axis grid
    :param (bool) showgrid_y: show/hide the y-axis grid
    :param (float) height: the height of the chart
    :param (float) width: the width of the chart

    Example 1: Simple Gantt Chart
    ```
    import plotly.plotly as py
    from plotly.figure_factory import create_gantt

    # Make data for chart
    df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-30'),
          dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
          dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

    # Create a figure
    fig = create_gantt(df)

    # Plot the data
    py.iplot(fig, filename='Simple Gantt Chart', world_readable=True)
    ```

    Example 2: Index by Column with Numerical Entries
    ```
    import plotly.plotly as py
    from plotly.figure_factory import create_gantt

    # Make data for chart
    df = [dict(Task="Job A", Start='2009-01-01',
               Finish='2009-02-30', Complete=10),
          dict(Task="Job B", Start='2009-03-05',
               Finish='2009-04-15', Complete=60),
          dict(Task="Job C", Start='2009-02-20',
               Finish='2009-05-30', Complete=95)]

    # Create a figure with Plotly colorscale
    fig = create_gantt(df, colors='Blues', index_col='Complete',
                       show_colorbar=True, bar_width=0.5,
                       showgrid_x=True, showgrid_y=True)

    # Plot the data
    py.iplot(fig, filename='Numerical Entries', world_readable=True)
    ```

    Example 3: Index by Column with String Entries
    ```
    import plotly.plotly as py
    from plotly.figure_factory import create_gantt

    # Make data for chart
    df = [dict(Task="Job A", Start='2009-01-01',
               Finish='2009-02-30', Resource='Apple'),
          dict(Task="Job B", Start='2009-03-05',
               Finish='2009-04-15', Resource='Grape'),
          dict(Task="Job C", Start='2009-02-20',
               Finish='2009-05-30', Resource='Banana')]

    # Create a figure with Plotly colorscale
    fig = create_gantt(df, colors=['rgb(200, 50, 25)', (1, 0, 1), '#6c4774'],
                       index_col='Resource', reverse_colors=True,
                       show_colorbar=True)

    # Plot the data
    py.iplot(fig, filename='String Entries', world_readable=True)
    ```

    Example 4: Use a dictionary for colors
    ```
    import plotly.plotly as py
    from plotly.figure_factory import create_gantt

    # Make data for chart
    df = [dict(Task="Job A", Start='2009-01-01',
               Finish='2009-02-30', Resource='Apple'),
          dict(Task="Job B", Start='2009-03-05',
               Finish='2009-04-15', Resource='Grape'),
          dict(Task="Job C", Start='2009-02-20',
               Finish='2009-05-30', Resource='Banana')]

    # Make a dictionary of colors
    colors = {'Apple': 'rgb(255, 0, 0)',
              'Grape': 'rgb(170, 14, 200)',
              'Banana': (1, 1, 0.2)}

    # Create a figure with Plotly colorscale
    fig = create_gantt(df, colors=colors, index_col='Resource',
                       show_colorbar=True)

    # Plot the data
    py.iplot(fig, filename='dictioanry colors', world_readable=True)
    ```

    Example 5: Use a pandas dataframe
    ```
    import plotly.plotly as py
    from plotly.figure_factory import create_gantt

    import pandas as pd

    # Make data as a dataframe
    df = pd.DataFrame([['Run', '2010-01-01', '2011-02-02', 10],
                       ['Fast', '2011-01-01', '2012-06-05', 55],
                       ['Eat', '2012-01-05', '2013-07-05', 94]],
                      columns=['Task', 'Start', 'Finish', 'Complete'])

    # Create a figure with Plotly colorscale
    fig = create_gantt(df, colors='Blues', index_col='Complete',
                       show_colorbar=True, bar_width=0.5,
                       showgrid_x=True, showgrid_y=True)

    # Plot the data
    py.iplot(fig, filename='data with dataframe', world_readable=True)
    ```
    """
    # validate gantt input data
    chart = validate_gantt(df)

    if index_col:
        if index_col not in chart[0]:
            raise exceptions.PlotlyError(
                "In order to use an indexing column and assign colors to "
                "the values of the index, you must choose an actual "
                "column name in the dataframe or key if a list of "
                "dictionaries is being used."
            )

        # validate gantt index column
        index_list = []
        for dictionary in chart:
            index_list.append(dictionary[index_col])
        utils.validate_index(index_list)

    # Validate colors
    if isinstance(colors, dict):
        colors = clrs.validate_colors_dict(colors, "rgb")
    else:
        colors = clrs.validate_colors(colors, "rgb")

    if reverse_colors is True:
        colors.reverse()

    if not index_col:
        if isinstance(colors, dict):
            raise exceptions.PlotlyError(
                "Error. You have set colors to a dictionary but have not "
                "picked an index. An index is required if you are "
                "assigning colors to particular values in a dictioanry."
            )
        fig = gantt(
            chart,
            colors,
            title,
            bar_width,
            showgrid_x,
            showgrid_y,
            height,
            width,
            tasks=None,
            task_names=None,
            data=None,
            group_tasks=group_tasks,
        )
        return fig
    else:
        if not isinstance(colors, dict):
            fig = gantt_colorscale(
                chart,
                colors,
                title,
                index_col,
                show_colorbar,
                bar_width,
                showgrid_x,
                showgrid_y,
                height,
                width,
                tasks=None,
                task_names=None,
                data=None,
                group_tasks=group_tasks,
            )
            return fig
        else:
            fig = gantt_dict(
                chart,
                colors,
                title,
                index_col,
                show_colorbar,
                bar_width,
                showgrid_x,
                showgrid_y,
                height,
                width,
                tasks=None,
                task_names=None,
                data=None,
                group_tasks=group_tasks,
            )
            return fig
