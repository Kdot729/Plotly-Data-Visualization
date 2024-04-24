
import backend.dataframe.transaction as Transaction_Dataframe, backend.graph.transaction as Transaction_Plotly
from backend.factory.graph.superclass import Graph_Factory
import backend.graph.scatter as scatter_graph
class Transaction(Graph_Factory):
    
    def __init__(self, Tool):
        super().__init__(Tool)

    def create_DataFrame(self):
        super().create_DataFrame()
        self.Dataframe = Transaction_Dataframe.Create_Transaction_Dataframe(self.Dataframe)

    def Create_Plotly(self):
        self.plotly_graph = Transaction_Plotly.Create_Transaction_Graph(self.Dataframe, self.columns_name["Inequality Column"])


class Scatter(Graph_Factory):

    def __init__(self, Tool):
        super().__init__(Tool)
        
    def create_DataFrame(self):
        super().create_DataFrame()

    def Create_Plotly(self):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.Dataframe)