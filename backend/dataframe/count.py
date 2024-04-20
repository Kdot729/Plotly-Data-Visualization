import pandas as panda

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)

def Create_Transaction_Dataframe(DataFrame):      
        seller_count = DataFrame["Seller"].value_counts()
        buyer_count =  DataFrame["Buyer"].value_counts()

        #Note Convert series to DataFrame
        seller_count = seller_count.to_frame()
        buyer_count = buyer_count.to_frame()

        #Note Convert the index to a column called Address
        seller_count = seller_count.reset_index(level=0)
        buyer_count = buyer_count.reset_index(level=0)

        #Note combine both DataFrame and fill the NaN values with 0
        result = (panda.concat([seller_count, buyer_count])).fillna(0)

        #Note Rename the columns
        result.columns = ["Address", "Sell", "Buy"] 
        result.eval('Total = Sell + Buy', inplace=True)

        #Note Group by address and sum the other columns
        aggregation_functions = {'Address': 'first', 'Sell': 'sum', 'Buy': 'sum', "Total": "sum"}
        result = result.groupby('Address', as_index=False).aggregate(aggregation_functions).reindex(columns=result.columns)

        return result




