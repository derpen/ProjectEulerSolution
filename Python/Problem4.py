"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def isPalindrome(digit):

    highestDigit = int("9" * digit)
    lowestDigit = int("1" + ("0" * (digit - 1)))
    palindrome = 0

    for num1 in range(int(highestDigit), -1, -1):
        for num2 in range(int(highestDigit), lowestDigit, -1):
            checkIfPalindrome = num1 * num2
            if str(checkIfPalindrome) == str(checkIfPalindrome)[::-1]:
                if checkIfPalindrome > palindrome:
                    palindrome = checkIfPalindrome

    return palindrome

print(isPalindrome(3))
