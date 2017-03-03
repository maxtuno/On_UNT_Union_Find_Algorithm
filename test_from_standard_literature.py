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
    element = (1 << a) | (1 << b)
    for item in universe:
        if item & element:
            return item
    return 0


def print_universe():
    print(', '.join([bin(element)[2:] for element in universe]))


if __name__ == '__main__':
    union(3, 4)
    print_universe()
    union(4, 9)
    print_universe()
    union(8, 0)
    print_universe()
    union(2, 3)
    print_universe()
    union(5, 6)
    print_universe()
    union(5, 9)
    print_universe()
    union(7, 3)
    print_universe()
    union(4, 8)
    print_universe()
    union(6, 1)
    print_universe()
