import plotly.express as plotly

def create_volume_graph(DataFrame):

    #Note Need to convert "Month Year" to a list to pass into "category_orders" because the y-axis is bugged. For some reason "February 2022" doesn't appear after "January 2022"
    #Note Reverse the list so the start of trading is at the bottom
    y_axis = (DataFrame["Month Year"].tolist())[::-1]

    figure = plotly.bar(DataFrame, 
                    x="ETH", 
                    y="Month Year", 
                    color='Day', 
                    orientation='h',
                    category_orders={
                            #Note Reorder the horizontal bars so "Monday" is first and "Sunday" is last
                            "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],

                            #Note This is to fix the y-axis because "February" is bugged
                            "Month Year": y_axis
                            })

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
    figure.update_layout(width=1580, 
                        height=750)

    return figure

