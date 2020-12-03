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
        
def debug(arg):
    pass
    #print arg

# Part One

def valid(spec):
    count = spec[3].count(spec[2])
    debug("{} {}".format(spec, count))
    return (count >= int(spec[0]) and count <= int(spec[1]))

def decode(line):
    m = re.match('(?P<_0>.+)-(?P<_1>.+) (?P<_2>.+): (?P<_3>.+)', line)
    spec = map(itemgetter(1), sorted(m.groupdict().items()))
    debug(spec)
    return spec

def part_one(lines):
    return sum(1 for l in lines if valid(decode(l)))

if __name__=='__main__':
#    unittest.main()
    lines = []
    for line in sys.stdin:
        lines.append(line)
    print(part_one(lines))
