# DECORATORS defination:

# In DECORATOR'S function's are taken as arugment  into  another fucntion  and then called inside the wrapper function

# This is the 2nd Decorators example
def hello_decorator(wrap):
    def inner1(*args, **kwargs): # defining 2 argument for inner1 function
        print(" this is before execution of the wrapper function")
        value = wrap(*args, **kwargs) # wrapper function
        print("sum of two number is : ", wrap.__name__)
        print("This is after execution of the wrapper function")
        return value
    return inner1

@hello_decorator
def sum_of_two_value(a,b): # defining fucntion for addition of 2 number
    summ = a + b
    return summ

a = 1
b = 2
print("sum of two number is : ", sum_of_two_value(a,b)) # this is the sum of the
