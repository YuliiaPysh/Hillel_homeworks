def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def prime_numbers(start, end):
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            yield num


start = 1
end = 100

print(f"Found prime numbers from the range {start}:{end}:")
for num in prime_numbers(start, end):
    print(num, end=", ")
