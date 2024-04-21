from backend.factory.superclass import Graph_Factory

def Render_Graph(Graph_Name, Tool):
    
    Chosen_Graph = Graph_Factory.build_graph(Graph_Name, Tool)
    Chosen_Graph.create_DataFrame()
    Chosen_Graph.Create_Plotly()
    Chosen_Graph.Convert_Plotly_to_JSON()
    return Chosen_Graph.Render_Graph()
