import nsepython
from nsepython import*
from datetime import date,timedelta,datetime
import pandas as pd


dt  = date.today()
# print(dt-timedelta(2))
# print(date.today())
# print(dir(nsepython))
#
# list1=dir(nsepython)
#
# for i in list1:
#     print(i)
#
# print(nse_get_index_list())
#
list1=[]
for j in range(5):

    dt = date.today()
    dt1=dt-timedelta(j)
    dt2 = datetime.strftime(dt1, '%d-%m-%Y')
    list1.append(dt2)
print(list1)
# list2 = ["09-01-2022","10-01-2022"]
for i in list1:
    print(i)
    str1 = '"'
    str2 = '"'
    str3 = i
    dat= str1 + str3 + str2
    print(dat)
    # dat=list1[i]
    df = get_bhavcopy(i)
    print(df.loc[df['SYMBOL'] == "SBIN"])


str1 = '"'
str2 = '"'
str3 = "09-01-2022"
print(str1+str3+str2)

#
#
# for i in range(5):
#
#     dt = date.today()
#     dt1=dt-timedelta(i)
#     # print(type(dt1.strptime('%d-%m-%Y')))
#     # print(dt1.day,"-",dt1.month,"-",dt1.year)
#     # print(dt.strftime('%m-%d-%Y'))
#
#     dt2=datetime.strftime(dt1,'%d-%m-%Y')
#     # dt2=date(2016,2,2)
#     print(dt2)
#     print(type(dt2))
#     # dt3 = datetime.strptime(dt2, "%d/%m/%Y").strftime('%Y-%m-%d')
#     # dt3=datetime.strptime(dt2,'%d-%m-%Y')
#     # print(dt3)
#     # print(type(dt3))
#     dd = []
#     dd.insert(0,dt2)
#     print(dd)
#     # dd=dt2
#     # df = get_bhavcopy(dd[0])
#     # #   # df = get_bhavcopy("09-01-2022")
#     # #
#     # print(df.loc[df['SYMBOL'] == "SBIN"])
#     # print(df.iloc[0])