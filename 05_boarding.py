import sys
import unittest
import re
from operator import itemgetter
import argparse
import traceback


class TestStuff(unittest.TestCase):

        
    def data(self):
        return [("FBFBBFFRLR",44,5,357),
                    ("BFFFBBFRRR", 70,7,567),
                    ("FFFBBBFRRR",14,7,119),
                    ("BBFFBBFRLL",102,4,820)]

    def test_one(self):
         cards = self.data()
         for card in cards:
             code, row, seat, seat_id = card
             self.assertTrue(calculate_id(code),seat_id)
            
def debug(arg):
    pass
#    print arg

def calculate_id(code):
    row,col = decode(code)
    return (row * 8) + col

def decode(code):
    row = int(code[:7].replace('F','0').replace('B','1'),2)
    col = int(code[7:].replace('L','0').replace('R','1'),2)
    return (row, col)
    
def parse(lines):
    cards = []
    for i in range(0,len(lines)):
        card = decode(lines[i])
        cards.append(card)
    
def part_one(codes):
    return max(calculate_id(code) for code in codes)
            
def part_two(codes):
    all_seats = sorted([calculate_id(code) for code in codes])
    for i in range(0,len(all_seats)):
        if i > 0:
            if all_seats[i+1] - all_seats[i] != 1:
                return all_seats[i] + 1

if __name__=='__main__':
    codes = []
    for line in sys.stdin:
        codes.append(line.strip())
    print(part_one(codes))
    print(part_two(codes))
