
import backend.factory.dataframe.transaction as Transaction_Dataframe, backend.graph.transaction as Transaction_Plotly
from backend.factory.graph.superclass import Graph_Factory
class Transaction(Graph_Factory):
    
    def __init__(self, Tool):
        super().__init__(Tool)

    def Create_Plotly(self):
        self.Plotly_Graph = Transaction_Plotly.Create_Transaction_Graph(self.Dataframe, self.columns_name["Inequality Column"])