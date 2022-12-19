import general_functions as general_functions
import bar.dataframe as dataframe
import bar.graph as bar_graph
import scatter.graph as scatter_graph
def create_DataFrame(specificity, tool):
    basic_DataFrame = general_functions.create_basic_DataFrame(tool)
    if specificity == "basic":
        return basic_DataFrame
    elif specificity == "count transactions":
        return dataframe.create_count_transactions_bar_DataFrame(basic_DataFrame)

def create_column_dictionary(specificity, type_column):
    if specificity == "basic":
        return {"Address Column": type_column, "Inequality Column": "ETH"}
    elif specificity == "count transactions":
        return {"Address Column": "Address", "Inequality Column": type_column}

def create_graph(specificity, DataFrame, type_column):
    if specificity == "basic":
        return scatter_graph.create_scatter_graph(DataFrame, type_column)
    elif specificity == "count transactions":
        return bar_graph.create_count_transactions_graph(DataFrame, type_column)


     