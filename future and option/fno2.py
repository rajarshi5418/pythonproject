import pandas as pd
import validators

a="https://archives.nseindia.com/content/nsccl/fao_participant_oi_"

b=str("12092022").zfill(8)
print(b)
c=".csv"

for i in range(1,31):
    dat = i*1000000
    dat1 = str(int(b)+dat).zfill(8)
    dat2 = a+dat1+c
    print(dat2)

    valid = validators.url(dat2)
    if valid == True:
        fno = pd.read_csv(dat2)

        df = pd.DataFrame(fno)
        df2 = df.rename(columns=df.iloc[0]).loc[1:]
        pd.set_option('display.max_columns', 15)
        print(df2)
    else:
        continue






