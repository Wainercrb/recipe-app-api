"""
Simple tests
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
  """Test the calc module"""

  def test_add_numbers(self):
    """Test adding number together"""

    res = calc.add(5, 1)

    self.assertEqual(res, 6)

  def test_subtract_numbers(self):
    """Test subtracting number together"""

    res = calc.subtract(10, 15)

    self.assertEqual(res, 5)


