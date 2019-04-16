# Clara Mohri with XPMAN
# April 16, 2019


def union(l1,l2):
    return [x for x in set(l1+l2)]

def intersect(l1,l2):
    return [x for x in l1 if x in l2]

l1 = [1,2,3]
l2 = [2,3,5]

p1 = [1,5,11]
p2 = [2,3,4]

print(union(l1,l2))
print(intersect(l1,l2))

print(union(p1,p2))
print(intersect(p1,p2))

def setdiff(l1, l2):
    return  [x for x in  l1 if x not in l2]

def symdiff(l1, l2):
    return [x for x in (l1+l2) if (l1 + l2).count(x) == 1]

def cartprod(l1, l2):
    return [[x,y] for x in a for y in b]
