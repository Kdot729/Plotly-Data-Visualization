import pandas as panda
from datetime import datetime
import json, plotly



panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)



def create_basic_DataFrame(Tool):   

    #Note Because we're using Docker which is on Linux, use "/" in file path                    
    return panda.read_csv(f"csv/updated_{Tool}_transactions.csv", names=('Date', 'Hash', 'ETH', 'Seller', 'Buyer'))        
