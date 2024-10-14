# string을 int로 변환하여 list에 저장하는 함수
def strToList(str):
    ls = []
    i = 0

    while i < len(str):
        ls.append((str[i]))
        i += 1

    return ls


# ls에서 제일 앞 요소 반환 후 삭제연산
def frontPop(ls):
    result = ls[0]
    del ls[0]
    return result

#CSV파일에서 읽은 iterator를 딕셔너리로 변환
def makeDFAmap(total_csv):
    #각 인풋값을 list로 지정
    key_str = next(total_csv)
    frontPop(key_str)

    start_state = '-'
    final_state = '*'
    dfa_map = {}

    for item in key_str:
        dfa_map[item] = {}

    for item in total_csv:
        tmp_key = frontPop(item)

        if start_state == '-':
            if '-' in tmp_key:
                tmp_key = tmp_key[0]
                start_state = tmp_key
        elif final_state == '*':
            if '*' in tmp_key:
                tmp_key = tmp_key[0]
                final_state = tmp_key

        for item2 in key_str:
            dfa_map[item2][tmp_key] = frontPop(item)

#dfa를 딕셔너리로 만들고, start_state와 final_state까지 list로 반환
    return [dfa_map, start_state, final_state]