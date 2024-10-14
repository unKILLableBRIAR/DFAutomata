import csv
import DFAutomata as dfa

f = open('test.csv', 'r')
ls = []
dfa_map = {}
rdr = csv.reader(f)

start_state = '-'
final_state = '*'

#리스트에서 딕셔너리의 키값 추출
key_str = next(rdr)
dfa.frontPop(key_str)

for item in key_str:
    dfa_map[item] = {}

for item in rdr:
    tmp_key = dfa.frontPop(item)

    if start_state == '-':
        if '-' in tmp_key:
            tmp_key = tmp_key[0]
            start_state = tmp_key
    elif final_state == '*':
        if '*' in tmp_key:
            tmp_key = tmp_key[0]
            final_state = tmp_key

    for item2 in key_str:
        dfa_map[item2][tmp_key] = dfa.frontPop(item)

print(start_state)
print(final_state)

print(dfa_map)

f.close()