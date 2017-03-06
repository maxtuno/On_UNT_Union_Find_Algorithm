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

class USTCONN:
    def __init__(self):
        self.universe = []

    def __str__(self):
        paths = ''
        for item in self.universe:
            paths += '{}, '.format(self.nary(item))
        return paths

    def nary(self, n):
        s = ''
        while n:
            s += str(n % 2)
            n //= 2
        return [idx for idx in range(len(s)) if s[idx] == '1']

    def union(self, a, b):
        element = (1 << a) | (1 << b)
        idx = 0
        while idx != len(self.universe):
            if self.universe[idx] & element:
                element |= self.universe[idx]
                del self.universe[idx]
                idx -= 1
            idx += 1
        self.universe.append(element)

    def connected(self, a, b):
        for item in self.universe:
            if (item & (1 << a)) and (item & (1 << b)):
                return item
        return 0

    def make_set(self, a):
        self.union(a, a)

    def find(self, a):
        return self.connected(a, a)


if __name__ == '__main__':

    import time
    import random

    import matplotlib.pyplot as plt    

    sizes = 1000

    unions = []

    for size in range(sizes):
        data = [(random.randint(0, size), random.randint(0, size)) for _ in range(size)]
        ustconn = USTCONN()
        ini = time.time()
        for a, b in data:
            ustconn.union(a, b)
        end = time.time()
        unions.append(end - ini)

    connections = []

    for size in range(sizes):
        data = [(random.randint(0, size), random.randint(0, size)) for _ in range(size)]
        ustconn = USTCONN()
        ini = time.time()
        for a, b in data:
            ustconn.connected(a, b)
        end = time.time()
        connections.append(end - ini)

    plt.figure(figsize=(8, 8))
    plt.title('UNION CONNECTED UNT ALGORITHM\nTIME(s) vs SIZE\nUNION(r)/CONNECTION(b)')
    plt.plot(range(len(unions)), unions, 'r-')

    plt.plot(range(len(connections)), connections, 'b-')
    plt.savefig('unions_connections.png')
