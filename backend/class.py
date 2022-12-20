impor

class Graph:

  def __init__(self, name, age):
    self.name = name
    self.age = age

def create_badges():
        badges = general_functions.create_badges(column_dictionary["Address Column"], graph_DataFrame)
    plotly_graph =  new_functions.create_graph(frontend_dictionary["Specificity"], graph_DataFrame, frontend_dictionary["Type"])
    #Note Using DataFrame instead of graph_DataFrame because DataFrame contains all the address. Allowing them to select multiple addresses
    address_list = general_functions.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address Column"])
    graphJSON = general_functions.convert_Graph_to_JSON(plotly_graph)