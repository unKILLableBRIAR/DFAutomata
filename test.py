input_list = []
state = []
dfa_dict = {}

tmp_str = input()
tmp_str2 = input()

for i in range(len(tmp_str)):
    input_list.append(tmp_str[i])

for i in range(len(tmp_str2)):
    state.append(tmp_str2[i])

for item in tmp_str:
    tmp_list = []
    for item_2 in tmp_str2:
        tmp_dict = {item_2: input()}
        tmp_list.append(tmp_dict)
    dfa_dict[item] = tmp_list

print(dfa_dict)