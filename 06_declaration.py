import sys
import unittest
import re
from operator import itemgetter
import argparse
import logging
import functools
import aoc

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class TestStuff(unittest.TestCase):

    def data(self):
        return ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b"]

    def test_one(self):
         self.assertEquals(part_one(self.data()),11)

    def test_two(self):
         self.assertEquals(part_two(self.data()),6)

def parse(lines, operator):
    groups = aoc.blocks(lines)
    logging.debug(groups)
    groups_as_sets = [[set(g) for g in group] for group in groups]
    logging.debug(groups_as_sets)
    collapsed_groups = [reduce(operator, g) for g in groups_as_sets]
    logging.debug(collapsed_groups)
    return collapsed_groups

def part_one(lines):
    declarations = parse(lines,lambda a, b: a.union(b))
    return sum(len(declaration) for declaration in declarations)
            
def part_two(lines):
    declarations = parse(lines,lambda a, b: a.intersection(b))
    return sum(len(declaration) for declaration in declarations)

if __name__=='__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    print(part_one(lines))
    print(part_two(lines))
