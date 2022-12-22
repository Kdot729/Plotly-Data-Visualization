import backend.general_functions as general_functions
import backend.bar.dataframe as dataframe
import backend.bar.graph as bar_graph
import backend.scatter.graph as scatter_graph
import backend.event as event
from abc import ABC, abstractmethod
from datetime import date
from flask import render_template
class Graph_Factory(ABC):

    def __init__(self):
        pass
        
    #Note This will chose which graph object to instantiate 
    @staticmethod
    def build_graph(specificity):
        if specificity == "basic":
            return Basic_Scatter_Graph()
        elif specificity == "count_transactions":
            return Count_Bar_Graph()

    @abstractmethod
    def find_filepath(self):
        pass
    
    @abstractmethod
    def hardcode_column_dictionary(self):
        pass

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
    def create_plotly(self, graph_type):
        pass

    @abstractmethod
    def get_template(self):
        pass

    @abstractmethod
    def hardcode_create_plotly(self):
        pass
    
    def create_badges(self):
        self.badges = general_functions.create_badges(self.columns_name["Address Column"], self.DataFrame)
    def create_address_list(self):
        #Note Using DataFrame instead of graph_DataFrame because DataFrame contains all the address. Allowing them to select multiple addresses
        self.address_list = general_functions.sort_descending_and_drop_duplicates_list(self.unmodifed_DataFrame, self.columns_name["Address Column"])

    def convert_JSON(self):
        self.graphJSON = general_functions.convert_Graph_to_JSON(self.plotly_graph)

    def create_inequality_dictionary(self):
        self.inequality_dictionary = general_functions.sort_Inequality_List(self.DataFrame, self.columns_name["Inequality Column"])

    def send_to_frontend(self, id_dropdown):
        if (id_dropdown == "Type"):
            return {"JSON Graph": self.graphJSON, 
            "Address List": self.address_list,
            "Badges": self.badges,
            "Descending List": self.inequality_dictionary["Descending List"],
            "Ascending List": self.inequality_dictionary["Ascending List"]}
        else:
            return {"JSON Graph": self.graphJSON, "Address List": self.address_list, "Badges": self.badges}


class Count_Bar_Graph(Graph_Factory):
    
    def __init__(self):
        pass

    def find_filepath(self):
        self.filepath = f"graph/bar/count_transactions.html"

    def hardcode_column_dictionary(self):
        self.columns_name = {"Address Column": "Address", "Inequality Column": "Total"}
        
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

    def hardcode_create_plotly(self):
        self.plotly_graph = bar_graph.create_count_transactions_graph(self.DataFrame, "Total")

    def create_plotly(self, graph_type):
        self.plotly_graph = bar_graph.create_count_transactions_graph(self.DataFrame, graph_type)

    def get_template(self):
        return render_template(template_name_or_list = self.filepath,
                            graphJSON=self.graphJSON, 
                            address_list=self.address_list,
                            inequality_dictionary=self.inequality_dictionary,
                            badges = self.badges)
class Basic_Scatter_Graph(Graph_Factory):

    def __init__(self):
        pass

    def find_filepath(self):
        self.filepath = f"graph/scatter/basic.html"

    def hardcode_column_dictionary(self):
        self.columns_name = {"Address Column": "Buyer", "Inequality Column": "ETH"}

    def create_DataFrame(self, tool):
        self.DataFrame = super().create_DataFrame(tool)
        #Note unmodifed_DataFrame is the original DataFrame which is going to be used to get the address_list
        self.unmodifed_DataFrame = self.DataFrame.copy(deep=True)


    def create_column_dictionary(self, type_column):
        self.columns_name = {"Address Column": type_column, "Inequality Column": "ETH"}

    def filter_columns_DataFrame(self, type_column_name):
        self.DataFrame = self.DataFrame.filter(["Date", "Hash", "ETH", type_column_name])

    def hardcode_create_plotly(self):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.DataFrame, "Buyer")

    def create_plotly(self, graph_type):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.DataFrame, graph_type)

    def get_template(self):
        return render_template(template_name_or_list = self.filepath,
                            graphJSON=self.graphJSON, 
                            address_list=self.address_list,
                            inequality_dictionary=self.inequality_dictionary,
                            date_dictionary={"Min Date": '2021-10-08',
                   "Max Date": date.today() },
                            badges = self.badges)

        