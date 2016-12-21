import plotly.plotly as py


from plotly.grid_objs import Grid, Column

column_1 = Column([1, 2, 3], 'x')
column_2 = Column([1, 3, 6], 'y')
column_3 = Column([2, 4, 6], 'new x')
column_4 = Column([1, 1, 5], 'new y')
grid = Grid([column_1, column_2, column_3, column_4])
py.grid_ops.upload(grid, 'animations_grid', auto_open=False)

# create figure
figure = {
    'data': [
        {
            'xsrc': grid.get_column_reference('x'),
            'ysrc': grid.get_column_reference('y')
        }
    ],
    'layout': {'title': 'First Title'},
    'frames': [
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('new x'),
                    'ysrc': grid.get_column_reference('new y')
                }
            ],
            'layout': {'title': 'Second Title'}
        }
    ]
}

py.icreate_animations(figure, 'new_plot_with_animations')

print('done 1')


from plotly.grid_objs import Grid, Column

column_1 = Column([1, 2, 3], 'x')
column_2 = Column([1, 3, 6], 'y')
column_3 = Column([2, 4, 6], 'new x')
column_4 = Column([1, 1, 5], 'new y')
grid = Grid([column_1, column_2, column_3, column_4])
py.grid_ops.upload(grid, 'animations_grid', auto_open=False)

# create figure
figure = {
    'data': [
        {
            'xsrc': grid.get_column_reference('x'),
            'ysrc': grid.get_column_reference('y')
        }
    ],
    'layout': {'title': 'First Title'},
    'frames': [
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('new x'),
                    'ysrc': grid.get_column_reference('new y')
                }
            ],
            'layout': {'title': 'Second Title'}
        }
    ]
}

py.icreate_animations(figure, 'new_plot_with_animations')


print('done 2')
