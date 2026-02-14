"""Test script to validate plotly.express type stubs."""

import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

# Create test data
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 3, 5, 6],
    'color': ['A', 'B', 'A', 'B', 'A'],
    'size': [10, 20, 15, 25, 30]
})

# Test scatter - should type-check correctly
fig1: go.Figure = px.scatter(df, x='x', y='y', color='color', size='size')

# Test line
fig2: go.Figure = px.line(df, x='x', y='y', color='color')

# Test bar
fig3: go.Figure = px.bar(df, x='color', y='y')

# Test histogram
fig4: go.Figure = px.histogram(df, x='y')

# Test box
fig5: go.Figure = px.box(df, x='color', y='y')

# Test with wrong types (should fail type check)
# fig_bad: int = px.scatter(df, x='x', y='y')  # Uncomment to test type error

print("✓ All type annotations work correctly!")
print(f"Figure type: {type(fig1)}")
