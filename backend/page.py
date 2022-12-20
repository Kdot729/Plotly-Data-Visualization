import backend.graph_object as graph_object
import backend.bar.dataframe as dataframe


def page_rerender(frontend_dictionary):
    print("type", frontend_dictionary["Type"])
    graph = graph_object.Graph(frontend_dictionary["Specificity"])
    graph.create_DataFrame(frontend_dictionary["Tool"])
    graph.create_column_dictionary(frontend_dictionary["Type"])
    graph.filter_columns_DataFrame(frontend_dictionary["Type"])
    graph.use_plotly(frontend_dictionary["Type"])

    graph.create_badges()
    
    graph.create_address_list()
    graph.convert_JSON()
    print(graph.send_to_frontend(frontend_dictionary["ID of Dropdown"]))

    return graph.send_to_frontend(frontend_dictionary["ID of Dropdown"])


    # DataFrame = new_functions.create_DataFrame(frontend_dictionary["Specificity"], frontend_dictionary["Tool"])
    # DataFrame = dataframe.filter_columns_DataFrame(frontend_dictionary["Specificity"], DataFrame, frontend_dictionary["Type"])


    # column_dictionary = new_functions.create_column_dictionary(frontend_dictionary["Specificity"], frontend_dictionary["Type"])

    # graph_DataFrame = event.sort_new_DataFrame(frontend_dictionary, DataFrame, column_dictionary)



    # badges = general_functions.create_badges(column_dictionary["Address Column"], graph_DataFrame)
    # plotly_graph =  new_functions.create_graph(frontend_dictionary["Specificity"], graph_DataFrame, frontend_dictionary["Type"])
    # #Note Using DataFrame instead of graph_DataFrame because DataFrame contains all the address. Allowing them to select multiple addresses
    # address_list = general_functions.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address Column"])
    # graphJSON = general_functions.convert_Graph_to_JSON(plotly_graph)

    # # print(address_list)
    #     #Note id of "Type" gets a special condition because the inqualities could be different
    # #TODO Trying to repopulate inequality when "Type" is changed because they're not going to be the same
    # if (frontend_dictionary["ID of Dropdown"] == "Type"):
    #     inequality_dictionary = general_functions.sort_Inequality_List(DataFrame, column_dictionary["Inequality Column"])
    #     return {"JSON Graph": graphJSON, 
    #     "Address List": address_list,
    #     "Badges": badges,
    #     "Descending List": inequality_dictionary["Descending List"],
    #     "Ascending List": inequality_dictionary["Ascending List"]}
    # else:
    #     return {"JSON Graph": graphJSON, "Address List": address_list, "Badges": badges}
