import sys
import unittest
import re
from operator import itemgetter
import argparse
import traceback

FIELDS_ONE = ["byr", "iyr", "eyr", "hgt",
              "hcl", "ecl", "pid"]

FIELD_PATTERNS = {
    'byr': r'\d{4}',
    'iyr': r'\d{4}',
    'eyr': r'\d{4}',
    'hgt': r'(\d{2}in)|(\d{3}cm)',
    'hcl': r'#[0-9a-f]{6}',
    'ecl': r'^amb|blu|brn|gry|grn|hzl|oth$',
    'pid': r'^(\d{9})$'}
    

OPTIONAL = ["cid"]

class TestStuff(unittest.TestCase):

    def invalids(self):
        return ["eyr:1972 cid:100",
                    "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
                    "",
                    "iyr:2019",
                    "hcl:#602927 eyr:1967 hgt:170cm",
                    "ecl:grn pid:012533040 byr:1946",
                    "",
                    "hcl:dab227 iyr:2012",
                    "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
                    "",
                    "hgt:59cm ecl:zzz",
                    "eyr:2038 hcl:74454a iyr:2023",
                    "pid:3556412378 byr:2007"]

    def valids(self):
         return ["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
             "hcl:#623a2f",
             "",
             "eyr:2029 ecl:blu cid:129 byr:1989",
             "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
             "",
             "hcl:#888785",
             "hgt:164cm byr:2001 iyr:2015 cid:88",
             "pid:545766238 ecl:hzl",
             "eyr:2022",
             "",
             "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"]
        
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
         self.assertTrue(True)

    def test_four(self):
         passports = parse(self.invalids())
         for passport in passports:
             self.assertFalse(valid_two(passport))

    def test_five(self):
        passports = parse(self.valids())
        for passport in passports:
            self.assertTrue(valid_two(passport))

            
def debug(arg):
#    pass
    print arg

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


def field_validation(passport, field):
    try:
        m = re.match(FIELD_PATTERNS[field], passport[field])
        if not m:
            return False
        if field == 'byr':
            year = int(passport[field])
            return year >= 1920 and year <= 2002
        if field == 'iyr':
            year = int(passport[field])
            return year >= 2010 and year <= 2020
        if field == 'eyr':
            year = int(passport[field])
            return year >= 2020 and year <= 2030
        if field == 'hgt':
            # dddcm or ddin
            hgt = passport['hgt']
            if hgt[2] == 'i':
                val = int(hgt[:2])
                return val >=59 and val <= 76
            else:
                val = int(hgt[:3])
                return val >=150 and val <= 193
    except Exception as e:
        return False
    return True
    
def valid_two(passport):
    for field in FIELDS_ONE:
        if not field in passport:
            return False
        if not field_validation(passport, field):
            return False        
    return True

    
def part_one(passports):
    return sum(1 for passport in passports if valid_one(passport))
            
def part_two(passports):
    return sum(1 for passport in passports if valid_two(passport))

if __name__=='__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    passports = parse(lines)
    print(part_one(passports))
    print(part_two(passports))
