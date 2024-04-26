
from backend.factory.graph.superclass import Graph_Factory
import plotly.express as plotlyX
class Transaction(Graph_Factory):
    
    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):

        Address_Column, Transction_Column, Count_Column = self.Dataframe_Object.Dataframe.columns

        #Note Using long format to create stacked bars
        self.Plotly_Graph = plotlyX.bar(self.Dataframe_Object._Dataframe, x=Address_Column, y=Count_Column, color=Transction_Column, 
                                        title="Sold/Bought",
                                        barmode="stack", text_auto=True, 
                                        
                                        #Note Red is for "Sold", green is for "bought"
                                        color_discrete_sequence=["#d71a09", "#2ddc0e"])
        
        self.Plotly_Graph.update_layout(title_x=0.5)
        self.Plotly_Graph.update_xaxes(tickfont_size=7)