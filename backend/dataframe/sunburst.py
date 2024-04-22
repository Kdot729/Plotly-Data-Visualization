import pandas as panda
import datetime


def Insert_Into_Row(Graph_Dataframe, Looped_Dataframe, Dataframe_Column):

    for index, row in Looped_Dataframe.iterrows():
        ETH_Column = row["ETH"]

        if Dataframe_Column == "Year":
            Replace_Row = [row[Dataframe_Column], "Total", ETH_Column]
        elif Dataframe_Column == "Month Year":
            Replace_Row = [row[Dataframe_Column], row[Dataframe_Column][:4], ETH_Column]
        elif Dataframe_Column == "Date":
            Replace_Row = [row[Dataframe_Column], row[Dataframe_Column][:7], ETH_Column]

        Dataframe_Index = len(Graph_Dataframe.index)
        Graph_Dataframe.loc[Dataframe_Index] = Replace_Row
    
    return Graph_Dataframe

def create_sunburst_DataFrame(Year_Dataframe, Month_Year_Dataframe, Dataframe):

    Graph_Dataframe = panda.DataFrame(columns=['id', 'parent', 'value'])

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
                Insert_Row = [Value, "Total", ETH_Value]
            elif Dataframe_Column == "Month Year":
                #Note Slicing "Month Year" value
                Insert_Row = [Value, Value[:4], ETH_Value]
            elif Dataframe_Column == "Date":
                #Note Slicing "Date" value
                Insert_Row = [Value, Value[:7], ETH_Value]

            Dataframe_Index = len(Graph_Dataframe.index)
            Graph_Dataframe.loc[Dataframe_Index] = Insert_Row

    override_text = []

    substring_checker = "0"

    for index in Graph_Dataframe['id']:

        #Note If len 4 then it's the year
        if index == "Total":
            value == "Total"
        elif len(index) == 4:
            value = index


        #Note If len 7 then it's the year and month
        elif len(index) == 7:
            month = datetime.datetime.strptime(index, '%Y-%m').strftime('%b')
            value = month

        elif len(index) == 10:
            nth_day = datetime.datetime.strptime(index, '%Y-%m-%d').strftime('%d')
            #Note Check to see if "0" is in the string
            if substring_checker in nth_day:
                    #Note Remove the zero from the string
                    nth_day = nth_day.replace('0', '')
            value = f"{nth_day}th "

        override_text.append(value)

    #Note Created a new column to be the text
    Graph_Dataframe["Text"] = override_text

    return Graph_Dataframe