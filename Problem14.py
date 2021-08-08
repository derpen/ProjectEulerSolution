"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz(limit):
    print("Calculating...") # Not optimized, slow
    longestChain = 0
    result = 0
    for i in range(limit, -1, -1):
        currentNumber = i
        chain = 1
        if i == 1:
            break
        while currentNumber != 1:
            if currentNumber % 2 == 0:
                currentNumber = currentNumber / 2
                chain += 1
            else:
                currentNumber = 3 * currentNumber + 1
                chain += 1
        if chain > longestChain:
            longestChain = max(longestChain, chain)
            result = i

    return result

print(collatz(1000000))
