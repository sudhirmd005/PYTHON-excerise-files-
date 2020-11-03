# This is the DECORATOR example
import time
import math
def calculate_time(func):
    # defining a inner1 function which wil have a wrapper function within it
    def inner1(*args, **kwargs): # this inner1 function takes 2 arguments * args and *kargs as we have only provided only 1 arugment from fact(num)
        begin = time.time()
        print(" the wrapper function")
        print(" begin of time and call of function")
        func(*args, **kwargs)
        end = time.time()
        print("function call has been completed --  end of time", func.__name__, end-begin)
    return inner1

@calculate_time
def fact(num):
    print(math.factorial(num))

fact(10)
