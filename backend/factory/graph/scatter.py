from backend.factory.graph.superclass import Graph_Factory
import plotly.express as plotlyX

class Scatter(Graph_Factory):

    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool)
        self.Dataframe_Object = Dataframe_Object

    def Create_Plotly(self):
            
        self.plotly_graph = plotlyX.scatter(self.Dataframe_Object.Dataframe,
                            x =self.Dataframe_Object.Date_Column,
                            y=self.Dataframe_Object.ETH_Column,
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

        self.plotly_graph.update_layout(title_x=0.5)