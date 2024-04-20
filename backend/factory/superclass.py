import json, plotly, pandas as panda
from abc import ABC, abstractmethod
from flask import render_template

class Graph_Factory(ABC):

    def __init__(self, Graph_Name, Tool):
        self.Graph_Name = Graph_Name
        self.Tool = Tool
        
    #Note This will chose which graph object to instantiate 
    @staticmethod
    def build_graph(Graph_Name, Tool):
        
        #Note import statement needs to be inside this function to avoid circular imports
        import backend.factory.subclass as subclass

        if Graph_Name == "basic":
            return subclass.Basic_Scatter_Graph(Graph_Name, Tool)
        elif Graph_Name == "count_transactions":
            return subclass.Count_Bar_Graph(Graph_Name, Tool)
        elif Graph_Name == "volume":
            return subclass.Volume_Bar_Graph(Graph_Name, Tool)
        elif Graph_Name == "heatmap":
            return subclass.Heatmap_Graph(Graph_Name, Tool)
        elif Graph_Name == "sunburst":
            return subclass.Sunburst_Graph(Graph_Name, Tool)

    @abstractmethod
    def Create_Plotly(self):
        pass

    def initialize_template(self):
        return render_template(template_name_or_list="graph.html", graphJSON=self.graphJSON, tool=self.Tool)

    def create_DataFrame(self):
        return panda.read_csv(f"csv/updated_{self.Tool}_transactions.csv", names=('Date', 'Hash', 'ETH', 'Seller', 'Buyer')) 
    
    def Convert_Plotly_to_JSON(self):
        self.graphJSON = json.dumps(obj=self.plotly_graph, cls=plotly.utils.PlotlyJSONEncoder) 



        