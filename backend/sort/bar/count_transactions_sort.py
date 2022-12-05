import pandas as panda
 
def create_count_transactions_bar_DataFrame(DataFrame):      
        #Note Count their transaction in their corresponding columns
        seller_count = DataFrame["Seller"].value_counts()
        buyer_count =  DataFrame["Buyer"].value_counts()


        #Note Make so the index is also a column which is the address
        DataFrame_seller = seller_count.to_frame().reset_index(level=0)
        DataFrame_buyer = buyer_count.to_frame().reset_index(level=0)

        #Note Combine both Dataframe and fill the NaN values with 0
        DataFrame_merge = (panda.concat([DataFrame_seller, DataFrame_buyer], ignore_index=True, sort=False)).fillna(0) 

        #Note Rename the columns
        DataFrame_merge.columns = ["Address", "Sell", "Buy"] 

        #Note Combine the "Sell" and "Buy" column into one column called "Type"
        #Note And make their values into it's own column called "Transaction Count"
        format_DataFrame = DataFrame_merge.melt(id_vars=["Address"], 
                var_name="Type", 
                value_name="Transaction Count")

        #Note Shorten the string so the x-axis looks better
        format_DataFrame["Address"] = format_DataFrame["Address"].str.slice(0,8)

        return format_DataFrame