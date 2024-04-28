import plotly.express as plotlyX
from backend.factory.graph.superclass import Graph_Factory

class Volume(Graph_Factory):

    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):

        #Note Need to convert "Month Year" to a list to pass into "category_orders" because the y-axis is bugged. For some reason "February 2022" doesn't appear after "January 2022"
        #Note Reverse the list so the start of trading is at the bottom
        y_axis = (self.Dataframe_Object._Dataframe[self.Dataframe_Object.Month_Year_Column].tolist())[::-1]

        self.Plotly_Graph = plotlyX.bar(self.Dataframe_Object._Dataframe, 
                                        x=self.Dataframe_Object.ETH_Column, 
                                        y=self.Dataframe_Object.Month_Year_Column, 
                                        color=self.Dataframe_Object.Day_Column, 
                                        orientation='h',
                                        category_orders={
                                                            #Note Reorder the horizontal bars so "Monday" is first and "Sunday" is last
                                                            self.Dataframe_Object.Day_Column: self.Dataframe_Object.Days_of_Week,

                                                            #Note This is to fix the y-axis because "February" is bugged
                                                            self.Dataframe_Object.Month_Year_Column: y_axis
                                                        }
                                        )

        self.Plotly_Graph.update_layout(width=self.Graph_Width, height=self.Graph_Height,
                                        
                                        #Note Create title for graph and center it
                                        title_text="Volume", title_x=0.5,
                                        
                                        legend={
                                                    #Note Change position of legend to be inside the graph
                                                    "yanchor": "top",
                                                    "y": 1,
                                                    "xanchor":"right",
                                                    "x": 1,

                                                    #Note Styling the legend box
                                                    "bgcolor": "#e5ecf6",
                                                    "bordercolor": "black",
                                                    "borderwidth": 1
                                                }
                                        )
