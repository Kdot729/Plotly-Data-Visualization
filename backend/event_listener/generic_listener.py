from xml.dom.minidom import parseString
import backend.sort.generic_sort as generic_sort
import pandas as panda
from datetime import date

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)


#FIXME dictionary["Address_Type"] doesn't work with bar chart
def sort_new_DataFrame(dictionary, DataFrame):

    if (dictionary["ID of Dropdown"] == "None") or (dictionary["ID of Dropdown"] == "Start-Date") or (dictionary["ID of Dropdown"] == "End-Date"):
        return generic_sort.sort_Date_DataFrame(dictionary["Start_Date"], dictionary["End_Date"], DataFrame)

    elif (dictionary["ID of Dropdown"] == "Address-Type"):
        pass

    elif (dictionary["ID of Dropdown"] == "Address"):
        print(generic_sort.sort_DataFrame_for_Addresses(dictionary, DataFrame))
        return generic_sort.sort_DataFrame_for_Addresses(dictionary, DataFrame)

    elif (dictionary["ID of Dropdown"] == "Less-Than") or (dictionary["ID of Dropdown"] == "Greater-Than"):
        return generic_sort.Get_ETH_DataFrame(dictionary, DataFrame)

               
