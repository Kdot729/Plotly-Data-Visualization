from backend.factory.graph.superclass import Graph_Factory
import backend.graph.scatter as scatter_graph

class Scatter(Graph_Factory):

    def __init__(self, Tool, Dataframe):
        super().__init__(Tool)
        self.Dataframe = Dataframe
        
    def create_DataFrame(self):
        super().create_DataFrame()

    def Create_Plotly(self):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.Dataframe)