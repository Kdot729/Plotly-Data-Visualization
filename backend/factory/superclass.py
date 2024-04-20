import backend.general_functions as general_functions
from datetime import date
import backend.event as event
from abc import ABC, abstractmethod
from flask import render_template

class Graph_Factory(ABC):

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
            return subclass.Sunburst_Graph(graph, specificity, tool)

    @abstractmethod
    def find_filepath(self):
        return f"graph/{self.graph}/{self.specificity}.html"

    @abstractmethod
    def create_plotly(self, graph_type):
        pass

    def initialize_template(self):
        return render_template(template_name_or_list=self.filepath, graphJSON=self.graphJSON)

    def create_DataFrame(self):
        return general_functions.create_basic_DataFrame(self.tool)

    def sort_DataFrame(self, dictionary):
        self.DataFrame = event.sort_new_DataFrame(dictionary, self.DataFrame, self.columns_name)
    
    def convert_JSON(self):
        self.graphJSON = general_functions.convert_Graph_to_JSON(self.plotly_graph)



        