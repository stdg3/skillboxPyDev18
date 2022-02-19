
import time
print(time.gmtime(0))

print(time.time())

start = time.monotonic()
huge_number = 2**10000000
elapsed = time.monotonic() - start
print(f"gecen zaman {elapsed} sn")

import datetime
# date time ile oynamak için genel kütüphane, saat yok içinde

x_dogum_gunu = datetime.date(year=1991, month=9, day=1)
print(f"typeOf: {type(x_dogum_gunu)}, atanan tarih{x_dogum_gunu}")

x_dogum_gunu_saat = datetime.time(hour=15, minute=55, second=32)

print(f"saat aq{x_dogum_gunu_saat} yada ayır {x_dogum_gunu_saat.minute}")

x_tarih_saat_karma = datetime.datetime(year=2022, month=1, day=30, hour=00, minute=45)
print(f"data time mixed {x_tarih_saat_karma} ayrı komponentine erişme imkanı: {x_tarih_saat_karma.minute}")
print(f"bu gunden halo{datetime.datetime.now()}")

# formatı değiştirmek için strftime()

print(f"strftime -> {x_tarih_saat_karma.strftime('%d#%m.%y !')}")

# strptime() str ve kuralları alıp datetime obsjesi döndermekte

kuralliTartihAtama = datetime.datetime.strptime("2030.12.15", "%Y.%m.%d")
print(f"str to dateTime {kuralliTartihAtama}, çek {kuralliTartihAtama.day}")

kombineolayi = datetime.datetime.combine(x_dogum_gunu, x_dogum_gunu_saat)
print(f"combined date time : {kombineolayi} type: {type(kombineolayi)}")

# aritmatik işlemler sonrası timedelta type'a dönüşür

su_an = datetime.datetime.now()
# su_an = datetime.datetime(year=2022, month=2, day=15)
x_dogum_gunu = datetime.datetime(year=1997, month=8, day=29, hour=10, minute=14)
x_dt_yas_kac = su_an - x_dogum_gunu

print(f"x suan {x_dt_yas_kac} yasında ve {x_dt_yas_kac.days} sn kadar yasli, type!!{type(x_dt_yas_kac)}")

manual_timeDelta = datetime.timedelta(weeks=40)
print(x_dt_yas_kac - manual_timeDelta)
