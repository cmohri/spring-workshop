def repeat(string):
    return lambda x: x * string

print(repeat("cool")(3))
r1 = repeat("hello")
print(r1(2))
r2 = repeat("goodbye")
print(r2(2))

"""
def outer():
    x = "foo"
    def inner():
        #nonlocal x
        x = "bat"
    inner()
    return x

print(outer())
"""

def outer():
    x =	"foo"
    def	inner():
        nonlocal x                                                                                        
        x = "bat"
    inner()
    return x

print(outer())


def make_counter():
    x = 0
    def inc():
        nonlocal x
        x += 1
        return x
    return inc
    
