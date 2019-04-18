def pythagoreanTriples(n):
    return [(s1, int(((h * h) - (s1 * s1)) ** 0.5), h) for h in range(1, n + 1) for s1 in range(1, h) if (((h * h) - (s1 * s1)) ** 0.5) % 1 == 0 and (h * h) - (s1 * s1) >= s1 * s1]


def quicksort(l):
    return [[x for x in l if x < l[a]] + [l[a]] + [x for x in l if x > l[a]] for a in range(len(l))][0]
    # didn't work


    #worked with PMAN


def quicksort1(list):
    if len(L) <= 1:
        return L
    pivot = random.choice(L)
