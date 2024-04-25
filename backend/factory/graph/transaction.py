
from backend.factory.graph.superclass import Graph_Factory
import plotly.express as plotlyX
class Transaction(Graph_Factory):
    
    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):

        self.Plotly_Graph = plotlyX.bar(
                                        self.Dataframe_Object._Dataframe, 
                                        x="Address", 
                                        y="Transaction Count",
                                        title="Transactions Per Address"
                                        )
        self.Plotly_Graph.update_layout(title_x=0.5)
        self.Plotly_Graph.update_xaxes(tickfont_size=7)