import pandas as pd

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

a="https://archives.nseindia.com/content/nsccl/fao_participant_oi_"

b=str("12092022").zfill(8)
print(b)
c=".csv"

for i in range(1,31):
    dat = i*1000000
    dat1 = str(int(b)+dat).zfill(8)
    dat2 = a+dat1+c
    print(dat2)

    validate = URLValidator()
    value = request.GET.get(dat2, None)
    if value:
        try:
            validate(value)
            fno = pd.read_csv(dat2)

            df=pd.DataFrame(fno)
            df2 = df.rename(columns=df.iloc[0]).loc[1:]
            pd.set_option('display.max_columns', 15)
            print(df2)
        except ValidationError:
            print("holiday")




