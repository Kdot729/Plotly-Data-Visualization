import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as panda
import datetime

# panda.set_option('display.max_rows', None)
# panda.set_option('display.max_columns', None)
# panda.set_option('display.width', None)
# panda.set_option('display.max_colwidth', None)
# DataFrame = panda.read_csv( "updated_thimble_transactions.csv", 
#               names=('Date', 'Hash', 'ETH', 'Seller', 'Buyer')
#               )   
# #! Might be a problem later
# #Note Ignoring the warning. Maybe solve later
# panda.set_option('mode.chained_assignment', None)   
# for i in range(0, len(DataFrame)):
#         DataFrame["Date"].iloc[i] = DataFrame["Date"].iloc[i][:10]      

# #Note Group by "Date" then sum their "ETH"
# DataFrame = DataFrame.groupby("Date").sum('ETH')

# #Note Make "Date" a column
# DataFrame = DataFrame.reset_index(level=0)

# weekday_number_list = []
# month_number_list = []
# year_list = []
# year_and_month_list = []
# for i in range(0, len(DataFrame)):
#         split_date = DataFrame["Date"][i][:10]

#         #Note Get full weekday name 
#         day_of_week_number = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%w')

#         #Note day_of_week_number is actually a string so were checking a string
#         #Note Sunday is default "0" so we make it a "7"
#         if day_of_week_number == "0":
#                 day_of_week_number = "7"

#         #Note Get abbreviated month name
#         month_number = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%m')

#         #Note Get full year
#         year = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%Y')

#         weekday_number_list.append(day_of_week_number)
#         month_number_list.append(month_number)
#         year_list.append(year)
#         year_and_month_list.append(f"{year}-{month_number}" )

# DataFrame.insert(2, "Year", year_list, True)
# DataFrame.insert(3, "Month Number", month_number_list, True)
# DataFrame.insert(4, "Weekday Number", weekday_number_list, True)
# DataFrame.insert(5, "Month Year", year_and_month_list, True)

# DataFrame_year = DataFrame.groupby("Year").sum("ETH").reset_index()

# #Note Group by "Month Year", then sum "ETH", then reset index
# DataFrame_month_year = DataFrame.groupby("Month Year").sum("ETH").reset_index()

# graph_DataFrame = panda.DataFrame(columns=['id', 'parent', 'value'])

# for index, row in DataFrame_year.iterrows():
#     # print(row["ETH"])
#     graph_DataFrame.loc[len(graph_DataFrame.index)] = [row["Year"], "Total" ,row["ETH"]]



# for index, row in DataFrame_month_year.iterrows():
#     graph_DataFrame.loc[len(graph_DataFrame.index)] = [row["Month Year"], row["Month Year"][:4] ,row["ETH"]]


# for index, row in DataFrame.iterrows():
#     graph_DataFrame.loc[len(graph_DataFrame.index)] = [row["Date"], row["Date"][:7] ,row["ETH"]]


# print(graph_DataFrame['id'])

# override_text = []

# substring_checker = "0"

# for index in graph_DataFrame['id']:


#         #Note If len 4 then it's the year
#         if index == "Total":
#             value == "Total"
#         elif len(index) == 4:
#             value = index

#         #Note If len 7 then it's the year and month
#         elif len(index) == 7:
#             month = datetime.datetime.strptime(index, '%Y-%m').strftime('%b')
#             value = month

#         elif len(index) == 10:
#             nth_day = datetime.datetime.strptime(index, '%Y-%m-%d').strftime('%d')
#             #Note Check to see if "0" is in the string
#             if substring_checker in nth_day:
#                     #Note Remove the zero from the string
#                     nth_day = nth_day.replace('0', '')
#             value = f"{nth_day}th "

#         override_text.append(value)

# #Note Created a new column to be the text
# graph_DataFrame["Text"] = override_text

def create_sunburst(DataFrame):

    figure = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]],)


    figure.add_trace(go.Sunburst(
        labels=DataFrame['id'],
        parents=DataFrame['parent'],
        values=DataFrame['value'],
        branchvalues='total',

        insidetextorientation="radial",
        # textinfo="label",
        
        texttemplate=DataFrame["Text"],



        name='',
        # level=''
        ), 1, 1)
    figure.update_layout(title="Volume")

    return figure