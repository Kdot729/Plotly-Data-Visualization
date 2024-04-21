
import backend.dataframe.transaction as Transaction_Dataframe, backend.graph.transaction as Transaction_Plotly
from backend.factory.superclass import Graph_Factory
import backend.graph.scatter as scatter_graph
import backend.dataframe.volume as Volume_Dataframe, backend.graph.volume as Volume_Graph
import backend.dataframe.heatmap as heatmap_dataframe, backend.graph.heatmap as heatmap_graph
import backend.dataframe.sunburst as sunburst_dataframe, backend.graph.sunburst as sunburst_graph
class Transaction(Graph_Factory):
    
    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)

    def create_DataFrame(self):
        self.Dataframe = super().create_DataFrame()
        self.Dataframe = Transaction_Dataframe.Create_Transaction_Dataframe(self.Dataframe)

    def Create_Plotly(self):
        self.plotly_graph = Transaction_Plotly.Create_Transaction_Graph(self.Dataframe, self.columns_name["Inequality Column"])

class Volume(Graph_Factory):
    
    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)

    def create_DataFrame(self):
        self.Dataframe = super().create_DataFrame()
        self.Dataframe = Volume_Dataframe.Create_Volume_Dataframe(self.Dataframe)

    def Create_Plotly(self):
        self.plotly_graph = Volume_Graph.Create_Volume_Graph(self.Dataframe)

class Scatter(Graph_Factory):

    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)
        
    def create_DataFrame(self):
        self.Dataframe = super().create_DataFrame()

    def Create_Plotly(self):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.Dataframe)

class Heatmap(Graph_Factory):
    
    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)

    def create_DataFrame(self):
        self.Dataframe = super().create_DataFrame()
        self.axes_dictionary = heatmap_dataframe.create_heatmap_DataFrame(self.Dataframe)

    def Create_Plotly(self):
        self.plotly_graph = heatmap_graph.create_heatmap(self.axes_dictionary)

class Sunburst(Graph_Factory):
    
    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)

    def create_DataFrame(self):
        self.Dataframe = super().create_DataFrame()
        self.Dataframe = sunburst_dataframe.create_sunburst_DataFrame(self.Dataframe)

    def Create_Plotly(self):
        self.plotly_graph = sunburst_graph.create_sunburst(self.Dataframe)