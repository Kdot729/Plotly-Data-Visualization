import pandas as panda
import datetime


def Insert_Into_Row(Graph_Dataframe, Looped_Dataframe, Replaced_Value):

    # Graph_Dataframe = panda.DataFrame(columns=['id', 'parent', 'value'])
    # Dataframe_Index = len(Graph_Dataframe.index)

    for index, row in Looped_Dataframe.iterrows():
        ETH_Column = row["ETH"]

        if Replaced_Value == "Year":
            Replace_Row = [row[Replaced_Value], "Total", ETH_Column]
        elif Replaced_Value == "Month Year":
            Replace_Row = [row[Replaced_Value], row[Replaced_Value][:4], ETH_Column]
        elif Replaced_Value == "Date":
            Replace_Row = [row[Replaced_Value], row[Replaced_Value][:7], ETH_Column]

        Dataframe_Index = len(Graph_Dataframe.index)
        Graph_Dataframe.loc[Dataframe_Index] = Replace_Row
    
    return Graph_Dataframe

def create_sunburst_DataFrame(Year_Dataframe, Month_Year_Dataframe, Dataframe):

    Graph_Dataframe = panda.DataFrame(columns=['id', 'parent', 'value'])
    Dataframe_Index = len(Graph_Dataframe.index)

    # for index, row in Year_Dataframe.iterrows():
    #     Graph_Dataframe.loc[len(Graph_Dataframe.index)] = [row["Year"], "Total", row["ETH"]]

    # for index, row in Month_Year_Dataframe.iterrows():
    #     Graph_Dataframe.loc[len(Graph_Dataframe.index)] = [row["Month Year"], row["Month Year"][:4], row["ETH"]]

    # for index, row in Dataframe.iterrows():
    #     Graph_Dataframe.loc[len(Graph_Dataframe.index)] = [row["Date"], row["Date"][:7], row["ETH"]]

    # print(graph_DataFrame.head())
    Graph_Dataframe = Insert_Into_Row(Graph_Dataframe, Year_Dataframe, "Year")
    Graph_Dataframe = Insert_Into_Row(Graph_Dataframe, Month_Year_Dataframe, "Month Year")
    Graph_Dataframe = Insert_Into_Row(Graph_Dataframe, Dataframe, "Date")
    
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