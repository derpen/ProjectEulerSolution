"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sumOfPrimes(num):
    primeNumbers = []
    for i in range(num+1):
        primeNumbers.append(i)

    primeNumbers[0] = 0
    primeNumbers[1] = 0

    p = 2
    while(p * p <= num):
        if p != 0:
            for i in range(p*2, num+1, p):
                primeNumbers[i] = 0

        p += 1

    sumOfAll = 0

    for i in range(len(primeNumbers)):
        if primeNumbers[i] != 0:
            sumOfAll += primeNumbers[i]

    return sumOfAll

print(sumOfPrimes(2000000))
