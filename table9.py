# reading all the csv file in directory
# formatting csv file
import os
import glob
import pandas as pd
from pandas import DataFrame
from datetime import datetime

path = r'C:\Users\USER\PycharmProjects\pythonProject\importing_html\html-table-extraction-main'
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
result.sort()
print(result)

# reading content of csv file

for j in result:
    df = pd.read_csv(j)
    # df = df.astype(str)

    cols = df.columns
    # df2 = DataFrame()
    for i in df.columns:
        print(type(i))
        df[i] = df[i].str.replace(',', '')

        print(" ")


    # df1 = df.drop(['Unnamed: 0.1'], axis=1, inplace=True)
    df.to_csv(j,index=False)
    # print(df.iloc[:,[2]])
    print(df)



