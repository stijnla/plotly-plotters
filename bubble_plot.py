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

fig = go.Figure()

# Done for perfect bbox (so no over- or underestimation)
# Distance 30cm estimate theta 
# x = inference time, y = offset to actual, size = 1.58*std

theta_data = [[(0.3652080105707956, 0.05194296162702821),
(0.1387780372623487, 0.05054793996952363),
(-0.3241233475060756, 0.06847341434997947),
(-0.9616975162035618, 0.0698925724880554)],
[(0.2694471806289244, 0.14228743698476176),
(-0.008251596351556943, 0.1286586126075342),
(-0.15736536079193444, 0.14451723354920684),
(-0.4238808417405931, 0.1593282193785395)],
[(1.1166128192472025, 0.4476280255655203),
(0.0479696111763983, 0.3824121892118669),
(0.11129378990755472, 0.4809592290776638),
(-0.47460845753252145, 0.34460233479193153)],
[(-8.293035870478527e-15, 4.2713697584816326e-14),
(0.25177289481720455, 0.5325675472157716),
(0.9347779293988557, 1.2449735273259654),
(-0.048658268683908885, 0.4226117517097966)],
[(0.49710531421100745, 0.1295332158841803),
(-0.053325191672768515, 0.10937435488807114),
(-0.3526573224777026, 0.10655646330364459),
(-0.28949576375584557, 0.15751353208532157)],
[(3.0114678127570893, 1.4630648715451233),
(1.5903113952885264, 1.048990496164621),
(0.8054677096595646, 1.2283278599080891),
(0.9395594256308064, 1.0729892745214746)],
[(-0.14716665329311013, 8.82068882311934),
(0.7216856157853521, 0.7791009171882793),
(8.963347284487483, 28.253037161107343),
(-17.964892001219788, 21.80529848341821)]]

compute_time = [0.02852179765701294, 
                0.018164982795715334, 
                0.010475106239318847, 
                0.009564864635467529, 
                0.018164982795715334, 
                0.010475106239318847, 
                0.009564864635467529]
texts = ['all points', 'pc2 fixed', 'pc5 fixed', 'pc10 fixed', 'pc2 variable', 'pc5 variable', 'pc10 variable']
names = ['all points', 'fixed kernel', 'variable kernel']
theta_values = [0, 0, 0, 0]
offsets = []
stds = []
for data in theta_data:
    data_offset = []
    data_stds = []
    for i, d in enumerate(data):
        data_offset.append(d[0] - theta_values[i])
        data_stds.append(d[1])
    offsets.append(np.abs(np.mean(np.array(data_offset))))
    stds.append(np.abs(np.mean(np.array(data_stds))))

x = 1/(np.array(compute_time)) # convert to ms
y = np.array(offsets)
bubble_sizes = 10*np.array(stds)
print(bubble_sizes)
d = [0, 1, 4, 1, 4, 7]
for i in range(3):
    bubbles = go.Scatter(
        x=x[d[i]:d[i+3]],
        y=y[d[i]:d[i+3]],
        mode='markers',
        marker=dict(color=full_colors[i], size=30),
        text=texts[d[i]],
        name=names[i],
        showlegend=True,
    )
    transparent_bubbles = go.Scatter(
        x=x[d[i]:d[i+3]],
        y=y[d[i]:d[i+3]],
        mode='markers',
        marker=dict(color=transparent_colors[i], size=bubble_sizes[d[i]:d[i+3]]),
        text=texts[d[i]],
        name=names[i],
        showlegend=False,
    )
    #fig.add_trace(transparent_bubbles)
    fig.add_trace(bubbles)
fig.update_layout(
    font_family="Courier New",
    font_size=35,
    yaxis=dict(title='Mean phi offset [degrees]', titlefont=dict(size=45), tickmode = 'linear', tick0 = 0, dtick =5, range=(0,45)),
    xaxis=dict(title='Frames Per Second (FPS)', titlefont=dict(size=45), tickmode = 'linear', tick0 = 0, dtick = 10),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
fig.show()  