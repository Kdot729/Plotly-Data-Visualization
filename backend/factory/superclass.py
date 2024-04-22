import json, plotly, pandas as panda
from abc import ABC, abstractmethod
from flask import render_template
from datetime import datetime

class Graph_Factory(ABC):

    def __init__(self, Graph_Name, Tool):
        self.Graph_Name = Graph_Name
        self.Tool = Tool
        
    #Note Choose which graph object to instantiate 
    @staticmethod
    def Choose_Graph(Graph_Name, Tool):
        
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
        self.Dataframe = panda.read_csv(f"csv/updated_{self.Tool}_transactions.csv", names=('Date', 'Hash', 'ETH', 'Seller', 'Buyer')) 
    
    def Strftime(self, Date, Format_Date):
        return datetime.strptime(Date, '%Y-%m-%d').strftime(Format_Date)
    
    def Truncate_Timestamp(self):
        #Note Removing the timestamp from "Date"
        self.Dataframe["Date"] = self.Dataframe["Date"].str[:10]

    def Sum_Grouped_ETH(self):
        #Note Group by "Date" then sum their "ETH"
        self.Dataframe = self.Dataframe.groupby("Date").sum('ETH')

    def Reset_Dataframe_Index(self):
        #Note Make "Date" a column
        self.Dataframe = self.Dataframe.reset_index(level=0)

    def Seperate_Date_Into_Lists(self, Day_Format, Month_Format, Year_Format):

        self.Formatted_Day_List = []
        self.Formatted_Month_List = []
        self.Formatted_Year_List = []
        self.Formatted_Year_and_Month_List = []

        for Current_Date in self.Dataframe["Date"].tolist():

            #Note Get day of week day as an number (0-6). 0 being Sunday. 6 being Saturday
            Day = self.Strftime(Current_Date, Day_Format)

            #Note Day is a string
            if Day == "0":
                    Day = "7"

            #Note Get zero padded month
            Month = self.Strftime(Current_Date, Month_Format)

            #Note Get year with century as a decimal number
            Year = self.Strftime(Current_Date, Year_Format)

            self.Formatted_Day_List.append(Day)
            self.Formatted_Month_List.append(Month)
            self.Formatted_Year_List.append(Year)
            self.Formatted_Year_and_Month_List.append(f"{Year}-{Month}")

    #Note Only heatmap and sunburst use this function. Volume will override this function
    def Insert_Date_Lists_into_Dataframe(self):
        self.Dataframe.insert(2, "Year", self.Formatted_Year_List, True)
        self.Dataframe.insert(3, "Month Number", self.Formatted_Month_List, True)
        self.Dataframe.insert(4, "Weekday Number", self.Formatted_Day_List, True)
        self.Dataframe.insert(5, "Month Year", self.Formatted_Year_and_Month_List, True)
    
    def Group_By_and_Sum(self, Group_By_Columns, Boolean_Sort=True):
        self.Dataframe.groupby(Group_By_Columns, sort=Boolean_Sort).sum('ETH').reset_index()

    def Convert_Plotly_to_JSON(self):
        self.graphJSON = json.dumps(obj=self.plotly_graph, cls=plotly.utils.PlotlyJSONEncoder) 



        