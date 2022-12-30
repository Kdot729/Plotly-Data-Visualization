import plotly.express as plotly
import pandas as panda
import datetime
#! Copy everything below
DataFrame = panda.read_csv( "updated_thimble_transactions.csv", 
              names=('Date', 'Hash', 'ETH', 'Seller', 'Buyer')
              )   

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None
)

#! Might be a problem later
#Note Ignoring the warning. Maybe solve later
panda.set_option('mode.chained_assignment', None)   
for i in range(0, len(DataFrame)):
        DataFrame["Date"].iloc[i] = DataFrame["Date"].iloc[i][:10]      

#Note Group by "Date" then sum their "ETH"
DataFrame = DataFrame.groupby("Date").sum('ETH')

#Note Make "Date" a column
DataFrame = DataFrame.reset_index(level=0)


day_list = []
month_list = []
year_list = []
year_and_month_list = []
for i in range(0, len(DataFrame)):
        split_date = DataFrame["Date"][i][:10]

        #Note Get full weekday name 
        day_of_week= datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%A')

        #Note Get abbreviated month name
        month = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%b')

        #Note Get full year
        year = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%Y')

        day_list.append(day_of_week)
        month_list.append(month)
        year_list.append(year)
        year_and_month_list.append(f"{month} {year}" )

DataFrame.insert(2, "Year", year_list, True)
DataFrame.insert(3, "Month", month_list, True)
DataFrame.insert(4, "Day", day_list, True)
DataFrame.insert(5, "Month Year", year_and_month_list, True)

figure = plotly.bar(DataFrame, 
x="ETH", 
y="Month Year", 
color='Day', 
orientation='h')

#Note Create title for graph and center it
figure.update_layout(title_text="Volume", title_x=0.5)

figure.update_layout(legend={
                #Note Change position of legend to be inside the graph
                "yanchor": "top",
                "y": 1,
                "xanchor":"right",
                "x": 1,

                #Note Styling the legend box
                "bgcolor": "#e5ecf6",
                "bordercolor": "black",
                "borderwidth": 1
                })

figure.show()
# print(DataFrame)
