import nsetools
from nsetools import Nse
nse = Nse()
list1=dir(nse)
for i in list1:
    print(i)

print(nse.get_index_list())
print(nse.get_index_quote("NIFTY 50"))
print(nse.get_stock_codes())
print(nse.get_fno_lot_sizes("SBIN"))



