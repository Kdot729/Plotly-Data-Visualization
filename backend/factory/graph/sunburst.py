from backend.factory.graph.superclass import Graph_Factory
import plotly.graph_objects as plotGO
from plotly.subplots import make_subplots
class Sunburst(Graph_Factory):
    
    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):

        self.plotly_graph = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]])

        self.plotly_graph.add_trace(plotGO.Sunburst(
            labels=self.Dataframe_Object.Dataframe["ID"],
            parents=self.Dataframe_Object.Dataframe["Parent"],
            values=self.Dataframe_Object.Dataframe["Value"],
            branchvalues='total',

            insidetextorientation="radial",
            # textinfo="label",
            texttemplate=self.Dataframe_Object.Dataframe["Text"],
            name='',
            # level=''
            ), 1, 1)
        self.plotly_graph.update_layout(title="Volume", 
                            title_x=0.2, 
                            width=1580, 
                            height=750)