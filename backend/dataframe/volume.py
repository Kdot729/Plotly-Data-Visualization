def Create_Volume_Dataframe(DataFrame):

        #Note Sort false will preserve the order which is acendening to the current date
        DataFrame = DataFrame.groupby(["Day", "Month Year"], sort=False).sum('ETH')

        #Note Make the index as columns
        DataFrame = DataFrame.reset_index()

        return DataFrame
