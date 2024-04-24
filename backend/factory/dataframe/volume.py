
from backend.factory.dataframe.superclass import Dataframe

class Volume(Dataframe):

    Day_Column = "Day"

    def __init__(self, Tool):
        super().__init__(Tool)
        self.Finish_Dataframe()

    def Insert_Date_Lists_into_Dataframe(self):
        self._Dataframe.insert(2, self.Day_Column, self.Formatted_Day_List, True)
        self._Dataframe.insert(3, self.Month_Year_Column, self.Formatted_Year_and_Month_List, True)

    def Finish_Dataframe(self):
        self.Truncate_Timestamp()
        self.Sum_Grouped_ETH()
        self.Reset_Dataframe_Index()
        self.Seperate_Date_Into_Lists("%A", "%b", "%Y")
        self.Insert_Date_Lists_into_Dataframe()
        self._Dataframe = self.Group_By_and_Sum([self.Day_Column, self.Month_Year_Column], False)