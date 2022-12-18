from xml.dom.minidom import parseString
import pandas as panda
import backend.general_functions as general_functions

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)



def sort_new_DataFrame(dictionary, DataFrame, column_dictionary):

    #Note ((dictionary["ID of Dropdown"] == "Address") and not dictionary["Chosen Addresses"]) means that they manually deselected the address's themselves
    #Note Meaning the "Address" dropdown is empty, so we just return the default DataFrame
    if (dictionary["ID of Dropdown"] == "Type") or (dictionary["ID of Dropdown"] == "Reset-Icon") or ((dictionary["ID of Dropdown"] == "Address") and not dictionary["Chosen Addresses"]):
        return DataFrame

    elif (dictionary["ID of Dropdown"] == "Address") and dictionary["Chosen Addresses"]:
            return general_functions.sort_DataFrame_for_Addresses(dictionary["Chosen Addresses"], DataFrame, column_dictionary["Address Column"])

    elif (dictionary["ID of Dropdown"] == "Less-Than") or (dictionary["ID of Dropdown"] == "Greater-Than"):
        return general_functions.sort_inequality_DataFrame(dictionary, DataFrame, column_dictionary["Inequality Column"])

               
