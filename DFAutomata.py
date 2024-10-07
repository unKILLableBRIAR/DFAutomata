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