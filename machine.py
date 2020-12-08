import sys
import unittest
import re
from operator import itemgetter
import argparse
import logging
import functools
import aoc

# Instructions

ACC = 0
JMP = 1
NOP = 2

class Machine:

    def dump(self):
        self.debug(self.memory)
        self.debug("pc: {}".format(self.counter))
        self.debug("rb: {}".format(self.base))
    
    def __init__(self):
        # Program
        self.program = []
        # Accumulator
        self.accumulator = 0
        # program counter
        self.pc = 0
        self.trace = []

    def __repr__(self):
        return ('Acc: {}\nPC:  {}\nPro: {}\nTrace: {}'.format(self.accumulator, self.pc, self.program, self.trace))

    def set_program(self,lines):
        self.program = self.parse_program(lines)
        self.accumulator = 0
        # program counter
        self.pc = 0
        self.trace = []

    def parse_program(self,lines):
        prog = []
        for line in lines:
            instruction, arg = line.split(' ')
            prog.append((instruction, int(arg)))
        return prog

    def execute_instruction(self):
        instruction, arg = self.program[self.pc]
        logging.debug('{} {}'.format(instruction, arg))
        if instruction == 'nop':
            self.pc += 1
        elif instruction == 'acc':
            self.accumulator += arg
            self.pc += 1
        elif instruction == 'jmp':
            self.pc += arg
        self.trace.append((self.pc,self.accumulator))
    

    
