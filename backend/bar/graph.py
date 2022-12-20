import plotly.express as plotlyX

#FIXME Figure out how to fix bar chart later
#TODO Maybe convert this to a horitzontal graph
def create_count_transactions_graph(DataFrame, type):
        if type == "Total":
                y_axis = ["Sell", "Buy"]
                color = {'Sell': 'red','Buy': 'green'}
                figure = multi_color_bar(DataFrame, y_axis, color)
        elif type == "Buy":
                y_axis = "Buy"
                color = "green"
                figure = single_color_bar(DataFrame, y_axis, color)
        elif type == "Sell":
                y_axis = "Sell"
                color = "red"
                figure = single_color_bar(DataFrame, y_axis, color)

                        
        figure.update_xaxes(tickfont_size=1, title="Address")
        figure.update_yaxes(title="Amount of Transactions")

        

        #Note Overwrite x-axis tick labels   
        figure.update_layout(
        title_x = 0.5,
        legend_title = "Type of Transaction",
        xaxis = {
                'tickmode': 'array',
                'tickvals': DataFrame["Address"].tolist(),
                #Note Slice the "Address" string from to include 6 characters
                'ticktext': DataFrame["Address"].str.slice(0,5).tolist()
                },
        yaxis = {
                "tickmode":'linear',
                "tick0": "0",
                #Note Increment y-axis by 3
                "dtick": "3",
                }
        )

        #! Delete later
        #Note Hide the ticklabels because it's too cluster but title is still visible
        figure.update_xaxes(visible=True, showticklabels=False)
        figure.update_layout(showlegend=False)

        figure.update_traces(textposition='outside')
        #Note Text size is 25 and if it can't fit then hide it
        figure.update_layout(uniformtext_minsize=25, uniformtext_mode='hide')
        return figure

def multi_color_bar(DataFrame, y_axis, color):
        return plotlyX.bar(DataFrame, 
                        x="Address", 
                        y=y_axis,
                        color_discrete_map=color,
                        text=DataFrame["Address"].str.slice(0,5).tolist(),
                        title="Transactions by Address")
                        # width=1500, height=700)

def single_color_bar(DataFrame, y_axis, color):
        figure = plotlyX.bar(DataFrame, 
        x="Address", 
        y=y_axis,
        title="Transactions by Address")
        figure.update_traces(marker_color=color)
        return figure
