def is_prime(n: int) -> bool:
    """Return True if n is a prime number, else False."""
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

def primes_up_to(limit: int):
    """Generate all prime numbers up to the given limit (inclusive)."""
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

# Example usage:
if __name__ == "__main__":
    limit = 50
    print(f"Prime numbers up to {limit}:")
    for p in primes_up_to(limit):
        print(p, end=" ")
    print()