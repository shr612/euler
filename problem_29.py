import time

# L = [] # old version with a list
L = set()  # new version with a set

limit = 101

start = time.time()

for a in range(2, limit):
    for b in range(2, limit):
        c = a ** b
        if c in L: pass
        # else: L.append(c) # old list version
        L.add(c)  # new version with set

elapsed = time.time() - start

print "found %s ints in %s seconds" % (len(L), elapsed)