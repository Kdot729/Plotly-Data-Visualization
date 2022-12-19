from flask import render_template
from datetime import date
import backend.general_functions as general_functions
import backend.event as event
import backend.scatter.graph as graph

#Note Beginning date of NFT. Default value for "Start Date" dropdown
#Note Gets current date. Default value for "End Date" dropdown
date_dictionary = {"Min Date": '2021-10-08',
                   "Max Date": date.today() }
                   
def initial_page_render(tool):  

    page_filepath =  f"graph/scatter/basic.html"

    DataFrame = general_functions.create_DataFrame(tool)
    
    column_dictionary = {"Address Column": "Buyer", "Inequality Column": "ETH"}
    badges = general_functions.create_badges(column_dictionary["Address Column"], DataFrame)
    
    plotly_graph = graph.create_scatter_graph(DataFrame, "Buyer")

    address_list = general_functions.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address Column"])

    inequality_dictionary = general_functions.sort_Inequality_List(DataFrame, column_dictionary["Inequality Column"])


    graphJSON = general_functions.convert_Graph_to_JSON(plotly_graph)

    return render_template(template_name_or_list = page_filepath,
                            graphJSON=graphJSON, 
                            address_list=address_list,
                            inequality_dictionary=inequality_dictionary,
                            date_dictionary=date_dictionary,
                            badges = badges)



def page_rerender(frontend_dictionary):

    DataFrame = general_functions.create_DataFrame(frontend_dictionary["Tool"])

    column_dictionary = {"Address Column": frontend_dictionary["Type"], "Inequality Column": "ETH"}
    
    graph_DataFrame = event.sort_new_DataFrame(frontend_dictionary, DataFrame, column_dictionary)
    badges = general_functions.create_badges(column_dictionary["Address Column"], graph_DataFrame)
    plotly_graph = graph.create_scatter_graph(graph_DataFrame, frontend_dictionary["Type"])

    #Note Using DataFrame instead of graph_DataFrame because DataFrame contains all the address. Allowing them to select multiple addresses
    address_list = general_functions.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address Column"])
    
    graphJSON = general_functions.convert_Graph_to_JSON(plotly_graph)

    return {"JSON Graph": graphJSON, "Address List": address_list, "Badges": badges}
