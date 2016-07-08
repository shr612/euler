import itertools
def is_palindromic(n): n=str(n); return n==n[::-1]

def pal_list(k):
    if k == 1:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return [sum([n*(10**i) for i,n in enumerate(([x]+list(ys)+[z]+list(ys)[::-1]+[x]) if k%2
                                else ([x]+list(ys)+list(ys)[::-1]+[x]))])
            for x in xrange(1, 10, 2)    #check odd numbers only
            for ys in itertools.product(xrange(10), repeat=k/2-1)
            for z in (xrange(10) if k%2 else (None,))]

# return a string of 1s and 0s representing n as a binary number
dec2bin = lambda n: bin(n)[2:]

L, s = 6, 0    # Limit, L, is expressed as maximum number of digits
for k in xrange(1, L+1):
    s += sum(n for n in pal_list(k) if is_palindromic(dec2bin(n)))

print "The sum of all numbers with 6 or fewer digits "
print "that are palindromic in base 10 and 2:", s