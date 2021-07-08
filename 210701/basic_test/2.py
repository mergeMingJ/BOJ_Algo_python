# 2. "SAFFY JOB FAIR" 단어를 뒤집는 함수를 하나 구현
# "SAFFY JOB FAIR" -> "FAIR JOB SAFFY"

string = "SAFFY JOB FAIR"
arr = list(string)

word = ''
stack = []
ans = ''

for char in arr:
    if char == ' ':
        stack.append(word)
        word = ''
    else:
        word += char
stack.append(word)


for i in range(len(stack)):
    ans += stack.pop(-1)
    if len(stack) != 0:
        ans += ' '

print(ans)

