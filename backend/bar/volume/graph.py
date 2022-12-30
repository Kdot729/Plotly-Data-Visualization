import plotly.express as plotly

def create_volume_graph(DataFrame):

    figure = plotly.bar(DataFrame, 
                        x="ETH", 
                        y="Month Year", 
                        color='Day', 
                        orientation='h')

    #Note Create title for graph and center it
    figure.update_layout(title_text="Volume", title_x=0.5)

    figure.update_layout(legend={
                    #Note Change position of legend to be inside the graph
                    "yanchor": "top",
                    "y": 1,
                    "xanchor":"right",
                    "x": 1,

                    #Note Styling the legend box
                    "bgcolor": "#e5ecf6",
                    "bordercolor": "black",
                    "borderwidth": 1
                    })

    return figure
