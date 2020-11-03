# this is an example of fiboonic serires
# printing a fiboonic series below are the 15 fiboonic series:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
#987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...
"""
def fibo(n):
    a = 0
    b = 1
    sum = 0
    for i in range(0, n):
        print(sum , end =' ')
        a = b
        b = sum
        sum = a + b
"""
# NOTE : ALTERNATE EXAMPLE FOR THE SAME:
# Function for nth fibonacci number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1
def fib(n):
    a = 0
    b = 1
    sum = 0
    if n <= 0:
        return print(" INVALID INPUT")
    elif (n >= 0) and (n<=1):
        return b
    else:
        for i in range(0,n):
            print(sum, end = " ")#if you want to start from 0 instead of 1 as per o/p : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
            a = b
            b = sum
            sum = a + b
            #print(sum, end = " ") #if you want to start from 1 instead of 0 as per o/p : 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610


n = int(input(" Please enter a number for fiboonic series : "))
fib(n)
