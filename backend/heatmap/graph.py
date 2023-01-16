import plotly.graph_objects as plotGO

#Note y_axis is the weekday as a number
weekday_names_list =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]

def create_heatmap(axes):

    figure = plotGO.Figure(
        data=plotGO.Heatmap(
                #Note The z-axis is the volume
                z=axes["z"],

                #Note X-axis is the month-year
                x=axes["x"],

                #Note Y-axis is the day of the week
                y=axes["y"],

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
    figure.update_yaxes(autorange="reversed")

    figure.update_layout(
                    title="Volume by Month",
                    title_x=0.5,
                    xaxis_title="Month-Year",
                    yaxis_title="Weekday",

                    #Note Get rid or margin to enlargen graph
                    margin=dict(l=0, r=0, t=25, b=0)
                    )

    figure.update_layout(width=1580, 
                        height=700)
    return figure
