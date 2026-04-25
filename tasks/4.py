lst = (30, 3)
for i in range(lst[0], lst[1] - 1, -1):
    if i % 3 == 0:
        print(i, end=" ")