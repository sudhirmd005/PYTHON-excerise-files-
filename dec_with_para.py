# This is the example of decorators with parameter
import time
def deccorator_parameter(*args, **kwargs):
    begin = time.time()
    print(" this is the inital start of the decorator parameter")
    def inside(argu): # defining the wrapper function inside the decorator function
        print(" this is begining of the wrapper function")
        argu() # call of another function inside wrapper function
        print(" this is the decorator argument we were talking about", kwargs['about'])
        end = time.time()
        print(" end of the wrapper function", argu.__name__, end - begin)

    return inside

@deccorator_parameter( about = "exmaple of deccorator_parameter")
def funv():
    print(" this text is printed inside the wrapper function")
