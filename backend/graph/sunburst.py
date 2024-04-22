import plotly.graph_objects as go
from plotly.subplots import make_subplots

def Create_Sunburst_Graph(DataFrame):

    figure = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]])

    figure.add_trace(go.Sunburst(
        labels=DataFrame['id'],
        parents=DataFrame['parent'],
        values=DataFrame['value'],
        branchvalues='total',

        insidetextorientation="radial",
        # textinfo="label",
        texttemplate=DataFrame["Text"],
        name='',
        # level=''
        ), 1, 1)
    figure.update_layout(title="Volume", 
                        title_x=0.2, 
                        width=1580, 
                        height=750)

    return figure