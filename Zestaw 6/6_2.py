import math
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):        # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)
    
    def __eq__(self, other):   # obsługa point1 == point2
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x
        

    def length(self):         # długość wektora
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")
        self.assertEqual(str(Point(0, 0)), "(0, 0)")
        self.assertEqual(repr(Point(0, 0)), "Point(0, 0)")
        self.assertEqual(str(Point(-1, -2)), "(-1, -2)")
        self.assertEqual(repr(Point(-1, -2)), "Point(-1, -2)")
        
    def test_cmp(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertTrue(Point(1, 2) != Point(2, 1))
        self.assertTrue(Point(1, 2) != Point(1, 1))
        self.assertTrue(Point(1, 2) != Point(2, 2))
        self.assertTrue(Point(1, 2) != Point(2, 1))
        self.assertTrue(Point(1, 2) != Point(2, 2))
        
    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(1, 2), Point(2, 4))
        self.assertEqual(Point(1, 2) + Point(0, 0), Point(1, 2))
        self.assertEqual(Point(1, 2) + Point(-1, -2), Point(0, 0))
        self.assertEqual(Point(1, 2) + Point(-1, 2), Point(0, 4))
        self.assertEqual(Point(1, 2) + Point(1, -2), Point(2, 0))
        
    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(1, 2), Point(0, 0))
        self.assertEqual(Point(1, 2) - Point(0, 0), Point(1, 2))
        self.assertEqual(Point(1, 2) - Point(-1, -2), Point(2, 4))
    
    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(1, 2), 5)
        self.assertEqual(Point(1, 2) * Point(0, 0), 0)
        self.assertEqual(Point(1, 2) * Point(-1, -2), -5)
        self.assertEqual(Point(1, 2) * Point(-1, 2), 3)
        self.assertEqual(Point(1, 2) * Point(1, -2), -3)
    
    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(1, 2)), 0)
        self.assertEqual(Point(1, 2).cross(Point(0, 0)), 0)
        self.assertEqual(Point(1, 2).cross(Point(-1, -2)), 0)
        self.assertEqual(Point(1, 2).cross(Point(2, 1)), -3)
        self.assertEqual(Point(1, 2).cross(Point(1, -2)), -4)
    
    def test_length(self):
        self.assertEqual(Point(1, 2).length(), math.sqrt(5))
        self.assertEqual(Point(0, 0).length(), 0)
        self.assertEqual(Point(-1, -2).length(), math.sqrt(5))
        self.assertEqual(Point(-1, 2).length(), math.sqrt(5))
        self.assertEqual(Point(1, -2).length(), math.sqrt(5))
    
     
if __name__ == "__main__":
    unittest.main()     # wszystkie testy
                              
