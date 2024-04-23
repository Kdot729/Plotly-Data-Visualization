
import backend.dataframe.transaction as Transaction_Dataframe, backend.graph.transaction as Transaction_Plotly
from backend.factory.superclass import Graph_Factory
import backend.graph.scatter as scatter_graph
import backend.dataframe.heatmap as heatmap_dataframe, backend.graph.heatmap as heatmap_graph
import backend.dataframe.sunburst as sunburst_dataframe, backend.graph.sunburst as sunburst_graph
import plotly.express as plotlyX
class Transaction(Graph_Factory):
    
    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)

    def create_DataFrame(self):
        super().create_DataFrame()
        self.Dataframe = Transaction_Dataframe.Create_Transaction_Dataframe(self.Dataframe)

    def Create_Plotly(self):
        self.plotly_graph = Transaction_Plotly.Create_Transaction_Graph(self.Dataframe, self.columns_name["Inequality Column"])

class Volume(Graph_Factory):
    
    Day_Column = "Day"

    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)

    def create_DataFrame(self):
        super().create_DataFrame()
        self.Truncate_Timestamp()
        self.Sum_Grouped_ETH()
        self.Reset_Dataframe_Index()
        self.Seperate_Date_Into_Lists("%A", "%b", "%Y")
        self.Insert_Date_Lists_into_Dataframe()
        self.Dataframe = self.Group_By_and_Sum([self.Day_Column, self.Month_Year_Column], False)

    def Insert_Date_Lists_into_Dataframe(self):
        self.Dataframe.insert(2, self.Day_Column, self.Formatted_Day_List, True)
        self.Dataframe.insert(3, self.Month_Year_Column, self.Formatted_Year_and_Month_List, True)

    def Create_Plotly(self):

        #Note Need to convert "Month Year" to a list to pass into "category_orders" because the y-axis is bugged. For some reason "February 2022" doesn't appear after "January 2022"
        #Note Reverse the list so the start of trading is at the bottom
        y_axis = (self.Dataframe[self.Month_Year_Column].tolist())[::-1]

        self.plotly_graph = plotlyX.bar(self.Dataframe, 
                        x=self.ETH_Column, 
                        y=self.Month_Year_Column, 
                        color=self.Day_Column, 
                        orientation='h',
                        category_orders={
                                #Note Reorder the horizontal bars so "Monday" is first and "Sunday" is last
                                self.Day_Column: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],

                                #Note This is to fix the y-axis because "February" is bugged
                                self.Month_Year_Column: y_axis
                                })

        #Note Create title for graph and center it
        self.plotly_graph.update_layout(title_text="Volume", title_x=0.5)

        self.plotly_graph.update_layout(legend={
                        #Note Change position of legend to be inside the graph
                        "yanchor": "top",
                        "y": 1,
                        "xanchor":"right",
                        "x": 1,

                        #Note Styling the legend box
                        "bgcolor": "#e5ecf6",
                        "bordercolor": "black",
                        "borderwidth": 1
                        })
        self.plotly_graph.update_layout(width=1580, 
                            height=750)

        self.plotly_graph

class Scatter(Graph_Factory):

    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)
        
    def create_DataFrame(self):
        super().create_DataFrame()

    def Create_Plotly(self):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.Dataframe)

class Heatmap(Graph_Factory):
    
    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)

    def create_DataFrame(self):
        super().create_DataFrame()
        self.Truncate_Timestamp()
        self.Sum_Grouped_ETH()
        self.Reset_Dataframe_Index()
        self.Seperate_Date_Into_Lists("%w", "%m", "%Y")
        self.Insert_Date_Lists_into_Dataframe()
        self.Dataframe = self.Group_By_and_Sum([self.Year_Column, self.Month_Number_Column, self.Weekday_Number_Column, self.Month_Year_Column], False)
        self.axes_dictionary = heatmap_dataframe.create_heatmap_DataFrame(self.Dataframe)

    def Create_Plotly(self):
        self.plotly_graph = heatmap_graph.Create_Heatmap_Graph(self.axes_dictionary)

class Sunburst(Graph_Factory):
    
    def __init__(self, Graph_Name, Tool):
        super().__init__(Graph_Name, Tool)

    def create_DataFrame(self):
        super().create_DataFrame()
        self.Truncate_Timestamp()
        self.Sum_Grouped_ETH()
        self.Reset_Dataframe_Index()
        self.Seperate_Date_Into_Lists("%w", "%m", "%Y")
        self.Insert_Date_Lists_into_Dataframe()
        Year_Dataframe = self.Group_By_and_Sum(self.Year_Column)
        Month_Year_Dataframe = self.Group_By_and_Sum(self.Month_Year_Column)
        self.Dataframe = sunburst_dataframe.create_sunburst_DataFrame(Year_Dataframe, Month_Year_Dataframe, self.Dataframe)

    def Create_Plotly(self):
        self.plotly_graph = sunburst_graph.Create_Sunburst_Graph(self.Dataframe)