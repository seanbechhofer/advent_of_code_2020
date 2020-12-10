import sys
import unittest
import re
import argparse
import logging
import functools
import aoc
from machine import Machine

logging.basicConfig(format='%(levelname)s:\n%(message)s', level=logging.INFO)

class TestStuff(unittest.TestCase):

    def data_one(self):
        return '''16
10
15
5
1
11
7
19
6
12
4'''.split('\n')

    def data_two(self):
            return '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.split('\n')

    def test_one(self):
        self.assertEqual(part_one(self.data_one()), 35)
            
    def test_two(self):
        self.assertEqual(part_one(self.data_two()), 220)

def part_one(lines):
    numbers = [0] + sorted([int(n) for n in lines])
    diffs = [0,0,0,0]
    for i in range(1,len(numbers)):
        diffs[numbers[i] - numbers[i-1]] += 1
    # add a 3 for the end
    diffs[3] += 1
    logging.debug('{}'.format(diffs))
    return diffs[1] * diffs[3]
                      
                
def part_two(lines):
    return 0

if __name__=='__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    print(part_one(lines))
    print(part_two(lines))
