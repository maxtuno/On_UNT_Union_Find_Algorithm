"""
        copyright (c) 2012-2017 Oscar Riveros. all rights reserved.
                           oscar.riveros@peqnp.com

    without any restriction, Oscar Riveros reserved rights, patents and
  commercialization of this knowledge or derived directly from this work.

http://twitter.com/maxtuno 
http://klout.com/maxtuno 
http://independent.academia.edu/oarr

A O(n) UNT ALGORITHM FOR THE UNION-FIND PROBLEM
https://www.academia.edu/31682983/A_O_n_UNT_ALGORITHM_FOR_THE_UNION-FIND_PROBLEM
"""

universe = []


def union(a, b):
    element = (1 << a) | (1 << b)
    idx = 0
    while idx != len(universe):
        if universe[idx] & element:
            universe[idx] |= element
            element = universe[idx]
            del universe[idx]
            idx -= 1
        idx += 1
    universe.append(element)


def connected(a, b):
    for item in universe:
        if (item & (1 << a)) and (item & (1 << b)):
            return item
    return 0


def print_universe():
    print(', '.join([bin(element)[2:] for element in universe]))


if __name__ == '__main__':
    print(connected(1, 2))
    union(1, 2)
    print(connected(1, 2))
    print_universe()
    print(connected(2, 3))
    union(2, 3)
    print_universe()
    print(connected(2, 3))
    print(connected(2, 4))
    union(2, 4)
    print(connected(2, 4))
    print_universe()
    print(connected(4, 5))
    union(4, 5)
    print(connected(4, 5))
    print_universe()
    print(connected(4, 6))
    union(4, 6)
    print(connected(4, 6))
    print_universe()
    print(connected(6, 7))
    union(6, 7)
    print(connected(6, 7))
    print(connected(6, 8))
    print_universe()
    union(6, 8)
    print(connected(6, 8))
    print_universe()
    n = connected(1, 8)
    print(n, bin(n)[2:])
    print(connected(1, 9))
    print(connected(0, 10))
