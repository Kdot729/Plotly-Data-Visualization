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
    badges = general_functions.create_badges(column_dictionary["Address Column"], DataFrame)

    #Note Harded coding the graph type because "Total" is the default value
    plotly_graph = graph.create_count_transactions_graph(DataFrame, "Total")

    address_list = general_functions.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address Column"])

    inequality_dictionary = general_functions.sort_Inequality_List(DataFrame, column_dictionary["Inequality Column"])


    graphJSON = general_functions.convert_Graph_to_JSON(plotly_graph)

    return render_template(template_name_or_list = page_filepath,
                            graphJSON=graphJSON, 
                            address_list=address_list,
                            inequality_dictionary=inequality_dictionary,
                            badges = badges)


def page_rerender(frontend_dictionary):

    DataFrame = general_functions.create_DataFrame(frontend_dictionary["Tool"])

    DataFrame = dataframe.create_count_transactions_bar_DataFrame(DataFrame)

    
    column_dictionary = {"Address Column": "Address", "Inequality Column": "Total"}

    graph_DataFrame = event.sort_new_DataFrame(frontend_dictionary, DataFrame, column_dictionary)

    # print(graph_DataFrame)

    badges = general_functions.create_badges(column_dictionary["Address Column"], graph_DataFrame)
    plotly_graph = graph.create_count_transactions_graph(graph_DataFrame, frontend_dictionary["Type"])
    
    address_list = general_functions.sort_descending_and_drop_duplicates_list(graph_DataFrame, column_dictionary["Address Column"])
    print("address list",address_list)
    graphJSON = general_functions.convert_Graph_to_JSON(plotly_graph)

    #!---------------------------Delete

    #FIXME Problem with this is when passing ["Buy", "Sell"] into the graph because we dropped it
    # for DataFrame_column_name in DataFrame:
    #     print("column name", DataFrame_column_name)
    #     if ((DataFrame_column_name != "Address") and (DataFrame_column_name != frontend_dictionary["Type"])):
    #         DataFrame.drop([DataFrame_column_name], axis=1, inplace=True)
    # print(DataFrame)

     #!---------------------------Delete
    return {"JSON Graph": graphJSON, "Address List": address_list, "Badges": badges}
