import sys
import unittest
import re
from operator import itemgetter

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertTrue(valid(decode("1-3 a: abcde")))

    def test_two(self):
        self.assertFalse(valid(decode("1-3 b: cdefg")))

    def test_three(self):
        self.assertTrue(valid(decode("2-9 c: ccccccccc")))

    def test_four(self):
        lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        self.assertEqual(part_one(lines), 2)

    def test_five(self):
        self.assertTrue(valid_two(decode("1-3 a: abcde")))

    def test_six(self):
        self.assertFalse(valid_two(decode("1-3 b: cdefg")))

    def test_seven(self):
        self.assertFalse(valid_two(decode("2-9 c: ccccccccc")))

    def test_eight(self):
        lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        self.assertEqual(part_two(lines), 1)

def debug(arg):
    pass
    #print arg

# Part One

def valid(spec):
    count = spec[3].count(spec[2])
    debug("{} {}".format(spec, count))
    return (count >= int(spec[0]) and count <= int(spec[1]))

def valid_two(spec):
    one = spec[3][int(spec[0])-1]
    two = spec[3][int(spec[1])-1]
    return (one == spec[2]) != (two == spec[2])

def decode(line):
    m = re.match('(?P<_0>.+)-(?P<_1>.+) (?P<_2>.+): (?P<_3>.+)', line)
    spec = map(itemgetter(1), sorted(m.groupdict().items()))
    debug(spec)
    return spec

def part_one(lines):
    return sum(1 for l in lines if valid(decode(l)))

def part_two(lines):
    return sum(1 for l in lines if valid_two(decode(l)))

if __name__=='__main__':
#    unittest.main()
    lines = []
    for line in sys.stdin:
        lines.append(line)
    print(part_one(lines))
    print(part_two(lines))
