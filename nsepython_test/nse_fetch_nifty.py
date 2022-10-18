from nsepython import *
import pandas as pd
# positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
# df = pd.DataFrame(positions['data'])
# print(df)


oi_data, ltp, crontime = oi_chain_builder("NIFTY","latest","full")
# pd.set_option('display.max_columns', None)  # or 1000
# pd.set_option('display.max_rows', None)  # or 1000
# pd.set_option('display.max_colwidth', -1)  # or 199
# print(oi_data)
# oi_data.to_csv("oi_data.csv")
# print(ltp)
# print(crontime)
print(oi_data.columns)

oi_data = oi_data.set_index("Strike Price")

print(oi_data)
oi_max_ce = oi_data.loc[oi_data['CALLS_Volume'].idxmax()]
print(oi_max_ce)

oi_max_ce = oi_data.loc[oi_data['CALLS_Volume'].idxmax()]
print(oi_max_ce)

print(oi_data.nlargest(5,"CALLS_Volume"))
print(oi_data.nsmallest(5,"CALLS_Volume"))
print(oi_data.nlargest(5,"CALLS_Chng in OI"))
print(oi_data.nsmallest(5,"CALLS_Chng in OI"))
