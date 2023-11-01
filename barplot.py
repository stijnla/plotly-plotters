import plotly.graph_objects as go
import numpy as np
x = ['All points', '1000 points','500 points', '250 points', '125 points'][::-1]
fit_times = 1000*np.array([0.006923367977142334, 0.0007454562187194824, 0.0006279802322387695, 0.00040032863616943357, 0.00037721395492553713][::-1])
pc_times = 1000*np.array([0.20567055225372313, 0.0573272180557251, 0.04523444652557373, 0.029667296409606934, 0.028711228370666503][::-1])


fig = go.Figure(data=[
    
    go.Bar(name='Pointcloud calculation', x=x, y=pc_times),
    go.Bar(name='Plane fit', x=x, y=fit_times),
])
# Change the bar mode
fig.update_layout(
    font_family="Courier New",
    font_size=45,
    barmode = 'stack',
    yaxis=dict(title='Inference time [ms]', titlefont=dict(size=55), tickmode = 'linear',  dtick=50),
    xaxis=dict(title='Pointcloud size', titlefont=dict(size=55), tickmode = 'linear'),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    showlegend=False)
fig.show()  