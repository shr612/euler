L = 1000
d = 10  # last d digits of series
s = sum(pow(n, n) for n in range(1, L + 1))

print "Project Euler 48 Solution = %010d" % (s % 10 ** d)