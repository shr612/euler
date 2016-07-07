#!/usr/bin/python
# -*- coding: utf-8 -*-
# there are simpler ways to solve this prime number libraries

import unittest
import time

start = time.time()

def getCycle(p, q):
    assert p >= 0
    assert q > 0

    while p >= q:
        p -= q

    if p == 0:
        # p/q is an integer
        return ""

    digits = {} # map rest to digit number
    # for 0.1234567, 1 is the digit #0, 2 digit #1, ...

    i = 0
    cycle = ""
    rest = p

    while True:
        digits[rest] = i
        rest *= 10
        tmp = rest / q
        rest -= tmp*q
        cycle += str(tmp)
        if rest in digits:
            return cycle[digits[rest]:]
        i += 1

def func(maximum=1000):
    maxCycleLength = 0
    number = 1
    for i in xrange(1, maximum +1):
        tmp = len(getCycle(1, i))
        if tmp > maxCycleLength:
            maxCycleLength = tmp
            number = i
    return (number, maxCycleLength)

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_simpleSequences(self):
        self.assertEqual(getCycle(4,2), "")
        self.assertEqual(getCycle(1,6), "6")
        for i in xrange(1,9):
            self.assertEqual(getCycle(i,9), str(i))
        self.assertEqual(getCycle(1,7), "142857")

if __name__ == '__main__':
    #unittest.main()
    print func(1000)

elapsed = time.time() - start

print("solved in %s seconds") % (elapsed)