'''
Sample tests
'''

from app import calc
from django.test import SimpleTestCase
from rest_framework.test import APITestCase
from django.test import TestCase


class CalcTests(SimpleTestCase):
    '''Test the calc module.'''

    def test_add_numbers(self):
        '''Test adding numbers together'''
        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_subtract_number(self):
        res = calc.subtract(5,4)

        self.assertEqual(res, 1)