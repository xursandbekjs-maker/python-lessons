# 1 + 2 + 3 + 4 + ... + n
# import math
# n = int(input())
# s = 0
# for number in range(1, n + 1):
#     s += int(math.sqrt(number)) # s = s + number

# print(s)
n = int(input())
s = 1
for number in range(1, n + 1):
    s += number # s = s + number

print(s)
# Example: n = 5
# Sikl qadamlari:
# number = 1; 0 + 1 = 1 = s
# number = 2; 1 + 2 = 3 = s
# number = 3; 3 + 3 = 6 = s 
# number = 4; 6 + 4 = 10 = s
# number = 5; 10 + 5 = 15 = s