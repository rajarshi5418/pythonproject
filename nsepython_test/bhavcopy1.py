import nsepython
from nsepython import*
from datetime import date,timedelta,datetime
import pandas as pd
from nsepy import get_history
from datetime import date, timedelta

end_day = date.today()
start_day = end_day - timedelta(20)

df = get_history(symbol="JSWSTEEL", start=start_day, end=end_day)
dat = df.index
print(dat)

list3=[]
for j in dat:
    dt2 = datetime.strftime(j, '%d-%m-%Y')
    list3.append(dt2)
print(list3)

fno_list = fnolist()

for k in range(3):
    fno_list.pop(0)
    fno_list=fno_list

for j in fno_list:
    print(j)
    df_set1 = pd.DataFrame()
    for i in list3:

        df = get_bhavcopy(i)

        df1= df.loc[(df['SYMBOL'] == j) & (df[' SERIES'] != "EQ")]

        df_set1 = pd.concat([df_set1,df1])


    if len(df_set1)==14:
        print(df_set1)

