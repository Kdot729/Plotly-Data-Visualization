from backend.factory.graph.superclass import Graph_Factory
import plotly.graph_objects as plotGO
from plotly.subplots import make_subplots
class Sunburst(Graph_Factory):
    
    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):

        self.Plotly_Graph = make_subplots(specs=[[{"type": "domain"}]])

        #Note Unpacking array
        ID_Column, Parent_Column, Value_Column, Text_Column, Color_Column = self.Dataframe_Object.Dataframe.columns

        Sunburst =  plotGO.Sunburst(
                                    labels=self.Dataframe_Object.Dataframe[ID_Column],
                                    parents=self.Dataframe_Object.Dataframe[Parent_Column],
                                    values=self.Dataframe_Object.Dataframe[Value_Column],
                                    branchvalues='total',
                                    insidetextorientation="radial",
                                    texttemplate=self.Dataframe_Object.Dataframe[Text_Column],
                                    hovertemplate='<b>%{label}</b><br> Volume: %{value} ETH',

                                    #Note name removes the extra box to the side when you hover
                                    name='',
                                    marker=dict(colors=self.Dataframe_Object.Dataframe[Color_Column])
                                    )
        
        self.Plotly_Graph.add_trace(Sunburst)
        
        self.Plotly_Graph.update_layout(title="Volume", title_x=0.5, 
                            width=self.Graph_Width, height=self.Graph_Height)