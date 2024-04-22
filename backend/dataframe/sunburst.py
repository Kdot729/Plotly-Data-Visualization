import pandas as panda
import datetime

def create_sunburst_DataFrame(Year_Dataframe, Month_Year_Dataframe, Dataframe):

    graph_DataFrame = panda.DataFrame(columns=['id', 'parent', 'value'])

    for index, row in Year_Dataframe.iterrows():
        graph_DataFrame.loc[len(graph_DataFrame.index)] = [row["Year"], "Total" ,row["ETH"]]

    for index, row in Month_Year_Dataframe.iterrows():
        graph_DataFrame.loc[len(graph_DataFrame.index)] = [row["Month Year"], row["Month Year"][:4] ,row["ETH"]]

    for index, row in Dataframe.iterrows():
        graph_DataFrame.loc[len(graph_DataFrame.index)] = [row["Date"], row["Date"][:7] ,row["ETH"]]

    override_text = []

    substring_checker = "0"

    for index in graph_DataFrame['id']:

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
    graph_DataFrame["Text"] = override_text

    return graph_DataFrame