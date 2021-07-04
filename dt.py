from datetime import datetime
from datetime import timedelta

def dt(d):
    d = datetime.strptime(d, '%m.%d.%Y')
    x = d + timedelta(days = 2)
    y = datetime(x.year, x.month, 1)
    return y