from math import sqrt
from urllib2 import urlopen
file_url = 'https://projecteuler.net/project/resources/p042_words.txt'
words = [x[1:-1] for x in urlopen(file_url).read().split(',')]

def is_tn(n): return not bool(((sqrt(1 + 8*n) - 1) / 2) % 1)
def score(word): return sum(abs(64 - ord(letter)) for letter in word)

print "Project Euler 42 Solution =", sum(is_tn(score(word)) for word in words)