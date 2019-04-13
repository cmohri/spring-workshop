nums = []
for x in range(8):
    nums.append(x)
squares = []
for x in range(8):
    squares.append(x**2)

a = [(x, x*x, x*x*x) for x in range(8)]
#print(a)


p = "alksjdfh"
#print ([x for x in p])
#print([x for x in "2134"]) #with this, easy to check for presence in p

UC_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
#print([ x for x in p if x in UC_LETTERS])
#print([1 for x in p if x in UC_LETTERS])
#print ([1 if x in UC_LETTERS else 0 for x in p])


# upper and lower case letters
# at least one number
def first(password):
    UC_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
    LC_LETTERS = UC_LETTERS.lower()
    NUMBERS = "0123456789"
    a = [1 for x in password if x in UC_LETTERS]
    a.extend([2 for x in password if x in LC_LETTERS])
    a.extend([3 for x in password if x in NUMBERS])          
    return 1 in a and 2 in a and 3 in a


# return rating from 1-10 of password strength
def second(password):
    UC_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
    LC_LETTERS = UC_LETTERS.lower()
    NUMBERS = "0123456789"
    a = [1 for x in password if x in UC_LETTERS]
    a.extend([2 for x in password if x in LC_LETTERS])
    a.extend([3 for x in password if x in NUMBERS])
    points = [1 for x in a if x == 2 or x == 3]
    print(points)
    return round((float(len(points)) / len(password) )*10)


print(first("aA1"))
print(second("aA1"))
      



