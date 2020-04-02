import datetime as dt

t = (3,30,2019,9,25)

date = dt.datetime(year=t[2], month=t[3], day=t[-1], hour=t[0], minute=t[1])
print (date) # 2019-09-25 03:30:00
print (date.strftime("%m/%d/%Y, %H:%M:%S")) # 09/25/2019, 03:30:00
