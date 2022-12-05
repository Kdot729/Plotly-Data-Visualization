import plotly.express as plotly
import pandas as panda


def create_count_transactions_graph(DataFrame):

        figure = plotly.bar(DataFrame, 
                        x="Address", 
                        y="Transaction Count", 
                        color="Type",
                        color_discrete_map=
                                {
                                'Sell': 'red',
                                'Buy': 'green'
                                },
                        title="Total Count of Transactions")
        figure.update_layout(title_x=0.5)
        figure.update_xaxes(tickfont_size=7)

        return figure