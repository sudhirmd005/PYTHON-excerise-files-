# this is the Memoization using decorators in python
# DEFINE: Memoization is the technine used for recording of
#         intermediate result so that it can be used to avoid
#         repeated calculation and speed up the program

def memo_dec(f):
    memory = {}
    def fac(num):
        if  num not in memory:
            memory[num] = f(num)
            print(memory)
        return memory[num]
    return fac
@memo_dec
def facto(n):
    if n == 1:
        return 1
    else:
        m = n*facto(n-1)
        return m
print(facto(5))
