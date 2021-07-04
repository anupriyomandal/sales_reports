import datetime
from dt import dt

def fy(PATH):
    year = int('20' + PATH[-6:-4]) - 1
    with open(PATH, 'r', encoding = 'utf-16') as f:
        re = {}
        co = {}
        next(f)
        months = [datetime.datetime(year, i, 1) for i in range(4,13)] + [datetime.datetime(year+1, i, 1) for i in range(1,4)]
        for line in f:
            line = line.split('\t')
            dl = line[2]
            ct = line[15]
            if ct not in co:
                co[ct] = {}
            mt = dt(line[5])
            val = int(line[28].replace(',', ''))
            qt = int(line[-3].replace(',', ''))
            if dl not in re:
                re[dl] = [0]*12
            if dl not in co[ct]:
                co[ct][dl] = [0]*12
            re[dl][months.index(mt)] += val
            co[ct][dl][months.index(mt)] += qt
    return re, co
