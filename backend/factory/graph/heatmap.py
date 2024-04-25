from backend.factory.graph.superclass import Graph_Factory
import plotly.graph_objects as plotGO
class Heatmap(Graph_Factory):
    
    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):

        self.Plotly_Graph = plotGO.Figure(
            data=plotGO.Heatmap(
                    #Note The z-axis is the volume
                    z=self.Dataframe_Object.axes_dictionary["z"],

                    #Note X-axis is the month-year
                    x=self.Dataframe_Object.axes_dictionary["x"],

                    #Note Y-axis is the day of the week
                    y=self.Dataframe_Object.axes_dictionary["y"],

                    colorscale='algae',

                    #Note Changes on hover text. <br> makes it go to next line, don't space after <br>
                    hovertemplate='Month-Year: %{x}<br>Day of Week: %{y}<br>Volume: %{z} ETH<extra></extra>',

                    #Note colorbar is the legend
                    colorbar={"title": "Volume"}
                    ))

        #Note Reverse data. Make Monday's data appear at the top of graph and Sunday's data at the bottom
        self.Plotly_Graph.update_yaxes(autorange="reversed")

        self.Plotly_Graph.update_layout(
                                            title="Monthly Volume",
                                            title_x=0.5,
                                            xaxis_title="Month-Year",
                                            yaxis_title="Day of Week",

                                            width=self.Graph_Width, height=self.Graph_Height,

                                            #Note Get rid of margin to give more room for graph
                                            margin=dict(l=0, r=0, t=25, b=0)
                                        )
