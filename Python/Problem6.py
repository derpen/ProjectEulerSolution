"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, (1+2+..,+10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

def differenceOfSums(limit):
    sumOfSquare = 0
    squareOfSum = 0
    for i in range(1, limit+1):
        sumOfSquare += i ** 2
        squareOfSum += i

    squareOfSum = squareOfSum ** 2
    difference = squareOfSum - sumOfSquare
    return difference

print(differenceOfSums(100))
