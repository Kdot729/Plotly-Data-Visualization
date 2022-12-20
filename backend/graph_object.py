import backend.general_functions as general_functions
import backend.bar.dataframe as dataframe
import backend.bar.graph as bar_graph
import backend.scatter.graph as scatter_graph
import pandas as panda

class Graph:
    #Note unmodifed_DataFrame is an unmodified version which is going to be used to get the address_list
    def __init__(self, specificity):
        self.specificity = specificity


    def create_DataFrame(self, tool):
        base_DataFrame = general_functions.create_basic_DataFrame(tool)
        if self.specificity == "basic":
            self.DataFrame = base_DataFrame
            self.unmodifed_DataFrame = base_DataFrame
        elif self.specificity == "count transactions":
            self.DataFrame = dataframe.create_count_transactions_bar_DataFrame(base_DataFrame)
            self.unmodifed_DataFrame = dataframe.create_count_transactions_bar_DataFrame(base_DataFrame)
            
    def create_column_dictionary(self, type_column):
        if self.specificity == "basic":
            self.columns_name = {"Address Column": type_column, "Inequality Column": "ETH"}

        elif self.specificity == "count transactions":
            self.columns_name = {"Address Column": "Address", "Inequality Column": type_column}


    def filter_columns_DataFrame(self, type_column_name):
        if self.specificity == "basic":
                self.DataFrame = self.DataFrame.filter(["Date", "Hash", "ETH", type_column_name])


        elif self.specificity == "count transactions":
                if type_column_name != "Total":
                        self.DataFrame = self.DataFrame.filter(["Address", type_column_name])
                        self.DataFrame = self.DataFrame[(self.DataFrame[list(self.DataFrame.columns)] != 0).all(axis=1)]

    def use_plotly(self, graph_type):
        if self.specificity == "basic":
            self.plotly_graph = scatter_graph.create_scatter_graph(self.DataFrame, graph_type)
        elif self.specificity == "count transactions":
            self.plotly_graph = bar_graph.create_count_transactions_graph(self.DataFrame, graph_type)


    def create_badges(self):
        print("column name", self.columns_name["Address Column"])
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