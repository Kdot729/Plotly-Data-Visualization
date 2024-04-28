from backend.factory.dataframe.superclass import Dataframe
import pandas as panda
from datetime import datetime 

class Sunburst(Dataframe):
    
    def __init__(self, Tool):
        super().__init__(Tool)
        self.Finish_Dataframe()

    def Finish_Dataframe(self):
        self.Call_Multiple_Functions_for_Dataframe()
        self.Year_Dataframe = self.Group_By_and_Sum(self.Year_Column)
        self.Month_Year_Dataframe = self.Group_By_and_Sum(self.Month_Year_Column)
        self._Dataframe = self.Create_Sunburst_Dataframe()

    def Create_Sunburst_Dataframe(self):

        Total_Column = "Total"
        Column_Key = "Column"
        Dataframe_Key = "Dataframe"

        Graph_Dataframe = panda.DataFrame(columns=["ID", "Parent", "Value", "Text", "Color"])

        #Note Doesn't matter which dataframe we sum
        Sum = self.Year_Dataframe[self.ETH_Column].sum()

        #Note This render the center of the sunburst
        #Note Root node is white
        #Important The ID (2nd index) has to be an empty string
        Graph_Dataframe.loc[0] = [Total_Column.lower(), "", Sum, Total_Column, "#ffffff"]

        Dataframe_Array =   [
                                {Dataframe_Key: self.Year_Dataframe, Column_Key: self.Year_Column},
                                {Dataframe_Key: self.Month_Year_Dataframe, Column_Key: self.Month_Year_Column},
                                {Dataframe_Key: self.Dataframe, Column_Key: self.Date_Column}
                            ]

        for Dictionary in Dataframe_Array:

            Dataframe_Column = Dictionary[Column_Key]

            for Index, Row in Dictionary[Dataframe_Key].iterrows():

                ETH_Value = Row[self.ETH_Column]
                Value = Row[Dataframe_Column]

                if Dataframe_Column == self.Year_Column:
                    Parent_Value = Total_Column.lower()
                    Text_Value = Value

                elif Dataframe_Column == self.Month_Year_Column:
                    #Note Slicing "Month Year" value
                    Parent_Value = Value[:4]
                    Text_Value = datetime.strptime(Value, '%Y-%m').strftime('%b')

                elif Dataframe_Column == self.Date_Column:    
                    #Note Slicing "Date" value
                    Parent_Value = Value[:7]
                    Non_Zero_Padded_Day = datetime.strptime(Value, '%Y-%m-%d').strftime('%-d')
                    Text_Value = f"{Non_Zero_Padded_Day}th"

                #Note Adding discrete color for each sector
                if "2021" in Value:
                    Discrete_Color = "rgb(42, 244, 234)"
                elif "2022" in Value:
                    Discrete_Color = "rgb(208, 34, 231)"
                elif "2023" in Value:
                    Discrete_Color = "rgb(230, 37, 146)"
                
                Insert_Row = [Value, Parent_Value, ETH_Value, Text_Value, Discrete_Color]
                Dataframe_Index = len(Graph_Dataframe.index)
                Graph_Dataframe.loc[Dataframe_Index] = Insert_Row

        return Graph_Dataframe