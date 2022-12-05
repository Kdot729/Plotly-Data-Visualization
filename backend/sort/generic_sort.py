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
    #! Need to change csv2 back to csv. Using csv2 to load graph faster         
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

def condition_for_Date_DataFrame(dictionary):
    print("Start", dictionary["Start_Date"], "end", dictionary["End_Date"])
    if (dictionary["ID of Dropdown"] == "None") or (dictionary["ID of Dropdown"] == "Address-Type"):
        DataFrame =  sort_Date_DataFrame(None, None, dictionary["DataFrame"])
    elif (dictionary["ID of Dropdown"] != "None") or (dictionary["ID of Dropdown"] != "Address-Type"):
        DataFrame = sort_Date_DataFrame(dictionary["Start_Date"], dictionary["End_Date"], dictionary["DataFrame"])
    return DataFrame

def sort_DataFrame_for_Addresses(dictionary, DataFrame):
    #! Need to pass the converted_list to the frontend and use that instead of the "Address List"
    converted_list = (dictionary["Chosen_Addresses"].rstrip()).split(",")
    return DataFrame[DataFrame[dictionary["Address_Type"]].isin(converted_list)]

def sort_DataFrame_for_ETH_Inequality(ETH_values, DataFrame):
    return DataFrame[(DataFrame["ETH"] >= ETH_values["Min_ETH"]) &
                                (DataFrame["ETH"] <= ETH_values["Max_ETH"])]

def reassign_ETH_min_and_max_in_dictionary(dictionary, DataFrame):
    if (dictionary["Less_Than"] == "") and (dictionary["Greater_Than"] == ""):
        dictionary["Less_Than"] = DataFrame["ETH"].max()
        dictionary["Greater_Than"] = DataFrame["ETH"].min()
    elif dictionary["Less_Than"] and (dictionary["Greater_Than"] == ""):
        dictionary["Greater_Than"] = DataFrame["ETH"].min()
    elif (dictionary["Less_Than"] == "") and dictionary["Greater_Than"]:
        dictionary["Less_Than"] = DataFrame["ETH"].max()
    return {"Max_ETH": float(dictionary["Less_Than"]), "Min_ETH": float(dictionary["Greater_Than"])}

def Chosen_Address_is_True(dictionary, DataFrame):
    #Note sort_DataFrame_for_Addresses will return a list with two values in ii
    address_DataFrame = sort_DataFrame_for_Addresses(dictionary, DataFrame)
    return Get_ETH_DataFrame(dictionary, address_DataFrame)


def Get_ETH_DataFrame(dictionary, DataFrame):
    ETH_values = reassign_ETH_min_and_max_in_dictionary(dictionary, DataFrame)
    ETH_DataFrame = sort_DataFrame_for_ETH_Inequality(ETH_values, DataFrame) 
    return ETH_DataFrame


def sort_Inequality_List(DataFrame, column_name):
    descending_list = sort_descending_and_drop_duplicates_list(DataFrame, column_name)
    ascending_list = sort_ascending_and_drop_duplicates_list(DataFrame, column_name)
    return {"Descending List": descending_list, "Ascending List": ascending_list}

def sort_Address_List(DataFrame, Address_Type):
    return {"Address List": sort_descending_and_drop_duplicates_list(DataFrame, Address_Type)}
    
def linking_address(selected_address):
    if selected_address == None:
        return {"Link_Address": None}
    elif selected_address:
        return {"Link_Address": selected_address} 






