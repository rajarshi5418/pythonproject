import pandas as pd
from pandas import DataFrame

tables = pd.read_html('https://www.nseindia.com/get-quotes/derivatives?symbol=NIFTY&identifier=OPTIDXNIFTY20-10-2022CE17300.00')
print(tables)

# print('Tables found:', len(tables))
# df1 = tables[0]  # Save first table in variable df1
# print('First Table')

