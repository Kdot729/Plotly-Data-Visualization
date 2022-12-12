from flask import render_template
import backend.general_functions as general_functions
import backend.bar.event as event 
import backend.bar.graph as graph
import backend.bar.dataframe as dataframe


                   
def initial_page_render(tool):  

    page_filepath =  f"graph/bar/count_transactions.html"

    DataFrame = general_functions.create_DataFrame(tool)

    DataFrame = dataframe.create_count_transactions_bar_DataFrame(DataFrame)

    column_dictionary = {"Address Column": "Address", "Inequality Column": "Total"}

    plotly_graph = graph.create_count_transactions_graph(DataFrame)

    address_list = general_functions.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address Column"])

    inequality_dictionary = general_functions.sort_Inequality_List(DataFrame, column_dictionary["Inequality Column"])


    graphJSON = general_functions.convert_Graph_to_JSON(plotly_graph)

    return render_template(template_name_or_list = page_filepath,
                            graphJSON=graphJSON, 
                            address_list=address_list,
                            inequality_dictionary=inequality_dictionary)


def page_rerender(frontend_dictionary):

    DataFrame = general_functions.create_DataFrame(frontend_dictionary["Tool"])

    DataFrame = dataframe.create_count_transactions_bar_DataFrame(DataFrame)

    column_dictionary = {"Address Column": "Address", "Inequality Column": "Total"}

    graph_DataFrame = event.sort_new_DataFrame(frontend_dictionary, DataFrame, column_dictionary)

    plotly_graph = graph.create_count_transactions_graph(graph_DataFrame)
    
    address_list = general_functions.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address Column"])
    
    graphJSON = general_functions.convert_Graph_to_JSON(plotly_graph)

    return {"JSON Graph": graphJSON, "Address List": address_list}
