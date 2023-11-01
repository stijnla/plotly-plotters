import pickle 
import plotly.graph_objects as go

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
"""
with open('detection_results/detection_and_classification_results_test.pkl', 'rb') as f:
    detection_results = pickle.load(f)
    print(detection_results)
# plot detection results
fig_map50_95 = go.Figure()
fig_map75 = go.Figure()
fig_map50 = go.Figure()
map50_95_bars = []
map75_bars = []
map50_bars = []
map_50_95_vals = []
map_75_vals = []
map_50_vals = []
keys = detection_results.keys()
for key in keys:
    # read results:
    text = ['nano  ', 'small ', 'medium ', 'large ']

    map50_95 = [d[0] for d in detection_results[key]]
    map75 = [d[1] for d in detection_results[key]]
    map50 = [d[2] for d in detection_results[key]]
    times = [d[3] for d in detection_results[key]]
    if key == 'SKU-110K-VS':
        text = ['nano  ', 'small ', 'medium', 'large ']
        map50_95 = [map50_95[0]] + [0] + map50_95[2::]
        map75 = [map75[0]] + [0] + map75[2::]
        map50 = [map50[0]] + [0] + map50[2::]
        times = [times[0]] + [0] + times[2::]
    # color per pre-trained dataset
    if "SKU-110K-VS" in str(key):
        color = full_colors[2]
    elif "SKU-110K" in str(key):
        color = full_colors[1]
    else:
        color = full_colors[0]
    if 'freeze3' in key:
        name = '3'
    elif 'freeze5' in key:
        name = '5'
    elif 'freeze7' in key:
        name = '7'
    elif 'freeze9' in key:
        name = '9'
    elif "SKU" in key:
        name = '0'
    else:
        name = ''
    model_size = 3
    if "SKU-110K" in str(key) and 'freeze' not in key and not "VS" in key:
        map50_95_bars.append(go.Bar(
                                y=map50_95,
                                x=['nano', 'small', 'medium', 'large'],
                                text=name,
                                marker_color=color,
                                name=name,
                                showlegend=False))
        map_50_95_vals.append(map50_95[model_size])
        map75_bars.append(go.Bar(
                                y=map75,
                                x=['nano', 'small', 'medium', 'large'],
                                text=name,
                                marker_color=color,
                                name=name,
                                showlegend=False))
        map_75_vals.append(map75[model_size])
        map50_bars.append(go.Bar(
                                y=map50,
                                x=['nano', 'small', 'medium', 'large'],
                                text=name,
                                marker_color=color,
                                name=name,
                                showlegend=False))
        map_50_vals.append(map50[model_size])

for b in map50_95_bars:
    fig_map50_95.add_trace(b)
for b in map75_bars:
    fig_map75.add_trace(b)
for b in map50_bars:
    fig_map50.add_trace(b)

for v, bar in sorted(zip(map_50_95_vals, map50_95_bars))[::-1]:
    fig_map50_95.add_trace(bar)
for v, bar in sorted(zip(map_75_vals, map75_bars))[::-1]:
    fig_map75.add_trace(bar)
for v, bar in sorted(zip(map_50_vals, map50_bars))[::-1]:
    fig_map50.add_trace(bar)

fig_map50_95.add_trace(go.Bar(y=[0],
                              x=[['nano', 'small', 'medium', 'large'][model_size]],
                              name="no pre-training",
                              marker_color=full_colors[0]
                              ))
fig_map50_95.add_trace(go.Bar(y=[0],
                              x=[['nano', 'small', 'medium', 'large'][model_size]],
                              name="pre-training SKU-110K",
                              marker_color=full_colors[1]
                              ))
fig_map50_95.add_trace(go.Bar(y=[0],
                              x=[['nano', 'small', 'medium', 'large'][model_size]],
                              name="pre-training SKU-110K-VS",
                              marker_color=full_colors[2]
                              ))
fig_map50_95.update_layout(
    font_family="Courier New",
    font_size=45,
    title='Albert Heijn Supermarket test set',
    xaxis=dict(title="Model Size", titlefont=dict(size=55), categoryorder='total descending'),
    yaxis=dict(title="mAP50-95", titlefont=dict(size=55), tickmode='linear', range=(0.72, 0.75), dtick=0.01),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, ),
    showlegend=False,

)

fig_map75.update_layout(
    font_family="Courier New",
    font_size=45,
    title='Albert Heijn Supermarket test set',
    xaxis=dict(title="Model Size", titlefont=dict(size=55), categoryorder='total descending'),
    yaxis=dict(title="mAP75", titlefont=dict(size=55), tickmode='linear', range=(0.87, 0.91), dtick=0.01),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    showlegend=False,
)

fig_map50.update_layout(
    font_family="Courier New",
    font_size=45,
    title='Albert Heijn Supermarket test set',
    xaxis=dict(title="Model Size", titlefont=dict(size=55), categoryorder='total descending'),
    yaxis=dict(title="mAP50", titlefont=dict(size=55), tickmode='linear', range=(0.95, 0.97), dtick=0.01),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    showlegend=False,
)
fig_map50_95.show()
fig_map75.show()
fig_map50.show()

"""
# plot detection and classification results
with open('detection_results/iou_results_intraclass_val.pkl', 'rb') as f:
    detection_and_classification_results = pickle.load(f)

fig_map50_95 = go.Figure()
fig_map75 = go.Figure()
fig_map50 = go.Figure()
iou_names = ['IoU_threshold=0.7', 'IoU_threshold=0.5', 'IoU_threshold=0.3', 'IoU_threshold=0.1']
for key in detection_and_classification_results.keys():


    iou7 = {}
    iou5 = {}
    iou3 = {}
    iou1 = {}
    ious = [iou7, iou5, iou3, iou1]
    for iou in ious:
        iou['map50_95'] = []
        iou['map75'] = []
        iou['map50'] = []
        iou['times'] = []
        iou['maps'] = []
    for model_size in detection_and_classification_results[key]:
        print(len(model_size))
        for i, test in enumerate(model_size):
            ious[i]['map50_95'].append(test[0])
            ious[i]['map75'].append(test[1])
            ious[i]['map50'].append(test[2])
            ious[i]['times'].append(test[3])
            ious[i]['maps'].append(test[4])
    
for i, iou in enumerate(ious):
    text = ['n', 's', 'm', 'l']
    if i==0:
        print(iou['map50'])
        print()
        print(iou['map75'])
        print()
        print(iou['map50_95'])
    fig_map50_95.add_trace(go.Bar(
                                y=iou['map50_95'],
                                x=['nano', 'small', 'medium', 'large'],
                                name=iou_names[i]))

    fig_map75.add_trace(go.Bar(
                                y=iou['map75'],
                                x=['nano', 'small', 'medium', 'large'],
                                name=iou_names[i]))
    
    fig_map50.add_trace(go.Bar(
                                y=iou['map50'],
                                x=['nano', 'small', 'medium', 'large'],
                                name=iou_names[i]))

fig_map50_95.update_layout(
    font_family="Courier New",
    font_size=45,
    xaxis=dict(title="Model sizes", titlefont=dict(size=55)),
    yaxis=dict(title="mAP50-95", titlefont=dict(size=55), tickmode='linear', range=(0.7, 0.8), tick0=0, dtick=0.02),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    showlegend=False     ,
)

fig_map75.update_layout(
    font_family="Courier New",
    font_size=45,
    xaxis=dict(title="Model sizes", titlefont=dict(size=55)),
    yaxis=dict(title="mAP75", titlefont=dict(size=55), tickmode='linear', range=(0.85, 0.95), tick0=0, dtick=0.02),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    showlegend=False,
)

fig_map50.update_layout(
    font_family="Courier New",
    font_size=45,
    xaxis=dict(title="Model sizes", titlefont=dict(size=55)),
    yaxis=dict(title="mAP50", titlefont=dict(size=55), tickmode='linear', range=(0.9, 1), tick0=0, dtick=0.02),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    showlegend=False,
)
fig_map50_95.show()
fig_map75.show()
fig_map50.show()
