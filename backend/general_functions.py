import pandas as panda
from datetime import datetime
from dotenv import load_dotenv
import json, plotly
load_dotenv()


panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)



def create_DataFrame(Tool):   
    #* Condense and dynamic way of creating DataFrame 
    #Note Need to use "lower()" function because csv file are lowercased                     
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


def sort_DataFrame_for_Addresses(choosen_address, DataFrame, address_column_name):
    converted_list = (choosen_address.rstrip()).split(",")
    return DataFrame[DataFrame[address_column_name].isin(converted_list)]


def sort_DataFrame_for_Inequality(ETH_values, DataFrame, inequality_column_name):
    return DataFrame[(DataFrame[inequality_column_name] >= ETH_values["Min ETH"]) &
                                (DataFrame[inequality_column_name] <= ETH_values["Max ETH"])]





def sort_inequality_DataFrame(dictionary, DataFrame, inequality_column_name):
    ETH_values = {"Max ETH": float(dictionary["Less Than"]), "Min ETH": float(dictionary["Greater Than"])}
    ETH_DataFrame = sort_DataFrame_for_Inequality(ETH_values, DataFrame, inequality_column_name) 
    return ETH_DataFrame


def sort_Inequality_List(DataFrame, column_name):
    descending_list = sort_descending_and_drop_duplicates_list(DataFrame, column_name)
    ascending_list = sort_ascending_and_drop_duplicates_list(DataFrame, column_name)
    return {"Descending List": descending_list, "Ascending List": ascending_list}



#TODO Return a list of the latest address, dropping duplicates
def linking_address(address_column_name, DataFrame):

    address =(DataFrame[address_column_name].drop_duplicates())

    #Note Going up the ninth index because it's needs to match the max in selectpicker
    #Note Getting 9 badges because 9 badges seem to fit on a width of 1080 screen
    full_address = address[:8].tolist() 
    short_address = address[:8].str.slice(0,5).tolist() 


    #Note full_address is key. short_address is value
    address_dictionary = dict(zip(full_address, short_address))
    print(address_dictionary)
    return address_dictionary


def convert_Graph_to_JSON(plotly_graph):
    graphJSON = json.dumps(obj=plotly_graph , cls=plotly.utils.PlotlyJSONEncoder) #! graphJSON needs to match graphJSON in render template because in the template it's graph graphJSON 

    return graphJSON