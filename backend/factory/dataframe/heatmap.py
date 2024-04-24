
from backend.factory.dataframe.superclass import Dataframe
import pandas as panda

class Heatmap(Dataframe):

    def __init__(self, Tool):
        super().__init__(Tool)
        self.Finish_Dataframe()

    def Finish_Dataframe(self):
        self.Truncate_Timestamp()
        self.Sum_Grouped_ETH()
        self.Reset_Dataframe_Index()
        self.Seperate_Date_Into_Lists("%w", "%m", "%Y")
        self.Insert_Date_Lists_into_Dataframe()
        self._Dataframe = self.Group_By_and_Sum([self.Year_Column, self.Month_Number_Column, self.Weekday_Number_Column, self.Month_Year_Column], False)
        self.axes_dictionary = self.Create_Heatmap_Dataframe()

    def Create_Heatmap_Dataframe(self):

        #Note Get the list of "Month Year" to use to reorder DataFrame columns
        columns_list = self._Dataframe["Month Year"].drop_duplicates().tolist()

        self._Dataframe = panda.pivot_table(self._Dataframe, 
                                        values='ETH', 
                                        index=["Weekday Number"],
                                        columns=["Month Year"], 

                                        #Note If a weekday didn't have any volumne use a zero
                                        fill_value=0)


        #Note Changing the column order so Oct-2021 is first
        self._Dataframe = self._Dataframe[columns_list]

        #Note y_axis is the weekday as a number
        #Delete? This is variable is in the graph.py
        weekday_names_list =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]



        z_axis = []

        for index, row in self._Dataframe.iterrows():
                #Note Get all the values of a row and convert it to a list
                row_list = row.values.tolist()

                #Note Put the row_list into z_axis to make it a 2D array
                z_axis.append(row_list)

        return {"x": columns_list,"y": weekday_names_list, "z":z_axis}
