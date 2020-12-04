import sys
import unittest
import re
from operator import itemgetter
import argparse

FIELDS_ONE = ["byr", "iyr", "eyr", "hgt",
              "hcl", "ecl", "pid"]

OPTIONAL = ["cid"]

class TestStuff(unittest.TestCase):
    
    def data(self):
        return ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
                    "byr:1937 iyr:2017 cid:147 hgt:183cm",
                    "",
                    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
                    "hcl:#cfa07d byr:1929",
                    "",
                    "hcl:#ae17e1 iyr:2013",
                    "eyr:2024",
                    "ecl:brn pid:760753108 byr:1931",
                    "hgt:179cm",
                    "",
                    "hcl:#cfa07d eyr:2025 pid:166559648",
                    "iyr:2011 ecl:brn hgt:59in"]

    def data2(self):
        return ["byr:1985",
                    "eyr:2021 iyr:2011 hgt:175cm pid:163069444 hcl:#18171d",
                    "",
                    "eyr:2023",
                    "hcl:#cfa07d ecl:blu hgt:169cm pid:494407412 byr:1936",
                    "",
                    "ecl:zzz",
                    "eyr:2036 hgt:109 hcl:#623a2f iyr:1997 byr:2029",
                    "cid:169 pid:170290956",
                    "",
                    "hcl:#18171d ecl:oth",
                    "pid:266824158 hgt:168cm byr:1992 eyr:2021"]

    def test_one(self):
        passports = parse(self.data())
        self.assertTrue(valid_one(passports[0]))
        self.assertFalse(valid_one(passports[1]))
        self.assertTrue(valid_one(passports[2]))
        self.assertFalse(valid_one(passports[3]))

    def test_two(self):
        passports = parse(self.data())
        self.assertEqual(part_one(passports), 2)

    def test_three(self):
        passports = parse(self.data2())
        print(passports)
        self.assertTrue(True)

def debug(arg):
    pass
#    print arg

def parse(lines):
    passports = []
    passport = {}
    for i in range(0,len(lines)):
        if lines[i] == "":
            passports.append(passport)
            passport = {}
        else:
            for component in lines[i].split(' '):
                key, value = component.split(':')
                passport[key] = value
    passports.append(passport)
    return passports

def valid_one(passport):
    for field in FIELDS_ONE:
        if not field in passport:
            return False
    return True

def part_one(passports):
    return sum(1 for passport in passports if valid_one(passport))
            
if __name__=='__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    print(part_one(parse(lines)))
