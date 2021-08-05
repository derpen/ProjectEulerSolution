"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagoreanTriplet():
    for m in range(1, 999):
        for n in range(1, m):
            a = (m**2) - (n**2)
            b = 2 * n * m
            c = (n**2) + (m**2)
            if a + b + c == 1000:
                return a, b, c

print(pythagoreanTriplet())
