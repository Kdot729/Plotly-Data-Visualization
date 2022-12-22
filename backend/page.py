from backend.factory.graph_object import Graph_Factory

def initial_page_render(specificity, tool):
    graph = Graph_Factory.build_graph(specificity)
    graph.find_filepath()
    graph.create_DataFrame(tool)
    graph.hardcode_column_dictionary()
    graph.hardcode_create_plotly()
    graph.create_badges()
    graph.create_address_list()
    graph.convert_JSON()
    return graph.get_template()

def page_rerender(frontend_dictionary):
    graph = Graph_Factory.build_graph(frontend_dictionary['Specificity'])
    graph.create_DataFrame(frontend_dictionary["Tool"])
    graph.create_column_dictionary(frontend_dictionary["Type"])
    graph.filter_columns_DataFrame(frontend_dictionary["Type"])
    graph.sort_DataFrame(frontend_dictionary)

    graph.create_plotly(frontend_dictionary["Type"])

    graph.create_badges()

    graph.create_address_list()
    graph.convert_JSON()

    return graph.send_to_frontend(frontend_dictionary["ID of Dropdown"])

