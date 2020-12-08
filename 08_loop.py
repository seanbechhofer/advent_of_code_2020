import sys
import unittest
import re
from operator import itemgetter
import argparse
import logging
import functools
import aoc
from machine import Machine

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

class TestStuff(unittest.TestCase):

    def data(self):
        return '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')

    def test_one(self):
        self.assertTrue(part_one(self.data()), 5)
            

def part_one(lines):
    m = Machine()
    m.set_program(lines)
    run = True
    while run:
        m.execute_instruction()
        (last_pc, last_acc) = m.trace[-1]
        for i in range(0,len(m.trace) -1):
            if m.trace[i][0] == last_pc:
                run = False
    return m.trace[-2][1]
            
def part_two(lines):
    return None

if __name__=='__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    print(part_one(lines))
    print(part_two(lines))
