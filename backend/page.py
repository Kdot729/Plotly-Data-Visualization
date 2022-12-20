import backend.graph_object as graph_object





def page_rerender(frontend_dictionary):
    graph = graph_object.Graph(frontend_dictionary["Specificity"])
    graph.create_DataFrame(frontend_dictionary["Tool"])
    graph.create_column_dictionary(frontend_dictionary["Type"])
    graph.filter_columns_DataFrame(frontend_dictionary["Type"])
    graph.sort_DataFrame(frontend_dictionary)

    graph.use_plotly(frontend_dictionary["Type"])

    graph.create_badges()

    graph.create_address_list()
    graph.convert_JSON()


    return graph.send_to_frontend(frontend_dictionary["ID of Dropdown"])

