import json, plotly, pandas as panda
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
    def Create_Plotly(self):
        pass

    def initialize_template(self):
        return render_template(template_name_or_list="graph.html", graphJSON=self.graphJSON, tool=self.tool)

    def create_DataFrame(self):
        return panda.read_csv(f"csv/updated_{self.tool}_transactions.csv", names=('Date', 'Hash', 'ETH', 'Seller', 'Buyer')) 
    
    def Convert_Plotly_to_JSON(self):
        self.graphJSON = json.dumps(obj=self.plotly_graph, cls=plotly.utils.PlotlyJSONEncoder) 



        