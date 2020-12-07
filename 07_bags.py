import sys
import unittest
import re
from operator import itemgetter
import argparse
import logging
import functools
import aoc

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

class TestStuff(unittest.TestCase):

    def data(self):
        return ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
                    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                    "bright white bags contain 1 shiny gold bag.",
                    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                    "faded blue bags contain no other bags.",
                    "dotted black bags contain no other bags."]

    def data_2(self):
        return ["shiny gold bags contain 2 dark red bags.",
                    "dark red bags contain 2 dark orange bags.",
                    "dark orange bags contain 2 dark yellow bags.",
                    "dark yellow bags contain 2 dark green bags.",
                    "dark green bags contain 2 dark blue bags.",
                    "dark blue bags contain 2 dark violet bags.",
                    "dark violet bags contain no other bags."]

    def test_one(self):
        bags = parse(self.data())
        logging.debug(bags)
        self.assertEqual(part_one(self.data()), 4)

    def test_two(self):
        bags = parse(self.data())
        logging.debug(bags)
        self.assertEqual(part_two(self.data_2()), 126)

class Bag():
    def __init__(self, colour, content_list, bags):
        self.colour = colour
        self.contents = {}
        self.bags = bags
        for (n,col) in content_list:
            self.contents[col] = n

    def __repr__(self):
        return "{} {}".format(self.colour,self.contents)

    def contains(self, colour):
        if colour in self.contents.keys():
            return True
        else:
            for c in self.contents.keys():
                if self.bags[c].contains(colour):
                    return True
        return False

    def bag_count(self):
        count = 1;
        for colour in self.contents.keys():
            count += (self.bags[colour].bag_count() * self.contents[colour])
        return count
        
def parse(lines):
    bags = {}
    for line in lines:
        h, t = line.split(' contain ')
        head = h[:-5]
        tails = t[:-1].split(', ')
        tails = [re.sub(' bag(s)?','',t) for t in tails]
        logging.debug("{}:{}".format(head,tails))
        contents = []
        if tails[0] != 'no other':
            for t in tails:
                (n,adj,col) = t.split(' ')
                contents.append((int(n), adj + ' ' + col))
        logging.debug("{}:{}".format(head,contents))
        bags[head] = Bag(head, contents, bags)
    return bags

def part_one(lines):
    bags = parse(lines)
    count = 0
    for c in bags.keys():
        if bags[c].contains('shiny gold'):
            logging.debug(c)
            count += 1
    return count
            
def part_two(lines):
    bags = parse(lines)
    return bags['shiny gold'].bag_count() - 1

if __name__=='__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    print(part_one(lines))
    print(part_two(lines))
