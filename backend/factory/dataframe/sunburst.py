from backend.factory.dataframe.superclass import Dataframe
import pandas as panda
from datetime import datetime 

class Sunburst(Dataframe):
    
    def __init__(self, Tool):
        super().__init__(Tool)
        self.Finish_Dataframe()

    def Finish_Dataframe(self):
        self.Truncate_Timestamp()
        self.Sum_Grouped_ETH()
        self.Reset_Dataframe_Index()
        self.Seperate_Date_Into_Lists("%w", "%m", "%Y")
        self.Insert_Date_Lists_into_Dataframe()
        self.Year_Dataframe = self.Group_By_and_Sum(self.Year_Column)
        self.Month_Year_Dataframe = self.Group_By_and_Sum(self.Month_Year_Column)
        self._Dataframe = self.Create_Sunburst_Dataframe()

    def Create_Sunburst_Dataframe(self):

        Year_Column = "Year"
        Month_Year_Column = "Month Year"
        Date_Column = "Date"
        ETH_Column = "ETH"

        Lowercase_Total = "total"

        Column_Key = "Column"
        Dataframe_Key = "Dataframe"

        Graph_Dataframe = panda.DataFrame(columns=["ID", "Parent", "Value", "Text"])

        #Note Doesn't matter which dataframe we sum
        Sum = self.Year_Dataframe[ETH_Column].sum()

        #Note This render the center of the sunburst
        #Important The ID (2nd index) has to be an empty string
        Graph_Dataframe.loc[0] = [Lowercase_Total, "", Sum, Lowercase_Total.upper()]

        Dataframe_Array =   [
                                {Dataframe_Key: self.Year_Dataframe, Column_Key: Year_Column},
                                {Dataframe_Key: self.Month_Year_Dataframe, Column_Key: Month_Year_Column},
                                {Dataframe_Key: self.Dataframe, Column_Key: Date_Column}
                            ]

        for Dictionary in Dataframe_Array:

            Dataframe_Column = Dictionary[Column_Key]

            for Index, Row in Dictionary[Dataframe_Key].iterrows():

                ETH_Value = Row[ETH_Column]
                Value = Row[Dataframe_Column]

                if Dataframe_Column == Year_Column:

                    Insert_Row = [Value, Lowercase_Total, ETH_Value, Value]

                elif Dataframe_Column == Month_Year_Column:

                    Abbreviated_Month = datetime.strptime(Value, '%Y-%m').strftime('%b')
                    #Note Slicing "Month Year" value
                    Insert_Row = [Value, Value[:4], ETH_Value, Abbreviated_Month]

                elif Dataframe_Column == Date_Column:    

                    Non_Zero_Padded_Day = datetime.strptime(Value, '%Y-%m-%d').strftime('%-d')
                    Nth_Day = f"{Non_Zero_Padded_Day}th"
                    #Note Slicing "Date" value
                    Insert_Row = [Value, Value[:7], ETH_Value, Nth_Day]

                Dataframe_Index = len(Graph_Dataframe.index)
                Graph_Dataframe.loc[Dataframe_Index] = Insert_Row

        return Graph_Dataframe