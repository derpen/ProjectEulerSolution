"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# Very Slow, be Patient

def prime(limit):

    print("Calculating...")

    for i in range(2, 999999999):
        if limit == 0:
            return NthPrime
        isPrime = True
        for j in range(2, ((i//2)+1), 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime == True:
            limit -= 1
            NthPrime = i

    return NthPrime

print(prime(10001))
