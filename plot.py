import plotly.graph_objects as go
import numpy as np

full_colors = [
    'rgba(31, 119, 180, 1)',  # muted blue
    'rgba(255, 127, 14, 1)',  # safety orange
    'rgba(44, 160, 44, 1)',  # cooked asparagus green
    'rgba(214, 39, 40, 1)',  # brick red
    'rgba(148, 103, 189, 1)',  # muted purple
    'rgba(140, 86, 75, 1)',  # chestnut brown
    'rgba(227, 119, 194, 1)',  # raspberry yogurt pink
    'rgba(127, 127, 127, 1)',  # middle gray
    'rgba(188, 189, 34, 1)',  # curry yellow-green
    'rgba(23, 190, 207, 1)'   # blue-teal
]

transparent_colors = [
    'rgba(31, 119, 180, 0.2)',  # muted blue
    'rgba(255, 127, 14, 0.2)',  # safety orange
    'rgba(44, 160, 44, 0.2)',  # cooked asparagus green
    'rgba(214, 39, 40, 0.2)',  # brick red
    'rgba(148, 103, 189, 0.2)',  # muted purple
    'rgba(140, 86, 75, 0.2)',  # chestnut brown
    'rgba(227, 119, 194, 0.2)',  # raspberry yogurt pink
    'rgba(127, 127, 127, 0.2)',  # middle gray
    'rgba(188, 189, 34, 0.2)',  # curry yellow-green
    'rgba(23, 190, 207, 0.2)'   # blue-teal
]

def scatter_mean_with_std(figure, x, data, name, color_idx, depth=0, confidence_interval=1.96, show_helper_line=False):
    y = np.array([d[0] for d in data])
    std = np.array([d[1] for d in data])
    
    y_upper = y + confidence_interval*std
    y_lower = y - confidence_interval*std

    figure.add_trace(go.Scatter(x=x, y=y, line_width=6, name=name, line_color=full_colors[color_idx]))
    if show_helper_line:
        if True:
            figure.add_trace(go.Scatter(x=x, y=np.array(5*[int(name.replace('theta=', '').replace('°',''))]), name=name,line=dict(color='rgba(0,0,0,0.2)'),hoverinfo='skip', showlegend=False))
            
        else:
            figure.add_trace(go.Scatter(x=x, y=np.array(5*[int(0)]), name=name,line=dict(color='rgba(0,0,0,0.2)'),hoverinfo='skip', showlegend=False))

    if depth != 0:
        figure.add_trace(go.Scatter(x=x, y=np.array(5*[depth]), name=name,line=dict(color='rgba(0,0,0,0.2)'),hoverinfo='skip', showlegend=False))
    figure.add_trace(go.Scatter(
            x=np.concatenate((x,x[::-1]), axis=0), # x, then x reversed
            y=np.concatenate((y_upper,y_lower[::-1]), axis=0), # upper, then lower reversed
            fill='toself',
            fillcolor=transparent_colors[color_idx],
            line=dict(color='rgba(255,255,255,0)'),
            hoverinfo="skip",
            showlegend=False
    ))

def scatter__std(figure, x, data, name):
    data = [(1000*d[0], 1000*d[1]) for d in data]
    std = np.array([d[1] for d in data])

    figure.add_trace(go.Scatter(x=x, y=std, line_width=5, name=name,fillcolor='rgba(0,100,80,1)',))
""" 
# depth plot at 30cm
fig = go.Figure()

x = np.array([0.5, 0.75, 1, 1.25, 1.5])

# 0 degrees
name = 'theta=0°'
data =[(1.0137400000000003, 0.0019058856209121934),
(1.0149700000000001, 0.0022111309323511524),
(1.01722, 0.0010637668917577658),
(1.0197900000000002, 0.0013659795020423636),
(1.02219, 0.0018584671102820456)]

scatter_mean_with_std(fig, x, data, name, 0)
# 15 degrees
name = 'theta=15°'
data =[(1.0121900000000004, 0.0009348261870529414),
(1.01313, 0.0009017205775626692),
(1.0132100000000002, 0.0006825686778632556),
(1.01438, 0.0009249864863877748),
(1.01486, 0.0009275774900244465),]
scatter_mean_with_std(fig, x, data, name, 1)

# 30 degrees
name = 'theta=30°'
data =[(1.01548, 0.0004995998398719277),
(1.0157700000000003, 0.0006907242575732066),
(1.0155800000000001, 0.0004935585071701779),
(1.01512, 0.0009410632284815277),
(1.0165300000000002, 0.0009322553298319146),]
scatter_mean_with_std(fig, x, data, name, 2)

# 45 degrees
name = 'theta=45°'
data =[(1.0144100000000003, 0.001158404074578492),
(1.01369, 0.0009348261870529748),
(1.01289, 0.0005812916651733131),
(1.0132100000000002, 0.0009725739046468145),
(1.01326, 0.0016529972776746797),]
scatter_mean_with_std(fig, x, data, name, 3)

fig.update_layout(
    font_family="Courier New",
    font_size=35,
    yaxis=dict(title='Distance [m]', titlefont=dict(size=45), tickmode = 'linear', range=(1.0,1.03), dtick=0.005),
    xaxis=dict(title='Bounding Box Multiplier', titlefont=dict(size=45), tickmode = 'linear', tick0 = 0.5, dtick = 0.25),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    showlegend=False,)

fig.add_trace(go.Scatter(x=x, y=np.array(5*[0.3]), name=name,line=dict(color='rgba(0,0,0,0.2)'),hoverinfo='skip', showlegend=False))
fig.show()

"""

# phi plot at 30cm
fig = go.Figure()
x = np.array([0.5, 0.75, 1, 1.25, 1.5])

all_data = [[(-4.810744648517601, 1.987818595275145),
(-4.676636941769365, 1.5944523552960674),
(-5.499640634834469, 1.9977098575221208),
(-5.576880589188892, 1.6190703367718315),
(-5.3853954147612795, 2.5138910413633555)],
[(-5.807201231746582, 2.047502548539867),
(-5.209057323474333, 0.8760225305200126),
(-5.656468373732304, 1.1171760930020926),
(-4.558841914723168, 2.0845945549634446),
(-4.4920600944965425, 2.710440044794979)],
[(-5.542967032594952, 2.8077306013936587),
(-3.6419488122490176, 1.2936151966880018),
(-4.983271309066464, 1.2647613446962376),
(-5.421828674623806, 1.673416420610877),
(-5.932322841748893, 1.7690389823334434)],
[(-7.51283699994583, 2.754759719178644),
(-3.857116730312988, 1.5495008404530146),
(-4.052015914663094, 1.8166129187584101),
(-4.416508111865959, 2.409898235381664),
(-4.452143001478013, 1.9626966583462486)],
[(-3.7752917210872823, 1.4480838606285686),
(-6.114140694170417, 1.0341298669142285),
(-5.023456908612161, 0.9774655488967982),
(-3.735868089435419, 1.477659487749489),
(-2.693146526441618, 2.28632286262727)]]


name = 'theta=0°'
data =[(p[0]+0, p[1]) for p in all_data[0]]

scatter_mean_with_std(fig, x, data, name, 0)

name = 'theta=20.7°'
data =[(p[0]+0, p[1]) for p in all_data[1]]
scatter_mean_with_std(fig, x, data, name, 1)

name = 'theta=39.2°'
data =[(p[0]+0, p[1]) for p in all_data[2]]
scatter_mean_with_std(fig, x, data, name, 2)

name = 'theta=54.7°'
data =[(p[0]+0, p[1]) for p in all_data[3]]
scatter_mean_with_std(fig, x, data, name, 3)
"""
name = 'all points'
data =all_data[4]

scatter_mean_with_std(fig, x, data, name, 4)
"""
fig.update_layout(
    font_family="Courier New",
    font_size=45,
    yaxis=dict(title='Mean predicted phi [degrees]', titlefont=dict(size=50), tickmode = 'linear', range=(-15, 10), tick0 = 0, dtick =5),
    xaxis=dict(title='Bounding Box Multiplier', titlefont=dict(size=53), tickmode = 'linear', tick0 = 0.5, dtick = 0.25),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    showlegend=True)
fig.show()
