import csv

# Dictionary used to tabulate results
potholes_by_block = {}

f = open('potholes.csv', 'r')
for row in csv.DictReader(f):
    status = row['STATUS']
    address = row['STREET ADDRESS']
    if status == 'Open':
        box = address.split(' ')
        block = box[0]
        box[0] = block[:-3]+'XXX'
        street = ' '.join(box)
        if street not in potholes_by_block :
            potholes_by_block[street] = 1
        else:
            potholes_by_block[street] += 1
            
#array to keep results
num_potholes = []

for num in potholes_by_block.keys():
    num_potholes.append((potholes_by_block[num],num))

num_potholes.sort(reverse=True)

for num,street in num_potholes[:5]:
    print(num,'potholes in',street[5:],'Street')