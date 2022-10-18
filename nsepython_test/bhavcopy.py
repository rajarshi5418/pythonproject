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

empty_dataframe = pd.DataFrame()
for i in list3:
    # print(i)
    df = get_bhavcopy(i)
    df1= df.loc[df['SYMBOL'] == "SBIN"]
    empty_dataframe = pd.concat([empty_dataframe,df1])
print(empty_dataframe)
del_per=empty_dataframe.mean()
print(del_per)
