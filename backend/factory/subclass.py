
import backend.bar.count.dataframe as count_dataframe
from backend.factory.superclass import Graph_Factory
import backend.bar.count.graph as count_graph
import backend.scatter.graph as scatter_graph
import backend.bar.volume.dataframe as volumne_dataframe, backend.bar.volume.graph as volumne_graph
import backend.heatmap.dataframe as heatmap_dataframe, backend.heatmap.graph as heatmap_graph
import backend.sunburst.dataframe as sunburst_dataframe, backend.sunburst.graph as sunburst_graph
class Count_Bar_Graph(Graph_Factory):
    
    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)

    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        self.DataFrame = count_dataframe.create_count_transactions_bar_DataFrame(self.DataFrame)

    def create_plotly(self):
        self.plotly_graph = count_graph.create_count_transactions_graph(self.DataFrame, self.columns_name["Inequality Column"])

class Volume_Bar_Graph(Graph_Factory):
    
    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)

    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        self.DataFrame = volumne_dataframe.create_volume_DataFrame(self.DataFrame)

    def create_plotly(self):
        self.plotly_graph = volumne_graph.create_volume_graph(self.DataFrame)

class Basic_Scatter_Graph(Graph_Factory):

    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)
        
    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()

    def create_plotly(self):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.DataFrame)

class Heatmap_Graph(Graph_Factory):
    
    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)

    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        self.axes_dictionary = heatmap_dataframe.create_heatmap_DataFrame(self.DataFrame)

    def create_plotly(self):
        self.plotly_graph = heatmap_graph.create_heatmap(self.axes_dictionary)

class Sunburst_Graph(Graph_Factory):
    
    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)

    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        self.DataFrame = sunburst_dataframe.create_sunburst_DataFrame(self.DataFrame)

    def create_plotly(self):
        self.plotly_graph = sunburst_graph.create_sunburst(self.DataFrame)