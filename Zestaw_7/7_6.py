import unittest
import itertools

class TestAlternatingIterator(unittest.TestCase):
    def test_alternating_iterator(self):
        iterator_a = itertools.cycle([0, 1])
        expected_sequence = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        actual_sequence = [next(iterator_a) for _ in range(10)]
        self.assertEqual(actual_sequence, expected_sequence)


class TestRandomDirectionIterator(unittest.TestCase):
    def test_random_direction_iterator(self):
        directions = ["N", "E", "S", "W"]
        iterator_b = itertools.cycle(directions)
        actual_sequence = [next(iterator_b) for _ in range(4)]
        for direction in directions:
            self.assertIn(direction, actual_sequence)
            
class TestDayOfWeekIterator(unittest.TestCase):
    def test_day_of_week_iterator(self):
        iterator_c = itertools.cycle(range(7))
        expected_sequence = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]
        actual_sequence = [next(iterator_c) for _ in range(14)]
        self.assertEqual(actual_sequence, expected_sequence)

if __name__ == "__main__":
    unittest.main()
