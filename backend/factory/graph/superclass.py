import json, plotly, pandas as panda
from abc import ABC, abstractmethod
from flask import render_template
from datetime import datetime

class Graph_Factory(ABC):

    Date_Column = "Date"
    ETH_Column = "ETH"
    Year_Column = "Year"
    Month_Number_Column = "Month Number"
    Weekday_Number_Column = "Weekday Number"
    Month_Year_Column = "Month Year"

    def __init__(self, Tool):
        self.Tool = Tool
        
    #Note Choose which graph object to instantiate 
    @staticmethod
    def Choose_Graph(Graph_Name, Tool):
        
        #Note import statement needs to be inside this function to avoid circular imports
        import backend.factory.graph.transaction as transaction
        import backend.factory.graph.sunburst as sunburst
        import backend.factory.graph.scatter as scatter
        import backend.factory.graph.volume as volume
        import backend.factory.graph.heatmap as heatmap
        import backend.factory.dataframe.scatter as Scatter_Dataframe
        import backend.factory.dataframe.heatmap as Heatmap_Dataframe

        match Graph_Name:
            case "scatter":
                return scatter.Scatter(Tool, Scatter_Dataframe.Scatter(Tool))
            case "transaction":
                return transaction.Transaction(Tool)
            case "volume":
                return volume.Volume(Tool)
            case "heatmap":
                return heatmap.Heatmap(Tool, Heatmap_Dataframe.Heatmap(Tool))
            case "sunburst":
                return sunburst.Sunburst(Tool)

    @abstractmethod
    def Create_Plotly(self):
        pass

    def Render_Graph(self):
        return render_template(template_name_or_list="graph.html", graphJSON=self.graphJSON, tool=self.Tool)

    def Convert_Plotly_to_JSON(self):
        self.graphJSON = json.dumps(obj=self.plotly_graph, cls=plotly.utils.PlotlyJSONEncoder) 



        