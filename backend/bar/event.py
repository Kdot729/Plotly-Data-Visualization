from xml.dom.minidom import parseString
import pandas as panda
import backend.general_functions as general_functions

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)


#FIXME dictionary["Address_Type"] doesn't work with bar chart
def sort_new_DataFrame(dictionary, DataFrame, column_dictionary):

    if (dictionary["ID of Dropdown"] == "Type-Address") or (dictionary["ID of Dropdown"] == "Reset-Icon"):
        return DataFrame

    elif (dictionary["ID of Dropdown"] == "Address"):
        return general_functions.sort_DataFrame_for_Addresses(dictionary["Chosen_Addresses"], DataFrame, column_dictionary["Address_Column"])

    elif (dictionary["ID of Dropdown"] == "Less-Than") or (dictionary["ID of Dropdown"] == "Greater-Than"):
        return general_functions.sort_inequality_DataFrame(dictionary, DataFrame, column_dictionary["Inequality_Column"])

               