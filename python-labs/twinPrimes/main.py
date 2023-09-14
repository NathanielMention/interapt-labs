def is_prime(candidate):
    for num in range(2, candidate):
        if candidate % num == 0:
            return False

    return True


def find_twin_primes(upper_bound):
    twin_primes = []
    for num in range(2, upper_bound):
        second = num + 2
        if is_prime(num) and is_prime(second):
            twin_primes.append((num, second))

    return twin_primes


bound = 1_000
twin_primes = find_twin_primes(bound)


for pair in twin_primes:
    print(f'{pair[0]} and {pair[1]} are twins prime')


'''
for prime1,prime2 in twin_primes:  
print(f'{prime1} and {prime2 }) are twin primes

'''
# Comprehension

'''
twin_primes =[(num, num +2) for num in range(2, bound) if ia_prime(num) and is_prime(num+2)]

'''

print(twin_primes)
