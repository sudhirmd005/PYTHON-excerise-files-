"""
Prerequisites : Constructors are generally used for instantiating an object.The task of constructors is to
                initialize(assign values) to the data members of the class when an object of class is created.
                In Python the __init__() method is called the constructor and is always called when an object is created.

Syntax of constructor declaration :

def __init__(self):
    # body of the constructor
Types of constructors :
default constructor :The default constructor is simple constructor which doesn’t accept any arguments.
                    It’s definition has only one argument which is a reference to the instance being constructed.
parameterized constructor :constructor with parameters is known as parameterized constructor.
                        The parameterized constructor take its first argument as a reference to the instance
                        being constructed known as self and the rest of the arguments are provided by the programmer.
"""
"""# class definiation
class music:
    # defining constructor without parameters
    def __init__(self):
        self.artist = "A.R.RAHAMAN", " SHAWN MENDICES", "SCAM-1992"
    def display(self):
        print(f" you have selected {self.artist} as your artisit")
m = music()
m.display()"""

#--------------------------------------------------------------------------------------------
# class definiation
"""class music:
    # defining constructor with parameters
    def __init__(self, artist):
        self.artist = artist
    def display(self):
        print(f" you have selected {self.artist} as your artisit")

m = music("A.R.RAHMAN")
mn = music(" SHAWN MENDICES")
mb= music("SCAM-1992")
m.display()
mn.display()
mb.display()"""

#------------------------------------------------------------
# class definiation
class adition:
    # defining constructor with parameters
    def __init__(self, f,s):
        self.first_number = f
        self.second_number = s
    def addition(self):
        self.ans = self.first_number + self.second_number
        print(f"the additon of two number's {self.first_number} and {self.second_number} is {self.ans}")

a = adition(124569874552556565656565665333236598989, 789546121877788598988998786466144698787)
a.addition()
