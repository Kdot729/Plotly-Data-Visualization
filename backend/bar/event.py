from xml.dom.minidom import parseString
import pandas as panda
import backend.general_functions as general_functions

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)



def sort_new_DataFrame(dictionary, DataFrame, column_dictionary):

    if (dictionary["ID of Dropdown"] == "Type") or (dictionary["ID of Dropdown"] == "Reset-Icon"):
        for DataFrame_column_name in DataFrame:

            #Note Harded coding when "Type" is "Total" don't change the DataFrame
            #Note If "Type" equal "Buy" or "Sell" drop the other columns except for "Address"
            if (DataFrame_column_name != "Address") and (DataFrame_column_name != dictionary["Type"]) and (dictionary["Type"] != "Total"):
                DataFrame.drop([DataFrame_column_name], axis=1, inplace=True)

        #Note Drop all rows that have 0 in it        
        DataFrame = DataFrame[(DataFrame[list(DataFrame.columns)] != 0).all(axis=1)]      
        print(DataFrame)
        return DataFrame

    elif (dictionary["ID of Dropdown"] == "Address"):
        return general_functions.sort_DataFrame_for_Addresses(dictionary["Chosen Addresses"], DataFrame, column_dictionary["Address Column"])

    elif (dictionary["ID of Dropdown"] == "Less-Than") or (dictionary["ID of Dropdown"] == "Greater-Than"):
        return general_functions.sort_inequality_DataFrame(dictionary, DataFrame, column_dictionary["Inequality Column"])

               
