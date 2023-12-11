class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Mianownik nie może być zerem.")
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}/{self.y}" if self.y != 1 else f"{self.x}"

    def __repr__(self):
        return f"Frac({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = Frac(other)
        return self.x * other.y == self.y * other.x

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            other = Frac(other)
        return self.x * other.y > self.y * other.x

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            other = Frac(other)
        return self.x * other.y < self.y * other.x

    def __le__(self, other):
        return self < other or self == other


    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Frac(other)
        return Frac(self.x * other.y + self.y * other.x, self.y * other.y)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Frac(other)
        return Frac(self.x * other.y - self.y * other.x, self.y * other.y)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = Frac(other)
        return other - self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Frac(other)
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = Frac(other)
        if other.x == 0:
            raise ValueError("Nie można dzielić przez zero.")
        return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            other = Frac(other)
        if self.x == 0:
            raise ValueError("Nie można dzielić przez zero.")
        return other / self

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        if self.x == 0:
            raise ValueError("Nie można wykonać operacji odwrotności na zerowym liczniku.")
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash((self.x, self.y))



import unittest

class TestFrac(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Frac(5, 1), Frac(5))
        self.assertEqual(Frac(0, 1), Frac(0))
        with self.assertRaises(ValueError):
            Frac(1, 0)

    def test_str(self):
        self.assertEqual(str(Frac(3, 4)), "3/4")
        self.assertEqual(str(Frac(5, 1)), "5")

    def test_repr(self):
        self.assertEqual(repr(Frac(3, 4)), "Frac(3, 4)")

    def test_eq(self):
        self.assertTrue(Frac(1, 2) == Frac(1, 2))
        self.assertFalse(Frac(1, 2) == Frac(3, 4))
        self.assertTrue(Frac(2, 4) == Frac(1, 2))

    def test_ne(self):
        self.assertTrue(Frac(1, 2) != Frac(3, 4))
        self.assertFalse(Frac(2, 4) != Frac(1, 2))
    def test_frac_int_comparison(self):
        self.assertTrue(Frac(2, 1) == 2)
        self.assertFalse(Frac(1, 2) == 1)
        self.assertTrue(Frac(1, 4) < 1)
        self.assertTrue(Frac(3, 3) <= 1)
        self.assertTrue(Frac(6, 2) >= 3)

    def test_frac_float_comparison(self):
        self.assertTrue(Frac(1, 2) == 0.5)
        self.assertFalse(Frac(1, 3) == 0.33)
        self.assertTrue(Frac(3, 4) > 0.5)
        self.assertTrue(Frac(1, 10) < 0.2)
        self.assertTrue(Frac(5, 5) <= 1.0)
        self.assertTrue(Frac(9, 3) >= 3.0)
    def test_lt(self):
        self.assertTrue(Frac(1, 2) < Frac(3, 4))
        self.assertFalse(Frac(3, 4) < Frac(1, 4))

    def test_le(self):
        self.assertTrue(Frac(1, 2) <= Frac(3, 4))
        self.assertTrue(Frac(1, 2) <= Frac(1, 2))
        self.assertFalse(Frac(3, 4) <= Frac(1, 4))

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 4), Frac(3, 4))
        self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))

    def test_sub(self):
        self.assertEqual(Frac(3, 4) - Frac(1, 4), Frac(1, 2))
        self.assertEqual(1 - Frac(1, 2), Frac(1, 2))

    def test_mul(self):
        self.assertEqual(Frac(1, 2) * Frac(2, 3), Frac(1, 3))
        self.assertEqual(Frac(1, 2) * 3, Frac(3, 2))

    def test_truediv(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 4), Frac(2, 1))
        self.assertEqual(Frac(3, 4) / 3, Frac(1, 4))
        with self.assertRaises(ValueError):
            Frac(1, 2) / Frac(0, 1)

    def test_rtruediv(self):
        self.assertEqual(2 / Frac(1, 4), Frac(8, 1))
        with self.assertRaises(ValueError):
            1 / Frac(0, 1)

    def test_invert(self):
        self.assertEqual(~Frac(2, 3), Frac(3, 2))
        with self.assertRaises(ValueError):
            ~Frac(0, 1)

    def test_float(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertEqual(float(Frac(3, 4)), 0.75)
    

if __name__ == '__main__':
    unittest.main()
