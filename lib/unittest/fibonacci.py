from lib.fibonacci import *
import unittest
import random

class FibonacciTest(unittest.TestCase):

    def setUp(self):
        self.uut = Fibonacci()

    def test_shouldReturnEmptySetWhenAskedForNegativeTerms(self):
        self.assertEqual(self.uut.getTerms(random.randint(-1000, -1)), [])

    def test_shouldReturnEmptySetWhenAskedForZeroTerms(self):
        self.assertEqual(self.uut.getTerms(0), [])

    def test_firstAndSecondTermsShouldBeOne(self):
        self.assertEqual(self.uut.getTerms(1), [1])
        self.assertEqual(self.uut.getTerms(2), [1, 1])

    def test_termsShouldFollowRecurrenceRelation(self):
        self.assertEqual(self.uut.getTerms(3), [1, 1, 2])
        self.assertEqual(self.uut.getTerms(4), [1, 1, 2, 3])
        self.assertEqual(self.uut.getTerms(5), [1, 1, 2, 3, 5])
        self.assertEqual(self.uut.getTerms(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        
