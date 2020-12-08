import sys
import unittest
import re
from operator import itemgetter
import argparse
import logging
import functools
import aoc

class Machine:

    def __init__(self):
        # Program
        self.program = []
        # Accumulator
        self.accumulator = 0
        # program counter
        self.pc = 0
        self.trace = []

    def __repr__(self):
        pro = '\n'.join(['{} {:+d}'.format(i,a) for (i,a) in self.program])
        tra = '\n'.join(['{}'.format(t) for t in self.trace])
        return ('Acc: {}, PC:  {}\n{}\n{}'.format(self.accumulator, self.pc, pro, tra))

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
        if instruction == 'nop':
            self.pc += 1
        elif instruction == 'acc':
            self.accumulator += arg
            self.pc += 1
        elif instruction == 'jmp':
            self.pc += arg
        self.trace.append((self.pc,self.accumulator))

    # Load and run a program. Will terminate when the program counter goes
    # beyond the program length or a loop is detected.
    def run(self, program):
        self.set_program(program)
        while True:
            # pc goes beyond program
            if self.pc == len(program):
                return True
            self.execute_instruction()
            (last_pc, last_acc) = self.trace[-1]
            for i in range(0,len(self.trace) -1):
                # Loop detection
                if self.trace[i][0] == last_pc:
                    return False

    
