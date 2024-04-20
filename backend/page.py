from backend.factory.superclass import Graph_Factory

def initial_page_render(graph, specificity, tool):
    
    #Note Graph_Factory is abstract so you can't call Graph_Factory() by itself thats why it's chained with build_graph
    graph = Graph_Factory.build_graph(graph, specificity, tool)
    graph.create_DataFrame()
    graph.create_plotly()
    graph.convert_JSON()
    return graph.initialize_template()
