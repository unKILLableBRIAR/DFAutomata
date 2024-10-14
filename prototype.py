import csv
import DFAutomata as dfa

f = open('DFAutomata.csv', 'r')
#csv파일을 iterator로 변환
rdr = csv.reader(f)

#makeDFAmap이 rdr을  dictionary, start_state, final_state로 반환해줌
map_start_final = dfa.makeDFAmap(rdr)

dfa_map = map_start_final[0]
start_state = map_start_final[1]
final_state = map_start_final[2]

input_ls = dfa.strToList(input('Please type input values : '))
#input_state의 초기 input은 아무 의미 없음 (state는 중요)
input_state =[0, start_state]
len_input_ls = len(input_ls)

for i in range(len_input_ls):
    input_state[0] = dfa.frontPop(input_ls)
    input_state[1] = dfa_map[input_state[0]][input_state[1]]

    print(input_state)

#마지막 상태와 입력값을 구분하기 위해
for i in range(30):
    print('-', end='')
print('')
print(input_state)

if input_state[1] == final_state:
    print("String is in the Language")
else:
    print("String isn't in the Language")

f.close()