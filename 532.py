def filter_prime(sequence):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return filter(is_prime, sequence)

print(list(filter_prime([5, -8, 5, 0, 12, -5])))