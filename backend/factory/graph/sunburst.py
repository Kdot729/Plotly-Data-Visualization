from backend.factory.graph.superclass import Graph_Factory
import backend.graph.sunburst as sunburst_graph

class Sunburst(Graph_Factory):
    
    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):
        self.plotly_graph = sunburst_graph.Create_Sunburst_Graph(self.Dataframe_Object.Dataframe)