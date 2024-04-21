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

        match Graph_Name:
            case "scatter":
                return subclass.Scatter(Graph_Name, Tool)
            case "transaction":
                return subclass.Transaction(Graph_Name, Tool)
            case "volume":
                return subclass.Volume(Graph_Name, Tool)
            case "heatmap":
                return subclass.Heatmap(Graph_Name, Tool)
            case "sunburst":
                return subclass.Sunburst(Graph_Name, Tool)

    @abstractmethod
    def Create_Plotly(self):
        pass

    def Render_Graph(self):
        return render_template(template_name_or_list="graph.html", graphJSON=self.graphJSON, tool=self.Tool)

    def create_DataFrame(self):
        return panda.read_csv(f"csv/updated_{self.Tool}_transactions.csv", names=('Date', 'Hash', 'ETH', 'Seller', 'Buyer')) 
    
    def Truncate_Timestamp(self):
        #Note Removing the timestamp from "Date"
        self.Dataframe["Date"] = self.Dataframe["Date"].str[:10]     

    def Convert_Plotly_to_JSON(self):
        self.graphJSON = json.dumps(obj=self.plotly_graph, cls=plotly.utils.PlotlyJSONEncoder) 



        