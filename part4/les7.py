#datetime
from datetime import datetime
dt_now = datetime.now ()
print (dt_now)
dt2 = datetime(2015, 5, 16, 17, 22, 54)
print(dt2)
delta = dt_now - dt2
print (delta)
dt3 = dt2 + delta
print (dt3)
print (dt_now.strftime ('%A %d.%m.%Y %H.%M'))
date_str = '23/12/2010'
date_s = datetime.strptime (date_str, '%d/%m/%Y')
print (date_s)