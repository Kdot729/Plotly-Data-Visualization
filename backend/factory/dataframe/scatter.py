
from backend.factory.dataframe.superclass import Dataframe

class Scatter(Dataframe):

    def __init__(self, Tool):
        super().__init__(Tool)
        
    def Create_Dataframe(self):
        super().Create_Dataframe()