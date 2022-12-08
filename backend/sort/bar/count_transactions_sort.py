import pandas as panda
 
def create_count_transactions_bar_DataFrame(DataFrame):      
        seller_count = DataFrame["Seller"].value_counts()
        buyer_count =  DataFrame["Buyer"].value_counts()
        # print("seller",seller_count)
        # print("buyer", buyer_count)

        #Note Convert series to DataFrame
        seller_count = seller_count.to_frame()
        buyer_count = buyer_count.to_frame()


        #Note Convert the index to a column called Address
        seller_count = seller_count.reset_index(level=0)
        buyer_count = buyer_count.reset_index(level=0)


        # print(seller_count)
        # print("")
        # print(buyer_count)

        #Note combine both DataFrame and fill the NaN values with 0
        result = (panda.concat([seller_count, buyer_count])).fillna(0)

        #Note Rename the columns
        result.columns = ["Address", "Sell", "Buy"] 
        result.eval('Total = Sell + Buy', inplace=True)

        #Note Group by address and sum the other columns
        aggregation_functions = {'Address': 'first', 'Sell': 'sum', 'Buy': 'sum', "Total": "sum"}
        result = result.groupby('Address', as_index=False).aggregate(aggregation_functions).reindex(columns=result.columns)


        return result

 
