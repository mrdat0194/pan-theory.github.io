"""
Chart for CV applying
"""

import plotly.graph_objects as go

fig =go.Figure(go.Sunburst(
    labels=["R", "Python", "SQL", "JAVA"],
    parents=["Technical Specialist", "Technical Specialist",
             "Technical Specialist", "Technical Specialist"],
    values=[25, 30, 25, ],
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.update_traces(textfont_size=25)

fig.show()
fig.write_image("fig_CV.png")