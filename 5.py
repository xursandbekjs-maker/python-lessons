# 1 + 2 + 3 + 4 + ... + n
n = int(input())
s = 0
for number in range(1, n + 1):
    s += number # s = s + number

print(s)