print("Calender".center(40, "-"))
months = ['dec', 'aug', 'oct', 'nov', 'sep', 'jan', 'apr', 'mar', 'jul', 'feb', 'jun', 'may']
print(f"months :{months}")
from calendar import month_name
def srt_month(name):
    l = []
    for i in list(month_name):
        l.append(i[0:3].lower())
    return l.index(name)

srtMnts = sorted(months, key=srt_month)
print(f"srtMnts :{srtMnts}")
