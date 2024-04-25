from backend.factory.dataframe.superclass import Dataframe
import pandas as panda
class Transaction(Dataframe):

    def __init__(self, Tool):
        super().__init__(Tool)
        self.Finish_Dataframe()

    def Finish_Dataframe(self):
        Address_Column = "Address"
        Buys_Column = "Buys"
        Sells_Column = "Sells"

        #Note Count their transaction in their corresponding columns
        Count_Sells = self.Dataframe["Seller"].value_counts()
        Count_Buys =  self.Dataframe["Buyer"].value_counts()

        #Note Make so the index is also a column which is the address
        Seller_Dataframe = Count_Sells.to_frame().reset_index(level=0)
        Buyer_Dataframe = Count_Buys.to_frame().reset_index(level=0)

        #Note Renaming columns
        Seller_Dataframe.columns = [Address_Column, Sells_Column]
        Buyer_Dataframe.columns = [Address_Column, Buys_Column]

        #Note Combine both Dataframe and fill the NaN values with 0
        self._Dataframe = panda.merge(Seller_Dataframe, Buyer_Dataframe, on=Address_Column, how='outer').fillna(0)

        #Note Get the total transactions an address has done
        self._Dataframe['Transaction Count'] = self._Dataframe[Sells_Column] + self._Dataframe[Buys_Column]

        #Note Shorten the string so the x-axis looks better
        self._Dataframe[Address_Column] = self._Dataframe[Address_Column].str.slice(0,8)




