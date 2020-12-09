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

    def data(self):
        return '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.split('\n')

    def test_one(self):
        self.assertEqual(part_one(self.data(), 5), 127)
            
    def test_two(self):
        self.assertEqual(part_two(self.data(), 127), 62)

def check(numbers, window, current):
    candidate = numbers[current]
    for i in range(1,window):
        for j in range (i+1,window+1):
            if (numbers[current-i] + numbers[current-j] == candidate):
                return True
    return False

def part_one(lines, window):
    numbers = [int(n) for n in lines]
    run = True
    current = window
    while check(numbers, window, current):
        current += 1
    return numbers[current]
                
def part_two(lines, candidate):
    numbers = [int(n) for n in lines]
    outer = True
    i = 0
    while outer:
        inner = True
        j = i+1
        while inner:
            logging.debug('{},{}'.format(i,j))
            if candidate == sum(numbers[i:j]):
                logging.debug('{},{}'.format(min(numbers[i:j]),max(numbers[i:j])))
                return (min(numbers[i:j]) + max(numbers[i:j]))
            elif candidate < sum(numbers[i:j]):
                inner = False
            j += 1
        i += 1

if __name__=='__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    print(part_one(lines, 25))
    print(part_two(lines, 556543474))
