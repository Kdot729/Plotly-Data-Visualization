import pandas as panda
import datetime

def create_heatmap_DataFrame(DataFrame):
        
        #! Might be a problem later
        #Note Ignoring the warning. Maybe solve later
        panda.set_option('mode.chained_assignment', None)   
        for i in range(0, len(DataFrame)):
                DataFrame["Date"].iloc[i] = DataFrame["Date"].iloc[i][:10]      

        #Note Group by "Date" then sum their "ETH"
        DataFrame = DataFrame.groupby("Date").sum('ETH')

        #Note Make "Date" a column
        DataFrame = DataFrame.reset_index(level=0)

        weekday_number_list = []
        month_number_list = []
        year_list = []
        year_and_month_list = []
        for i in range(0, len(DataFrame)):
                split_date = DataFrame["Date"][i][:10]

                #Note Get full weekday name 
                day_of_week_number = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%w')

                #Note day_of_week_number is actually a string so were checking a string
                #Note Sunday is default "0" so we make it a "7"
                if day_of_week_number == "0":
                        day_of_week_number = "7"

                #Note Get abbreviated month name
                month_number = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%m')

                #Note Get full year
                year = datetime.datetime.strptime(split_date, '%Y-%m-%d').strftime('%Y')

                weekday_number_list.append(day_of_week_number)
                month_number_list.append(month_number)
                year_list.append(year)
                year_and_month_list.append(f"{month_number}-{year}" )

        DataFrame.insert(2, "Year", year_list, True)
        DataFrame.insert(3, "Month Number", month_number_list, True)
        DataFrame.insert(4, "Weekday Number", weekday_number_list, True)
        DataFrame.insert(5, "Month Year", year_and_month_list, True)


        #Note Sort false will preserve the order which is acendening to the current date
        DataFrame = DataFrame.groupby(["Year", "Month Number", "Weekday Number", "Month Year"], sort=False).sum('ETH')

        #Note Make the index as columns
        DataFrame = DataFrame.reset_index()

        #Note Get the list of "Month Year" to use to reorder DataFrame columns
        columns_list = DataFrame["Month Year"].drop_duplicates().tolist()



        DataFrame = panda.pivot_table(DataFrame, 
                                        values='ETH', 
                                        index=["Weekday Number"],
                                        columns=["Month Year"], 

                                        #Note If a weekday didn't have any volumne use a zero
                                        fill_value=0)


        #Note Changing the column order so Oct-2021 is first
        DataFrame = DataFrame[columns_list]

        #Note y_axis is the weekday as a number
        #Delete? This is variable is in the graph.py
        weekday_names_list =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]



        z_axis = []

        for index, row in DataFrame.iterrows():
                #Note Get all the values of a row and convert it to a list
                row_list = row.values.tolist()

                #Note Put the row_list into z_axis to make it a 2D array
                z_axis.append(row_list)

        return {"x": columns_list,"y": weekday_names_list, "z":z_axis}



