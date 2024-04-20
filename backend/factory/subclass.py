
import backend.bar.count.dataframe as count_dataframe
from backend.factory.superclass import Graph_Factory
from flask import render_template
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

        #Note unmodifed_DataFrame is the original DataFrame which is going to be used to get the address_list
        self.unmodifed_DataFrame = self.DataFrame.copy(deep=True)

    def hardcode_column_dictionary(self):
        self.columns_name = {"Address Column": "Address", "Inequality Column": "Total"}

    def create_column_dictionary(self, type_column_name):
        self.columns_name = {"Address Column": "Address", "Inequality Column": type_column_name}

    def filter_columns_DataFrame(self):
            if self.columns_name["Inequality Column"] != "Total":
                self.DataFrame = self.DataFrame.filter(["Address", self.columns_name["Inequality Column"]])
                self.DataFrame = self.DataFrame[(self.DataFrame[list(self.DataFrame.columns)] != 0).all(axis=1)]

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
        # self.DataFrame = dataframe.create_count_transactions_bar_DataFrame(self.DataFrame)

        # #Note unmodifed_DataFrame is the original DataFrame which is going to be used to get the address_list
        # self.unmodifed_DataFrame = self.DataFrame.copy(deep=True)

    def hardcode_column_dictionary(self):
        pass
        # self.columns_name = {"Address Column": "Address", "Inequality Column": "Total"}

    def create_column_dictionary(self, type_column_name):
        pass
        # self.columns_name = {"Address Column": "Address", "Inequality Column": type_column_name}

    def filter_columns_DataFrame(self):
        pass
            # if self.columns_name["Inequality Column"] != "Total":
            #     self.DataFrame = self.DataFrame.filter(["Address", self.columns_name["Inequality Column"]])
            #     self.DataFrame = self.DataFrame[(self.DataFrame[list(self.DataFrame.columns)] != 0).all(axis=1)]

    def create_plotly(self):
        pass
        self.plotly_graph = volumne_graph.create_volume_graph(self.DataFrame)

    #! Overriding superclass method
    def create_badges(self):
        pass

    #! Overriding superclass method
    def create_address_list(self):
        pass

    #! Overriding superclass method
    def create_inequality_dictionary(self):
        pass
class Basic_Scatter_Graph(Graph_Factory):

    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)
        
    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        
        #Note unmodifed_DataFrame is the original DataFrame which is going to be used to get the address_list
        self.unmodifed_DataFrame = self.DataFrame.copy(deep=True)

    def hardcode_column_dictionary(self):
        self.columns_name = {"Address Column": "Buyer", "Inequality Column": "ETH"}

    def create_column_dictionary(self, type_column_name):
        self.columns_name = {"Address Column": type_column_name, "Inequality Column": "ETH"}

    def filter_columns_DataFrame(self):
        self.DataFrame = self.DataFrame.filter(["Date", "Hash", "ETH", self.columns_name["Address Column"]])

    def create_plotly(self):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.DataFrame, self.columns_name["Address Column"])

class Heatmap_Graph(Graph_Factory):
    
    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)

    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        self.axes_dictionary = heatmap_dataframe.create_heatmap_DataFrame(self.DataFrame)

    def hardcode_column_dictionary(self):
        pass

    def create_column_dictionary(self, type_column_name):
        pass

    def filter_columns_DataFrame(self):
        pass
            # if self.columns_name["Inequality Column"] != "Total":
            #     self.DataFrame = self.DataFrame.filter(["Address", self.columns_name["Inequality Column"]])
            #     self.DataFrame = self.DataFrame[(self.DataFrame[list(self.DataFrame.columns)] != 0).all(axis=1)]

    def create_plotly(self):
        self.plotly_graph = heatmap_graph.create_heatmap(self.axes_dictionary)

    #Note Overriding superclass method
    def create_badges(self):
        pass

    #Note Overriding superclass method
    def create_address_list(self):
        pass

    #Note Overriding superclass method
    def create_inequality_dictionary(self):
        pass

class Sunburst_Graph(Graph_Factory):
    
    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)

    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        self.DataFrame = sunburst_dataframe.create_sunburst_DataFrame(self.DataFrame)

    def hardcode_column_dictionary(self):
        pass

    def create_column_dictionary(self, type_column_name):
        pass

    def filter_columns_DataFrame(self):
        pass
            # if self.columns_name["Inequality Column"] != "Total":
            #     self.DataFrame = self.DataFrame.filter(["Address", self.columns_name["Inequality Column"]])
            #     self.DataFrame = self.DataFrame[(self.DataFrame[list(self.DataFrame.columns)] != 0).all(axis=1)]

    def create_plotly(self):
        self.plotly_graph = sunburst_graph.create_sunburst(self.DataFrame)

    #Note Overriding superclass method
    def create_badges(self):
        pass

    #Note Overriding superclass method
    def create_address_list(self):
        pass

    #Note Overriding superclass method
    def create_inequality_dictionary(self):
        pass