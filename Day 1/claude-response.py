def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes(start, end):
    """Return a list of prime numbers in the given range."""
    return [n for n in range(start, end + 1) if is_prime(n)]


def print_primes(start, end):
    """Print all prime numbers between start and end."""
    primes = get_primes(start, end)
    if not primes:
        print(f"No prime numbers found between {start} and {end}.")
    else:
        print(f"Prime numbers between {start} and {end}:")
        print(primes)
        print(f"Total count: {len(primes)}")


# --- Run it ---
print_primes(1, 50)


RESULT:
Prime numbers between 1 and 50:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Total count: 15