import plotly.express as plotlyX
import plotly
import pandas as panda
import json
import backend.graph.bar.count_transactions_graph as count_transactions_graph
import backend.sort.bar.count_transactions_sort as count_transactions_sort

#FIXME Need to make this dynamic latter
def convert_Graph_to_JSON(plotly_graph):
    graphJSON = json.dumps(obj=plotly_graph , cls=plotly.utils.PlotlyJSONEncoder) #! graphJSON needs to match graphJSON in render template because in the template it's graph graphJSON 

    return graphJSON

def create_scatter_graph(DataFrame, Address_Type):
    
    figure = plotlyX.scatter(DataFrame,
                            x ='Date',
                            y='ETH',
                            # text=Address_Type,
                            color=Address_Type, #! Not sure if color is necessary
                            # color_discrete_sequence=f"rgb(0,0,{viridis(1)})",
                            hover_data=['Hash'],
                            title="Transactions")
                            # symbol=Address_Type) #! Not sure if symbol is necessary


    #! Uncomment below?
    # figure.update_traces(textposition='top center')
    # if Address_Type == "Buyer":             #Note Made the graph green to represent people buying. Note sure if necessary
    #     figure.update_traces(marker=dict(
    #     color="green"
    #     ))
    # elif Address_Type == "Seller":          #Note Made the graph red to represent people selling. Note sure if necessary
    #     figure.update_traces(marker=dict(
    #     color='red'))

    figure.update_layout(title_x=0.5)

    #! Make it so there's a button which can turn the legend on and off
    # figure.layout.update(showlegend=False)
    return figure



#! Might Need later
# def graph(DataFrame, graph_type):
#     if graph_type == "Scatter":
#         return scatter_graph(DataFrame)
#     elif graph_type == "Bar":
#         return bar_graph(DataFrame)


