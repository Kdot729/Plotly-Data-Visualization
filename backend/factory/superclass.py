import backend.general_functions as general_functions

import backend.event as event
from abc import ABC, abstractmethod

class Graph_Factory(ABC):

    def __init__(self):
        pass
        
    #Note This will chose which graph object to instantiate 
    @staticmethod
    def build_graph(specificity):
        
        #Note import statement needs to be inside this function to avoid circular imports
        import backend.factory.subclass as subclass

        if specificity == "basic":
            return subclass.Basic_Scatter_Graph()
        elif specificity == "count_transactions":
            return subclass.Count_Bar_Graph()

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




        