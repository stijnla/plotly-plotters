import plotly.graph_objects as go
import numpy as np

fig = go.Figure()


x = [1, 10, 36]
y = [11762, 354, 1166]
names = ['SKU-110K', 'Cigarette', 'Albert Heijn Supermarket']
fig.add_trace(go.Scatter(x=x, y=y, line_width=4, text=names, name="Shelf", mode='markers+text'))
x =[200]
y = [83739]
names= ['RPC']
fig.add_trace(go.Scatter(x=x, y=y, line_width=4, text=names, name="Check Out", mode='markers+text'))

fig.update_yaxes(type="log")
fig.update_traces(textposition='top center', marker_size=20)

fig.update_layout(
    font_family="Courier New",
    font_size=25,
    yaxis=dict(title='Number of images', titlefont=dict(size=30), dtick=1, tick0=100),
    xaxis=dict(title='Number of categories', titlefont=dict(size=30)))

fig.show()