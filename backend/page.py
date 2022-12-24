from backend.factory.superclass import Graph_Factory

def initial_page_render(graph, specificity, tool):
    #Note Graph_Factory is abstract so you can't call Graph_Factory() by itself thats why it's chained with build_graph
    graph = Graph_Factory.build_graph(graph, specificity, tool)
    graph.find_filepath()
    graph.create_DataFrame()
    graph.hardcode_column_dictionary()
    graph.create_plotly()
    graph.create_badges()
    graph.create_address_list()
    graph.convert_JSON()
    graph.create_inequality_dictionary()
    return graph.get_template()

def page_rerender(frontend_dictionary):
    print("len", len(frontend_dictionary))
    graph = Graph_Factory.build_graph(frontend_dictionary["Graph"], frontend_dictionary['Specificity'], frontend_dictionary["Tool"])
    graph.create_DataFrame()
    graph.create_column_dictionary(frontend_dictionary["Type"])
    graph.filter_columns_DataFrame()
    graph.sort_DataFrame(frontend_dictionary)

    graph.create_plotly()

    graph.create_badges()

    graph.create_address_list()
    graph.convert_JSON()
    graph.create_inequality_dictionary()
    return graph.send_to_frontend(frontend_dictionary["ID of Dropdown"])

