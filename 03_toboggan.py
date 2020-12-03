import sys
import unittest
import re
from operator import itemgetter

class TestStuff(unittest.TestCase):
    def mmap(self):
        return ["..##.......",
                "#...#...#..",
                ".#....#..#.",
                "..#.#...#.#",
                ".#...##..#.",
                "..#.##.....",
                ".#.#.#....#",
                ".#........#",
                "#.##...#...",
                "#...##....#",
                ".#..#...#.#"]

    def test_one(self):
        self.assertTrue(tree((2,0),self.mmap()))
        
    def test_two(self):
        point = (0,0)
        point = move_one(point)
        self.assertFalse(tree(point,self.mmap()))

    def test_two(self):
        point = (14,0)
        self.assertTrue(tree(point,self.mmap()))

    def test_three(self):
        point = (15,0)
        self.assertFalse(tree(point,self.mmap()))
        
    def test_four(self):
        self.assertEqual(part_one(self.mmap()), 7)

    def test_five(self):
        point = (0,1)
        self.assertTrue(tree(point,self.mmap()))
        

def debug(arg):
#    pass
    print arg

# Part One

def move_one(point):
    x,y = point
    return (x+3, y+1)

def square(point, lines):
    x,y = point
    line = lines[y]
    index = x % len(line)
    return line[index]
    
def tree(point,lines):
    return square(point, lines) == '#'

def part_one(lines):
    debug(len(lines))
    trees = 0
    x,y = (0,0)
    while y < len(lines):
        debug("{} {}".format((x,y), square((x,y), lines)))
        if tree((x,y), lines):
            trees += 1
        x,y = move_one((x,y))
    return trees
    
if __name__=='__main__':
#    unittest.main()
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    print(part_one(lines))
