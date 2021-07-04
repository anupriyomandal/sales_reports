import colorama
import os
import csv
import datetime
import shutil
from colorama import Fore, Back, Style

colorama.init()

def l():
    print('-' * 50)
src = '/home/anupriyo/Downloads/'
des = '/home/anupriyo/Documents/Programming/current_month.csv'
os.chdir(src)


files = os.listdir(src)
for file in files:
    if file == 'Sheet_1_(5)_crosstab.csv':
        print('File Found')
        shutil.move(file, des)

re = {}
with open(des, 'r', encoding = 'utf-16') as f:
    csv_reader = csv.reader(f, delimiter = '\t')
    cols = {col: i for i, col in enumerate(next(csv_reader))}
    RO = [0, 0]
    for line in csv_reader:
            t, d, v = line[17], line[5], line[28]
            if t not in re:
                re[t] = [0, 0]
            re[t][1] += int(v.replace(',',''))
            RO[1] += int(v.replace(',',''))
            dt = datetime.datetime.strptime(d, "%m.%d.%Y")
            if dt.date() == datetime.datetime.today().date():
                re[t][0] += int(v.replace(',',''))
                RO[0] += int(v.replace(',',''))

l()
print(Fore.BLUE + '{:<30s}{:>10s}{:>10s}'.format('Territory', 'Today', 'MTD'))
l()
for t in sorted(re):
    print(Fore.GREEN + '{:<30s}{:>10.2f}{:>10.2f}'.format(t, *map(lambda x: x * 10**-5, re[t])))
l()
print(Fore.CYAN + '{:<30s}{:>10.2f}{:>10.2f}'.format('RO', *map(lambda x: x * 10**-5, RO)))
l()