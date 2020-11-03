# This is the example of the decorator with parameter with the @decorator call method
import datetime
def deccorator(x, y):
    print("BEGINNING OF THE PROCEDURE")
    def inner_fun():
        print(" START OF THE PROCEDURE ")
        date = datetime.datetime.now()
        print(f"Today's date is : {date}" )
        print(f" summation of 2 number {x}, and {y} is : {x+y}")
        print(" END OF THE PROCEDURE")
        print("*******************************")
    return inner_fun()

def addition(*args):
    for element in args:
        print(f"{element}". split (" ") )
deccorator(1,2),(addition)('this', 'is',' the' ,'text' ,'msg')
