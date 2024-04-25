from backend.factory.graph.superclass import Graph_Factory
import plotly.graph_objects as plotGO
from plotly.subplots import make_subplots
class Sunburst(Graph_Factory):
    
    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):

        self.Plotly_Graph = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]])

        #Note Unpacking array
        ID_Column, Parent_Column, Value_Column, Text_Column = self.Dataframe_Object.Dataframe.columns

        self.Plotly_Graph.add_trace(plotGO.Sunburst(
            labels=self.Dataframe_Object.Dataframe[ID_Column],
            parents=self.Dataframe_Object.Dataframe[Parent_Column],
            values=self.Dataframe_Object.Dataframe[Value_Column],
            branchvalues='total',

            insidetextorientation="radial",
            # textinfo="label",
            texttemplate=self.Dataframe_Object.Dataframe[Text_Column],
            name='',
            # level=''
            ), 1, 1)
        
        self.Plotly_Graph.update_layout(title="Volume", title_x=0.2, 
                            width=self.Graph_Width, height=self.Graph_Height)