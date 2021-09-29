"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def powerdigitsum(power):
    num = str(2 ** power)
    total = 0
    for i in range(0, len(num)):
        total += int(num[i])
    return total

print(powerdigitsum(1000))
