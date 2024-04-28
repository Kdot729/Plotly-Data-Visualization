from abc import ABC, abstractmethod
import pandas as panda
from datetime import datetime

class Dataframe(ABC):

    Date_Column = "Date"
    ETH_Column = "ETH"
    Year_Column = "Year"
    Month_Number_Column = "Month Number"
    Weekday_Number_Column = "Weekday Number"
    Month_Year_Column = "Month Year"
    Days_of_Week =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
    
    def __init__(self, Tool):
        self.Tool = Tool
        self.Create_Dataframe()
        self.Set_Pandas_Options()

    @property
    def Dataframe(self): 
        return self._Dataframe
    
    def Create_Dataframe(self):
        self._Dataframe = panda.read_csv(f"csv/{self.Tool}.csv", names=(self.Date_Column, 'Hash', self.ETH_Column, 'Seller', 'Buyer'))

    def Strftime(self, Date, Format_Date):
        return datetime.strptime(Date, '%Y-%m-%d').strftime(Format_Date)
    
    def Truncate_Timestamp(self):
        #Note Removing the timestamp from self.Date_Column
        self._Dataframe[self.Date_Column] = self._Dataframe[self.Date_Column].str[:10]

    def Sum_Grouped_ETH(self):
        #Note Group by self.Date_Column then sum their "ETH"
        self._Dataframe = self._Dataframe.groupby(self.Date_Column).sum(self.ETH_Column)

    def Reset_Dataframe_Index(self):
        #Note Make self.Date_Column a column
        self._Dataframe = self._Dataframe.reset_index(level=0)

    def Seperate_Date_Into_Lists(self, Day_Format, Month_Format, Year_Format):

        self.Formatted_Day_List = []
        self.Formatted_Month_List = []
        self.Formatted_Year_List = []
        self.Formatted_Year_and_Month_List = []

        for Current_Date in self._Dataframe[self.Date_Column].tolist():

            #Note Get day of week day as an number (0-6). 0 being Sunday. 6 being Saturday
            Day = self.Strftime(Current_Date, Day_Format)

            #Note Day is a string
            if Day == "0":
                    Day = "7"

            #Note Get zero padded month
            Month = self.Strftime(Current_Date, Month_Format)

            #Note Get year with century as a decimal number
            Year = self.Strftime(Current_Date, Year_Format)

            self.Formatted_Day_List.append(Day)
            self.Formatted_Month_List.append(Month)
            self.Formatted_Year_List.append(Year)
            self.Formatted_Year_and_Month_List.append(f"{Year}-{Month}")

    #Note Only heatmap and sunburst use this function. Volume will override this function
    def Insert_Date_Lists_into_Dataframe(self):
        self._Dataframe.insert(2, self.Year_Column, self.Formatted_Year_List, True)
        self._Dataframe.insert(3, self.Month_Number_Column, self.Formatted_Month_List, True)
        self._Dataframe.insert(4, self.Weekday_Number_Column, self.Formatted_Day_List, True)
        self._Dataframe.insert(5, self.Month_Year_Column, self.Formatted_Year_and_Month_List, True)
    
    def Group_By_and_Sum(self, Group_By_Columns, Boolean_Sort=True):
        return self._Dataframe.groupby(Group_By_Columns, sort=Boolean_Sort).sum(self.ETH_Column).reset_index()
    
    def Call_Multiple_Functions_for_Dataframe(self, Day_Format="%w", Month_Format="%m", Year_Format="%Y"):
        self.Truncate_Timestamp()
        self.Sum_Grouped_ETH()
        self.Reset_Dataframe_Index()
        self.Seperate_Date_Into_Lists(Day_Format, Month_Format, Year_Format)
        self.Insert_Date_Lists_into_Dataframe()
    
    def Set_Pandas_Options(self):
        panda.set_option('display.max_rows', None)
        panda.set_option('display.max_columns', None)
        panda.set_option('display.width', None)
        panda.set_option('display.max_colwidth', None)