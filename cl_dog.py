# this is simple example of the class and object
#-----------------------------
# Date = 2/11/2020
# SUB: class and OBJECT
#--------------------------------------------------
class dog: # defining class
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def bark(self):
        print(f"your dog '{self.name}' barks")
    def ag(self):
        print(f"You Pet {self.name} has been aged {self.age} has to be brought to medicial care ")
    def cl(self):
        print(f"your dog {self.name} has a beautiful {self.color}")

na = input("please enter your dog name: ")
ag = int(input("please enter your dog's age: "))
col = input("please enter your dog's color: ")
d = dog(na, ag, col)
"""d.bark()
d.ag()
d.cl()"""
try:
    your_input = int(input(" please provide your dogs actions 1. Bark , 2. Age_for_medicial_care, 3. color"))

    if your_input == 1:
        d.bark()
    elif your_input == 2:
        d.ag()
    elif your_input == 3:
        d.cl()
    else:
        raise Exception
except Exception as e:
        print(" you have entered invaild output")
