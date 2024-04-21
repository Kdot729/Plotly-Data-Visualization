from backend.factory.superclass import Graph_Factory

def Render_Graph(Graph_Name, Tool):
    
    #Note Graph_Factory is abstract so you can't call Graph_Factory() by itself thats why it's chained with build_graph
    graph = Graph_Factory.build_graph(Graph_Name, Tool)
    graph.create_DataFrame()
    graph.Create_Plotly()
    graph.Convert_Plotly_to_JSON()
    return graph.Render_Graph()
