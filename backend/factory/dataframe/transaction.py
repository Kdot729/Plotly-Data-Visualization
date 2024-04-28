from backend.factory.dataframe.superclass import Dataframe
import pandas as panda
class Transaction(Dataframe):

    def __init__(self, Tool):
        super().__init__(Tool)
        self.Finish_Dataframe()

    def Finish_Dataframe(self):

        Address_Column = "Address"
        Bought_Column = "Bought"
        Sold_Column = "Sold"

        #Note Count their transaction in their corresponding columns
        Count_Sold = self.Dataframe["Seller"].value_counts()
        Count_Bought =  self.Dataframe["Buyer"].value_counts()

        #Note Make so the index is also a column which is the address
        Seller_Dataframe = Count_Sold.to_frame().reset_index(level=0)
        Buyer_Dataframe = Count_Bought.to_frame().reset_index(level=0)

        #Note Renaming columns
        Seller_Dataframe.columns = [Address_Column, Sold_Column]
        Buyer_Dataframe.columns = [Address_Column, Bought_Column]

        #Note Join both dataframe on index "Address". Fill NaN values with 0
        self._Dataframe = Seller_Dataframe.set_index(Address_Column).join(Buyer_Dataframe.set_index(Address_Column)).reset_index(level=0).fillna(0)

        #Note Convert data from wide format to long format
        self._Dataframe = panda.melt(self._Dataframe, id_vars=[Address_Column], value_vars=[Sold_Column, Bought_Column])

        #Note Slicing the address strings because they're too long
        self._Dataframe[Address_Column] = self._Dataframe[Address_Column].str[:8]

        #Note Rename columns
        self._Dataframe.columns = [Address_Column, "Transaction", "Count"]



