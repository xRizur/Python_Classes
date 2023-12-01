class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y < 0:
            x, y = -x, -y
        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 1:
            return "{}".format(self.x)
        else:
            return "{}/{}".format(self.x, self.y)

    def __repr__(self):
        return "Frac({}, {})".format(self.x, self.y)

    def __cmp__(self, other):  # cmp(frac1, frac2)    # Py2
        return (self.x * other.y > self.y * other.x) - (self.x * other.y < self.y * other.x)

    def __eq__(self, other):
        return self.x * other.y == self.y * other.x

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.x * other.y < self.y * other.x
    
    def __le__(self, other):
        return self.x * other.y <= self.y * other.x

    def __gt__(self, other):
        return self.x * other.y > self.y * other.x

    def __ge__(self, other):
        return self.x * other.y >= self.y * other.x

    def __add__(self, other):
        return Frac(self.x * other.y + self.y * other.x, self.y * other.y)

    def __sub__(self, other):
        return Frac(self.x * other.y - self.y * other.x, self.y * other.y)

    def __mul__(self, other):
        return Frac(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Frac(self.x * other.y, self.y * other.x)

    def __truediv__(self, other): 
        return Frac(self.x * other.y, self.y * other.x)

    def __floordiv__(self, other): pass  # frac1 // frac2, opcjonalnie
    

    def __mod__(self, other): pass  # frac1 % frac2, opcjonalni

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):      # float(frac)
        return float(self.x) / float(self.y)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    
        def setUp(self): pass
    
        def test_print(self):
            self.assertEqual(str(Frac(1, 2)), "1/2")
            self.assertEqual(str(Frac(2, 1)), "2")
            self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")
            self.assertEqual(repr(Frac(2, 1)), "Frac(2, 1)")
    
        def test_cmp(self):
            self.assertTrue(Frac(1, 2) == Frac(1, 2))
            self.assertTrue(Frac(1, 2) != Frac(2, 1))
            self.assertTrue(Frac(1, 2) < Frac(2, 1))
            self.assertTrue(Frac(1, 2) <= Frac(2, 1))
            self.assertTrue(Frac(2, 1) > Frac(1, 2))
            self.assertTrue(Frac(2, 1) >= Frac(1, 2))
    
        def test_add_frac(self):
            self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
            self.assertEqual(Frac(1, 2) + Frac(1, 4), Frac(3, 4))
    
        def test_sub_frac(self):
            self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
            self.assertEqual(Frac(1, 2) - Frac(1, 4), Frac(1, 4))
    
        def test_mul_frac(self):
            self.assertEqual(Frac(1, 2) * Frac(1, 3), Frac(1, 6))
            self.assertEqual(Frac(1, 2) * Frac(1, 4), Frac(1, 8))
    
        def test_div_frac(self):
            self.assertEqual(Frac(1, 2) / Frac(1, 3), Frac(3, 2))
            self.assertEqual(Frac(1, 2) / Frac(1, 4), Frac(2, 1))
        
        def test_pos_frac(self):
            self.assertEqual(+Frac(1, 2), Frac(1, 2))
            self.assertEqual(+Frac(-1, 2), Frac(-1, 2))
        
        def test_neg_frac(self):
            self.assertEqual(-Frac(1, 2), Frac(-1, 2))
            self.assertEqual(-Frac(-1, 2), Frac(1, 2))
        
        def test_invert_frac(self):
            self.assertEqual(~Frac(1, 2), Frac(2, 1))
            self.assertEqual(~Frac(-1, 2), Frac(-2, 1))
        
        def test_float_frac(self):
            self.assertEqual(float(Frac(1, 2)), 0.5)
            self.assertEqual(float(Frac(-1, 2)), -0.5)
        
        def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy