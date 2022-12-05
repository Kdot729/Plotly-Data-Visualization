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


    if Graph == "scatter":
        if Specificity == "basic":
            address_column_name = "Buyer"
            inequality_column_name = "ETH"
            plotly_graph = graph_functions.create_scatter_graph(DataFrame, "Buyer")
            
    elif Graph == "bar":
        if Specificity == "count_transactions":
            DataFrame = count_transactions_sort.create_count_transactions_bar_DataFrame(DataFrame)
            address_column_name = "Address"
            inequality_column_name = "Transaction Count"
            plotly_graph = count_transactions_graph.create_count_transactions_graph(DataFrame)

    address_list = generic_sort.sort_Address_List(DataFrame, address_column_name)["Address List"]
    inequality_dictionary = generic_sort.sort_Inequality_List(DataFrame, inequality_column_name)
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
    if frontend_dictionary["Graph"] == "scatter":
        if frontend_dictionary["Specificity"] == "basic":
            DataFrame = generic_listener.sort_new_DataFrame(frontend_dictionary, DataFrame)
            plotly_graph = graph_functions.create_scatter_graph(DataFrame, "Buyer")
            
            
    elif frontend_dictionary["Graph"] == "bar":
        if frontend_dictionary["Specificity"] == "count_transactions":
            DataFrame = generic_listener.sort_new_DataFrame(frontend_dictionary, DataFrame)
            plotly_graph = count_transactions_graph.create_count_transactions_graph(DataFrame)
    graphJSON = graph_functions.convert_Graph_to_JSON(plotly_graph)
    return {"JSON Graph": graphJSON}



