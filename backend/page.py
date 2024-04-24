from backend.factory.graph.superclass import Graph_Factory

def Render_Graph(Graph_Name, Tool):
    
    Chosen_Graph = Graph_Factory.Choose_Graph(Graph_Name, Tool)
    Chosen_Graph.Create_Plotly()
    Chosen_Graph.Convert_Plotly_to_JSON()
    return Chosen_Graph.Render_Graph()
