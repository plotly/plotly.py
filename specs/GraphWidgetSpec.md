### Spec

```python
g = Graph(url)
```

```python
g.on_click(callback, remove=False)
    Assign a callback to click events propagated
    by clicking on point(s) in the Plotly graph.

    Args:
        callback (function): Callback function this is called
            on click events with the signature:
            callback(widget, hover_obj) -> None

            Args:
                widget (GraphWidget): The current instance
                of the graph widget that this callback is assigned to.

                click_obj (dict): a nested dict that describes
                which point(s) were clicked on.

                click_obj example:
                    [
                        {
                            'curveNumber': 1,
                            'pointNumber': 2,
                            'x': 4,
                            'y': 14
                        }
                    ]

        remove (bool, optional): If False, attach the callback.
            If True, remove the callback. Defaults to False.


    Returns:
        None

    Example:
    ```
    from IPython.display import display
    def message_handler(widget, msg):
        display(widget._graph_url)
        display(msg)

    g = Graph('https://plot.ly/~chris/3375')
    display(g)

    g.on_hover(message_handler)
    ```

```

```python
g.on_hover(callback, remove=False)
    Assign a callback to hover events propagated
    by hovering over points in the Plotly graph.

    Args:
        callback (function): Callback function this is called
            on hover events with the signature:
            callback(widget, hover_obj) -> None

            Args:
                widget (GraphWidget): The current instance
                of the graph widget that this callback is assigned to.

                hover_obj (dict): a nested dict that describes
                which point(s) was hovered over that the
                points belong to.

                hover_obj example:
                    [
                        {
                            'curveNumber': 1,
                            'pointNumber': 2,
                            'x': 4,
                            'y': 14
                        }
                    ]

        remove (bool, optional): If False, attach the callback.
            If True, remove the callback. Defaults to False.


    Returns:
        None

    Example:
    ```
    from IPython.display import display
    def message_handler(widget, msg):
        display(widget._graph_url)
        display(msg)

    g = Graph('https://plot.ly/~chris/3375')
    display(g)

    g.on_hover(message_handler)
    ```

```

```python
g.on_zoom(callback, remove=False)
    Assign a callback to zoom events propagated
    by zooming in regions in the Plotly graph.

    Args:
        callback (function): Callback function this is called
            on zoom events with the signature:
            callback(widget, zoom_obj) -> None

            Args:
                widget (GraphWidget): The current instance
                of the graph widget that this callback is assigned to.

                zoom_obj (dict): A description of the
                    region that was zoomed into.

                    zoom_obj example:
                    {
                        'x': [1.8399058038561549, 2.1644335966246384],
                        'y': [4.640902872777017, 7.8556771545827635]
                    }

                remove (bool, optional): If False, attach the callback.
                    If True, remove the callback. Defaults to False.

    Returns:
        None

    Example:
    ```
    from IPython.display import display
    def message_handler(widget, msg):
        display(widget._graph_url)
        display(msg)

    g = Graph('https://plot.ly/~chris/3375')
    display(g)

    g.on_zoom(message_handler)
    ```

```

```python
g.restyle(update, indices=None)
    Update the style of existing traces in the Plotly graph.

    Args:
        update (dict):
            Single-nested dict where keys are the graph attribute strings
            and values are the value of the graph attribute.

            To update graph objects that are nested, like
            a marker's color, combine the keys with a period,
            e.g. `marker.color`

            To update an attribute of multiple traces, set the
            value to an list of values. If the list is shorter
            than the number of traces, the values will wrap around.
            Note: this means that for values that are naturally an array, like
            `x` or `colorscale`, you need to wrap the value in an extra array,
            i.e. {'colorscale': [[[0, 'red'], [1, 'green']]]}

            You can also supply values to different traces with the
            indices argument.

            See all of the graph attributes in our reference documentation
            here: https://plot.ly/python/reference or by calling `help` on
            graph objects in `plotly.graph_objs`.

        indices (list, optional):
            Specify which traces to apply the update dict to.
            Negative indices are supported.

    Examples:
        Initialization - Start each example below with this setup:
        ```
        from plotly.widgets import Graph
        from IPython.display import display

        graph = Graph('https://plot.ly/~chris/3979')
        display(graph)
        ```

        Example 1 - Set `marker.color` to red in every trace in the graph
        ```
        graph.restyle({'marker.color': 'red'})
        ```

        Example 2 - Set `marker.color` to red in the first trace of the graph
        ```
        graph.restyle({'marker.color': 'red'}, indices=[0])
        ```

        Example 3 - Set `marker.color` of all of the traces to
            alternating sequences of red and green
        ```
        graph.restyle({'marker.color': ['red', 'green']})
        ```

        Example 4 - Set just `marker.color` of the first two traces to red and green
        ```
        graph.restyle({'marker.color': ['red', 'green']}, indices=[0, 1])
        ```

        Example 5 - Set multiple attributes of all of the traces
        ```
        graph.restyle({
            'marker.color': 'red',
            'line.color': 'green'
        }, indices=[0, 1])
        ```

        Example 6 - Update the data of the first trace
        ```
        graph.restyle({
            'x': [[1, 2, 3]],
            'y': [[10, 20, 30]],
        }, indices=[0])
        ```

        Example 7 - Update the data of the first two traces
        ```
        graph.restyle({
            'x': [[1, 2, 3],
                  [1, 2, 4]],
            'y': [[10, 20, 30],
                  [5, 8, 14]],
        }, indices=[0, 1])
        ```

        Example 8 - Set the `marker.color` of the last trace to red
        # TODO: This doesn't seem to work
        ```
        graph.restyle({'marker.color': 'red'}, indices=[-1])
        ```

```

```
g.relayout(layout)
    Update the layout of the Plotly graph.

    Args:
        layout (dict):
            Single-nested dict where keys are the graph attribute strings
            and values are the value of the graph attribute.

            To update graph objects that are nested, like
            the title of an axis, combine the keys with a period
            e.g. `xaxis.title`. To set a value of an element in an array,
            like an axis's range, use brackets, e.g. 'xaxis.range[0]'.

            See all of the layout attributes in our reference documentation:
            https://plot.ly/python/reference/#Layout
            Or by calling `help` on `plotly.graph_objs.Layout`

    Examples - Start each example below with this setup:
        Initialization:
        ```
        from plotly.widgets import Graph
        from IPython.display import display

        graph = Graph('https://plot.ly/~chris/3979')
        display(graph)
        ```

        Example 1 - Update the title
        ```
        graph.relayout({'title': 'Experimental results'})
        ```

        Example 2 - Update the xaxis range
        ```
        graph.relayout({'xaxis.range': [-1, 6]})
        ```

        Example 3 - Update the first element of the xaxis range
        ```
        graph.relayout({'xaxis.range[0]': -3})
        ```

```

```
g.hover(*hover_objs)
    Show hover labels over the points specified in hover_obj.

    Hover labels are the labels that normally appear when the
    mouse hovers over points in the plotly graph.

    Args:
        hover_objs (tuple of dicts):
            Specifies which points to place hover labels over.

            The location of the hover labels is described by a dict with keys
            'xval' and/or 'yval' or 'curveNumber' and 'pointNumber'
            and optional keys 'hovermode' and 'subplot'

            'xval' and 'yval' specify the (x, y) coordinates to place the label(s).
            'xval' and 'yval need to be close to a point drawn in a graph.

            'curveNumber' and 'pointNumber' specify the trace number and the index
            of the point in that trace respectively.

            'subplot' describes which axes to the coordinates above refer to.
            By default, it is equal to 'xy'. For example, to specify the second
            x-axis and the third y-axis, set 'subplot' to 'x2y3'

            'hovermode' is either 'closest', 'x', or 'y'.
            When set to 'x', all data sharing the same 'x' coordinate will be
            shown on screen with corresponding trace labels. When set to 'y' all
            data sharing the same 'y' coordinates will be shown on the screen with
            corresponding trace labels. When set to 'closest', information about
            the data point closest to where the viewer is hovering will appear.

            Note: If 'hovermode' is 'x', only 'xval' needs to be set.
                  If 'hovermode' is 'y', only 'yval' needs to be set.
                  If 'hovermode' is 'closest', 'xval' and 'yval' both need to be set.

            Note: 'hovermode' can be toggled by the user in the graph toolbar.

            Note: It is not currently possible to apply multiple hover labels to
                  points on different axes.

            Note: `hover` can only be called with multiple dicts if
                  'curveNumber' and 'pointNumber' are the keys of the dicts.

    Examples:
        Initialization - Start each example below with this setup:
        ```
        from plotly.widgets import Graph
        from IPython.display import display

        graph = Graph('https://plot.ly/~chris/3979')
        display(graph)
        ```

        Example 1 - Apply a label to the (x, y) point (3, 2)
        ```
        graph.hover({'xval': 3, 'yval': 2, 'hovermode': 'closest'})
        ```

        Example 2 - Apply a labels to all the points with the x coordinate 3
        ```
        graph.hover({'xval': 3, 'hovermode': 'x'})
        ```

        Example 3 - Apply a label to the first point of the first trace
                    and the second point of the second trace.
        ```
        graph.hover({'curveNumber': 0, 'pointNumber': 0},
                    {'curveNumber': 1, 'pointNumber': 1})
        ```

```

```
g.add_traces(*traces, new_indices=None)

        Add new data traces to a graph.

        If `new_indices` isn't specified, they are simply appended.

        Args:
            traces (dict or list of dicts, or class of plotly.graph_objs): trace
            new_indices (list[int]|None), optional: The final indices the
                added traces should occupy in the graph.

        Examples:
            Initialization - Start each example below with this setup:
            ```
            from plotly.widgets import Graph
            from plotly.graph_objs import Scatter
            from IPython.display import display

            graph = Graph('https://plot.ly/~chris/3979')
            display(graph)
            ```

            Example 1 - Add a scatter/line trace to the graph
            ```
            graph.add_traces(Scatter(x = [1, 2, 3], y = [5, 4, 5]))
            ```

            Example 2 - Add a scatter trace and set it to to be the
                        second trace. This will appear as the second
                        item in the legend.
            ```
            graph.add_traces(Scatter(x = [1, 2, 3], y = [5, 6, 5]),
                             new_indices=[1])
            ```

            Example 3 - Add multiple traces to the graph
            ```
            graph.add_traces([
                Scatter(x = [1, 2, 3], y = [5, 6, 5]),
                Scatter(x = [1, 2.5, 3], y = [5, 8, 5])
            ])
            ```

```

```
g.delete_traces(indices)
    Delete data traces from a graph.

    Args:
        indices (list[int]): The indices of the traces to be removed

    Example - Delete the 2nd trace:
        ```
        from plotly.widgets import Graph
        from IPython.display import display

        graph = Graph('https://plot.ly/~chris/3979')
        display(graph)


        graph.delete_traces([1])
        ```

```

```
g.move_traces(current_indices, new_indices=None)
    Reorder the traces in a graph.

    The order of the traces determines the order of the legend entries
    and the layering of the objects drawn in the graph, i.e. the first trace
    is drawn first and the second trace is drawn on top of the first trace.

    Args:
        current_indices (list[int]): The index of the traces to reorder.

        new_indices (list[int], optional): The index of the traces
            specified by `current_indices` after ordering.
            If None, then move the traces to the end.

    Examples:
        Example 1 - Move the first trace to the second to last
            position, the second trace to the last position
        ```
        graph.move_traces([0, 1])
        ```

        Example 2 - Move the first trace to the second position,
            the second trace to the first position.
        ```
        graph.move_traces([0], [1])
        ```

```

```
g.get_figure(expose_defaults=False)
    Return the figure object JSON described in the
    current drawing of the graph.

    Note: For large figures, this call can be slow as it is passing
        the object from the JavaScript client to the Python backend.
        To retrieve a single attribute, use `GraphWidget.get_figure_attribute`.

    Args:
        expose_defaults (bool, default False): If True, then populate the
            figure object with the unspecified default values in the figure.

```

```
g.get_figure_attribute(attribute_string)
    Retrieve a single value of the figure specified
    by the attribute_string.

    Args:
        attribute_string

    Examples:
        Example 1:
        ```
        graph.get_figure_attribute('layout.title')
        ```

        Example 2:
        ```
        graph.get_figure_attribute('layout.xaxis.title')
        ```

        Example 3:
        ```
        graph.get_figure_attribute('data[0].x')
        ```
```

```
g.plot(figure_or_data)
    Plot a figure or data object.

```

```
g.save(filename, **plot_options)
    Send the current representation of the Plotly
    graph to your Plotly account. Save the file in your
    Plotly account with the given filename.

    Returns:
        A url where you can view the graph

```
