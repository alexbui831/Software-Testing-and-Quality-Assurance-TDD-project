import unittest
from stqa_pythonprogram import *

class TestBMICase(unittest.TestCase):

  # Tests if calculations are correct
  def test_bmi_calc(self):

    actual = bmi_calc(5, 9, 160)
    expected = 24.19659735349716
    self.assertAlmostEqual(actual, expected)

  # Tests if results are correct
  def test_bmi_analysis(self):

    actual = bmi_analysis(26)
    expected = "overweight"
    self.assertEqual(actual, expected)
    
class TestRetirementCase(unittest.TestCase):

  # Tests if calculations are correct
  def test_retirement_calc(self):

    actual = retirement_calc(25, 65000, .1, 1500000)
    expected = 195.94017094017093
    self.assertAlmostEqual(actual, expected)

  # Tests if results are correct
  def test_retirement_analysis(self):

    actual = retirement_analysis(70)
    expected = "saving was a success"
    self.assertEqual(actual, expected)







