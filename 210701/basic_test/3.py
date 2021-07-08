# 3. floatToString 함수를 구현
# 필요한 가정은 스스로 하시기 바랍니다.
# 문제가 어려운 경우 integerToString으로 대체 해 풀어주시기 바랍니다.

# 10.23 -> "10.23"
# -10.909 -> "-10.909"

n = 10.23

def floatToString(n):
    s = str(n)
    print(type(s))
    return s

floatToString(n)
