import pandas as panda
import datetime

def Create_Volume_Dataframe(DataFrame):

        day_of_week_name_list = []
        year_and_month_list = []

        for Current_Date in DataFrame["Date"].tolist():

                #Note Get full weekday name 
                day_of_week= datetime.datetime.strptime(Current_Date, '%Y-%m-%d').strftime('%A')

                #Note Get abbreviated month name
                month = datetime.datetime.strptime(Current_Date, '%Y-%m-%d').strftime('%b')

                #Note Get full year
                year = datetime.datetime.strptime(Current_Date, '%Y-%m-%d').strftime('%Y')

                day_of_week_name_list.append(day_of_week)
                year_and_month_list.append(f"{month} {year}" )

        #Note Insert the lists as columns
        DataFrame.insert(2, "Day", day_of_week_name_list, True)
        DataFrame.insert(3, "Month Year", year_and_month_list, True)

        #Note Sort false will preserve the order which is acendening to the current date
        DataFrame = DataFrame.groupby(["Day", "Month Year"], sort=False).sum('ETH')

        #Note Make the index as columns
        DataFrame = DataFrame.reset_index()

        return DataFrame
