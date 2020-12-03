import sys
import unittest

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertEqual(calculate([1721,979,366,299,675,1456]),514579)
        
def debug(arg):
    pass
    #print arg

def calculate(list):
    for i in range(0,len(list)):
        for j in range(i+1, len(list)):
            if (list[i] + list[j]) == 2020:
                return list[i] * list[j]
    return 0
                    
if __name__=='__main__':
#    unittest.main()
    numbers = []
    for line in sys.stdin:
        num = int(line.strip())
        numbers.append(num)
    print(calculate(numbers))
