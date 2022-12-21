import backend.graph_factory as graph_factory





def page_rerender(frontend_dictionary):
    graph = graph_factory.Graph_Factory.build_graph(frontend_dictionary['Specificity'])
    graph.create_DataFrame(frontend_dictionary["Tool"])
    graph.create_column_dictionary(frontend_dictionary["Type"])
    graph.filter_columns_DataFrame(frontend_dictionary["Type"])
    graph.sort_DataFrame(frontend_dictionary)

    graph.use_plotly(frontend_dictionary["Type"])

    graph.create_badges()

    graph.create_address_list()
    graph.convert_JSON()


    return graph.send_to_frontend(frontend_dictionary["ID of Dropdown"])

