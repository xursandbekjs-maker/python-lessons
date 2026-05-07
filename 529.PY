# map(func, iterable)
def map_divisors_count(son):
    count = 0
    # natural bo'luvchilari = 0, 1, 2, ... 9, ... son
    for i in range(1, son + 1):
        if son % i == 0:
            count += 1

    return count

def map_divisors_count(sequence):
    return map(lambda x: map_divisors_count(x), sequence)

print(list(map_divisors_count([10, -2]))) # [4, 0]