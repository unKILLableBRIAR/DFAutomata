import csv

f = open('test.csv', 'r')
ls = []
tmp_dict = {}
rdr = csv.reader(f)

start_state = '-'
final_state = '*'

tmp_str = next(rdr)

for item in rdr:
    print(item)

print(start_state)
print(final_state)

f.close()