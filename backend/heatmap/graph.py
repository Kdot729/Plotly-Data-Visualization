import plotly.graph_objects as plotGO

#Note y_axis is the weekday as a number
weekday_names_list =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]

def create_heatmap(DataFrame, z_axis, columns_list):

    figure = plotGO.Figure(
        data=plotGO.Heatmap(
                #Note The z-axis is the volume
                z=z_axis,

                #Note X-axis is the month-year
                x=columns_list,

                #Note Y-axis is the day of the week
                y=weekday_names_list,

                colorscale='algae',

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
    return figure
