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
    return graph.initialize_template()
