from backend.factory.graph.superclass import Graph_Factory
import backend.graph.heatmap as heatmap_graph

class Heatmap(Graph_Factory):
    
    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):
        self.plotly_graph = heatmap_graph.Create_Heatmap_Graph(self.Dataframe_Object.axes_dictionary)