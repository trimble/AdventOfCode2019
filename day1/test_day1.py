#! /usr/bin/env python
import unittest
from day1 import *

class MyTests(unittest.TestCase):
  def test_basic_fuel_calc(self):
    self.assertEqual(calc_fuel_needed_for_mass(12), 2)
    self.assertEqual(calc_fuel_needed_for_mass(14), 2)
    self.assertEqual(calc_fuel_needed_for_mass(1969), 654)
    self.assertEqual(calc_fuel_needed_for_mass(100756), 33583)

  def test_total_fuel_calc(self):
    self.assertEqual(calc_total_fuel_needed_for_mass(14), 2)
    self.assertEqual(calc_total_fuel_needed_for_mass(1969), 966)
    self.assertEqual(calc_total_fuel_needed_for_mass(100756), 50346)

if __name__ == '__main__':
  unittest.main()
