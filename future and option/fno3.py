from nsepy import get_history
from datetime import date, timedelta

end_day = date.today()
start_day = end_day - timedelta(365)

df = get_history(symbol="JSWSTEEL", start=start_day, end=end_day)
dat = df.index

date_set = []

for i in dat:
    # print(i)
    # print(type(i))
    j=str(i)
    str1 = j[-2]
    str2 = j[-1]
    str3 = j[-5]
    str4 = j[-4]
    str5 = j[0]
    str6 = j[1]
    str7 = j[2]
    str8 = j[3]
    string = str1+str2+str3+str4+str5+str6+str7+str8
    # print(string)
    date_set.append(string)

print(date_set)