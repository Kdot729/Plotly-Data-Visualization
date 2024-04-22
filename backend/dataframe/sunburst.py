import pandas as panda
from datetime import datetime 

def create_sunburst_DataFrame(Year_Dataframe, Month_Year_Dataframe, Dataframe):

    Graph_Dataframe = panda.DataFrame(columns=['id', 'parent', 'value', "Text"])

    Dataframe_Array =   [
                            {"Dataframe": Year_Dataframe, "Column": "Year"},
                            {"Dataframe": Month_Year_Dataframe, "Column": "Month Year"},
                            {"Dataframe": Dataframe, "Column": "Date"}
                        ]

    for Dictionary in Dataframe_Array:

        Dataframe_Column = Dictionary["Column"]

        for Index, Row in Dictionary["Dataframe"].iterrows():

            ETH_Value = Row["ETH"]
            Value = Row[Dataframe_Column]

            if Dataframe_Column == "Year":

                Insert_Row = [Value, "Total", ETH_Value, Value]

            elif Dataframe_Column == "Month Year":

                Abbreviated_Month = datetime.strptime(Value, '%Y-%m').strftime('%b')
                #Note Slicing "Month Year" value
                Insert_Row = [Value, Value[:4], ETH_Value, Abbreviated_Month]

            elif Dataframe_Column == "Date":    

                Non_Zero_Padded_Day = datetime.strptime(Value, '%Y-%m-%d').strftime('%-d')
                Nth_Day = f"{Non_Zero_Padded_Day}th"
                #Note Slicing "Date" value
                Insert_Row = [Value, Value[:7], ETH_Value, Nth_Day]

            Dataframe_Index = len(Graph_Dataframe.index)
            Graph_Dataframe.loc[Dataframe_Index] = Insert_Row

    return Graph_Dataframe