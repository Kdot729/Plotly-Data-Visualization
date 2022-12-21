import backend.general_functions as general_functions
import backend.bar.dataframe as dataframe
import backend.bar.graph as bar_graph
import backend.scatter.graph as scatter_graph
import backend.event as event
from backend.factory.superclass import Graph_Factory

class Count_Bar_Graph(Graph_Factory):
    def create_DataFrame(self, tool):
        self.DataFrame = super().create_DataFrame(tool)

        self.DataFrame = dataframe.create_count_transactions_bar_DataFrame(self.DataFrame)
        #Note unmodifed_DataFrame is the original DataFrame which is going to be used to get the address_list
        self.unmodifed_DataFrame = self.DataFrame.copy(deep=True)

    def create_column_dictionary(self, type_column):
        self.columns_name = {"Address Column": "Address", "Inequality Column": type_column}

    def filter_columns_DataFrame(self, type_column_name):
            if type_column_name != "Total":
                self.DataFrame = self.DataFrame.filter(["Address", type_column_name])
                self.DataFrame = self.DataFrame[(self.DataFrame[list(self.DataFrame.columns)] != 0).all(axis=1)]

    def use_plotly(self, graph_type):
        self.plotly_graph = bar_graph.create_count_transactions_graph(self.DataFrame, graph_type)

class Basic_Scatter_Graph(Graph_Factory):

    def create_DataFrame(self, tool):
        self.DataFrame = super().create_DataFrame(tool)
        #Note unmodifed_DataFrame is the original DataFrame which is going to be used to get the address_list
        self.unmodifed_DataFrame = self.DataFrame.copy(deep=True)

    def create_column_dictionary(self, type_column):
        self.columns_name = {"Address Column": type_column, "Inequality Column": "ETH"}

    def filter_columns_DataFrame(self, type_column_name):
        self.DataFrame = self.DataFrame.filter(["Date", "Hash", "ETH", type_column_name])

    def use_plotly(self, graph_type):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.DataFrame, graph_type)