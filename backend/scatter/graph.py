import plotly.express as plotlyX

def create_scatter_graph(DataFrame):
    
    figure = plotlyX.scatter(DataFrame,
                            x ='Date',
                            y='ETH',
                            # text=Type,
                            # color_discrete_sequence=f"rgb(0,0,{viridis(1)})",
                            hover_data=['Hash'],
                            title="Transactions",

                            #FIXME Testing width and height
                            #! Delete later
                            width=1600, height=630)
                            # symbol=Type) #! Not sure if symbol is necessary


    #! Uncomment below?
    # figure.update_traces(textposition='top center')
    # if Type == "Buyer":             #Note Made the graph green to represent people buying. Note sure if necessary
    #     figure.update_traces(marker=dict(
    #     color="green"
    #     ))
    # elif Type == "Seller":          #Note Made the graph red to represent people selling. Note sure if necessary
    #     figure.update_traces(marker=dict(
    #     color='red'))

    figure.update_layout(title_x=0.5)


    #! Make it so there's a button which can turn the legend on and off
    # figure.layout.update(showlegend=False)
    return figure

