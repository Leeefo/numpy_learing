

n = int(input("Enter a number : "))


def is_prime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            return prime
    return prime


print(is_prime(n))
