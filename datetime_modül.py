import locale
print(locale.setlocale(locale.LC_ALL,""))

from datetime import datetime

simdi = datetime.now()

print(simdi)
print(simdi.year,simdi.month,simdi.day,simdi.hour,simdi.minute,simdi.second,simdi.microsecond,end="\n\n")

print(datetime.ctime(simdi),end="\n\n")

print(datetime.strftime(simdi,"%Y %B %A %X %D"),end="\n\n")

saniye_cinsinden_zaman = datetime.timestamp(simdi)
print(saniye_cinsinden_zaman)

print(datetime.fromtimestamp(saniye_cinsinden_zaman),end="\n\n")

tarih = datetime(2018,9,3)
fark = simdi - tarih

print(fark)
print(fark.days,fark.seconds,fark.microseconds)
