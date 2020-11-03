"""
Destructors are called when an object gets destroyed. In Python, destructors are not needed as
 much needed in C++ because Python has a garbage collector that handles memory management automatically.
The __del__() method is a known as a destructor method in Python.
It is called when all references to the object have been deleted i.e when an object is garbage collected.
Syntax of destructor declaration :

def __del__(self):
  # body of destructor

Note : A reference to objects is also deleted when the object goes out of reference or when the program ends.
"""
"""class dest:
    def __init__(self):
        print(" EMployee created")
    def __del__(self):
        print(" destructor has been called and its end of object created.")
o = dest()
del o"""
#-------------------------------------------------------------------------------------------------------
"""
This example gives the explanation of above mentioned note.
Here, notice that the destructor is called after the ‘Program End…’ printed.
"""
"""
class employee:
    def __init__(self):
        print(" employee is created")

    def __del__(self):
        print(" destruction has been called and end of the program")

def emp_d():
    print(" start of the program")
    o = employee()
    print(" fucntion is over")
    return o
print(" start of process")
oo = emp_d()
print(" end of process")
"""
#-------------------------------------------------------------------------------------------------

# Python program to illustrate destructor
class A:
    def __init__(self, bb):
        print("hello")
        self.a = bb
class B:
    def __init__(self):
        self.a = A
    def __del__(self):
        print(" program destroy")
def fu():
    b = B()
fu()

"""
In this example when the function fun() is called, it creates an instance of class B
which passes itself to class A, which then sets a reference to class B and resulting
in a circular reference.

Generally, Python’s garbage collector which is used to detect these types of
cyclic references would remove it but in this example the use of custom destructor
marks this item as “uncollectable”.

Simply, it doesn’t know the order in which to destroy the objects, so it leaves them.
Therefore, if your instances are involved in circular references they will live in
memory for as long as the application run.
"""
