'''
Clara Mohri
SoftDev2 Pd06
K22 -- Closure
2019-05-01
'''

def repeat(string):
    return lambda x: x * string

print(repeat("cool")(3))
r1 = repeat("hello")
print(r1(2))
r2 = repeat("goodbye")
print(r2(2))

'''
def outer():
    x =	"foo"
    def	inner():
        nonlocal x                                                                                        
        x = "bat"
    inner()
    return x

print(outer())

'''
def make_counter():
    x = 0
    def inc():
        nonlocal x
        x += 1
        return x
    def access():
        nonlocal x
        return x
    return( inc, access)
    
ctr1, acc1 = make_counter()

print(ctr1())
print(acc1())
print(ctr1())
print(ctr1())
print(ctr1())
print(ctr1())
print(acc1())
