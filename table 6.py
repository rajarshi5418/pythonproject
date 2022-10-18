# reading all the csv file in directory
# Displaying data sector wise
# combining all data files in one
import os
import glob
import pandas as pd

path = r'C:\Users\USER\PycharmProjects\pythonProject\importing_html\html-table-extraction-main\csv1'
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
result.sort()
print(result)

# reading content of csv file
sector_list=[]
df3=pd.DataFrame()
list_sector=[]
for k in range(2,48):
    list1=[]
    for i in result:
        df = pd.read_csv(i)
        # print(df.iloc[3][0])
        # print(df.iloc[3][2])
        val=df.iloc[k][2]
        list1.append(val)
    print(df.iloc[k][0])
    sector_name = df.iloc[k][0]
    sector_list.append(df.iloc[k][0])
    print(list1)

    list2 = []
    for j in range(len(list1)-1):
        # print(list1[j])
        # k=j+1
        val2 = int(list1[j+1])-int(list1[j])
        list2.append(val2)
# creating dictionary
    dict_sector = {}
    dict_sector[sector_name] = list2
    print(dict_sector)
    list_sector.append(dict_sector)
    df2=pd.DataFrame.from_dict(dict_sector).transpose()

    # df3.append(df2)
    print(df2)
    print(list_sector)

df4=pd.DataFrame(list_sector)
print(df4)

# print(sector_list)