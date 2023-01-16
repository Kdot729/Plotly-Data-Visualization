import backend.general_functions as general_functions
from datetime import date
import backend.event as event
from abc import ABC, abstractmethod

class Graph_Factory(ABC):

    date_dictionary = {"Min Date": '2021-10-08',
                        "Max Date": date.today()}

    def __init__(self, graph, specificity, tool):
        self.graph = graph
        self.specificity = specificity
        self.tool = tool


        
    #Note This will chose which graph object to instantiate 
    @staticmethod
    def build_graph(graph, specificity, tool):
        
        #Note import statement needs to be inside this function to avoid circular imports
        import backend.factory.subclass as subclass

        if specificity == "basic":
            return subclass.Basic_Scatter_Graph(graph, specificity, tool)
        elif specificity == "count_transactions":
            return subclass.Count_Bar_Graph(graph, specificity, tool)
        elif specificity == "volume":
            return subclass.Volume_Bar_Graph(graph, specificity, tool)
        elif specificity == "heatmap":
            return subclass.Heatmap_Graph(graph, specificity, tool)
        elif specificity == "sunburst":
            return subclass.Heatmap_Graph(graph, specificity, tool)

    @abstractmethod
    def find_filepath(self):
        return f"graph/{self.graph}/{self.specificity}.html"

    @abstractmethod
    def create_plotly(self, graph_type):
        pass

    @abstractmethod
    def initialize_template(self):
        pass
    
    @abstractmethod
    def hardcode_column_dictionary(self):
        pass

    def create_DataFrame(self):
        return general_functions.create_basic_DataFrame(self.tool)

    @abstractmethod
    def create_column_dictionary(self, type_column):
        pass

    @abstractmethod
    def filter_columns_DataFrame(self, type_column_name):
        pass

    def sort_DataFrame(self, dictionary):
        # print("dictionary",dictionary)
        self.DataFrame = event.sort_new_DataFrame(dictionary, self.DataFrame, self.columns_name)
    
    def create_badges(self):
        self.badges = general_functions.create_badges(self.columns_name["Address Column"], self.DataFrame)

    def create_address_list(self):
        #Note Using DataFrame instead of graph_DataFrame because DataFrame contains all the address. Allowing them to select multiple addresses
        self.address_list = general_functions.sort_descending_and_drop_duplicates_list(self.unmodifed_DataFrame, self.columns_name["Address Column"])

    def convert_JSON(self):
        self.graphJSON = general_functions.convert_Graph_to_JSON(self.plotly_graph)

    def create_inequality_dictionary(self):
        self.inequality_dictionary = general_functions.sort_Inequality_List(self.DataFrame, self.columns_name["Inequality Column"])

    def rerender_template(self, dropdown_id):
        if (dropdown_id == "Type"):
            return {"JSON Graph": self.graphJSON, 
            "Address List": self.address_list,
            "Badges": self.badges,
            "Descending List": self.inequality_dictionary["Descending List"],
            "Ascending List": self.inequality_dictionary["Ascending List"]}
        elif (dropdown_id != "Type"):
            return {"JSON Graph": self.graphJSON, "Address List": self.address_list, "Badges": self.badges}



        