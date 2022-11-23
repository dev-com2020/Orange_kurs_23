import time
from datetime import date, datetime
import calendar as c
import arrow

from _zoneinfo import ZoneInfo

print("Raz dwa...")
# time.sleep(2)
print("trzy...")
print(time.gmtime())
print(time.strftime("Mamy %Y rok", time.gmtime()))
dzis = date.today()
print(dzis)
krotka = dzis.year, dzis.month, dzis.day
print(krotka)
# print(c.month(2022, 12))
print(arrow.utcnow())
print(arrow.now())
rzym = arrow.now('America/Los_Angeles')
print(rzym)