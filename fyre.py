import csv
import datetime
from dt import dt

def fy(PATH):
    year = int('20' + PATH[-6:-4]) - 1
    with open(PATH, 'r', encoding = 'utf-16') as f:
        csv_reader = csv.reader(f, delimiter = '\t')
        next(csv_reader)
        months = [datetime.datetime(year, i, 1) for i in range(4,13)] + [datetime.datetime(year+1, i, 1) for i in range(1,4)]
        re = {}
        re['val'] = {}
        f = lambda x: int(x.replace(',',''))
        for line in csv_reader:
            dl, ct, mt, val, qt = line[2], line[15], dt(line[5]), f(line[-2]), f(line[-3])
            re[ct] = {}
            if dl not in re[ct]:
                re[ct][dl] = [0]*12
            if dl not in re['val']:
                re['val'][dl] = [0]*12
            re['val'][dl][months.index(mt)] += val
            re[ct][dl][months.index(mt)] += qt
    return re