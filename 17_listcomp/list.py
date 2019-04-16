# Clara Mohri

import copy

# 1

def loop1():
    l = []
    num = 0
    while num < 10:
        l.append(2*str(num))
        num += 2
    return l

print(loop1())

def comp1():
    return [ 2*str(x) for x in range(0, 10, 2)]

print(comp1())

# 2

def loop2():
    l = []
    for i in range(7, 48, 10):
        l.append(i)
    return l

print(loop2())

def comp2():
    return [x for x in range(7, 48, 10)]

print(comp2())

# 3

def loop3():
    l = []
    for i in range(0, 9):
        l.append( int(i/3) *( i%3))
    return l

print(loop3())

def comp3():
    return [ (int(x/3)) * (x%3) for x in range (0, 9)]

print(comp3())


# 4
# composites

def loop4():
    l = []
    for i in range(0, 101):
        val = False
        for x in range(2, i):
            if i % x == 0:
                val = True
                break
        if val:
            l.append(i)

    return l

print(loop4())

def comp4():
    return [ x for x in range(0, 101) if 0 in [ x%i for i in range(2, x)]]

print(comp4())


# 5
# primes

def loop5():
    l = []
    for i in range(0, 101):
        val = all (i% x != 0 for x in range(2, i) )
        # another way: (uncomment, intialize val in line above to True)
        '''if i > 2:
            for x in range(2, i):
                if i % x == 0:
                    val = False
                    break'''
        if val:
            l.append(i)
    return l

print(loop5())

def comp5():
    return [ x for x in range(0, 101) if all(x%i != 0 for i in range(2, x))]

print(comp5())


# 6
# all divisors

def loop6(num):
    l = []
    if num > 2:
        for x in range(1, num):
            if num % x == 0:
                l.append(x)
    return l

print(loop6(10))
print(loop6(60))

def comp6(num):
    return [ x for x in range(1, num) if num % x == 0]

print(comp6(10))
print(comp6(60))

# 7
# matrix transposition

def loop7(matrix):
    new = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        row = matrix[i]
        for x in range(len(row)):
            new[x][i] = row[x]
    return new

a = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

print(loop7(a))

def comp7(matrix):
    return [[row[x] for row in matrix] for x in range(len(matrix))]

print(comp7(a))

