import pandas as panda

def create_heatmap_DataFrame(DataFrame):

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



