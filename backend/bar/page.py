from flask import render_template
import backend.bar.dataframe as dataframe
import backend.bar.event as event 
import backend.bar.graph as graph


                   
def initial_page_render(tool):  

    page_filepath =  f"graph/bar/count_transactions.html"

    DataFrame = dataframe.create_DataFrame(tool)

    print("path",page_filepath)

    DataFrame = dataframe.create_count_transactions_bar_DataFrame(DataFrame)
    column_dictionary = {"Address": "Address", "Inequality": "Total"}
    plotly_graph = graph.create_count_transactions_graph(DataFrame)

    address_list = dataframe.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address"])
    inequality_dictionary = dataframe.sort_Inequality_List(DataFrame, column_dictionary["Inequality"])
    # #FIXME Need to look at convert_Graph_to_JSON()
    graphJSON = graph.convert_Graph_to_JSON(plotly_graph)
    return render_template(template_name_or_list = page_filepath,
                            graphJSON=graphJSON, 
                            address_list=address_list,
                            inequality_dictionary=inequality_dictionary)


def page_rerender(frontend_dictionary):

    DataFrame = dataframe.create_DataFrame(frontend_dictionary["Tool"])

    DataFrame = dataframe.create_count_transactions_bar_DataFrame(DataFrame)
    column_dictionary = {"Address": "Address", "Inequality": "Total"}
    graph_DataFrame = event.sort_new_DataFrame(frontend_dictionary, DataFrame, column_dictionary)
    plotly_graph = graph.create_count_transactions_graph(graph_DataFrame)

    address_list = dataframe.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address"])
    graphJSON = graph.convert_Graph_to_JSON(plotly_graph)

    return {"JSON Graph": graphJSON, "Address List": address_list}
