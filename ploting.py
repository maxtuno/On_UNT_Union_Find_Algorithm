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


if __name__ == '__main__':

    import time
    import random

    import matplotlib.pyplot as plt

    size = 10000

    unions = []
    connections = []

    for _ in range(size):
        a, b = random.randint(0, size), random.randint(0, size)

        ini = time.time()
        union(a, b)
        end = time.time()
        unions.append(end - ini)

        ini = time.time()
        connected(a, b)
        end = time.time()
        connections.append(end - ini)

    plt.title('UNION CONNECTED UNT ALGORITHM\nTIME (s) vs SIZE')
    plt.plot(range(len(unions)), unions, 'r-', alpha=0.4)
    plt.plot(range(len(connections)), connections, 'b-', alpha=0.4)
    plt.savefig('union_connected.png')
