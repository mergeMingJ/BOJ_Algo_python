inputs = "cbacdcbc"

string = list(inputs)
ordering = sorted(inputs)
result = []
answer = ""


for order in ordering:
    count = ordering.count(order)
    if count == 1:
        result.append(order)

for char in string:
    if string.count(char) > 1:
        string.remove(char)
        print(string)

print(string)

if b < c:
    print(true)

