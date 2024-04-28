
from backend.factory.dataframe.superclass import Dataframe
import pandas as panda

class Heatmap(Dataframe):

    def __init__(self, Tool):
        super().__init__(Tool)
        self.Finish_Dataframe()

    def Finish_Dataframe(self):
        self.Call_Multiple_Functions_for_Dataframe()
        self._Dataframe = self.Group_By_and_Sum([self.Year_Column, self.Month_Number_Column, self.Weekday_Number_Column, self.Month_Year_Column], False)
        self.axes_dictionary = self.Create_Heatmap_Dataframe()

    def Create_Heatmap_Dataframe(self):

        #Note Get the list of "Month Year" to use to reorder DataFrame columns
        List_of_Month_Years = self._Dataframe[self.Month_Year_Column].drop_duplicates().tolist()

        self._Dataframe = panda.pivot_table(self._Dataframe, 
                                        values=self.ETH_Column, 
                                        index=self.Weekday_Number_Column,
                                        columns=self.Month_Year_Column, 

                                        #Note If day of week doesn't have any volumne then fill it with 0
                                        fill_value=0)

        #Note Changing the column order so Oct-2021 is first
        self._Dataframe = self._Dataframe[List_of_Month_Years]

        #Note Put each row into a 2D array
        Monthly_Day_of_Week_Volume = self._Dataframe.values.tolist()

        return {"x": List_of_Month_Years, "y": self.Days_of_Week, "z": Monthly_Day_of_Week_Volume}
