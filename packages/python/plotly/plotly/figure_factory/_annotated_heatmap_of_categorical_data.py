from __future__ import absolute_import

from plotly import optional_imports, exceptions
import plotly.figure_factory as ff

pd = optional_imports.get_module("pandas")
if pd is None:
    raise ImportError(
        """\
This function requires the pandas package"""
    )

def create_annotated_heatmap_of_categorical_data(
    data_frame=None, 
    x=None, 
    y=None,  
    colorscale='Plasma', 
    font_colors=None, 
    showscale=False, 
    reversescale=False, 
    **kwargs,
):
    """
    Function that creates annotated heatmaps for categorcal data.

    This function adds annotations to each cell of the heatmap.
    :param (data_frame) data_frame: DataFrame 
    :param (str|series) x: Name of a column in DataFrame or Series object
    :param (str|series) y: Name of a column in DataFrame or Series object
    :param (list|str) colorscale: heatmap colorscale.
    :param (list) font_colors: List of two color strings: [min_text_color,
        max_text_color] where min_text_color is applied to annotations for
        heatmap values < (max_value - min_value)/2. If font_colors is not
        defined, the colors are defined logically as black or white
        depending on the heatmap's colorscale.
    :param (bool) showscale: Display colorscale. Default = False
    :param (bool) reversescale: Reverse colorscale. Default = False
    :param kwargs: kwargs passed through plotly.graph_objs.Heatmap.
        These kwargs describe other attributes about the annotated Heatmap
        trace such as the colorscale. For more information on valid kwargs
        call help(plotly.graph_objs.Heatmap)

    Example 1: Simple annotated heatmap of categorical data with x and y both are series objects 

    >>> import plotly.figure_factory as ff

    >>> languages = pd.Series(["Germany", "Spanish", "Germany", "French", "Spanish", "French", "French", "Spanish", "Spanish", "French", "Germany"])
    >>> levels = pd.Series(["A1", "B1", "A1", "A1", "B1", "C1", "B1", "A1", "C1","A1", "B1"])
    
    >>> fig = ff.create_annotated_heatmap_of_categorical_data(data_frame=None, x=languages, y=levels)
    >>> fig.show()
    """

    if type(data_frame) != pd.core.frame.DataFrame:
        if type(x) != pd.core.series.Series:
            raise exceptions.PlotlyError("'x' must be a series object or name of a column in 'data_frame'")
        
        if type(y) != pd.core.series.Series:
            raise exceptions.PlotlyError("'y' must be a series object or name of a column in 'data_frame'")
        
        else:
            data_frame = pd.concat([x, y], axis=1, keys=["x", "y"])
            x = "x"
            y = "y"
            
    else:
        if x not in data_frame.columns:
            raise exceptions.PlotlyError(
                                "Value of 'x' is not the name of a column in 'data_frame'. "
                                "Expected one of %s but received: %s"
                                % (str(list(data_frame.columns)), x))

        if y not in data_frame.columns:
            raise exceptions.PlotlyError(
                                "Value of 'y' is not the name of a column in 'data_frame'. "
                                "Expected one of %s but received: %s"
                                % (str(list(data_frame.columns)), y))
    print(x, y)
    if data_frame[x].nunique() + data_frame[y].nunique() > 21:
        raise exceptions.PlotlyError("Count of unique values from both `x` and `y` columns should not increase 20 but it is: %s"
                            % (data_frame[x].nunique() + data_frame[y].nunique()))
    
    x_unique, y_unique = data_frame[x].unique().tolist(), data_frame[y].unique().tolist() 
    z = []
    for xs in x_unique:
        temp = []
        for ys in y_unique:
            temp.append(len(data_frame[(data_frame[x]==xs) & (data_frame[y]==ys)]))
        z.append(temp)
    
    fig=ff.create_annotated_heatmap(z=z, 
                                    x=y_unique, 
                                    y=x_unique, 
                                    colorscale=colorscale, 
                                    font_colors=font_colors, 
                                    showscale=showscale, 
                                    reversescale=reversescale, 
                                    **kwargs)
    return fig