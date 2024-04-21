import pandas as panda
import datetime

def create_sunburst_DataFrame(DataFrame):

    DataFrame_year = DataFrame.groupby("Year").sum("ETH").reset_index()

    #Note Group by "Month Year", then sum "ETH", then reset index
    DataFrame_month_year = DataFrame.groupby("Month Year").sum("ETH").reset_index()

    graph_DataFrame = panda.DataFrame(columns=['id', 'parent', 'value'])

    for index, row in DataFrame_year.iterrows():
        # print(row["ETH"])
        graph_DataFrame.loc[len(graph_DataFrame.index)] = [row["Year"], "Total" ,row["ETH"]]



    for index, row in DataFrame_month_year.iterrows():
        graph_DataFrame.loc[len(graph_DataFrame.index)] = [row["Month Year"], row["Month Year"][:4] ,row["ETH"]]


    for index, row in DataFrame.iterrows():
        graph_DataFrame.loc[len(graph_DataFrame.index)] = [row["Date"], row["Date"][:7] ,row["ETH"]]


    # print(graph_DataFrame['id'])

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