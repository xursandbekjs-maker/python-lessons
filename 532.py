
def filter_primes(sequence):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return filter(is_prime, sequence)

# Tekshirish uchun:
print(list(filter_primes([11, 1, 10, 9, 2, 5, 4]))) # Natija: [11, 2, 5]
