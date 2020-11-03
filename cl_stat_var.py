""" this is the demonstation of static and class variables in python
 DEFINE  CLASS are like blueprint and OBJECT are like the copy of the CLASS with actual values

 OBJECT CONSIST OF STATE , BEHAVIOUR AND IDENTITY
        WHERE STATE : respresents the attribute of OBJECT
        BEHVIOUR : represents methods of OBJECT
        IDENTITY: respresents uinque name we provide to an OBJECT
# EXAMPLE :
conside a class DOG

    IDENTITY            |             STATE     |   BEHAVIOUR
   [Name of the dog]    |  [Breed, age, color]  | [Bark, Sleep, Eat, Run]

NOTE: A CLASS can have more than one OBJECT.
DEFINE: SELF: class method must have one extra argument as self which is defined while defining
              function or method. We dont call it during call method

        __init__ method: this is similar to the constructor in C++ and java.
                        method is useful if you want to so any modification or changes in the class ClassName(object):


                            def __init__(self, arg):
                                super(, self).__init__()
                                self.arg = arg


DEFINE: In python is simple unlike java and C++ where they use static keyword to DEFINE
           variables for the class. Where it is not the same for python, variables defined
           inside the class are class variables and which are defined inside the method
           are called instance variables"""
import datetime
class student:

    def __init__(self, stream ="ECE", domain ="Engineering"):
        self.stream = stream
        self.domain = domain

    def display(self):
        print(f"*******Welcome to {self.domain} Domain*********")
        print(f"you have you have selected '{self.stream}' as your main stream in {self.domain}" )

candidate = student()
print("------------------------------------")
print(datetime.datetime.now())
print("-----------------------------------")
print(f" STREAM SELECTED : {candidate.stream}")
print(f" DOMAIN SELECTED : {candidate.domain}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
candidate.display()
