from xml.dom.minidom import parseString
import backend.sort.generic_sort as generic_sort
import pandas as panda
from datetime import date

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)


#FIXME dictionary["Address_Type"] doesn't work with bar chart
def get_dictionary(dictionary):
    date_DataFrame = generic_sort.condition_for_Date_DataFrame(dictionary)

    if (dictionary["ID of Dropdown"] == "None") or (dictionary["ID of Dropdown"] == "Start-Date") or (dictionary["ID of Dropdown"] == "End-Date"):
        both_address = both_address_dictionary(dictionary, date_DataFrame, dictionary["Address_Type"])
        return {"DataFrame": date_DataFrame} | both_address 

    #! Testing condition for when switching from buyer to sell with an address already selected
    if (dictionary["ID of Dropdown"] == "Address-Type"):
        if dictionary["Chosen_Addresses"]:
            dictionary["Chosen_Addresses"] = None
        print("choosen address", dictionary["Chosen_Addresses"])
        both_address = both_address_dictionary(dictionary, date_DataFrame, dictionary["Address_Type"])
        return {"DataFrame": date_DataFrame} | both_address 

    elif (dictionary["ID of Dropdown"] == "Address"):
            if dictionary["Chosen_Addresses"]:  
                DataFrame = generic_sort.Chosen_Address_is_True(dictionary, date_DataFrame)
                link_address_dictionary = linking_address(dictionary, DataFrame)
                address_dictionary = generic_sort.sort_Address_List(date_DataFrame, dictionary["Address_Type"])
                return {"DataFrame": DataFrame} | link_address_dictionary | address_dictionary 

            elif not dictionary["Chosen_Addresses"]:
                both_address = both_address_dictionary(dictionary, date_DataFrame, dictionary["Address_Type"])
                return {"DataFrame": date_DataFrame} | both_address

    elif (dictionary["ID of Dropdown"] == "Less-Than") or (dictionary["ID of Dropdown"] == "Greater-Than"):
            if dictionary["Chosen_Addresses"]:                
                DataFrame = generic_sort.Chosen_Address_is_True(dictionary, date_DataFrame)
                both_address = both_address_dictionary(dictionary, DataFrame, dictionary["Address_Type"])
                return {"DataFrame": DataFrame} | both_address
                
            elif not dictionary["Chosen_Addresses"]:
                ETH_DataFrame = generic_sort.Get_ETH_DataFrame(dictionary, date_DataFrame)
                both_address = both_address_dictionary(dictionary, ETH_DataFrame, dictionary["Address_Type"])
                return {"DataFrame": ETH_DataFrame} | both_address
               

#! Testing below
def linking_address(dictionary, DataFrame):
    print("in linking",dictionary["Chosen_Addresses"])
    if dictionary["Chosen_Addresses"]:
        if (dictionary["ID of Dropdown"] == "Address") or (dictionary["ID of Dropdown"] == "Less-Than") or (dictionary["ID of Dropdown"] == "Greater-Than"):
                link_list = list(generic_sort.sort_descending_and_drop_duplicates_list(DataFrame, dictionary["Address_Type"]))
                return generic_sort.linking_address(link_list)
                
    #* Else will also execute if dictionary["Chosen_Addresses"] is None
    else:
         return generic_sort.linking_address(None)

#Note Fucntion isn't used if both dictionary["ID of Dropdown"] == "Address" and dictionary["Chosen_Addresses"] are True 
#Note Because it uses two different DataFrames for linking_list and address_list
def both_address_dictionary(dictionary, DataFrame, Address_Type):
    link_address_dictionary = linking_address(dictionary, DataFrame)
    address_dictionary = generic_sort.sort_Address_List(DataFrame, Address_Type)
    return link_address_dictionary | address_dictionary