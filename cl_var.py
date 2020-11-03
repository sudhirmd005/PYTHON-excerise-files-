# instance variable and class variable
""" DEFINE : INSTANCE variable can be accessable inside the each instances where as
             class variable can be accessible through out the class
             Instance variables are variables whose value is assigned inside
             a constructor or method with 'self' whereas class variables are variables
             whose value is assigned in the class."""

# defining a class
class pet:
    family = 'animal'
    def __init__(self, name, age, category):
        self.name = name
        self.age = age
        self.category = category
    def pet_details(self):
        print(f" you pet's name is {self.name}, \n and it is {self.age} years old and it is a {self.family} .\n it belongs to a category of {self.category} ")

#p = pet ("motu", 6, "carnivours")  for one time entry
# if user want to change the entry every time then we need to modify the code
try:
    check = int(input(" Press 1 if your pet is an animal: "))

    if check == 1:
        print("your PET is an animal")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        mane = input("please enter your Pet's name: ")
        ag = int(input("please enter your Pet's age: "))
        cat = input("please enter your Pet's category: ")
        p = pet (mane, ag, cat)
        p.pet_details()
        print(p.family)
    else:
        raise Exception
except Exception as e:
    print(" your have a pet which is not a animal category")
