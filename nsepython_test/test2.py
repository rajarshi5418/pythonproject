from nsepython import*
import nsepy
import nsetools
import pandas as pd

# df = nsepython.get_bhavcopy("09-01-2022")
#
# # df2=df.sort_values(by=['NO_OF_TRADES'], ascending=True)
#
# print(df.iat['NO_OF_TRADES'])

# print(dir(nsepy))
# print(dir(nsetools))
# for i in dir(nsepython):
#     print(i)
#     print(dir(i))

print(nse_fiidii())

# print(indices)
#
# # nse_get_fno_lot_sizes("all","pandas"))
#
print(fnolist())
# print(len(fnolist()))
# print(get_preopen_nifty())

# gainers,movers=nse_preopen_movers("NIFTY")
# print(gainers)
# print(movers)
#
# df = nse_most_active(type="securities",sort="value")
# pd.set_option('display.max_column',20)
# print(df)

def nse_optionchain_ltp(payload,strikePrice,optionType,inp=0,intent=""):
    expiryDate=payload['records']['expiryDates'][inp]
    for x in range(len(payload['records']['data'])):
        if((payload['records']['data'][x]['strikePrice']==strikePrice) & (payload['records']['data'][x]['expiryDate']==expiryDate)):
            if(intent==""): return payload['records']['data'][x][optionType]['lastPrice']
            if(intent=="sell"): return payload['records']['data'][x][optionType]['bidprice']
            if(intent=="buy"): return payload['records']['data'][x][optionType]['askPrice']


payload = nse_optionchain_scrapper('BANKNIFTY')
print(payload)
print(nse_optionchain_ltp(payload,40000,"CE",0,"sell"))

payload=nse_optionchain_scrapper('BANKNIFTY')
currentExpiry,dte=nse_expirydetails(payload,1)
print(currentExpiry)
print(dte)


print(payload['records'])
