try:
    num = int(input("please enter a number to find a factorial : "))
except:
    print(" you have entered a string")
def facto(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else:
        enum = num*facto(num-1)
        return enum

print(f" the factorial of {num} is : {facto(num)}")
