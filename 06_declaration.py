import sys
import unittest
import re
from operator import itemgetter
import argparse
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class TestStuff(unittest.TestCase):

    def data(self):
        return ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b"]

    def test_one(self):
         declarations = parse(self.data())
         self.assertEquals(part_one(declarations),11)

def parse(lines):
    declarations = []
    declaration = set()
    for i in range(0,len(lines)):
        if lines[i] == "":
            declarations.append(declaration)
            declaration = set()
        else:
            logging.debug(lines[i])
            for character in lines[i]:
                declaration.add(character)
    declarations.append(declaration)
    logging.debug(declarations)
    return declarations
        
def part_one(declarations):
    return sum(len(declaration) for declaration in declarations)
            
def part_two(declrations):
    return 0


if __name__=='__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    declarations = parse(lines)
    print(part_one(declarations))
    print(part_two(declarations))
