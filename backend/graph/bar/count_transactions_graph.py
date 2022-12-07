import plotly.express as plotly
import pandas as panda


def create_count_transactions_graph(DataFrame):

        figure = plotly.bar(DataFrame, 
                        x="Address", 
                        y=["Sell", "Buy"],
                        color_discrete_map={
                        'Sell': 'red',
                        'Buy': 'green'
                        },
                        title="Transactions by Address")
                        
        figure.update_xaxes(tickfont_size=7)
        figure.update_yaxes(title="Amount of Transactions")

        #Note Overwrite x-axis tick labels   
        figure.update_layout(
        title_x = 0.5,
        legend_title = "Type of Transaction",
        xaxis = {
                'tickmode': 'array',
                'tickvals': DataFrame["Address"].tolist(),
                #Note Slice the "Address" string from the 0 index up to the 5th index but don't include the 5th
                'ticktext': DataFrame["Address"].str.slice(0,5).tolist(),
                },
        yaxis = {
                "tickmode":'linear',
                "tick0": "0",
                "dtick": "1",
                }
        )
        return figure