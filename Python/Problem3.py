"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def primeFactor(number):

    for i in range(2, number):

        biggestPrimeFactor = number

        if number / i == 1:
            break

        if number % i == 0:
            number = int(number / i)

    return biggestPrimeFactor
        
print(primeFactor(600851475143))
