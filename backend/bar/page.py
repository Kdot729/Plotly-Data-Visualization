from flask import render_template
import backend.general_functions as general_functions
import backend.event as event 
import backend.bar.graph as graph
import backend.bar.dataframe as dataframe


                   
def initial_page_render(tool):  

    page_filepath =  f"graph/bar/count_transactions.html"

    DataFrame = general_functions.create_basic_DataFrame(tool)

    DataFrame = dataframe.create_count_transactions_bar_DataFrame(DataFrame)

    column_dictionary = {"Address Column": "Address", "Inequality Column": "Total"}
    badges = general_functions.create_badges(column_dictionary["Address Column"], DataFrame)

    #Note Harded coding the graph type because "Total" is the default value
    plotly_graph = graph.create_count_transactions_graph(DataFrame, "Total")

    
    address_list = general_functions.sort_descending_and_drop_duplicates_list(DataFrame, column_dictionary["Address Column"])

    inequality_dictionary = general_functions.sort_Inequality_List(DataFrame, column_dictionary["Inequality Column"])


    graphJSON = general_functions.convert_Graph_to_JSON(plotly_graph)

    return render_template(template_name_or_list = page_filepath,
                            graphJSON=graphJSON, 
                            address_list=address_list,
                            inequality_dictionary=inequality_dictionary,
                            badges = badges)