# reading all the csv file in directory
# Displaying FII data sector wise
import os
import glob
import pandas as pd

path = r'C:\Users\USER\PycharmProjects\pythonProject\importing_html\html-table-extraction-main'
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
result.sort()
print(result)

# reading content of csv file
sector_list=[]
for k in range(2,48):
    list1=[]
    for i in result:
        df = pd.read_csv(i)
        # print(df.iloc[3][0])
        # print(df.iloc[3][2])
        val=df.iloc[k][2]
        list1.append(val)
    # print(df.iloc[k][0])
    sector_list.append(df.iloc[k][0])
    # print(list1)

    list2 = []
    for j in range(len(list1)-1):
        # print(list1[j])
        # k=j+1
        val2 = int(list1[j+1])-int(list1[j])
        list2.append(val2)

    if list2[-1]>0 :
        print(df.iloc[k][0])
        print(list2)
        print("")
        if list2[-2]>0 :
            print(df.iloc[k][0])
            print(list2)
            print("")
            if list2[-3]>0 :
                print(df.iloc[k][0])
                print(list2)
                print("")

    

print(sector_list)