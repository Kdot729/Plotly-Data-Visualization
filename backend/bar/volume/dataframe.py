import pandas as panda
import datetime

def create_volume_DataFrame(DataFrame):

        #! Might be a problem later
        #Note Ignoring the warning. Maybe solve later
        panda.set_option('mode.chained_assignment', None)   
        for i in range(0, len(DataFrame)):
                DataFrame["Date"].iloc[i] = DataFrame["Date"].iloc[i][:10]      

        #Note Group by "Date" then sum their "ETH"
        DataFrame = DataFrame.groupby("Date").sum('ETH')

        #Note Make "Date" a column
        DataFrame = DataFrame.reset_index(level=0)

        day_of_week_name_list = []
        year_and_month_list = []

        for i in range(0, len(DataFrame)):
                split_date = DataFrame["Date"][i][:10]

                #Note Get full weekday name 
                day_of_week= datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%A')

                #Note Get abbreviated month name
                month = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%b')

                #Note Get full year
                year = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%Y')

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
