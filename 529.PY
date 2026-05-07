# map(func, iterable)
def map_divisors_count(son):
    count = 0
    # natural bo'luvchilari = 0, 1, 2, ... 9, ... son
    for i in range(1, son + 1):
        if son % i == 0:
            count += 1

    return count

print(map_divisors_count(10)) # 4
print(map_divisors_count(-2)) # 0