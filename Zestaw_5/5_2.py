
def add_frac(frac1, frac2):
    return [ frac1[0]*frac2[1] + frac2[0]*frac1[1] , frac1[1]*frac2[1] ]

def sub_frac(frac1, frac2):
    return [ frac1[0]*frac2[1] - frac2[0]*frac1[1] , frac1[1]*frac2[1] ]

def mul_frac(frac1, frac2):
    return [ frac1[0]*frac2[0] , frac1[1]*frac2[1] ]

def div_frac(frac1, frac2):
    return [ frac1[0]*frac2[1] , frac1[1]*frac2[0] ]

def is_positive(frac): 
    if frac[0] > 0 and frac[1] > 0:
        return True
    elif frac[0] < 0 and frac[1] < 0:
        return True
    else:
        return False

def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):
    if frac1[0]*frac2[1] > frac2[0]*frac1[1]:
        return 1
    elif frac1[0]*frac2[1] < frac2[0]*frac1[1]:
        return -1
    else:
        return 0

def frac2float(frac):
    return float(frac[0]/frac[1])

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([1, -2]), False)
        self.assertEqual(is_positive([-1, -2]), True)
        
    def test_is_zero(self):
        self.assertEqual(is_zero([0, 1]), True)
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero([-1, 2]), False)
        self.assertEqual(is_zero([1, -2]), False)
        self.assertEqual(is_zero([-1, -2]), False)
    
    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([2, 4], [1, 2]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([1, 3]), 0.3333333333333333)
        self.assertEqual(frac2float([1, 4]), 0.25)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy