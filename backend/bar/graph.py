import plotly.express as plotlyX



def create_count_transactions_graph(DataFrame, type):

        if type == "Total":
                y_axis = ["Sell", "Buy"]
                color = {'Sell': 'red', 'Buy': 'green'}
        elif type == "Buy":
                y_axis = "Buy"
                color = {'Buy': 'green'}
        elif type == "Sell":
                y_axis = "Sell"
                color = {'Sell': 'red'}
        figure = plotlyX.bar(DataFrame, 
                        x="Address", 
                        y=y_axis,
                        color_discrete_map=color,
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
                #Note Slice the "Address" string from to include 6 characters
                'ticktext': DataFrame["Address"].str.slice(0,5).tolist(),
                },
        yaxis = {
                "tickmode":'linear',
                "tick0": "0",
                "dtick": "1",
                }
        )
        return figure