# downloading FII table from NSDL website and saving in csv format
import pandas as pd
from pandas import DataFrame
import pprint
tables = pd.read_html('https://www.fpi.nsdl.co.in/web/StaticReports/Fortnightly_Sector_wise_FII_Investment_Data/FIIInvestSector_Mar152022.html')
print('Tables found:', len(tables))
df1 = tables[0]  # Save first table in variable df1
print('First Table')
print(df1[1],df1[22],df1[32])

pd.set_option('display.max_columns',None)

df = DataFrame(df1, columns= [1,22,32])
print(df)

# df = DataFrame(df1.iloc[0])
# print(df)

# writer = pd.ExcelWriter('SAMPLE.xlsx')
#
# df.to_excel(writer, 'Sheet3')
# writer.save()


df.to_csv('220315.csv', header=False, index=False)


