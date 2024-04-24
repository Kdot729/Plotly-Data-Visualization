from backend.factory.graph.superclass import Graph_Factory
import plotly.graph_objects as plotGO
class Heatmap(Graph_Factory):
    
    def __init__(self, Tool, Dataframe_Object):
        super().__init__(Tool, Dataframe_Object)

    def Create_Plotly(self):

        self.plotly_graph = plotGO.Figure(
        data=plotGO.Heatmap(
                #Note The z-axis is the volume
                z=self.Dataframe_Object.axes_dictionary["z"],

                #Note X-axis is the month-year
                x=self.Dataframe_Object.axes_dictionary["x"],

                #Note Y-axis is the day of the week
                y=self.Dataframe_Object.axes_dictionary["y"],

                colorscale='algae',

                #! For some reason texttemplate won't work on website but works when on local
                #Note Put the volume amount inside the each box
                texttemplate="%{z} ETH",

                #Note Changes on hover text. <br> makes it go to next line, don't space after <br>
                hovertemplate='Month-Year: %{x}<br>Weekday: %{y}<br>Volume: %{z} ETH<extra></extra>',

                #Note colorbar is the legend
                colorbar={"title": "Volume"}

                ))

        #Note Reverse data. Make Monday's data appear at the top of graph and Sunday's data at the bottom
        self.plotly_graph.update_yaxes(autorange="reversed")

        self.plotly_graph.update_layout(
                        title="Volume by Month",
                        title_x=0.5,
                        xaxis_title="Month-Year",
                        yaxis_title="Weekday",

                        #Note Get rid or margin to enlargen graph
                        margin=dict(l=0, r=0, t=25, b=0)
                        )

        self.plotly_graph.update_layout(width=1580, 
                            height=700)