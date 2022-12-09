from flask import render_template
import backend.sort.generic_sort as generic_sort
import backend.graph.graph_functions as graph_functions, backend.event_listener.generic_listener as generic_listener
import backend.sort.generic_sort as generic_sort, backend.graph.bar.count_transactions_graph as count_transactions_graph
import backend.sort.bar.count_transactions_sort as count_transactions_sort
from datetime import date


#Note Beginning date of NFT. Default value for "Start Date" dropdown
#Note Gets current date. Default value for "End Date" dropdown
date_dictionary = {"Min Date": '2021-10-08',
                   "Max Date": date.today() }
                   
def initial_page_render(Graph, Specificity, Tool):  

    page_filepath =  f"graph/{Graph}/{Specificity}.html"

    DataFrame = generic_sort.create_DataFrame(Tool)

    print("path",page_filepath)


    if Specificity == "basic":
        column_dictionary = {"Address": "Buyer", "Inequality": "ETH"}
        plotly_graph = graph_functions.create_scatter_graph(DataFrame, "Buyer")

    elif Specificity == "count_transactions":
        DataFrame = count_transactions_sort.create_count_transactions_bar_DataFrame(DataFrame)
        column_dictionary = {"Address": "Address", "Inequality": "Total"}
        plotly_graph = count_transactions_graph.create_count_transactions_graph(DataFrame)

    address_list = generic_sort.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address"])
    inequality_dictionary = generic_sort.sort_Inequality_List(DataFrame, column_dictionary["Inequality"])
    # #FIXME Need to look at convert_Graph_to_JSON()
    graphJSON = graph_functions.convert_Graph_to_JSON(plotly_graph)
    return render_template(template_name_or_list = page_filepath,
                            graphJSON=graphJSON, 
                            address_list=address_list,
                            inequality_dictionary=inequality_dictionary,
                            date_dictionary=date_dictionary)



def page_rerender(frontend_dictionary):

    DataFrame = generic_sort.create_DataFrame(frontend_dictionary["Tool"])

    #Note Scatter Works
    if frontend_dictionary["Specificity"] == "basic":
        column_dictionary = {"Address": frontend_dictionary["Address_Type"], "Inequality": "ETH"}
        graph_DataFrame = generic_listener.sort_new_DataFrame(frontend_dictionary, DataFrame, column_dictionary)
        plotly_graph = graph_functions.create_scatter_graph(graph_DataFrame, frontend_dictionary["Address_Type"])

    elif frontend_dictionary["Specificity"] == "count_transactions":
        DataFrame = count_transactions_sort.create_count_transactions_bar_DataFrame(DataFrame)
        column_dictionary = {"Address": "Address", "Inequality": "Total"}
        graph_DataFrame = generic_listener.sort_new_DataFrame(frontend_dictionary, DataFrame, column_dictionary)
        plotly_graph = count_transactions_graph.create_count_transactions_graph(graph_DataFrame)

    address_list = generic_sort.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address"])
    graphJSON = graph_functions.convert_Graph_to_JSON(plotly_graph)

    return {"JSON Graph": graphJSON, "Address List": address_list}



