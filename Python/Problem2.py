""" Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

 By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. """

def Fibonacci():
    i,j = 1,2
    sum = 0
    while(True):
        if j > 4000000:
            break
        if j % 2 == 0:
            sum += j
        i,j = j, i+j
    print(sum)

Fibonacci()