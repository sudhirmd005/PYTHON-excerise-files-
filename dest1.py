# EXAMPLE OF DESTRUCTION
class A:
    def __init__(self):
        print(" this is second phase")
        self.c = C
    def __del__(self):
        print(" this is seconds phase")

class B:
    def __init__(self):
        print(" this is first phase")
        self.c = A
    def __del__(self):
        print(" this is first phase")

class C:
    def __init__(self):
        print(" this is third phase")
    def __del__(self):
        print(" this is call of destruction: end of phase")

def fu():
    ab = B()
    a = A()
    ac = C()

fu()
