# string을 int로 변환하여 list에 저장하는 함수
def strToList(str):
    ls = []
    i = 0

    while i < len(str):
        ls.append(int(str[i]))
        i += 1

    return ls


# ls에서 제일 앞 요소 반환 후 삭제연산
def frontPop(ls):
    result = ls[0]
    del ls[0]
    return result


# 기본
str = input()
ls = strToList(str)
i = 0

# DFA의 구조 start = A, final = C
state = ['A', 'B', 'C']

current_state_input = {'STATE': 'A', 'INPUT': 0}

while i < len(ls):
    if current_state_input['STATE'] == state[0]:
        if current_state_input['INPUT'] == 0:
            current_state_input['STATE'] = state[1]
            current_state_input['INPUT'] = frontPop(ls)
        else:
            current_state_input['INPUT'] = frontPop(ls)

    elif current_state_input['STATE'] == state[1]:
        if current_state_input['INPUT'] == 0:
            current_state_input['STATE'] = state[2]
            current_state_input['INPUT'] = frontPop(ls)
        else:
            current_state_input['STATE'] = state[0]
            current_state_input['INPUT'] = frontPop(ls)

    else:
        current_state_input['INPUT'] = frontPop(ls)

if current_state_input['STATE'] == state[2]:
    print("String is in the Language")
else:
    print("String isn't in the Language")