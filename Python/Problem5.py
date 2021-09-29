"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
def evenlyDivisible(numRange):

    smallestNumber = 2520
    checkList = [11, 13, 14, 16, 17, 18, 19, 20]
    print("Calculating...")

    while True:
        if all(smallestNumber % n == 0 for n in checkList):
            break
        smallestNumber += 2520

    return smallestNumber

print(evenlyDivisible(20))
