import sys
import unittest
import re
from operator import itemgetter
import argparse
import logging
import functools
import aoc
from machine import Machine

logging.basicConfig(format='%(levelname)s:\n%(message)s', level=logging.INFO)

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
            
    def test_two(self):
        self.assertTrue(part_two(self.data()), 8)

def part_one(lines):
    m = Machine()
    m.run(lines)
    return m.trace[-2][1]
                
def part_two(lines):
    program = lines
    for i in range(0, len(lines)):
        new_program = program.copy()
        (instruction, arg) = new_program[i].split(' ')
        if instruction == 'nop':
            new_program[i] = 'jmp {}'.format(arg)
        elif instruction == 'jmp':
            new_program[i] = 'nop {}'.format(arg)
        m = Machine()
        if (m.run(new_program)):
            return m.accumulator
    return None

if __name__=='__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    print(part_one(lines))
    print(part_two(lines))
