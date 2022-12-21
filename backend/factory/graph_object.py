import backend.general_functions as general_functions
import backend.bar.dataframe as dataframe
import backend.bar.graph as bar_graph
import backend.scatter.graph as scatter_graph
import backend.event as event
from abc import ABC, abstractmethod


class Graph_Factory(ABC):
    
    def __init__(self):
        pass

    #Note This will choose which graph object to instantiate 
    @staticmethod
    def build_graph(specificity):
        if specificity == "basic":
            return Basic_Scatter_Graph()
        elif specificity == "count_transactions":
            return Count_Bar_Graph()

    def create_DataFrame(self, tool):
        return general_functions.create_basic_DataFrame(tool)

    @abstractmethod
    def create_column_dictionary(self, type_column):
        pass

    @abstractmethod
    def filter_columns_DataFrame(self, type_column_name):
        pass

    def sort_DataFrame(self, dictionary):
        # print("dictionary",dictionary)
        self.DataFrame = event.sort_new_DataFrame(dictionary, self.DataFrame, self.columns_name)

    @abstractmethod
    def use_plotly(self, graph_type):
        pass

    def create_badges(self):
        self.badges = general_functions.create_badges(self.columns_name["Address Column"], self.DataFrame)
    def create_address_list(self):
        #Note Using DataFrame instead of graph_DataFrame because DataFrame contains all the address. Allowing them to select multiple addresses
        self.address_list = general_functions.sort_descending_and_drop_duplicates_list(self.unmodifed_DataFrame, self.columns_name["Address Column"])

    def convert_JSON(self):
        self.graphJSON = general_functions.convert_Graph_to_JSON(self.plotly_graph)

    def send_to_frontend(self, id_dropdown):
        if (id_dropdown == "Type"):
            self.inequality_dictionary = general_functions.sort_Inequality_List(self.DataFrame, self.columns_name["Inequality Column"])
            return {"JSON Graph": self.graphJSON, 
            "Address List": self.address_list,
            "Badges": self.badges,
            "Descending List": self.inequality_dictionary["Descending List"],
            "Ascending List": self.inequality_dictionary["Ascending List"]}
        else:
            return {"JSON Graph": self.graphJSON, "Address List": self.address_list, "Badges": self.badges}

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

        