def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def find_primes(up_to):
    primes = []
    for num in range(2, up_to + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
number = int(input("Enter a number: "))
prime_numbers = find_primes(number)
print("Prime numbers up to", number, "are:")
print(prime_numbers)
