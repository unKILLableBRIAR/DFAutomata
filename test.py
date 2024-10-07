import DFAutomata as dfa

dfa_dict = {}

tmp_str = input()
tmp_str2 = input()
start_state = input()
#final state가 1개라고 가정하고
final_state = input()

input_list = dfa.strToList(tmp_str)
state = dfa.strToList(tmp_str2)

for item in tmp_str:
    dfa_dict[item] = {}
    for item_2 in tmp_str2:
        dfa_dict[item][item_2] = input()

print(f"start : {start_state}\nfinal : {final_state}")
print(dfa_dict)

input_str_list = dfa.strToList(input('Please Type input String\n'))
#input_state의 초기값은 아무 의미 없음
input_state =[0, start_state]

len_input_str_list = len(input_str_list)

#print(input_str_list)
#print(input_state)

for i in range(len_input_str_list):
    input_state[0] = dfa.frontPop(input_str_list)
    input_state[1] = dfa_dict[input_state[0]][input_state[1]]
    #print(input_str_list)
    print(input_state)

print(input_state)

if input_state[1] == final_state:
    print("String is in the Language")
else:
    print("String isn't in the Language")