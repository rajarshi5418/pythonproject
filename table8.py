import pandas as pd
from pandas import DataFrame

xls = pd.ExcelFile(r'C:\Users\USER\PycharmProjects\pythonProject\importing_html\html-table-extraction-main\master_copy-copy1.xlsx')
df1 = pd.read_excel(xls, 'Sheet26')
rows = df1.index

# df1.drop(rows, inplace=True)

df2 = DataFrame(df1, columns= ["Column2","Column23","Column33"])

df2.to_csv("test1.csv")

# cs = pd.read_csv('220331.csv')
# print(cs)





#
# xls2 = pd.read_csv('220315.csv')
# # df1 = pd.read_excel(xls, 'Sheet1')
#
# print(xls2.columns)
# print(xls2)
