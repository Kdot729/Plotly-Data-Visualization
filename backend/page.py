from backend.factory.superclass import Graph_Factory

def Render_Graph(graph, specificity, tool):
    
    #Note Graph_Factory is abstract so you can't call Graph_Factory() by itself thats why it's chained with build_graph
    graph = Graph_Factory.build_graph(graph, specificity, tool)
    graph.create_DataFrame()
    graph.create_plotly()
    graph.Convert_Plotly_to_JSON()
    return graph.initialize_template()
