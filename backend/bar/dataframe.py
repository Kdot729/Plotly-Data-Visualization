import pandas as panda
import pandas as panda
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)



def create_DataFrame(Tool):   
    #* Condense and dynamic way of creating DataFrame 
    #Note Need to use "lower()" function because csv file are lowercased       
    print(f"csv\\updated_{Tool.lower()}_transactions.csv")                
    return panda.read_csv(f"csv\\updated_{Tool.lower()}_transactions.csv",
                                        names=('Date', 'Hash', 'ETH', 'Seller', 'Buyer')
                          )        

def sort_Date_DataFrame(chosen_start_date, chosen_end_date, DataFrame):                     #* Filter the dataframe to only include the inputs which are start_date and end_date
     if chosen_start_date and chosen_end_date:
        return DataFrame[(DataFrame["Date"] >= chosen_start_date) & #* Returns the DataFrame inbetween the dates
                                  (DataFrame["Date"] <= chosen_end_date)]                                                       
     elif not chosen_start_date and not chosen_end_date:
        return DataFrame[(DataFrame["Date"] >= "2021-10-08") & 
                                  (DataFrame["Date"] <= datetime.now().strftime("%Y-%m-%d"))]                           
                                
#* Drop the duplicates of whatever column was passed in the DataFrame. Sort it descending. Then, convert it to a list. Returns passed in "column_name" of DataFrame. In that order
def sort_descending_and_drop_duplicates_list(DataFrame, column_name):
    return ((DataFrame[column_name].drop_duplicates()).sort_values(ascending=False)).tolist() 

#* Drop the duplicates of whatever column was passed in the DataFrame. Sort it ascending. Then, convert it to a list. Returns passed in "column_name" of DataFrame.  In that order
def sort_ascending_and_drop_duplicates_list(DataFrame, column_name):
    return ((DataFrame[column_name].drop_duplicates()).sort_values(ascending=True)).tolist() 


def sort_DataFrame_for_Addresses(dictionary, DataFrame, address_column_name):
    converted_list = (dictionary["Chosen_Addresses"].rstrip()).split(",")
    #FIXME Hardcoded the "Buyer" need to change it to be dynamic
    return DataFrame[DataFrame[address_column_name].isin(converted_list)]

def sort_DataFrame_for_Inequality(ETH_values, DataFrame, inequality_column_name):
    return DataFrame[(DataFrame[inequality_column_name] >= ETH_values["Min_ETH"]) &
                                (DataFrame[inequality_column_name] <= ETH_values["Max_ETH"])]





def sort_inequality_DataFrame(dictionary, DataFrame, inequality_column_name):
    ETH_values = {"Max_ETH": float(dictionary["Less_Than"]), "Min_ETH": float(dictionary["Greater_Than"])}
    ETH_DataFrame = sort_DataFrame_for_Inequality(ETH_values, DataFrame, inequality_column_name) 
    return ETH_DataFrame


def sort_Inequality_List(DataFrame, column_name):
    descending_list = sort_descending_and_drop_duplicates_list(DataFrame, column_name)
    ascending_list = sort_ascending_and_drop_duplicates_list(DataFrame, column_name)
    return {"Descending List": descending_list, "Ascending List": ascending_list}



#TODO Return a list of the latest address, dropping duplicates
def linking_address(DataFrame):
    pass

def create_count_transactions_bar_DataFrame(DataFrame):      
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