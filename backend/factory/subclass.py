
import backend.bar.dataframe as dataframe
from backend.factory.superclass import Graph_Factory
from flask import render_template
import backend.bar.graph as bar_graph
import backend.scatter.graph as scatter_graph
import backend.bar.volume.dataframe as volumne_dataframe, backend.bar.volume.graph as volumne_graph
class Count_Bar_Graph(Graph_Factory):
    
    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)

    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        self.DataFrame = dataframe.create_count_transactions_bar_DataFrame(self.DataFrame)

        #Note unmodifed_DataFrame is the original DataFrame which is going to be used to get the address_list
        self.unmodifed_DataFrame = self.DataFrame.copy(deep=True)

    def hardcode_column_dictionary(self):
        self.columns_name = {"Address Column": "Address", "Inequality Column": "Total"}

    def create_column_dictionary(self, type_column_name):
        self.columns_name = {"Address Column": "Address", "Inequality Column": type_column_name}

    def filter_columns_DataFrame(self):
            if self.columns_name["Inequality Column"] != "Total":
                self.DataFrame = self.DataFrame.filter(["Address", self.columns_name["Inequality Column"]])
                self.DataFrame = self.DataFrame[(self.DataFrame[list(self.DataFrame.columns)] != 0).all(axis=1)]

    def create_plotly(self):
        self.plotly_graph = bar_graph.create_count_transactions_graph(self.DataFrame, self.columns_name["Inequality Column"])

    def initialize_template(self):
        return render_template(template_name_or_list = self.filepath,
                            graphJSON=self.graphJSON, 
                            address_list=self.address_list,
                            inequality_dictionary=self.inequality_dictionary,
                            badges = self.badges)

class Volume_Bar_Graph(Graph_Factory):
    
    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)

    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        self.DataFrame = volumne_dataframe.create_volumne_DataFrame(self.DataFrame)
        # self.DataFrame = dataframe.create_count_transactions_bar_DataFrame(self.DataFrame)

        # #Note unmodifed_DataFrame is the original DataFrame which is going to be used to get the address_list
        # self.unmodifed_DataFrame = self.DataFrame.copy(deep=True)

    def hardcode_column_dictionary(self):
        pass
        # self.columns_name = {"Address Column": "Address", "Inequality Column": "Total"}

    def create_column_dictionary(self, type_column_name):
        pass
        # self.columns_name = {"Address Column": "Address", "Inequality Column": type_column_name}

    def filter_columns_DataFrame(self):
        pass
            # if self.columns_name["Inequality Column"] != "Total":
            #     self.DataFrame = self.DataFrame.filter(["Address", self.columns_name["Inequality Column"]])
            #     self.DataFrame = self.DataFrame[(self.DataFrame[list(self.DataFrame.columns)] != 0).all(axis=1)]

    def create_plotly(self):
        pass
        self.plotly_graph = volumne_graph.create_volume_graph(self.DataFrame)

    def initialize_template(self):
        return render_template(template_name_or_list = self.filepath,
                            graphJSON=self.graphJSON)

    #! Overriding superclass method
    def create_badges(self):
        pass

    #! Overriding superclass method
    def create_address_list(self):
        pass

    #! Overriding superclass method
    def create_inequality_dictionary(self):
        pass
class Basic_Scatter_Graph(Graph_Factory):

    def __init__(self, graph, specificity, tool):
        super().__init__(graph, specificity, tool)
        
    def find_filepath(self):
        self.filepath = super().find_filepath()

    def create_DataFrame(self):
        self.DataFrame = super().create_DataFrame()
        
        #Note unmodifed_DataFrame is the original DataFrame which is going to be used to get the address_list
        self.unmodifed_DataFrame = self.DataFrame.copy(deep=True)

    def hardcode_column_dictionary(self):
        self.columns_name = {"Address Column": "Buyer", "Inequality Column": "ETH"}

    def create_column_dictionary(self, type_column_name):
        self.columns_name = {"Address Column": type_column_name, "Inequality Column": "ETH"}

    def filter_columns_DataFrame(self):
        self.DataFrame = self.DataFrame.filter(["Date", "Hash", "ETH", self.columns_name["Address Column"]])

    def create_plotly(self):
        self.plotly_graph = scatter_graph.create_scatter_graph(self.DataFrame, self.columns_name["Address Column"])

    def initialize_template(self):
        return render_template(template_name_or_list = self.filepath,
                            graphJSON=self.graphJSON, 
                            address_list=self.address_list,
                            inequality_dictionary=self.inequality_dictionary,
                            date_dictionary=self.date_dictionary,
                            badges = self.badges)