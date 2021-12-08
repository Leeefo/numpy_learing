def is_prime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            return prime
    return prime


def prime_list(n):
    prime_list = [1]
    for i in range(2, n):
        if is_prime(i):
            prime_list.append(i)
    print(prime_list)


prime_list(100)
