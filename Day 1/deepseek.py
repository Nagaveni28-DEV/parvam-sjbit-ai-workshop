def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to square root
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def print_primes(start, end):
    """Print all prime numbers between start and end"""
    print(f"Prime numbers between {start} and {end}:")
    primes_found = []
    
    for num in range(start, end + 1):
        if is_prime(num):
            primes_found.append(num)
            print(num, end=" ")
    
    if not primes_found:
        print("No prime numbers found in this range")
    else:
        print(f"\nTotal primes found: {len(primes_found)}")

# Example usage
print_primes(1, 100)


RESULT:
Prime numbers between 1 and 100:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Total primes found: 25