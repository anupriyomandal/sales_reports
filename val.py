from fyre import fy
import csv
import time

t0 = time.perf_counter()

fy21c, fy21 = fy('/home/anupriyo/Documents/Programming/Dumps/fy21.csv')
fy22c, fy22 = fy('/home/anupriyo/Documents/Programming/Dumps/fy22.csv')

cus = {}
with open('/home/anupriyo/Documents/Programming/Dumps/customer_master.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for line in csv_reader:
        cus[line[0]] = line[1], line[2]

dealers = sorted(set([*fy21c.keys()] + [*fy22c.keys()]), key = lambda x: cus[x][1])

for d in dealers:
    print('{:<10s}{:<50s}{:<8s}{:>8.2f}{:>8.2f}{:>8.2f}'.format(d, cus[d][0], cus[d][1], sum(fy21c[d][2:])/10 * 10 **-5, sum(fy22c[d][:3])/3 * 10**-5 if d in fy22c else 0, fy22c[d][2] * 10**-5 if d in fy22c else 0))
t1 = time.perf_counter()

print('Done in {:0.2f} secs'.format(t1-t0))
