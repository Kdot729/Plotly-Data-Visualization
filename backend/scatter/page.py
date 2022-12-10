from flask import render_template
from datetime import date
import backend.scatter.dataframe as dataframe
import backend.scatter.event as event
import backend.scatter.graph as graph

#Note Beginning date of NFT. Default value for "Start Date" dropdown
#Note Gets current date. Default value for "End Date" dropdown
date_dictionary = {"Min Date": '2021-10-08',
                   "Max Date": date.today() }
                   
def initial_page_render(tool):  

    page_filepath =  f"graph/scatter/basic.html"

    DataFrame = dataframe.create_DataFrame(tool)

    print("path",page_filepath)

    column_dictionary = {"Address": "Buyer", "Inequality": "ETH"}
    plotly_graph = graph.create_scatter_graph(DataFrame, "Buyer")


    address_list = dataframe.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address"])
    inequality_dictionary = dataframe.sort_Inequality_List(DataFrame, column_dictionary["Inequality"])

    # #FIXME Need to look at convert_Graph_to_JSON()
    graphJSON = graph.convert_Graph_to_JSON(plotly_graph)
    return render_template(template_name_or_list = page_filepath,
                            graphJSON=graphJSON, 
                            address_list=address_list,
                            inequality_dictionary=inequality_dictionary,
                            date_dictionary=date_dictionary)



def page_rerender(frontend_dictionary):

    DataFrame = dataframe.create_DataFrame(frontend_dictionary["Tool"])

    column_dictionary = {"Address": frontend_dictionary["Address_Type"], "Inequality": "ETH"}
    graph_DataFrame = event.sort_new_DataFrame(frontend_dictionary, DataFrame, column_dictionary)
    plotly_graph = graph.create_scatter_graph(graph_DataFrame, frontend_dictionary["Address_Type"])


    address_list = dataframe.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address"])
    graphJSON = graph.convert_Graph_to_JSON(plotly_graph)

    return {"JSON Graph": graphJSON, "Address List": address_list}
