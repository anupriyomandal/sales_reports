import csv

re = {}
with open('/home/anupriyo/Documents/Programming/Dumps/fy21.csv', 'r', encoding = 'utf-16') as f:
    csv_reader = csv.reader(f, delimiter = '\t')
    for line in csv_reader:
        re[line[2]] = line[3], line[18]

with open('/home/anupriyo/Documents/Programming/Dumps/fy22.csv', 'r', encoding = 'utf-16') as f:
    csv_reader = csv.reader(f, delimiter = '\t')
    for line in csv_reader:
        re[line[2]] = line[3], line[18]

with open('/home/anupriyo/Documents/Programming/Dumps/customer_master.csv', 'w') as f:
    csv_writer = csv.writer(f)
    for c in re:
        csv_writer.writerow([c, *re[c]])
